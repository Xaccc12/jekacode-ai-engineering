# MODULE 5 — Prompt Engineering & AI Workflows

**day1.ipynb** theory · **day2.ipynb** lab · **day3.ipynb** project.  
Terms: [../guides/AI_ENGINEERING_TERMS.md](../guides/AI_ENGINEERING_TERMS.md)

## This week — novice guide

**What we want to achieve:** Role, few-shot, constraints, chaining. Reduce hallucination (“do not invent prices”). Ship a Business Assistant.

**Tools:** Gemini/Grok. Gradio or Streamlit.

**How to:**

```bash
python week05-prompt-engineering/gradio_app.py
streamlit run week05-prompt-engineering/business_assistant.py
```

[../guides/HOW_TO.md](../guides/HOW_TO.md)

**What goes on behind the scenes:** A **system prompt** is extra text prepended as policy. The model still only predicts tokens. **Chaining** = output of step 1 becomes input of step 2. Each `ask()` is a new inference (more latency).

**Class files:** `day1.ipynb` · `day2.ipynb` · `day3.ipynb`.

## Outline

1. Prompt engineering
2. System prompts
3. Few-shot
4. Role prompting
5. Structured prompts
6. Prompt chaining
7. Workflows
8. Structured outputs
9. Reliability (less hallucination, less inconsistency)

## Tasks

- Prompts for five industries
- Weak vs effective
- Reusable system prompt
- Multi-step workflow
- Unstructured → structured

## Labs

- Prompt template
- Multi-step workflow
- JSON-like output
- Content workflow
- Test and improve

## Project

**AI Business Assistant** — product text, posts, replies, summaries, social ideas.

[../visuals/chat-vs-engineer.html](../visuals/chat-vs-engineer.html)

Submit: `projects/YOUR_NAME/week05/` · [PR guide](../guides/fork_push_pr.md)
