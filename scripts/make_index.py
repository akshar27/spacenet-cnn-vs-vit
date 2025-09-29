import json, csv, pathlib
root = pathlib.Path("outputs")
rows = []
for run in root.iterdir():
    if not run.is_dir(): 
        continue
    m = run / "metrics.json"
    if m.exists():
        d = json.loads(m.read_text())
        rows.append({
            "run": run.name,
            "accuracy": d.get("accuracy"),
            "macro_f1": d.get("macro_f1"),
            "precision_macro": d.get("precision_macro"),
            "recall_macro": d.get("recall_macro"),
            "num_test": d.get("num_test"),
        })
rows = sorted(rows, key=lambda r: r["run"])
with open(root / "index.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader(); w.writerows(rows)
print("Wrote", root/"index.csv")
