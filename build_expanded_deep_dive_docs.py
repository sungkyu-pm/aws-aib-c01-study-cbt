#!/usr/bin/env python3
"""
AWS Certified AI Business Strategist (AIB-C01)
Expanded Deep-Dive Bilingual Study Guide Generator & Synchronizer
"""

import os
import json

from generate_domain1_deepdive import get_domain1_markdown
from generate_domain2_deepdive import get_domain2_markdown
from generate_domain3_deepdive import get_domain3_markdown
from generate_domain4_deepdive import get_domain4_markdown
from generate_aws_services_deepdive import get_aws_services_markdown

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
os.makedirs(DOCS_DIR, exist_ok=True)

def main():
    print("=== Generating Comprehensive In-Depth Study Guides ===")
    
    # Read existing 00 and 01
    with open(os.path.join(DOCS_DIR, '00_AIB-C01_EXAM_GUIDE.md'), 'r', encoding='utf-8') as f:
        exam_guide_content = f.read()

    with open(os.path.join(DOCS_DIR, '01_GLOSSARY_KR_EN.md'), 'r', encoding='utf-8') as f:
        glossary_content = f.read()

    d1_content = get_domain1_markdown()
    d2_content = get_domain2_markdown()
    d3_content = get_domain3_markdown()
    d4_content = get_domain4_markdown()
    aws_services_content = get_aws_services_markdown()

    files = {
        '00_AIB-C01_EXAM_GUIDE.md': exam_guide_content,
        '01_GLOSSARY_KR_EN.md': glossary_content,
        '02_DOMAIN_1_AI_FUNDAMENTALS.md': d1_content,
        '03_DOMAIN_2_AI_STRATEGY_VALUE.md': d2_content,
        '04_DOMAIN_3_GOVERNANCE_RESPONSIBLE_AI.md': d3_content,
        '05_DOMAIN_4_TRANSFORMATION_READINESS.md': d4_content,
        '06_AWS_SERVICES_CHEAT_SHEET.md': aws_services_content
    }

    # Write each file in docs/
    for filename, content in files.items():
        filepath = os.path.join(DOCS_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Written {filename} ({len(content)} chars)")

    # Prepare portal-docs-data.js
    portal_docs = {
        'overview': exam_guide_content,
        'exam_guide': exam_guide_content,
        'glossary': glossary_content,
        'domain1': d1_content,
        'domain2': d2_content,
        'domain3': d3_content,
        'domain4': d4_content,
        'aws_services': aws_services_content
    }

    js_code = (
        "// AWS Certified AI Business Strategist (AIB-C01) Complete Bilingual Study Materials\n"
        "// Exhaustive 120-Topic Taxonomy & Exam Question Matching in Dual-Track Layout\n"
        f"const PORTAL_DOCS = {json.dumps(portal_docs, ensure_ascii=False, indent=2)};\n\n"
        "if (typeof window !== 'undefined') {\n  window.PORTAL_DOCS = PORTAL_DOCS;\n}\n"
        "if (typeof module !== 'undefined' && module.exports) {\n  module.exports = PORTAL_DOCS;\n}\n"
    )

    portal_js_path = os.path.join(BASE_DIR, 'portal-docs-data.js')
    with open(portal_js_path, 'w', encoding='utf-8') as f:
        f.write(js_code)
    print(f"✓ Synchronized portal-docs-data.js ({len(js_code)} bytes)")

    print("\n🎉 ALL COMPREHENSIVE STUDY GUIDES SUCCESSFULLY EXPANDED & SYNCHRONIZED! 🎉")

if __name__ == '__main__':
    main()
