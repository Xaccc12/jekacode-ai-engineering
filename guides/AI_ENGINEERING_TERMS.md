# AI engineering terms (theory you must be able to say out loud)

This is the dictionary for the Jekacode cohort. **Day 1** of each week points here. You do not need maths. You do need the *idea*.

Classroom models: **Gemini**, **Grok**, **DeepSeek**, **Ollama**, Hugging Face.

---

## 1. The big map

| Term | Simple meaning | Jekacode example |
|---|---|---|
| **Artificial Intelligence (AI)** | Computers doing jobs that used to need human judgement | Suggesting a study plan |
| **Machine Learning (ML)** | Learn patterns from examples instead of writing every rule | Spam filters, next-word prediction |
| **Generative AI** | AI that *makes* new content | A quiz, a caption, a draft email |
| **LLM (Large Language Model)** | Generative AI trained on huge text, predicts useful next words | Gemini, Grok, DeepSeek, Llama |
| **Inference** | *Using* a trained model (asking it a question now) | Every `ask()` call |
| **Training** | *Teaching* the model (expensive, not this course) | What Google / xAI already did |
| **Parameters / weights** | Millions/billions of tiny knobs set during training | You do not turn them; you send prompts |
| **AI Engineer** | Builds products around models (apps, RAG, agents, deploy, test) | This programme |
| **Software Engineer** | Builds exact-rule programs | Student grade calculator |
| **Data Scientist** | Finds stories in numbers | “Which class failed most?” |

**Trade-off:** Software engineering wants the *same* output every time. AI engineering often gets a *useful* output that can change slightly.

---

## 2. How a request works

| Term | Simple meaning |
|---|---|
| **Prompt** | The text you send the model |
| **System prompt** | The job description (“You are a WAEC tutor…”) |
| **User prompt** | What the person typed today |
| **Completion / response** | What the model writes back |
| **API** | A doorway with rules (waiter + kitchen) |
| **API key** | Password for that doorway. Lives in `.env` | 
| **Endpoint** | The URL you POST to |
| **JSON** | How computers pack data `{ "reply": "..." }` |
| **SDK** | A library that hides HTTP. We often use `requests` so you *see* the door |

```
You → Python app → internet (API) → Gemini or Grok → tokens back → screen
```

---

## 3. Tokens, context, cost

| Term | Simple meaning |
|---|---|
| **Token** | A small piece of text (often ~¾ of a word in English) |
| **Context window** | How much text the model can “see” at once (prompt + history) |
| **Context overflow** | You pasted too much; the start gets dropped or the call fails |
| **Input tokens** | What you send (you pay for these) |
| **Output tokens** | What it writes (you usually pay more per token) |
| **Rate limit** | Too many requests; the API says “slow down” |

**Engineering habit:** short, clear prompts. Do not paste a whole textbook when five paragraphs would do (that is why **RAG** exists).

---

## 4. Latency (how fast)

**Latency** = waiting time from “send” to “I have the full answer” (we measure **milliseconds**, 1000 ms = 1 second).

Related words:

| Term | Meaning |
|---|---|
| **TTFT (time to first token)** | How long until the *first* word appears (streaming UIs care about this) |
| **Throughput** | How many requests per minute a system can handle |
| **Timeout** | Your app gives up if the model is too slow |
| **Cold start** | First local Ollama call can be slower; the model is waking up |
| **Streaming** | Tokens arrive one by one (chat feels faster even if total time is similar) |

**What changes speed**

- Model size (tiny local Llama vs big cloud Gemini)
- How long the prompt is
- How long you asked it to write
- Your Wi‑Fi vs a nearby data centre
- Whether the server is busy

**Classroom expectation (rough, not a promise):**

| Provider | Often feels | Why |
|---|---|---|
| Gemini Flash | Fast | Built for cheap, quick answers |
| Grok mini | Fast–medium | Depends on xAI load and your network |
| DeepSeek | Medium | Cross-border network + model |
| Ollama on a weak laptop | Slow | Your CPU/GPU is the kitchen |
| Hugging Face free inference | Unpredictable | Queue + which model you picked |

Measure it yourself with `ask_timed()` — see [TEST_ALL_MODELS.md](TEST_ALL_MODELS.md).

