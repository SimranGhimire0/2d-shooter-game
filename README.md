# AI Code Reviewer

A rebuilt portfolio project that reviews Python code through a browser interface. The FastAPI backend parses Python source without executing it and returns line-level findings, a function count, and an estimated complexity score.

## Features

- Paste Python code, open a `.py` file, or load a built-in example.
- Review syntax errors, mutable default arguments, broad exception handling, and other flagged patterns.
- Get optional Gemini explanations with a server-side API key. The local checks work without a key.

[Browse the source code](./ai-code-reviewer) · [Read the full project documentation](./ai-code-reviewer/README.md)

## Run locally

From the repository folder, run:

```bash
cd ai-code-reviewer
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn app:app
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) and click **Load example → Run review**.
