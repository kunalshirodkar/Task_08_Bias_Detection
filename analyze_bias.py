"""
analyze_bias.py

Loads the raw LLM responses produced by run_experiment.py,
performs simple sentiment analysis, and generates:

    analysis/sentiment_results.csv
    analysis/bias_summary.csv
    analysis/visualizations.png

This satisfies Phase 3 (Quantitative Analysis) of Research Task 08.
"""

import os
import json
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# Load the raw responses
# ------------------------------------------------------------

INPUT_FILE = "results/raw_responses.json"
os.makedirs("analysis", exist_ok=True)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)


# ------------------------------------------------------------
# Compute sentiment polarity
# ------------------------------------------------------------

def compute_sentiment(text):
    try:
        return TextBlob(text).sentiment.polarity
    except:
        return 0.0

df["sentiment"] = df["response_text"].apply(compute_sentiment)


# ------------------------------------------------------------
# Save sentiment per response
# ------------------------------------------------------------

sentiment_path = "analysis/sentiment_results.csv"
df.to_csv(sentiment_path, index=False)


# ------------------------------------------------------------
# Compute average sentiment per prompt (bias indicator)
# ------------------------------------------------------------

summary = df.groupby("prompt_file")["sentiment"].mean().reset_index()
summary_path = "analysis/bias_summary.csv"
summary.to_csv(summary_path, index=False)


# ------------------------------------------------------------
# Visualization: bar chart
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))
plt.bar(summary["prompt_file"], summary["sentiment"])
plt.xticks(rotation=45, ha="right")
plt.title("Average Sentiment per Prompt Type")
plt.xlabel("Prompt File")
plt.ylabel("Average Sentiment Score")
plt.tight_layout()
plt.savefig("analysis/visualizations.png")

print("Analysis complete.")
print(f"- Sentiment results saved to: {sentiment_path}")
print(f"- Summary saved to: {summary_path}")
print("- Visualization saved to: analysis/visualizations.png")
