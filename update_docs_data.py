#!/usr/bin/env python3
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, 'docs')

file_map = {
    'exam_guide': '00_AIB-C01_EXAM_GUIDE.md',
    'glossary': '01_GLOSSARY_KR_EN.md',
    'domain1': '02_DOMAIN_1_AI_FUNDAMENTALS.md',
    'domain2': '03_DOMAIN_2_AI_STRATEGY_VALUE.md',
    'domain3': '04_DOMAIN_3_GOVERNANCE_RESPONSIBLE_AI.md',
    'domain4': '05_DOMAIN_4_TRANSFORMATION_READINESS.md',
    'aws_services': '06_AWS_SERVICES_CHEAT_SHEET.md'
}

docs = {}
for k, filename in file_map.items():
    filepath = os.path.join(DOCS_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        docs[k] = f.read()

js_content = f"const PORTAL_DOCS = {json.dumps(docs, ensure_ascii=False, indent=2)};\n\nif (typeof window !== 'undefined') {{\n  window.PORTAL_DOCS = PORTAL_DOCS;\n}}\n"

with open(os.path.join(BASE_DIR, 'portal-docs-data.js'), 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Updated portal-docs-data.js ({len(js_content)} bytes)")
