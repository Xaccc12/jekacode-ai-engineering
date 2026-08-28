# How to — the classroom guide (novices)

Do these steps **once**. Later weeks only say “open HOW_TO if you forgot.”

Dictionary of words: [AI_ENGINEERING_TERMS.md](AI_ENGINEERING_TERMS.md)  
Test every kitchen: [TEST_ALL_MODELS.md](TEST_ALL_MODELS.md)  
Git / fork / PR: [fork_push_pr.md](fork_push_pr.md)

---

## What you are installing (the picture)

| Thing | What it is | Why a beginner needs it |
|---|---|---|
| **VS Code** | The editor (where you type) | Not Cursor. This course is VS Code. |
| **Python 3.11+** | The language | Every notebook and app |
| **`.venv`** | A private Python “box” for this course | Stops other projects from breaking yours |
| **Ollama** | AI **on your laptop** | Works with no Google key |
| **Gemini key** | Ticket to Google’s LLM | Fast classroom default |
| **Grok key** | Ticket to xAI | Second kitchen to compare |
| **DeepSeek / HF** | Optional extra kitchens | Skip if you have no key |
| **Gradio** | Draws a website from Python | Fastest UI |
| **Streamlit** | Another website from Python | Tabs and forms |
| **GitHub** | Where code lives online | Week 10 deploy + portfolio |

**Behind the scenes of `ask()`**

```
You type a prompt
    → Python (jekacode.ai)
        → HTTP request (JSON)
            → Gemini / Grok / DeepSeek  (cloud)
            OR Ollama on localhost:11434 (your laptop)
        ← tokens (pieces of words)
    → the notebook or Gradio paints the text
```

Nobody in this room is **training** a model. You are doing **inference** (asking a model that is already trained).

---

## 0. VS Code + Python (once)

