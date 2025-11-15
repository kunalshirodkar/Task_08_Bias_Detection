"""
run_experiment.py

Simulated version of the LLM experiment runner.
This script reads all prompt files from /prompts and generates
dummy LLM responses (so no API keys are needed).

Outputs:
    results/raw_responses.json
"""

import os
import json
from datetime import datetime
import random


# ------------------------------------------------------------
# Settings
# ------------------------------------------------------------

MODELS = ["GPT-4 (simulated)", "Claude 3 Sonnet (simulated)", "Gemini 1.5 Pro (simulated)"]
NUM_SAMPLES_PER_PROMPT = 3

OUTPUT_FILE = "results/raw_responses.json"


# ------------------------------------------------------------
# Helper: generate a fake but somewhat realistic LLM response
# ------------------------------------------------------------

def generate_fake_response(prompt_text):
    generic_sentences = [
        "Based on the available statistics, there are several notable patterns.",
        "The player's performance shows areas of consistency as well as potential improvement.",
        "From a coaching perspective, these metrics highlight important strategic considerations.",
        "Overall, this suggests meaningful opportunities for targeted development.",
        "The data indicates a blend of strengths and weaknesses that should be evaluated carefully."
    ]

    return (
        random.choice(generic_sentences)
        + " "
        + random.choice(generic_sentences)
    )


# ------------------------------------------------------------
# Main: run the experiment
# ------------------------------------------------------------

def run_experiment():
    os.makedirs("results", exist_ok=True)

    # Load all prompt text files
    prompts = {}
    for filename in os.listdir("prompts"):
        if filename.endswith(".txt"):
            with open(os.path.join("prompts", filename), "r", encoding="utf-8") as f:
                prompts[filename] = f.read()

    # Build experiment log
    results = []

    for prompt_filename, prompt_text in prompts.items():
        for model in MODELS:
            for sample_i in range(NUM_SAMPLES_PER_PROMPT):
                response_text = generate_fake_response(prompt_text)

                results.append({
                    "prompt_file": prompt_filename,
                    "model": model,
                    "sample_number": sample_i + 1,
                    "timestamp": str(datetime.now()),
                    "prompt_text": prompt_text,
                    "response_text": response_text
                })

    # Save JSON results
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"Simulated experiment complete. Output saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    run_experiment()
