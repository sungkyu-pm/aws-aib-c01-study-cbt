#!/usr/bin/env python3
"""
AWS Certified AI Business Strategist (AIB-C01)
Deep-Dive Study Guide & Practice Question Synchronizer
Rebuilds generate_domain[1-4]_deepdive.py so every one of the 120 sections (30 per domain)
aligns 100% with the upgraded high-complexity AIB-C01 taxonomy (AI learning methodologies,
staged Envision-Experiment-Launch-Scale strategies, governance trade-offs) and embeds
the corresponding high-complexity practice question directly underneath each topic.
"""

import json
import os

from build_deduplicated_question_bank import D1_TAXONOMY
from generate_all_deduplicated_domains import D2_TAXONOMY, D3_TAXONOMY, D4_TAXONOMY

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_DIR = os.path.join(BASE_DIR, "questions")

DOMAIN_META = {
    1: {
        "title": "도메인 1: AI 기초 및 활용 능력 (AI Fundamentals and Literacy)",
        "weight": "20% (실전 시험 약 12~13문항 출제)",
        "objective": (
            "머신러닝 학습 패러다임(지도/비지도/강화학습, 자기지도 사전학습 ➔ SFT ➔ RLHF/DPO)과 "
            "모델 커스터마이징 단계별 우선순위(Prompting ➔ RAG ➔ PEFT/LoRA ➔ CPT/Distillation)를 비즈니스 제약 조건에 맞게 판별하고, "
            "하이브리드 RAG, 멀티 에이전트 오케스트레이션, RAG Triad/LLM-as-a-Judge 평가 및 데이터/개념 드리프트 대응 전략을 수립할 수 있는가?"
        ),
        "chapters": [
            ("제1장: AI 학습 방법론 및 커스터마이징 단계별 의사결정 (ML Paradigms & Customization Hierarchy)", 1, 6),
            ("제2장: 판별형 ML vs 생성형 AI 결합 및 추론 파라미터 제어 (Hybrid AI & Inference Control)", 7, 10),
            ("제3장: 엔터프라이즈 RAG 심화 아키텍처 (Chunking, Hybrid Search, Managed RAG & GraphRAG)", 11, 15),
            ("제4장: 모델 일반화, 합성 데이터 및 고급 프롬프트 엔지니어링 (Generalization & Prompting)", 16, 20),
            ("제5장: 프롬프트 인젝션 방어 및 자율 멀티 에이전트 아키텍처 (Security & Agentic AI)", 21, 24),
            ("제6장: 정량적 모델 평가(RAG Triad/LLM-as-a-Judge), 드리프트 감시 및 하이브리드 추론 (Evaluation & MLOps)", 25, 30),
        ],
        "taxonomy": D1_TAXONOMY,
        "func_name": "get_domain1_markdown",
    },
    2: {
        "title": "도메인 2: AI 전략 및 비즈니스 가치 창출 (AI Strategy & Business Value)",
        "weight": "31% (시험 내 최고 비중 영역! 약 19~20문항 출제)",
        "objective": (
            "Build vs Buy vs Partner의 단계적 포트폴리오 전환 전략을 수립하고, 빙산 아래의 숨은 TCO와 행동하지 않는 비용(COI), "
            "사전 베이스라인(Baseline) 기반 인과적 ROI를 정량 산출하며, 2x2 우선순위 매트릭스와 Go/No-Go 게이트로 PoC 연옥을 타파하고, "
            "AI FinOps(모델 라우팅, 시맨틱/프롬프트 캐싱, 과금 모델 최적화) 및 단위 경제학(Unit Economics)을 통제할 수 있는가?"
        ),
        "chapters": [
            ("제1장: 솔루션 조달 전략(Buy ➔ Partner ➔ Build) 및 데이터 주권 아키텍처 (Sourcing & Sovereignty)", 1, 3),
            ("제2장: 포괄적 AI TCO, 행동하지 않는 비용(COI) 및 매몰 비용 통제 (Financial Governance)", 4, 6),
            ("제3장: 사전 베이스라인 확립, 선행/후행 KPI 연계 및 정량적 ROI 모델링 (Value Measurement)", 7, 11),
            ("제4장: 2x2 포트폴리오 우선순위, PoC 연옥 탈출, 데이터 플라이휠 및 인과적 A/B 검증 (Portfolio & Scaling)", 12, 15),
            ("제5장: AI FinOps 운영 체계, 부서별 Chargeback 및 추론 단가 최적화 (AI FinOps & Cost Optimization)", 16, 21),
            ("제6장: 멀티 모델 전략, SDLC ROI, 비즈니스 모델 수익화 및 리스크 분산 (Monetization & Strategy)", 22, 30),
        ],
        "taxonomy": D2_TAXONOMY,
        "func_name": "get_domain2_markdown",
    },
    3: {
        "title": "도메인 3: AI 거버넌스 및 책임 있는 AI 리더십 (AI Governance & Responsible AI)",
        "weight": "27% (실전 시험 2위 핵심 비중! 약 16~17문항 출제)",
        "objective": (
            "전 생애주기(Pre-processing ➔ In-processing ➔ Post-processing)에 걸친 편향 감사와 설명 가능성(SHAP)을 구현하고, "
            "개인정보(PII) 이중 마스킹과 Amazon Bedrock Guardrails(Grounding Check, Denied Topics), 신뢰도 기반 HITL(Amazon A2I) 및 비상 Kill-Switch를 설계하며, "
            "EU AI Act 4단계 위험 등급, NIST AI RMF, ISO/IEC 42001, 공동 책임 모델 및 사고 대응 SOP를 집행할 수 있는가?"
        ),
        "chapters": [
            ("제1장: 생애주기별 책임 있는 AI(RAI), 편향 완화 및 설명 가능성(SHAP) (Fairness & Explainability)", 1, 5),
            ("제2장: 민감 정보(PII) 심층 방어, 데이터 비학습 보증 및 출처 워터마킹 (Privacy & Provenance)", 6, 8),
            ("제3장: Amazon Bedrock Guardrails, 환각 차단(Grounding Check), HITL(A2I) 및 비상 Kill-Switch (Runtime Safety)", 9, 13),
            ("제4장: EU AI Act 4대 위험 등급, NIST AI RMF 및 ISO/IEC 42001 글로벌 표준 (Regulatory Frameworks)", 14, 17),
            ("제5장: 차등 거버넌스 위원회, 공동 책임 모델, Model/System Cards 및 계보 추적 (Accountability & Lineage)", 18, 21),
            ("제6장: 저작권 면책(IP), 데이터 중독 방어, 에이전트 최소 권한 및 사고 대응 SOP (Security & Incident Response)", 22, 30),
        ],
        "taxonomy": D3_TAXONOMY,
        "func_name": "get_domain3_markdown",
    },
    4: {
        "title": "도메인 4: 비즈니스 준비성, 리더십, AI 혁신 (Business Readiness & Transformation)",
        "weight": "22% (실전 시험 약 13~14문항 출제)",
        "objective": (
            "People·Process·Technology·Governance 4대 준비성 차원과 AI 성숙도 4단계(Exploration ➔ Opportunistic ➔ Systematic ➔ Transformational) 전환 전략을 수립하고, "
            "AWS CAF 6대 관점 진단, 데이터 메시(DataZone/Lake Formation/Data Contracts) 현대화, Hub-and-Spoke AI CoE 및 AI 챔피언 변화 관리를 주도하며, "
            "Envision ➔ Experiment ➔ Launch ➔ Scale 4단계 구현과 비즈니스 프로세스 재설계(BPR)를 완수할 수 있는가?"
        ),
        "chapters": [
            ("제1장: AI 준비성 4대 차원, 조직 성숙도 1~4단계 진화 로드맵 및 AWS CAF 진단 (Readiness & Maturity)", 1, 5),
            ("제2장: 데이터 사일로 타파, 데이터 메시(DataZone/Lake Formation) 및 데이터 계약 (Data Modernization)", 6, 10),
            ("제3장: AI CoE 허브 앤 스포크 조직, AI 챔피언 네트워크 및 변화 관리/심리적 안전감 (CoE & Culture)", 11, 15),
            ("제4장: 직무별 맞춤형 업스킬링, 노코드 샌드박스 및 Envision-Experiment-Launch-Scale 4단계 구현 (Execution Lifecycle)", 16, 21),
            ("제5장: 비즈니스 프로세스 재설계(BPR), AI 기술 부채 청산 및 윤리 제보 거버넌스 (BPR & Tech Debt)", 22, 24),
            ("제6장: 다학제 AI 스쿼드, 성과 기반 인센티브 재정렬, 신뢰 보정 UX 및 레거시 현대화 (Operating Model & Scaling)", 25, 30),
        ],
        "taxonomy": D4_TAXONOMY,
        "func_name": "get_domain4_markdown",
    },
}