**Trade-off:** faster models can be “thinner.” Slower / larger models can be smarter. Pick for the *job*, not for Twitter.

---

## 5. Hallucination and inconsistency

### Hallucination

The model **sounds sure** and is **wrong**. It invented a school fee, a law, a citation, a Python library.

Why it happens (idea, not maths): it is predicting *likely sentences*, not looking up a database unless **you** gave it documents (**RAG**) or tools.

**Tests:** ask something that is *not* in the handbook. A good RAG bot says “I cannot find it.” A hallucinating chat invents a paragraph.

### Inconsistency (stochastic behaviour)

Same prompt, **different** answers on run 2 and run 3.

Why: generation is partly random (**temperature**). Higher temperature = more variety (and more chaos). Lower = more repeatable (and more boring).

**Engineering response:**

- Do not use an LLM to compute exam averages (use Python).
- For brand voice, lock a **system prompt** and test 3 times.
- For facts, ground with RAG or a tool.
- For marks/money, **deterministic code**.

### Other reliability words

| Term | Meaning |
|---|---|
| **Grounding** | Tying the answer to sources you provided |
| **Citation** | Pointing at a chunk / page (even if informal) |
| **Guardrail** | Extra rules: refuse medical dosage, refuse API keys |
| **Jailbreak / prompt injection** | User tries to override your system prompt |
| **Bias** | Unfair patterns copied from training data or your prompt |
| **Evaluation** | Scoring answers on purpose (Week 11) |
| **Golden question** | A test item with a known good answer |

---

## 6. Prompting (how people chat vs how we engineer)

| Style | What people do | What engineers do |
|---|---|---|
| Zero-shot | “Write about Python.” | Role + task + limits |
| **Few-shot** | — | Show 1–3 examples of good output |
| **Role prompt** | — | “You are a Lagos SME copywriter.” |
| **Structured output** | Wall of text | Labels, bullets, JSON-like blocks |
| **Prompt chaining** | One huge ask | Step 1 output feeds step 2 |
| **Temperature** | Default in the website | You may ask for more/less creativity (concept) |

---

## 7. RAG and memory-ish ideas

| Term | Meaning |
|---|---|
| **Hallucination (again)** | Guessing without your textbook |
| **Knowledge base** | Your files (handbook, policies) |
| **Chunking** | Cutting a long doc into pieces |
| **Embedding** | Turning a chunk into a list of numbers that mean “aboutness” (no formula this term) |
| **Vector database** | A cupboard that can find *similar* number-lists |
| **Retrieval** | Pick the useful chunks |
| **Augmented generation** | Send chunks + question to the LLM |
| **Keyword retrieval** | Our beginner method: shared words (good enough to learn the idea) |

---

## 8. Agents and automation

| Term | Meaning |
|---|---|
| **Chatbot** | Ask → answer |
| **Agent** | Goal → think → **tool** → maybe another step → result |
| **Tool / function calling** | A Python function the model may request |
| **Workflow / automation** | Trigger → AI → action (n8n or Python) |
| **Human in the loop** | A person clicks Send on the email |

---

## 9. Product and ops

| Term | Meaning |
|---|---|
| **Frontend** | What humans see (HTML, Gradio, Streamlit) |
| **Backend** | Python + keys + `ask()` |
| **Latency budget** | “This button must answer in under 8 seconds or we show a spinner” |
| **Observability** | Logs: what was asked, how long, did it fail |
| **MVP** | Smallest product that helps one real user |
| **Eval set** | A list of test prompts you reuse every week |

---

## 10. Models in this classroom

| Name | Maker | How we call it |
|---|---|---|
| **Gemini** | Google | `provider="gemini"` |
| **Grok** | xAI | `provider="grok"` |
| **DeepSeek** | DeepSeek | `provider="deepseek"` |
| **Llama (etc.)** | Meta / others via Ollama | `provider="ollama"` |
| **YarnGPT** | Saheed Azeez / HF | Voice; Week 9 — not `ask()` text by default |

**GPT / Claude** appear in the curriculum as *names you should recognise* (ChatGPT-like systems, Claude from Anthropic). We do **not** require those APIs.

Read this file twice in Week 1 and once before every Day 1. If you can explain **latency**, **hallucination**, and **inconsistency** to a 12-year-old, you are ready for Week 3 testing.
