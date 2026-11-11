#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part 1 of the Master Glossary & Exam Expressions Builder for AWS AIB-C01.
Generates:
- Section 1: Green-Flag (정답 시그널) vs. Red-Flag (오답 함정 시그널) 실전 영어/한국어 상용구 사전
- Section 2: C-Suite 임원진 의사결정 & 재무/거버넌스 핵심 표현 사전
- Section 3: AI/ML 학습 방법론 & 모델 최적화 핵심 표현 사전
"""

PART1_MD = """# 📖 AWS Certified AI Business Strategist (AIB-C01) 마스터 용어사전 & 실전 시험 표현집 (Master Glossary & Exam Idioms)

> **본 용어사전의 목적**: 실제 `AIB-C01` 시험은 단순 약어 암기가 아니라, **전략적 의사결정 맥락에서 쓰이는 고급 비즈니스/아키텍처 관용구(Idioms), 임원진(C-Suite) 거버넌스 용어, AI/ML 학습 방법론, 그리고 산업별(바이오·제조·R&D·유통·소매·금융) 실무 표현**을 정확히 독해할 수 있는지를 평가합니다.
> 시험장에서 선지를 읽자마자 **정답 시그널(Green Flag)** 과 **매력적인 오답 함정(Red Flag)** 을 3초 만에 판별할 수 있도록 핵심 표현과 마스터 용어를 6개 파트로 체계화했습니다.

---

## 🎯 Part 1. 실전 시험 정답 시그널(Green Flags) vs. 오답 함정(Red Flags) 필수 관용구 사전

실제 시험의 긴 영어/한국어 선지에서 **반복적으로 등장하는 정답 표현과 오답 함정 표현**을 대비한 실전 판별 사전입니다.

### 1-1. 전략·재무·의사결정 핵심 관용구 (Strategy, FinOps & Decision Idioms)