def format_practice_question(q):
    lines = [
        f"> ### 📝 기출 기반 고난도 실전 문제 (Real Exam Scenario Practice - {q['id']})",
        ">",
        f"> **Q. [{q['topic_category']}]**  ",
        f"> **🇺🇸 English Scenario**: {q['question_en']}  ",
        f"> **🇰🇷 한국어 시나리오**: {q['question_kr']}",
        ">",
    ]
    correct_key = q.get("correct_answer", "").strip().upper()
    for opt in q.get("options", []):
        key = opt["key"].strip().upper()
        text_en = opt["text_en"].strip()
        text_kr = opt["text_kr"].strip()
        if key == correct_key:
            lines.append(f"> * **({key})** **[정답]** {text_en}  \n>   *(🇰🇷 {text_kr})*")
        else:
            lines.append(f"> * **({key})** {text_en}  \n>   *(🇰🇷 {text_kr})*")
    lines.append(">")
    lines.append("> 💡 **정답 및 오답 함정 상세 해설 (Strategic Rationale & Distractor Analysis)**:  ")
    exp_kr = q.get("explanation_kr", "").strip()
    for exp_line in exp_kr.split("\n"):
        if exp_line.strip():
            lines.append(f"> {exp_line}")
        else:
            lines.append(">")
    return "\n".join(lines)


