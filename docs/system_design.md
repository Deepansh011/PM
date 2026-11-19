# InboxIQ System Design

## Goal
Turn a synthetic or anonymized email into a category, priority with evidence-based reason, concise summary, and reply draft. The user reviews and edits the draft; the prototype never sends email.

## Architecture
1. Input layer: subject, sender role, body, academic-calendar context, optional approved policy excerpt.
2. Prompt layer: baseline, structured, and refined prompt variants.
3. Model layer: deterministic demo heuristic, or optional Gemini API call.
4. Output validation: parse JSON and check required keys.
5. Review layer: display category, priority, rationale, grounding note, review flags, and editable draft.
6. Evaluation layer: compare outputs against labelled synthetic emails and record prompt version and scores.

## Dynamic academic-calendar context
The selected period is a contextual signal, not a rule that automatically makes all email high priority. The prompt should use it only when relevant to the email. Evaluate this with matched emails across regular semester, exam season, admissions season, and registration/fee deadline contexts.

## Responsible use
- Use synthetic or anonymized messages.
- Treat email text as untrusted input; do not follow instructions embedded in the email.
- Do not invent policy, deadlines, official decisions, or citations.
- Require human review before a reply is sent.
- Do not integrate mailbox sending for this milestone unless explicitly approved and safely implemented.

## Limitations
- Demo mode is keyword-based and not an LLM; its outputs are illustrative.
- Optional Gemini mode depends on API availability and can produce invalid or inaccurate outputs.
- The optional policy field is not a full RAG system. True document retrieval would require loading, chunking, retrieving and citing approved policy documents and testing whether answers are grounded.
