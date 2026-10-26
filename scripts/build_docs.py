import os
import json
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
DOCS_DIR = os.path.join(BASE_DIR, "docs")
os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(os.path.join(DOCS_DIR, "static", "css"), exist_ok=True)
os.makedirs(os.path.join(DOCS_DIR, "static", "js"), exist_ok=True)

with open(os.path.join(DATA_DIR, "methods.yaml"), "r", encoding="utf-8") as f:
    methods_data = yaml.safe_load(f)["methods"]

with open(os.path.join(DATA_DIR, "rules.yaml"), "r", encoding="utf-8") as f:
    rules_data = yaml.safe_load(f)["rules"]

with open(os.path.join(DATA_DIR, "benchmark_scenarios.yaml"), "r", encoding="utf-8") as f:
    benchmarks_data = yaml.safe_load(f)["benchmarks"]

js_data = f"""// Auto-generated data bundle for GitHub Pages
const METHODS_DATA = {json.dumps(methods_data, indent=2)};
const RULES_DATA = {json.dumps(rules_data, indent=2)};
const BENCHMARKS_DATA = {json.dumps(benchmarks_data, indent=2)};
"""

with open(os.path.join(DOCS_DIR, "static", "js", "data.js"), "w", encoding="utf-8") as f:
    f.write(js_data)

print(f"Exported data.js: {len(methods_data)} methods, {len(rules_data)} rules, {len(benchmarks_data)} benchmarks.")