1. Install VS Code: [https://code.visualstudio.com](https://code.visualstudio.com)
2. Extensions: **Python** and **Jupyter** (publisher: Microsoft)
3. **File → Open Folder** → this course folder (the one that contains `jekacode/` and `week01-intro-to-ai/`)
4. Open the terminal in VS Code (**Terminal → New Terminal**)

**Mac**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

**Windows (PowerShell)**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

If Windows says scripts are disabled:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then try `Activate.ps1` again.

When it works, the terminal starts with `(.venv)`.

**Notebooks:** top-right **Select Kernel** → the Python inside `.venv` (often named Python 3.11 or “Python (Jekacode)”).

**Why `pip install -e .`?** It installs the `jekacode` package in *editable* mode so `from jekacode.ai import ask` works from any week folder.

---

## 1. Ollama (AI on your laptop, no cloud key)

**What it is:** a free app. It downloads a small open-source model (we use `llama3.2`). Your computer becomes the kitchen.

**Install**

1. Open [https://ollama.com](https://ollama.com)
2. Download **Mac** or **Windows**
3. Run the installer (Windows: “Run as administrator” if it asks)
4. Finish until you see the llama / Ollama icon in the menu bar or system tray

**First chat (in a terminal)**

```bash
ollama run llama3.2
```

The **first** time this downloads a few gigabytes. Do it on Wi‑Fi **before** class if you can.

Weak laptop / little RAM:

```bash
ollama run llama3.2:1b
```

Then in `.env` set:

```
OLLAMA_MODEL=llama3.2:1b
```

Do **not** download a 70B model on a school laptop.

Type: `Explain Jekacode like I am 12.` Quit with `/bye`.

If it fails:

1. Open a **second** terminal
2. Run `ollama serve`
3. In the first terminal, try `ollama run llama3.2` again

**From Python (after the model is pulled once)**

```python
from jekacode.ai import ask
print(ask("Hello", provider="ollama"))
```

**Behind the scenes:** Python sends HTTP to `http://localhost:11434` on *your* machine. No Google, no xAI, no bill. **Latency** can be high on first call (**cold start** — the model is waking up).

---

## 2. Gemini key (Google) — classroom default

**What it is:** Google’s LLM. Fast **Flash** models are the classroom default.

1. Browser: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Sign in with Google
3. Click **Create API key** → copy the long string
4. In the **course folder**, copy `.env.example` to `.env`
   - Mac: `cp .env.example .env`
   - Windows: `copy .env.example .env`
5. Open `.env` and paste:

```
GEMINI_API_KEY=paste_the_long_key_here
GEMINI_MODEL=gemini-2.0-flash
```

6. Never put `.env` on GitHub, WhatsApp, a screenshot, or a projector

```python
from jekacode.ai import ask
print(ask("Reply: Jekacode is ready.", provider="gemini"))
```

**Behind the scenes:** your prompt + key travel to Google’s servers. They run **inference** and send **tokens** back. You wait (**latency**). You may pay later if you leave the free quota.

If Google says the model name is wrong, open AI Studio → pick a Flash model → put that exact name in `GEMINI_MODEL=`.

---

## 3. Grok key (xAI)

1. Open [https://console.x.ai](https://console.x.ai)
2. Create an account and an **API key**
3. In `.env`:

```
GROK_API_KEY=paste_here
GROK_MODEL=grok-3-mini
```

If the dashboard shows a **newer** model name, use **that** name. The string must match.

```python
print(ask("Reply: Jekacode is ready.", provider="grok"))
```

**Behind the scenes:** Grok uses a Chat Completions URL (`https://api.x.ai/v1/chat/completions`) — the same *shape* as DeepSeek. Your helper `_openai_style_chat` in `jekacode/ai.py` is that shared shape.

---

## 4. DeepSeek (optional third cloud)

1. [https://platform.deepseek.com](s://plhttpatform.deepseek.com)
2. Create an API key
3. In `.env`: `DEEPSEEK_API_KEY=...`

Skip this week if you have no key. That is allowed.

---

## 5. Hugging Face (model market + YarnGPT)

**What it is:** a website of models, datasets, and **Spaces** (live Gradio apps). YarnGPT lives here.

1. Join: [https://huggingface.co/join](https://huggingface.co/join)
2. Optional token: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) → `HF_TOKEN=...` in `.env`

You can **browse** without a token. You need a token only for some Inference API calls.

YarnGPT (Nigerian-accented speech): [https://huggingface.co/saheedniyi/YarnGPT](https://huggingface.co/saheedniyi/YarnGPT)  
Classroom path: text with Gemini first (`interesting-projects/yarngpt-voice-notice/`), voice later on Colab/Space if the laptop cannot hold the weights.

---

## 6. Gradio (UI in one Python file)

Gradio **draws a website from Python**. You write a function. Gradio draws boxes. No HTML required.

From the **course root**, with `(.venv)` on:

```bash
python week04-ai-apps/gradio_chat.py
```

It prints a local URL like `http://127.0.0.1:7860`. Open it in the browser.

If the port is busy, Gradio picks another. Read the terminal.

**Why we import it**

```python
import gradio as gr
# gr is a nickname so we type less.
# Interface() = "here is a form: inputs, one function, outputs".
```

**Every later week** also has `gradio_app.py` so you are never stuck if Streamlit feels heavy.

Stop the server with **Ctrl+C** in the terminal.

**Behind the scenes:** Gradio starts a small web server on your laptop. The browser is the **frontend**. Your function + `ask()` is the **backend**. Then `ask()` makes a *second* hop to Gemini/Grok/Ollama.

---

## 7. Streamlit (tabs and forms)

```bash
streamlit run week04-ai-apps/study_assistant.py
```

The browser often opens itself. Stop with Ctrl+C.

**Why we import it**

```python
import streamlit as st
# st.text_input, st.button, st.tabs — widgets that become HTML for you.
```

---

## 8. HTML chatbot (real frontend)

This is what a company product looks like: HTML + CSS + JavaScript talking to Python.

```bash
python week04-ai-apps/html-chatbot/server.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000)

Every line is explained in `week04-ai-apps/html-chatbot/EXPLAINED.md`.

---

## 9. The `.env` file (secrets)

| Rule | Why |
|---|---|
| Copy from `.env.example` | Template with empty names |
| Keep `.env` in the **course root** | `load_dotenv()` looks there |
| Never `git add .env` | Keys get stolen |
| Cloud hosts (Week 10) | Paste the **same names** into the host’s Secrets form |

**Behind the scenes:** `from dotenv import load_dotenv` then `load_dotenv()` reads the file into environment variables (`os.getenv("GEMINI_API_KEY")`). The key never needs to sit in a notebook cell.

---

## 10. Test every model you actually have

Open `setup/test_all_models.ipynb` or read [TEST_ALL_MODELS.md](TEST_ALL_MODELS.md).

Skip providers with no key. That is allowed. Fill the table: provider, **latency_ms**, ok, notes.

```python
from jekacode.ai import ask_timed
print(ask_timed("Say hi in one word.", provider="gemini"))
```

`ask_timed` is `ask()` plus a stopwatch. **Latency** is how long you waited.

---

## 11. n8n (Week 8, optional visual automation)

1. [https://n8n.io](https://n8n.io) — desktop or cloud trial
2. Import `week08-automation/n8n-email-assistant.json` if the file exists
3. If n8n is painful, **Python is the backup**: `streamlit run week08-automation/email_assistant.py` or `python week08-automation/gradio_app.py`

n8n is visual Lego: **trigger** (new mail) → **AI node** → **human review**. Never auto-send money this term.

---

## 12. Deploy (Week 10) — two easy hosts

**Streamlit Community Cloud**

1. Push your app to GitHub
2. [https://share.streamlit.io](https://share.streamlit.io) → New app → pick the `.py` file
3. Secrets: paste `GEMINI_API_KEY` (same name as `.env`)

**Hugging Face Space (Gradio)**

1. [https://huggingface.co/new-space](https://huggingface.co/new-space)
2. SDK = **Gradio**, hardware = CPU
3. Settings → Secrets → same key names

**Behind the scenes:** on your laptop, `.env` is a file. In the cloud, **secrets** are a form. First request can be a **cold start** (slow). Show a spinner. Measure with a phone stopwatch.

---

## Why we import these (novice table)

| Line | What it means |
|---|---|
| `import sys` | Talk to Python itself (especially `sys.path`) |
| `from pathlib import Path` | Folders that work on Mac and Windows |
| `sys.path.append(...)` | “Also look in the course root for packages” |
| `from jekacode.ai import ask` | One door to Gemini / Grok / Ollama |
| `from jekacode.ui import banner` | Logo + navy/green title (Streamlit) |
| `import streamlit as st` | Draw a website with Python |
| `import gradio as gr` | Draw a *simpler* website with Python |
| `from flask import Flask` | Tiny web server for the HTML chat |
| `import requests` | HTTP — how APIs speak (used *inside* `jekacode.ai`) |
| `from dotenv import load_dotenv` | Load `.env` so keys are not in GitHub |
| `import os` | Read those keys (`os.getenv`) |
| `import time` | Stopwatch for **latency** |

---

## If something is red

1. Read the **last line** of the error (that is the treasure)
2. Ask Gemini/Grok: `Explain this error like I am 12:` and paste it
3. Checklist:
   - Is `(.venv)` on?
   - Did you **Select Kernel** to that same Python?
   - Is Ollama running? (`ollama run llama3.2`)
   - Is `.env` in the **course root**, not inside `week04`?
   - Did you copy the key without extra spaces or quotes?
4. Common messages

| Error | Likely meaning |
|---|---|
| `Missing GEMINI_API_KEY` | No `.env` or empty key — see section 2 |
| `Ollama is not running` | Install + `ollama run llama3.2` |
| `ModuleNotFoundError: jekacode` | Run the **boot** cell, or `pip install -e .` |
| `ConnectionError` / timeout | Wi‑Fi, VPN, or the API is slow (**latency** / timeout) |
| `429` | **Rate limit** — wait, then retry |
| `401` / `403` | Wrong or revoked key — rotate it |

---

## How a typical class day starts

1. Open the **week folder** README (goals, tools, how-to, behind the scenes)
2. Open `day1.ipynb` or `day2` / `day3`
3. Run the **first code cell** (`boot()`) so `import jekacode` works
4. Follow the markdown: theory first, then typed code with comments
5. If the day has a UI: run Gradio **or** Streamlit from the course root
