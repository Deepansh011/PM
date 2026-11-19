"""Evaluate actual prompt outputs. This script does not generate model outputs."""
import csv, sys
from pathlib import Path

if len(sys.argv) != 2:
    print("Usage: python evaluation/evaluate.py evaluation/actual_results.csv")
    raise SystemExit(2)

root = Path(__file__).resolve().parents[1]
expected_path = root / "evaluation" / "expected_results.csv"
actual_path = Path(sys.argv[1])

with expected_path.open(newline="", encoding="utf-8") as f:
    expected = {r["test_id"]: r for r in csv.DictReader(f)}
with actual_path.open(newline="", encoding="utf-8") as f:
    actual = list(csv.DictReader(f))

if not actual:
    raise SystemExit("No actual results found.")

by_version = {}
for r in actual:
    by_version.setdefault(r.get("prompt_version", "unspecified"), []).append(r)

for version, rows in sorted(by_version.items()):
    valid = [r for r in rows if r.get("test_id") in expected]
    if not valid:
        print(f"\n{version}: no matching test IDs")
        continue
    cat_scored = [(r, expected[r["test_id"]]) for r in valid if r.get("category","").strip()]
    pri_scored = [(r, expected[r["test_id"]]) for r in valid if r.get("priority","").strip()]
    cat_acc = sum(r["category"].strip() == e["expected_category"] for r,e in cat_scored) / len(cat_scored) if cat_scored else 0
    pri_acc = sum(r["priority"].strip() == e["expected_priority"] for r,e in pri_scored) / len(pri_scored) if pri_scored else 0
    json_valid = [r for r in valid if r.get("json_valid","").strip().lower() in ("true","1","yes")]
    print(f"\nPrompt version: {version}")
    print(f"Rows matched: {len(valid)}")
    print(f"Category accuracy: {cat_acc:.1%} ({sum(r['category'].strip()==e['expected_category'] for r,e in cat_scored)}/{len(cat_scored)})")
    print(f"Priority accuracy: {pri_acc:.1%} ({sum(r['priority'].strip()==e['expected_priority'] for r,e in pri_scored)}/{len(pri_scored)})")
    print(f"JSON valid rate (reported by evaluator): {len(json_valid)/len(valid):.1%} ({len(json_valid)}/{len(valid)})")
    scored = []
    for r in valid:
        try:
            scored.append(float(r["reply_quality_1_to_5"]))
        except (KeyError, ValueError):
            pass
    if scored:
        print(f"Mean reply-quality score: {sum(scored)/len(scored):.2f}/5 (human-assigned scores)")
    grounding = [r for r in valid if r.get("grounding_ok","").strip().lower() in ("true","false","1","0","yes","no")]
    if grounding:
        yes = sum(r["grounding_ok"].strip().lower() in ("true","1","yes") for r in grounding)
        print(f"Grounding pass rate: {yes/len(grounding):.1%} ({yes}/{len(grounding)})")
    print("Review misclassifications in the CSV; aggregate scores do not replace error analysis.")
