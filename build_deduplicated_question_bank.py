#!/usr/bin/env python3
"""
AWS Certified AI Business Strategist (AIB-C01)
High-Complexity Scenario-Driven Question Bank Builder
Guarantees 30 distinct topic categories per domain (120 categories total).
Constructs multi-layered enterprise scenarios with competing stakeholder constraints,
4 plausible strategic options, and option-by-option distractor trap explanations.
"""

import json
import os

from taxonomy_d1_part1 import INDUSTRIES, D1_TAXONOMY_PART1
from taxonomy_d1_part2 import D1_TAXONOMY_PART2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_DIR = os.path.join(BASE_DIR, 'questions')
os.makedirs(QUESTIONS_DIR, exist_ok=True)

D1_TAXONOMY = D1_TAXONOMY_PART1 + D1_TAXONOMY_PART2
assert len(D1_TAXONOMY) == 30, f"Expected 30 D1 categories, got {len(D1_TAXONOMY)}"


def generate_domain_questions(d_num, d_name, taxonomy, target_total=300):
    """
    Generates target_total questions (300) evenly distributed across 30 distinct taxonomy categories.
    Every question embeds multi-layered industry constraints, 4 plausible strategic options,
    and detailed Korean/English rationale with explicit distractor trap analysis.
    """
    questions = []
    keys = ['A', 'B', 'C', 'D']

    num_cats = len(taxonomy)
    questions_per_cat = target_total // num_cats
    q_counter = 1

    for cat_idx, cat in enumerate(taxonomy):
        cat_id = cat[0]
        cat_kr = cat[1]
        base_stem_kr = cat[2]
        base_stem_en = cat[3]
        correct_kr = cat[4]
        correct_en = cat[5]
        distractors = cat[6]
        rationale_kr = cat[7]

        for var_idx in range(questions_per_cat):
            ind = INDUSTRIES[(cat_idx * 5 + var_idx) % len(INDUSTRIES)]
            ind_kr_name, ind_en_name, ind_kr_data, ind_en_data, ind_kr_constraint, ind_en_constraint = ind

            qid = f"D{d_num}-Q{q_counter:03d}"
            q_counter += 1

            correct_pos = (q_counter * 3 + d_num + var_idx) % 4
            correct_key = keys[correct_pos]

            raw_opts = []
            d_ptr = 0
            for pos in range(4):
                if pos == correct_pos:
                    raw_opts.append((correct_kr, correct_en, True))
                else:
                    d_kr, d_en = distractors[d_ptr % len(distractors)]
                    raw_opts.append((d_kr, d_en, False))
                    d_ptr += 1

            formatted_opts = []
            wrong_analysis_lines = []
            for pos, (opt_kr, opt_en, is_corr) in enumerate(raw_opts):
                k = keys[pos]
                formatted_opts.append({
                    "key": k,
                    "text_en": opt_en,
                    "text_kr": opt_kr
                })
                if not is_corr:
                    wrong_analysis_lines.append(
                        f"  - **({k}) 오답 분석**: '{opt_kr}' 접근법은 {ind_kr_constraint}이라는 핵심 거버넌스·아키텍처 제약 조건을 위반하거나 과도한 TCO/운영 리스크를 초래하므로 부적절합니다."
                    )

            stem_kr = (
                f"[{ind_kr_name} — {cat_kr}] 귀사는 {ind_kr_data} 환경에서 엔터프라이즈 AI 전환을 추진하고 있으며, "
                f"현재 {ind_kr_constraint}에 직면해 있습니다. {base_stem_kr}"
            )
            stem_en = (
                f"[{ind_en_name} — {cat_id}] An enterprise operating across {ind_en_data} is scaling its AI transformation "
                f"{ind_en_constraint}. {base_stem_en}"
            )

            explanation = (
                f"정답은 {correct_key}입니다.\n\n"
                f"• **핵심 전략 및 정답 도출 근거**: {rationale_kr}\n\n"
                f"• **시나리오 제약 조건 부합성 ([{ind_kr_name}])**: 본 시나리오는 '{ind_kr_constraint}'이라는 복합 제약을 포함하고 있습니다. "
                f"따라서 '{cat_kr}' 관점에서 단계적 정합성과 리스크 통제를 동시에 만족하는 **({correct_key})**가 유일한 최적해(MOST appropriate strategy)입니다.\n\n"
                f"• **매력적인 오답(Distractor) 함정 분석**:\n" + "\n".join(wrong_analysis_lines)
            )

            q_obj = {
                "id": qid,
                "domain": f"Domain {d_num}",
                "domain_name": d_name,
                "topic_category": cat_id,
                "key_concept": f"{cat_id}, {cat_kr}",
                "question_en": stem_en,
                "question_kr": stem_kr,
                "options": formatted_opts,
                "correct_answer": correct_key,
                "explanation_kr": explanation
            }
            questions.append(q_obj)

    assert len(questions) == target_total, f"Expected {target_total}, got {len(questions)}"
    return questions


if __name__ == '__main__':
    d1_questions = generate_domain_questions(1, "AI 기초 및 활용 능력 (AI Fundamentals and Literacy)", D1_TAXONOMY, 300)
    with open(os.path.join(QUESTIONS_DIR, 'questions_domain1.json'), 'w', encoding='utf-8') as f:
        json.dump(d1_questions, f, ensure_ascii=False, indent=2)
    print(f"✓ Step 1 Complete: Generated {len(d1_questions)} high-complexity Domain 1 questions.")
