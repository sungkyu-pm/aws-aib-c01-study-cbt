#!/usr/bin/env python3
"""
AWS Certified AI Business Strategist (AIB-C01)
High-Complexity Scenario-Driven Question Bank Builder
Guarantees 30 distinct topic categories per domain (120 categories total).
Constructs multi-layered enterprise scenarios combining:
- 16 Diverse Industry Domains (Bio/Pharma, Smart Manufacturing, Corporate R&D, Omnichannel Retail, Cold-Chain Distribution, etc.)
- 10 C-Suite / Executive Decision-Making Archetypes (CEO, CFO, CISO/CLO, COO, CHRO, CMO/CPO, CIO/CTO, CDO, LOB VP, Board Steering Committee)
- 4 Plausible Strategic Options & Option-by-Option Distractor Trap Analysis
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

# 10 Distinct C-Suite / Executive Decision-Making & Stakeholder Conflict Archetypes
EXECUTIVE_CONTEXTS = [
    (
        "이사회 및 CEO vs CFO 투자 심의 갈등",
        "Board & CEO vs. CFO Capital Allocation Conflict",
        "CEO는 경쟁사 대비 시장 선점(First-Mover Advantage)을 위해 즉각적인 전사 확장을 압박하는 반면, CFO는 불확실한 초기 수익성과 숨은 클라우드 운영비(OpEx) 폭증을 우려해 일괄 예산(Lump-sum) 승인을 보류하고 단계별 정량 검증(Stage-Gated Tranche Funding)을 요구하고 있습니다.",
        "While the CEO pushes for immediate enterprise-wide rollout to capture first-mover market share, the CFO has frozen lump-sum capital approval due to unverified unit economics and hidden cloud OpEx risks, demanding strict stage-gated tranche justification."
    ),
    (
        "CPO/CMO(비즈니스 속도) vs CISO/CLO(보안·법무 거부권) 대립",
        "CPO/CMO Speed-to-Market vs. CISO/CLO Risk Veto",
        "최고제품책임자(CPO)와 CMO는 이번 분기 내 고객 대면 AI 신기능 출시(Fast TTM)를 강행하려 하나, 정보보안 최고책임자(CISO)와 법무실장(CLO)은 데이터 주권 위반, 프롬프트 인젝션, 제3자 IP 침해 및 규제 과징금 리스크가 통제되지 않으면 배포 거부권(Veto)을 행사하겠다고 통보한 상태입니다.",
        "The CPO and CMO demand launching customer-facing AI capabilities this quarter, whereas the CISO and General Counsel (CLO) have threatened an immediate deployment veto unless data sovereignty, adversarial prompt injection, and regulatory liability risks are deterministically mitigated."
    ),
    (
        "COO(운영 효율화) vs CHRO/현장 노조(직무 불안 및 변화 저항) 충돌",
        "COO Operational Automation vs. CHRO Workforce & Union Resistance",
        "최고운영책임자(COO)는 처리 시간(AHT) 40% 단축을 목표로 현장 도입을 서두르고 있으나, 최고인사책임자(CHRO)는 현장 실무자들의 고용 대체 불안감으로 인한 도구 보이콧, 자동화 편향(Rubber-stamping), 숙련 인력 이탈 리스크를 해결할 변화 관리 및 직무 재설계가 선행되어야 한다고 지적합니다.",
        "The COO mandates a 40% cycle-time reduction via rapid automation, but the CHRO warns that frontline fears of job replacement are driving passive sabotage, high turnover, and uncalibrated automation bias unless paired with augmentation-centered change management."
    ),
    (
        "CIO/중앙 플랫폼 팀 vs 현업 사업부장(LOB VP) 주도권 갈등",
        "Central CIO Standardization vs. Line-of-Business (LOB) VP Autonomy",
        "중앙 CIO 조직은 전사 표준 아키텍처와 보안 통제 일원화를 주장하는 반면, 각 현업 사업부 총괄 임원(VP)들은 중앙 IT의 느린 승인 대기열에 불만을 품고 자체 예산으로 개별 AI 솔루션을 도입(Shadow AI)하려 하여 거버넌스 파편화와 중복 투자가 우려되는 상황입니다.",
        "The central CIO insists on unified architectural governance, while Line-of-Business (LOB) VPs frustrated by central IT backlogs are threatening to procure fragmented Shadow AI tools independently, risking massive duplication and compliance blind spots."
    ),
    (
        "CDO(최고데이터책임자) vs R&D/사업부 간 데이터 소유권 사일로 분쟁",
        "Chief Data Officer (CDO) vs. Departmental Data Hoarding & Silos",
        "CDO는 전사 AI 정확도 향상을 위해 부서 간 통합 데이터 파이프라인 구축을 추진 중이나, 개별 사업부 및 R&D 임원들은 자부서 데이터의 품질 책임 소재 불명확성과 기밀 유출을 이유로 원천 데이터 공유를 거부하고 있어 경영진 차원의 데이터 거버넌스 결단이 필요한 시점입니다.",
        "The Chief Data Officer (CDO) is championing cross-enterprise data integration for AI, but departmental VPs and R&D directors refuse to share proprietary domain datasets due to unclear liability and access controls, requiring an executive federated governance ruling."
    ),
    (
        "AI 운영위원회(Steering Committee)의 PoC 연옥 및 매몰 비용 결단",
        "AI Steering Committee PoC Purgatory & Sunk-Cost Decision Gate",
        "분기별 AI 임원 운영위원회(Steering Committee) 감사에서 수개월간 막대한 예산이 투입된 과제가 프로덕션 확장 요건(지연 시간, 정확도, 단위 비용)을 충족하지 못했음이 드러났으나, 과제 스폰서 임원이 매몰 비용(Sunk Cost)을 이유로 추가 예산 투입을 고집하고 있어 객관적인 Go/No-Go 결단이 요구됩니다.",
        "During a quarterly AI Steering Committee review, a heavily funded initiative fails production-readiness gates on latency, accuracy, and unit cost, yet the sponsoring executive lobbies to double funding to recover sunk costs, forcing an objective Go/No-Go governance decision."
    ),
    (
        "수동적 명목상 임원 스폰서십(Figurehead)에서 능동적 실행 리더십으로의 전환",
        "Transitioning from Passive Figurehead to Active Executive Sponsorship",
        "초기 킥오프 행사에만 참석하고 실제 부서 간 R&R 조율, 예산 장애물 제거, 인사 평가(KPI) 재정렬에는 관여하지 않는 '명목상 임원 스폰서십(Passive Sponsorship)'으로 인해 중간 관리자들의 비협조가 심화되어, 임원진의 실질적인 의사결정 개입 형태를 재정의해야 하는 상황입니다.",
        "Because executive sponsors have acted merely as passive figureheads—attending kickoff events without resolving cross-unit political roadblocks or realigning manager KPIs—middle-management inertia has stalled execution, demanding active executive governance."
    ),
    (
        "글로벌 본사 임원진(HQ) vs 지역 지사장(Regional Directors) 규제·로컬라이제이션 조율",
        "Global HQ Executive Mandate vs. Regional Regulatory Localization",
        "글로벌 본사 경영진은 단일 AI 모델과 정책의 전 세계 일괄 배포를 원하지만, 유럽·아시아 등 지역 지사장들은 국가별 상이한 데이터 거주성(Data Residency) 법규, EU AI Act 고위험 적합성 의무, 로컬 언어·문화적 편향 차이를 반영한 차등 아키텍처를 요구하고 있습니다.",
        "Global HQ executives want a single uniform AI deployment worldwide, whereas Regional Directors warn that strict national Data Residency laws, EU AI Act High-Risk conformity rules, and local linguistic nuances require a federated regional architecture."
    ),
    (
        "CRO(최고리스크책임자) 및 감사위원회의 블랙박스 설명 가능성·감사 추적 명령",
        "Chief Risk Officer (CRO) & Audit Committee Explainability Mandate",
        "기업 리스크 관리 위원회와 CRO는 외부 규제 기관의 불시 감사 및 소비자 집단 소송에 대비하여, AI의 의사결정 근거를 비기술 임원과 규제 감독관이 즉시 이해할 수 있게 투명화하고 데이터부터 추론까지 100% 역추적(Lineage) 가능한 통제 체계를 구축할 것을 조건부 승인 요건으로 내걸었습니다.",
        "The Chief Risk Officer (CRO) and Audit Committee have issued a conditional mandate: production approval is contingent upon proving human-understandable explainability to regulators and maintaining immutable end-to-end lineage across all model decisions."
    ),
    (
        "차기 연도 이사회 포트폴리오 배분: 단기 비용 절감(Efficiency) vs 신규 수익 모델(Monetization)",
        "Annual Board Portfolio Rebalancing: Cost Efficiency vs. Top-Line Monetization",
        "차기 회계연도 AI 예산 심의에서 보수적인 사외이사들은 확실한 백오피스 원가 절감(Quick Wins)에만 집중할 것을 주문하는 반면, 성장 전략 임원들은 독점 데이터 플라이휠을 활용한 유료 AI 프로덕트 출시(Strategic Bets)를 요구하고 있어 균형 잡힌 임원진 포트폴리오 의사결정이 필요한 상황입니다.",
        "In the annual Board budget session, conservative directors demand focusing 100% on auditable back-office cost savings, while growth executives push for customer-facing AI monetization bets, requiring a balanced Horizon 1–2–3 portfolio strategy."
    )
]


def generate_domain_questions(d_num, d_name, taxonomy, target_total=300):
    """
    Generates target_total questions (300) evenly distributed across 30 distinct taxonomy categories.
    Every question embeds:
    - 1 of 16 specialized industry domains (Bio, Manufacturing, R&D, Retail, Distribution, etc.)
    - 1 of 10 C-Suite / Executive Decision-Making contexts
    - 4 plausible strategic options & detailed option-by-option distractor trap analysis
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
            ind = INDUSTRIES[(cat_idx * 3 + d_num * 2 + var_idx) % len(INDUSTRIES)]
            ind_kr_name, ind_en_name, ind_kr_data, ind_en_data, ind_kr_constraint, ind_en_constraint = ind

            exec_ctx = EXECUTIVE_CONTEXTS[(cat_idx + d_num + var_idx) % len(EXECUTIVE_CONTEXTS)]
            exec_title_kr, exec_title_en, exec_desc_kr, exec_desc_en = exec_ctx

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
                        f"  - **({k}) 오답 분석**: '{opt_kr}' 선택지는 [{exec_title_kr}] 상황에서 요구되는 거버넌스 균형을 무너뜨리고, {ind_kr_constraint}이라는 산업 도메인 제약을 위반하므로 부적절합니다."
                    )

            stem_kr = (
                f"[{ind_kr_name} | 임원 의사결정: {exec_title_kr}] 귀사는 {ind_kr_data} 환경에서 AI 전환을 추진하며 "
                f"{ind_kr_constraint}에 놓여 있습니다. 특히 경영진 회의에서 {exec_desc_kr} {base_stem_kr}"
            )
            stem_en = (
                f"[{ind_en_name} | Executive Governance: {exec_title_en}] An enterprise operating across {ind_en_data} is scaling AI "
                f"{ind_en_constraint}. At the executive level, {exec_desc_en} {base_stem_en}"
            )

            explanation = (
                f"정답은 {correct_key}입니다.\n\n"
                f"• **핵심 전략 및 정답 도출 근거**: {rationale_kr}\n\n"
                f"• **임원진 의사결정 조율 ([{exec_title_kr}])**: {exec_desc_kr} 이 갈등을 해결하기 위해 AI 비즈니스 전략가는 일방적인 강행이나 전면 중단이 아닌, 정량적 게이트와 안전망이 결합된 **({correct_key})**를 경영진 합의안으로 도출해야 합니다.\n\n"
                f"• **산업 도메인 제약 부합성 ([{ind_kr_name}])**: '{ind_kr_constraint}'이라는 도메인 특수성을 가장 안전하고 경제적으로 충족합니다.\n\n"
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
    print(f"✓ Generated {len(d1_questions)} executive-scenario Domain 1 questions.")
