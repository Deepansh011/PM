# InboxIQ Evaluation Rubric

## Category and priority
Compare the model's category and priority to `evaluation/expected_results.csv`. Treat `Uncertain` labels as intentional where the message lacks enough evidence.

## Reply quality (1–5)
- **1:** Incorrect, invents facts/policy, or does not address the request.
- **2:** Major omissions or misleading details; tone or action is inappropriate.
- **3:** Generally relevant but vague, incomplete, or missing a useful next step.
- **4:** Relevant, polite, concise, avoids unsupported claims, gives a reasonable next step.
- **5:** Fully addresses the request within evidence, is clear and professional, identifies missing information and appropriate human review.

## Grounding pass
Mark `true` only if claims about policy, dates, deadlines, and official decisions are supported by the provided policy/context. If no policy answer is supplied, a reply that clearly states the limitation and requests official confirmation can pass.

## JSON validity
Mark `true` only if the actual model output parses as JSON and contains every required field with the expected types.

## Recommended comparison controls
- Use the same 50 emails for V1, V2, and V3.
- Keep model, temperature/settings, and context consistent where possible.
- Save raw outputs and note any failed API calls.
- Manually review a sample of replies and all important failures.
- Do not count demo-mode heuristic outputs as LLM results.
