# InboxIQ: Email Triage and Reply Assistant
## Milestone 2 Technical Report Draft

**Course:** Prompt Engineering  
**Problem ID:** C16  
**Team members:** [Add names and roles]  
**Faculty:** [Add faculty name]  
**Date:** [Add submission date]

## 1. Project overview
InboxIQ is a prompt-engineering workflow intended to help university faculty and office staff organize incoming emails. Given an email, the system proposes a category, priority, evidence-based reason, short summary and polite reply draft. A human must review and edit the draft before use.

## 2. Problem and target users
Faculty and office staff receive emails with mixed purposes and urgency. Important requests may be missed and replies may be delayed or inconsistent. Target users include faculty, administrative office staff and other authorized university personnel. The prototype uses fictional emails only.

## 3. Scope and input/output
**Inputs:** subject, sender role, email body, academic-calendar context, optional approved policy excerpt.  
**Outputs:** category, priority, priority reason, summary, draft reply, policy-grounding note, human-review flag and review flags.

## 4. Prompt design and iterations
- **V1 Baseline:** asks for a JSON response with classification, priority and reply drafting, with an exam-related example.
- **V2 Structured:** defines category labels, priority criteria and required JSON fields, plus a few-shot example.
- **V3 Refined:** adds untrusted-email handling, context-sensitive academic-calendar guidance, policy-grounding constraints, uncertainty flags and mandatory human review.

**Changes after testing:** [Describe changes supported by actual experiment logs.]

## 5. System design and implementation
The prototype uses Python and Streamlit. It supports demo mode for interface testing and optional Gemini API mode for actual model experiments. JSON output is parsed and required fields are checked. The prototype does not connect to a mailbox or send email.

## 6. Test dataset and evaluation
The starter dataset contains 50 synthetic emails with expected categories and priorities. Run all prompt versions against the same examples and model settings where possible. Evaluate:
- category accuracy;
- priority accuracy;
- JSON validity;
- reply quality using a defined 1–5 rubric;
- grounding correctness;
- appropriate uncertainty and human-review flags.

**Actual results table:** [Insert results from evaluation/actual_results.csv after running real tests. Do not invent results.]

## 7. Error analysis
[Insert at least three real failure examples: input, expected output, actual output, failure type, and prompt change proposed.]

## 8. Responsible AI and limitations
The system uses synthetic data and should not receive confidential messages. Email content is treated as untrusted. The system must not invent university policies or official dates. All drafts require human review. Demo mode is a heuristic only. The optional policy excerpt field does not by itself constitute a full retrieval-augmented generation (RAG) system.

## 9. Conclusion and next steps
The current milestone provides a prototype foundation and an experiment plan. Next steps are to run actual model comparisons, analyze failures, refine the prompt, and document evidence and limitations.

## References and tools
- Bennett University, *Prompt Engineering Mini-Project Guidelines 2026*, Appendix A, problem C16.
- [Add the exact model documentation and other sources actually used.]
