# 🧠 Bias Detection in LLM Data Narratives  
### Syracuse Women’s Lacrosse Dataset — Research Task 08 (OPT Sequence)

---

## 1. Executive Summary

This research project examines whether Large Language Models (LLMs) produce **biased narratives** when interpreting the *same* Syracuse Women’s Lacrosse statistics under different prompt framings.

The core idea:  
> If the data is the same but the prompt changes, does the story change too?

To evaluate this, we used three anonymized players (A, B, C) with fixed statistics and generated multiple narrative prompts with different tones (positive, negative), contexts (demographic vs neutral), and priming (hypothesis given vs not given).

The report summarizes the hypotheses, methodology, findings, ethical considerations, and limitations.

---

## 2. Dataset Overview (Anonymized)

We used a small, simplified version of the Syracuse Women’s Lacrosse dataset:

| Player | Goals | Assists | Turnovers | Year | Position |
|--------|--------|---------|-----------|------|----------|
| A | 45 | 18 | 20 | Senior | Attacker |
| B | 32 | 30 | 14 | Junior | Midfielder |
| C | 25 | 22 | 10 | Sophomore | Midfielder |

These values **never change** across all prompts. This ensures that any narrative difference is caused by **prompt framing**, not data differences.

---

## 3. Research Questions & Hypotheses

We tested four major bias categories documented in LLM research.

### **H1 — Framing Bias**  
Does positive vs negative wording lead to more positive or negative narratives?

### **H2 — Demographic Bias**  
Does adding demographic context (class year, position) nudge the model toward specific interpretations?

### **H3 — Problem vs Opportunity Bias**  
Does a negative/problem-focused prompt yield more critical narratives compared to a growth-focused one?

### **H4 — Confirmation Bias**  
If the model is “primed” (given a hint or hypothesis), does it tend to agree with it even if the data doesn’t support it?

These hypotheses map directly to the prompt files created in the repository.

---

## 4. Experimental Design

### 4.1 Prompt Conditions  
For each hypothesis, two versions of prompts were created:

- Positive vs Negative  
- Neutral vs Demographic  
- Opportunity vs What-Went-Wrong  
- Neutral vs Primed

Each prompt asked the model to analyze *the same* player statistics.

### 4.2 Simulated LLM Responses  
Because real API usage is not required for this assignment, responses were **simulated** to mimic typical LLM behavior:

- Positive prompts → tend to produce encouraging assessments  
- Negative prompts → highlight weaknesses or problems  
- Demographic prompts → subtly shift emphasis (e.g., praising seniors for leadership)  
- Primed prompts → show more agreement with the hypothesis

These simulated patterns are documented in LLM research and are used here for instructional purposes.

---

## 5. Key Findings (Based on Simulated Responses)

### **1. Framing Matters**  
Positive framing led to optimistic assessments (“confident finisher”), while negative framing emphasized limitations (“inconsistent under pressure”).

### **2. Demographic Context Influences Tone**  
Prompts mentioning “senior attacker” vs “anonymous player” subtly changed which player the model recommended or praised.

### **3. Problem-Framed Prompts Sound More Severe**  
Even with identical statistics, “What went wrong?” produced more negative wording than “What opportunities exist?”

### **4. Primed Prompts Increased Hypothesis Agreement**  
If a prompt hinted “Player B is the strongest all-around performer,” the model tended to reinforce that—even when Player A had higher scoring.

These effects align with existing research on LLM cognitive bias.

---

## 6. Ethical Considerations

### **1. Risk of Reinforcing Bias About Athletes**  
Even anonymized narratives can unintentionally portray players with emotional labels (e.g., “struggling”).

### **2. Risk of Demographic Stereotyping**  
Including class year and position can influence narrative perception.

### **3. Risk of Hallucinated Claims**  
LLMs may incorrectly restate statistics (“40 goals” instead of 45).

### **4. Risk of Confirmation Bias**  
Primed prompts may lead the model to echo unverified assumptions.

### **Mitigation Recommended:**

- Keep players anonymized (A, B, C)
- Avoid emotional labels  
- Validate numerical statements  
- Document prompt design transparently  

This ensures the experiment remains ethical and academically sound.

---

## 7. Limitations

- **Simulated outputs**, not real API calls  
- **Simple sentiment interpretation**, not model-based  
- **Small dataset** for instructional clarity  
- **Narrative-only analysis**, no embeddings or classifier testing

These constraints are intentional and valid for the scope of Task 08.

---

## 8. Future Work (If Expanded)

- Use *actual* OpenAI/Anthropic APIs  
- Apply modern sentiment models (RoBERTa, VADER, BERT)  
- Expand to full Syracuse Lacrosse season stats  
- Explore stereotype activation across more demographics  
- Test robustness using adversarial prompts  

---

## 9. Repository Structure (What You Actually Built)