| 실전 시험 표현 (English / Korean) | 판별 신호 | 실전 의미 및 시험 출제 맥락 (Exam Context & Trap Analysis) |
| :--- | :---: | :--- |
| **Undifferentiated Heavy Lifting**<br>(비차별화 중노동 / 범용 반복 인프라 작업) | 🟢 **정답 신호** | 기업의 고유 경쟁력(Core IP)과 무관한 범용 작업(인프라 구축, 기본 OCR/번역, 범용 LLM 밑바닥 훈련). 시험에서는 **"Managed AI Service(SaaS/API)를 Buy하여 외주화/제거해야 할 대상"** 으로 등장합니다. |
| **Core Competitive Differentiator**<br>(핵심 경쟁 차별화 요소 / 독점적 해자) | 🟢 **정답 신호** | 경쟁사가 복제할 수 없는 당사만의 고유 알고리즘·독점 R&D 데이터. 시험에서는 **"Proprietary Custom Build 또는 PEFT/RAG로 내재화해야 할 영역"** 으로 등장합니다. |
| **Stage-Gated Tranche / Metered Funding**<br>(단계별 관문 기반 분할 펀딩) | 🟢 **정답 신호** | 대규모 일괄 예산(Upfront CapEx) 대신, `Envision ➔ Experiment ➔ Launch ➔ Scale` 각 단계의 KPI/비즈니스 가설 검증을 통과할 때마다 다음 예산을 집행하는 **CFO/투자심의위원회의 모범 재무 통제 방식**입니다. |
| **Build-Operate-Transfer (BOT) & Co-Delivery**<br>(구축-운영-이전 파트너십 및 공동 수행) | 🟢 **정답 신호** | 내부 AI 역량은 부족하지만 독점 IP 내재화가 필요할 때, 외부 파트너와 **혼성 스쿼드(Co-Delivery)** 로 구축한 뒤 **지식 이전(Knowledge Transfer) 마일스톤을 계약에 명시하여 점진적으로 내재화**하는 정답 패턴입니다. |
| **Paving the Cow Path**<br>(비효율적인 기존 수작업 프로세스를 그대로 자동화함) | 🔴 **오답 함정** | 레거시 병목이나 불필요한 결재 단계를 재설계(`BPR: Business Process Re-engineering`)하지 않고 옛날 방식 위에 AI만 덧씌우는 실패 패턴입니다. |
| **Sunk Cost Fallacy**<br>(매몰 비용의 오류) | 🔴 **오답 함정** | 이미 투입한 예산과 시간이 아까워 비즈니스 가치가 없거나 데이터 드리프트가 심각한 AI 프로젝트를 중단(Kill/Pivot)하지 못하고 추가 예산을 투입하는 오답 패턴입니다. |
| **Vanity Metrics vs. Actionable Value KPIs**<br>(허수 지표 vs. 실행 가능한 비즈니스 가치 KPI) | 🟢/🔴 **비교 핵심** | 단순 누적 챗봇 로그인 수·프롬프트 호출 건수는 **Vanity Metric(오답)** 이며, `First-Contact Resolution(FCR)`, `Cost per Resolved Ticket`, `Retention Uplift`가 **진정한 Value KPI(정답)** 입니다. |
| **Showback ➔ Chargeback**<br>(클라우드/토큰 비용 가시화 ➔ 부서별 예산 실청구) | 🟢 **정답 신호** | 현업 부서의 무분별한 프롬프트/토큰 오남용을 막기 위해 태깅(`Cost Allocation Tags`)으로 부서별 사용량을 공개(`Showback`)하고 실제 부서 예산에서 차감(`Chargeback`)하는 **AI FinOps 핵심 거버넌스**입니다. |
| **Semantic Caching & Prompt Caching**<br>(시맨틱 캐싱 및 프롬프트 프리픽스 캐싱) | 🟢 **정답 신호** | 유사한 질문의 기존 응답을 벡터 유사도로 재활용(`Semantic Caching`)하거나 반복되는 긴 시스템 지시문/문서를 캐싱(`Prompt Caching`)하여 **추론 단가(Token Cost)와 지연시간(Latency)을 60~80% 절감**하는 기법입니다. |
| **Tiered Model Routing / Model Cascading**<br>(계층형 모델 라우팅 / 모델 캐스케이딩) | 🟢 **정답 신호** | 모든 질의를 고비용 Frontier LLM으로 보내지 않고, 경량 분류기/라우터가 **단순 질의(70~80%)는 SLM(소형 모델)으로, 고난도 추론(20%)만 Frontier 모델로 분기**시켜 단위 경제성(`Unit Economics`)을 달성하는 정답 아키텍처입니다. |
| **Shadow Deployment / Dark Launch**<br>(섀도우 배포 / 다크 런치) | 🟢 **정답 신호** | 실제 고객에게 영향을 주지 않고 프로덕션 실시간 트래픽을 복제(Mirroring)하여 신규 AI 모델의 성능·지연시간·드리프트를 기존 시스템과 병렬 검증하는 안전한 출시 전략입니다. |
| **Big-Bang Cutover / Rip-and-Replace**<br>(전면 일괄 교체 / 기존 시스템 일거 철거) | 🔴 **오답 함정** | 기존 레거시 ERP/MES를 하루아침에 내리고 검증되지 않은 AI 시스템으로 100% 전환하는 고위험 방식입니다. 정답은 항상 **Strangler Fig Pattern(점진적 우회 전환)** 또는 **Canary/Phased Rollout** 입니다. |

---

### 1-2. 거버넌스·보안·책임 있는 AI 핵심 관용구 (Governance, Risk & Responsible AI Idioms)

