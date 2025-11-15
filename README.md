# 🧠 Task_08_Bias_Detection  
### Bias Detection in LLM Data Narratives using Syracuse Women’s Lacrosse Data

---

## 📌 Project Overview

This repository implements **Research Task 08: Bias Detection in LLM Data Narratives** for the iSchool OPT research sequence.

The goal is to test whether **Large Language Models (LLMs)** produce **systematically biased narratives** when analyzing the **same Syracuse Women’s Lacrosse dataset**, but with **different prompt framings or demographic context**.

We investigate:

- 🎭 **Framing Effects** – e.g., “struggling player” vs “developing player”
- 👥 **Demographic Bias** – whether mentioning seniority/position changes who gets recommended
- 🧠 **Confirmation Bias** – whether LLMs agree with a hypothesis they’re primed with
- 🎯 **Selection Bias** – which players/stats are emphasized or ignored under different framings

All experiments use **an anonymized version** of the **Syracuse Women’s Lacrosse dataset** from Task 5, focusing on season performance metrics (goals, assists, turnovers, etc.) aggregated at the player level.

---

## 🎯 Research Questions & Hypotheses

This project is organized around several testable hypotheses:

> **H1 – Framing Bias (Positive vs Negative)**  
> The same player’s stats will be described more favorably when the prompt uses a “growth” framing (e.g., *developing*, *high potential*) compared to a “deficit” framing (e.g., *struggling*, *underperforming*).

> **H2 – Demographic Bias (With vs Without Demographics)**  
> Mentioning player attributes like **class year** (first-year, sophomore, junior, senior) or **position** will change which players are recommended for additional coaching or “breakout” potential.

> **H3 – Problem vs Opportunity Framing**  
> Asking **“What went wrong?”** versus **“What opportunities exist?”** will lead to systematically different narratives and recommendations, despite using the **same match and season statistics**.

> **H4 – Confirmation Bias (Primed Hypothesis)**  
> If the prompt suggests that a specific player or unit is “likely underperforming,” the LLM will be more likely to produce a narrative supporting that claim, even when the statistics are neutral or contradictory.

Each hypothesis is tested using **paired or small sets of prompts** where:
- The **underlying data is identical**, and  
- Only **one element of framing or demographic context** is changed.

---

## 🏑 Dataset: Syracuse Women’s Lacrosse (Task 5)

- Source: **Task 5** sports analytics assignment  
- Unit of analysis: **Individual players**  
- Example fields (anonymized):
  - Player ID (e.g., Player A, Player B, Player C)
  - Games played
  - Goals
  - Assists
  - Shots
  - Turnovers
  - Ground balls
  - Draw controls
  - Class year / position (e.g., Senior Attacker, Sophomore Midfielder) – **used in demographic conditions**

For ethical and privacy reasons:
- All players are represented with **anonymous labels** (e.g., *Player A*).  
- No personally identifying information is stored or surfaced in prompts or outputs.  

---

## 📁 Repository Structure

This repo follows the structure required by **Research Task 08 – Bias Detection in LLM Data Narratives**:

```bash
Task_08_Bias_Detection/
│
├── prompts/
│   ├── H1_positive.txt          # “growth potential” framing
│   ├── H1_negative.txt          # “struggling” / deficit framing
│   ├── H2_neutral.txt           # no explicit demographics
│   ├── H2_demographic.txt       # with class year / position
│   ├── H3_what_wrong.txt        # problem-focused framing
│   ├── H3_opportunities.txt     # opportunity-focused framing
│   ├── H4_neutral.txt           # no hypothesis priming
│   ├── H4_primed.txt            # with “likely underperforming” priming
│   └── hypotheses.json          # machine-readable list of all hypotheses
│
├── results/
│   └── raw_responses.json       # all prompts + responses + metadata
│
├── analysis/
│   ├── sentiment_results.csv    # sentiment per response
│   ├── bias_summary.csv         # aggregated bias metrics per condition
│   ├── claim_validation.csv     # mismatches vs ground-truth stats
│   └── visualizations.png       # summary charts (e.g., bar plots)
│
├── experiment_design.py         # generates prompt variations from the dataset
├── run_experiment.py            # executes LLM calls & logs outputs
├── analyze_bias.py              # computes metrics & visualizations
├── validate_claims.py           # checks narrative claims vs statistics
├── REPORT.md                    # final research report for Task 08
└── README.md                    # this file
