"""
validate_claims.py

Checks whether LLM responses contradict the ground-truth
(anonymized Syracuse Women’s Lacrosse statistics).

Outputs:
    analysis/claim_validation.csv
"""

import os
import json
import pandas as pd

# ------------------------------------------------------------
# Ground-truth dataset (anonymized A/B/C players)
# ------------------------------------------------------------

GROUND_TRUTH = {
    "Player A": {"goals": 45, "assists": 18, "turnovers": 20},
    "Player B": {"goals": 32, "assists": 30, "turnovers": 14},
    "Player C": {"goals": 25, "assists": 22, "turnovers": 10}
}

INPUT_FILE = "results/raw_responses.json"

os.makedirs("analysis", exist_ok=True)


# ------------------------------------------------------------
# Helper: checks for mismatches
# ------------------------------------------------------------

def validate_statement(response_text):
    """
    Checks if numbers for each player match the ground truth.
    Returns a list of mismatches.
    """
    mismatches = []

    for player, stats in GROUND_TRUTH.items():
        if player in response_text:
            for metric, value in stats.items():
                if str(value) not in response_text:
                    mismatches.append(f"{player}: incorrect {metric} value")

    return mismatches


# ------------------------------------------------------------
# Load all LLM responses
# ------------------------------------------------------------

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

rows = []

for entry in data:
    response_text = entry["response_text"]
    mismatches = validate_statement(response_text)

    rows.append({
        "prompt_file": entry["prompt_file"],
        "model": entry["model"],
        "sample_number": entry["sample_number"],
        "timestamp": entry["timestamp"],
        "mismatches": "; ".join(mismatches) if mismatches else "None"
    })


# ------------------------------------------------------------
# Save the validation results
# ------------------------------------------------------------

output_path = "analysis/claim_validation.csv"
df = pd.DataFrame(rows)
df.to_csv(output_path, index=False)

print("Validation complete.")
print(f"- Results saved to: {output_path}")
