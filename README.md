# InboxIQ — Email Triage and Reply Assistant

OpenRouter-powered email triage and reply drafting prototype.

## What it does
- Takes a subject, sender role, email body, academic-calendar context, and optional policy excerpt.
- Produces a category, priority, reason, summary, draft reply, policy-grounding note, and review flags.
- Uses OpenRouter's chat completions API to analyze messages.
- Requires human review; it does not connect to or send email from a mailbox.

## Important
Use synthetic or anonymized emails only. Do not enter real personal or confidential data.

## Run locally
Python 3.10+ is recommended.

```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

## Configure OpenRouter

The app reads `OPENROUTER_API_KEY` from `.streamlit/local_secrets.json`. This local JSON file is ignored by Git and is not exposed in the frontend. The app defaults to OpenRouter's `openrouter/free` model router; model selection is not exposed in the UI.

You can also set `OPENROUTER_API_KEY` in your shell environment. Never commit API keys to Git. OpenRouter receives the email content you enter for analysis; use synthetic or anonymized emails. The Settings tab contains only appearance and mail preferences.

macOS/Linux:
```bash
export OPENROUTER_API_KEY="YOUR_KEY"
streamlit run app.py
```

Windows PowerShell:
```powershell
$env:OPENROUTER_API_KEY="YOUR_KEY"
streamlit run app.py
```

The `openrouter/free` router is rate limited and selects among available free models, so output quality and response availability can vary.

## Files
- `prompts/baseline.txt`: initial JSON prompt.
- `prompts/structured.txt`: prompt with explicit categories and priority rules.
- `prompts/refined.txt`: refined prompt with untrusted-email handling, grounding, and review requirements.
- `data/synthetic_emails.json`: 50 fictional labelled emails.
- `evaluation/evaluate.py`: evaluates a results CSV against labels.
- `evaluation/expected_results.csv`: labelled reference set.
- `docs/system_design.md`: architecture and design decisions.
- `docs/milestone2_report.md`: editable report draft with placeholders for real results.
- `docs/demo_video_script.md`: 90–150 second recording plan.

## Evaluation workflow
1. Run the same test emails with each prompt version using the same model/settings.
2. Save one result per test ID in a CSV with columns `test_id,prompt_version,category,priority,json_valid,reply_quality_1_to_5,grounding_ok`.
3. Run:
```bash
python evaluation/evaluate.py evaluation/actual_results.csv
```
4. Inspect failures, update prompts, and rerun. Do not fill actual-results files with invented data.

## Output schema
See `prompts/refined.txt`. All outputs require human review before use.
