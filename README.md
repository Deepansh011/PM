# InboxIQ — Email Triage and Reply Assistant (C16)

Prompt Engineering mini-project starter package for Milestone 2.

## What it does
- Takes a subject, sender role, email body, academic-calendar context, and optional policy excerpt.
- Produces a category, priority, reason, summary, draft reply, policy-grounding note, and review flags.
- Supports a deterministic demo mode without an API key and an optional Gemini API mode.
- Requires human review; it does not connect to or send email from a mailbox.

## Important
Demo mode uses simple keyword heuristics. It is only for testing the UI and should **not** be described as an LLM result or as evidence of model accuracy. Gemini mode is the actual model integration. Record actual outputs and evaluate them against labelled expected results before reporting scores.

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

Choose **Demo mode** to run without an API key.

## Optional Gemini API mode
1. Obtain permitted access to the Gemini API.
2. Set `GEMINI_API_KEY` in your shell environment; do not commit it to Git.
3. Run `streamlit run app.py`, select Gemini API, and choose an available model.

macOS/Linux:
```bash
export GEMINI_API_KEY="YOUR_KEY"
streamlit run app.py
```

Windows PowerShell:
```powershell
$env:GEMINI_API_KEY="YOUR_KEY"
streamlit run app.py
```

API access, quotas, and model names can change. Verify the model is available in your account.

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