| 실전 시험 표현 (English / Korean) | 판별 신호 | 실전 의미 및 시험 출제 맥락 (Exam Context & Trap Analysis) |
| :--- | :---: | :--- |
| **Shift-Left Governance / Governance-by-Design**<br>(거버넌스 좌측 이동 / 설계 단계 내재화) | 🟢 **정답 신호** | 배포 직전 사후 감사(Late-stage audit)가 아니라, **문제 정의·데이터 수집 초기 단계(Envision/Design)부터 법무·보안·윤리 가드레일을 파이프라인에 자동 내재화**하는 원칙입니다. |
| **Risk-Tiered Governance Triage (Fast-Track vs. Deep Review)**<br>(위험 등급별 차등 거버넌스 심사) | 🟢 **정답 신호** | 모든 AI 과제를 똑같이 느리게 심사하지 않고, **내부 저위험 과제는 자동화된 가드레일(Fast-Track)로 즉시 승인**하고 **고객 대면·고위험 과제만 심층 위원회 심사(Deep Review)** 로 집중하는 전략입니다. |
| **Fairness Through Unawareness**<br>(민감 변수 단순 삭제를 통한 공정성 착시) | 🔴 **오답 함정** | 성별·인종·연령 컬럼만 지우면 공정해질 것이라 믿는 치명적 함정입니다. 우편번호(`Zip Code`), 구매 시간대 등 **대리 변수(Proxy Variables)** 를 통해 편향이 그대로 재현되므로 반드시 **사전/사후 편향 측정(SageMaker Clarify)** 이 병행되어야 합니다. |
| **Forced Output Parity / Arbitrary Quota Adjustment**<br>(결과값 강제 동등 할당 / 사후 임의 조작) | 🔴 **오답 함정** | 편향 문제를 해결한다며 지원자의 실제 자격·위험도 점수를 무시하고 결과 비율을 인위적으로 50:50으로 강제 조정하는 오답입니다. 역차별 및 모델 정확도 붕괴를 초래합니다. |
| **Contextual Grounding Check & Automated Reasoning**<br>(문맥 기반 사실성 검증 및 수학적 자동 추론 검증) | 🟢 **정답 신호** | `Amazon Bedrock Guardrails`에서 LLM 답변이 검색된 출처 문서(Source Context)에 실제로 근거하는지 검증하고, 핵심 비즈니스 규칙을 논리적으로 위반하지 않는지 차단하는 **환각(Hallucination) 방지 핵심 기능**입니다. |
| **Confidence-Based HITL & Rubber-Stamping Prevention**<br>(신뢰도 임계치 기반 인간 개입 및 무비판적 승인 방지) | 🟢 **정답 신호** | 모든 건을 사람이 검수(100% 수동 검수 = 오답)하거나 무조건 자동 통과시키는 대신, **신뢰도 점수가 임계치 미달이거나 고위험인 건만 인간 전문가(`Amazon A2I`)에게 라우팅**하고, 검수자가 AI 추천을 맹목적으로 승인(`Automation Bias / Rubber-stamping`)하지 못하도록 근거 확인 UI를 강제하는 설계입니다. |
| **Principle of Least Privilege (PoLP) & Step-Up Auth for Agents**<br>(에이전트 최소 권한 원칙 및 고위험 작업 단계별 승인) | 🟢 **정답 신호** | 자율형 AI 에이전트에게 DB 전체 관리자 권한(`Excessive Agency`)을 주는 대신, **읽기 전용 권한을 기본 부여하고 일정 금액 이상 환불/송금 시 결정론적 API 검증 또는 인간 승인(Step-Up Authorization)** 을 거치게 하는 아키텍처입니다. |
| **Non-Outsourceable Accountability**<br>(외주화할 수 없는 최종 법적·윤리적 책임) | 🟢 **정답 신호** | AWS나 외부 SaaS 벤더의 모델을 사용하더라도(`Shared Responsibility Model`), **자사 고객에게 발생한 차별·개인정보 유출·규제 위반의 최종 법적/비즈니스 책임(Ultimate Accountability)은 전적으로 도입 기업(Deployer)의 경영진에게 귀속**된다는 원칙입니다. |
| **Amnesty Funnel / Safe-Harbor Sandbox**<br>(섀도우 AI 양성화 통로 및 안전 샌드박스) | 🟢 **정답 신호** | 현업 직원들이 몰래 외부 무료 생성형 AI를 쓰는 `Shadow AI` 문제를 적발·징계로만 막으면 음지화가 심해집니다. **기존 비인가 프롬프트/워크플로우를 처벌 없이 신고(Amnesty)받아 엔터프라이즈 보안 샌드박스로 안전하게 이관**해주는 전략이 정답입니다. |
"""

if __name__ == "__main__":
    print("PART1_MD length:", len(PART1_MD))