def build_domain_markdown(d_num):
    meta = DOMAIN_META[d_num]
    taxonomy = meta["taxonomy"]

    q_path = os.path.join(QUESTIONS_DIR, f"questions_domain{d_num}.json")
    with open(q_path, "r", encoding="utf-8") as f:
        q_list = json.load(f)

    md_lines = [
        f"# {meta['title']}",
        "",
        f"> **출제 비중 (Exam Weight)**: **{meta['weight']}**  ",
        f"> **공식 시험 평가 목표 (Exam Objective)**: {meta['objective']}",
        "",
        "---",
        "",
        f"## 📌 도메인 {d_num} 출제 로드맵 및 30대 핵심 전략 토픽",
        "실제 AIB-C01 시험은 단순 용어 암기가 아닌 **복합 제약 조건(예산 상한, 출시 기한, 데이터 주권, 인력 부족, 규제 감사) 하에서의 단계별 도입 및 대응 전략(MOST appropriate strategy)**을 묻습니다. 각 항목의 영문/국문 핵심 원리와 그 아래 배치된 실전 고난도 시나리오 문제를 함께 학습하세요.",
        "",
    ]

    for ch_title, s_idx, e_idx in meta["chapters"]:
        md_lines.append(f"* **{ch_title}** (Topic {d_num}.{s_idx} ~ {d_num}.{e_idx})")
    md_lines.append("")
    md_lines.append("---")

    chapter_start_map = {s_idx: ch_title for ch_title, s_idx, _ in meta["chapters"]}

    for idx, cat in enumerate(taxonomy, 1):
        cat_id, cat_kr, stem_kr, stem_en, corr_kr, corr_en, distractors, rationale_kr = cat
        if idx in chapter_start_map:
            md_lines.append("")
            md_lines.append(f"## {chapter_start_map[idx]}")
            md_lines.append("")

        # Representative question from questions_domain{d_num}.json rotating across diverse industries (Bio, Manufacturing, R&D, Retail, Distribution, etc.)
        rep_q = q_list[(idx - 1) * 10 + ((idx + d_num) % 10)]

        trap_bullets_en = "\n".join([f"  * *Common Exam Trap*: {d_en}" for _, d_en in distractors])
        trap_bullets_kr = "\n".join([f"  * *주의해야 할 오답 함정*: {d_kr}" for d_kr, _ in distractors])

        section_block = f"""### {d_num}.{idx} {cat_kr} ({cat_id})
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context & Strategic Trade-offs
* **Core Exam Scenario Dilemma**: {stem_en}
* **Optimal Strategic Decision (MOST Appropriate)**: **{corr_en}**
* **Plausible Distractor Archetypes to Eliminate**:
{trap_bullets_en}

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 단계별 대응 기준
* **실전 핵심 딜레마**: {stem_kr}
* **최적의 전략적 해법 (정답 기준)**: **{corr_kr}**
* **아키텍처 및 거버넌스 핵심 원리**:
  * {rationale_kr}
* **실전 시험 오답 소거 포인트**:
{trap_bullets_kr}

</div>
</div>

{format_practice_question(rep_q)}

---"""
        md_lines.append(section_block)

    return "\n".join(md_lines)


def main():
    for d_num in range(1, 5):
        meta = DOMAIN_META[d_num]
        md_content = build_domain_markdown(d_num)
        py_path = os.path.join(BASE_DIR, f"generate_domain{d_num}_deepdive.py")
        py_code = (
            f"# Domain {d_num} High-Complexity Deep Dive Generator (Covers all 30 Categories)\n\n"
            f"def {meta['func_name']}():\n"
            f"    return {json.dumps(md_content, ensure_ascii=False)}\n"
        )
        with open(py_path, "w", encoding="utf-8") as f:
            f.write(py_code)
        print(f"✓ Rebuilt generate_domain{d_num}_deepdive.py ({len(md_content):,} chars)")


if __name__ == "__main__":
    main()
