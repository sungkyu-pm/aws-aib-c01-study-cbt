#!/usr/bin/env python3
"""
AWS Certified AI Business Strategist (AIB-C01)
Complete 120-Category High-Complexity Question Bank Generator
- 30 distinct topic categories per domain (Total 120 categories).
- 10 diverse, multi-constraint enterprise scenarios per category (300 questions per domain, 1,200 total).
- Explicit `topic_category` on every question for 100% duplicate-free CBT sampling.
"""

import json
import os

from build_deduplicated_question_bank import D1_TAXONOMY, generate_domain_questions
from taxonomy_d2_part1 import D2_TAXONOMY_PART1
from taxonomy_d2_part2 import D2_TAXONOMY_PART2
from taxonomy_d3_part1 import D3_TAXONOMY_PART1
from taxonomy_d3_part2 import D3_TAXONOMY_PART2
from taxonomy_d4_part1 import D4_TAXONOMY_PART1
from taxonomy_d4_part2 import D4_TAXONOMY_PART2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_DIR = os.path.join(BASE_DIR, 'questions')
os.makedirs(QUESTIONS_DIR, exist_ok=True)

D2_TAXONOMY = (D2_TAXONOMY_PART1 + D2_TAXONOMY_PART2)[:30]
D3_TAXONOMY = (D3_TAXONOMY_PART1 + D3_TAXONOMY_PART2)[:30]
D4_TAXONOMY = (D4_TAXONOMY_PART1 + D4_TAXONOMY_PART2)[:30]

assert len(D1_TAXONOMY) == 30, f"D1 count {len(D1_TAXONOMY)}"
assert len(D2_TAXONOMY) == 30, f"D2 count {len(D2_TAXONOMY)}"
assert len(D3_TAXONOMY) == 30, f"D3 count {len(D3_TAXONOMY)}"
assert len(D4_TAXONOMY) == 30, f"D4 count {len(D4_TAXONOMY)}"


def main():
    print("=== Generating Full 1,200 High-Complexity Question Bank across 120 Categories ===")

    # 1. Domain 1 (30 categories x 10 = 300 questions)
    d1 = generate_domain_questions(1, "AI 기초 및 활용 능력 (AI Fundamentals and Literacy)", D1_TAXONOMY, 300)
    print(f"✓ Domain 1: Generated {len(d1)} questions across {len(D1_TAXONOMY)} categories.")

    # 2. Domain 2 (30 categories x 10 = 300 questions)
    d2 = generate_domain_questions(2, "AI 전략 및 비즈니스 가치 창출 (AI Strategy & Business Value Creation)", D2_TAXONOMY, 300)
    print(f"✓ Domain 2: Generated {len(d2)} questions across {len(D2_TAXONOMY)} categories.")

    # 3. Domain 3 (30 categories x 10 = 300 questions)
    d3 = generate_domain_questions(3, "AI 거버넌스 및 책임 있는 AI 리더십 (AI Governance & Responsible AI Leadership)", D3_TAXONOMY, 300)
    print(f"✓ Domain 3: Generated {len(d3)} questions across {len(D3_TAXONOMY)} categories.")

    # 4. Domain 4 (30 categories x 10 = 300 questions)
    d4 = generate_domain_questions(4, "비즈니스 준비성, 리더십, AI 혁신 (Business Readiness, Leadership & Transformation)", D4_TAXONOMY, 300)
    print(f"✓ Domain 4: Generated {len(d4)} questions across {len(D4_TAXONOMY)} categories.")

    # Save each domain JSON
    with open(os.path.join(QUESTIONS_DIR, 'questions_domain1.json'), 'w', encoding='utf-8') as f:
        json.dump(d1, f, ensure_ascii=False, indent=2)
    with open(os.path.join(QUESTIONS_DIR, 'questions_domain2.json'), 'w', encoding='utf-8') as f:
        json.dump(d2, f, ensure_ascii=False, indent=2)
    with open(os.path.join(QUESTIONS_DIR, 'questions_domain3.json'), 'w', encoding='utf-8') as f:
        json.dump(d3, f, ensure_ascii=False, indent=2)
    with open(os.path.join(QUESTIONS_DIR, 'questions_domain4.json'), 'w', encoding='utf-8') as f:
        json.dump(d4, f, ensure_ascii=False, indent=2)
    print("✓ All 4 domain JSON files written.")

    # Canonical Mock Exam 1: 60 questions from 60 distinct categories weighted by official exam blueprint
    # D1 (20%): 12 questions, D2 (31%): 19 questions, D3 (27%): 16 questions, D4 (22%): 13 questions
    mock_qs = []
    for c_idx in range(12):
        mock_qs.append(d1[c_idx * 10 + (c_idx % 10)])
    for c_idx in range(19):
        mock_qs.append(d2[c_idx * 10 + (c_idx % 10)])
    for c_idx in range(16):
        mock_qs.append(d3[c_idx * 10 + (c_idx % 10)])
    for c_idx in range(13):
        mock_qs.append(d4[c_idx * 10 + (c_idx % 10)])

    assert len(mock_qs) == 60, f"Expected 60 mock questions, got {len(mock_qs)}"

    with open(os.path.join(QUESTIONS_DIR, 'mock_exam_1.json'), 'w', encoding='utf-8') as f:
        json.dump(mock_qs, f, ensure_ascii=False, indent=2)
    print("✓ Canonical 60-question mock exam written (60 distinct categories, varied industries).")

    # Combine all into questions-data.js
    all_pool = d1 + d2 + d3 + d4
    exam_data = {
        "domain1": d1,
        "domain2": d2,
        "domain3": d3,
        "domain4": d4,
        "mock1": mock_qs,
        "all_pool": all_pool
    }

    js_content = (
        "// AWS Certified AI Business Strategist (AIB-C01) High-Complexity Question Bank\n"
        f"// Total {len(all_pool)} Questions across 120 Distinct Topic Categories (30 per Domain)\n"
        f"const EXAM_DATA = {json.dumps(exam_data, ensure_ascii=False, indent=2)};\n\n"
        "if (typeof window !== 'undefined') {\n  window.EXAM_DATA = EXAM_DATA;\n}\n"
        "if (typeof module !== 'undefined' && module.exports) {\n  module.exports = EXAM_DATA;\n}\n"
    )

    with open(os.path.join(BASE_DIR, 'questions-data.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)
    cbt_app_dir = os.path.join(BASE_DIR, 'cbt-app')
    if os.path.isdir(cbt_app_dir):
        with open(os.path.join(cbt_app_dir, 'questions-data.js'), 'w', encoding='utf-8') as f:
            f.write(js_content)
    print("✓ Synchronized questions-data.js and cbt-app/questions-data.js")
    print("\n🎉 ALL 1,200 HIGH-COMPLEXITY QUESTIONS GENERATED & COMPILED! 🎉")


if __name__ == '__main__':
    main()
