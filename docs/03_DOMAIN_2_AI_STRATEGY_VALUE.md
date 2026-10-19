# 도메인 2: AI 전략 및 비즈니스 가치 창출 (AI Strategy & Business Value Creation)

> **출제 비중 (Exam Weight)**: **31% (가장 높은 출제 비중)**  
> **공식 시험 평가 목표 (Exam Objective)**: 비즈니스 목표에 부합하는 고임팩트 AI 유스케이스를 발굴하고, Build vs Buy vs Partner 의사결정을 내리며, Baseline 측정, 선행/후행 지표, TCO 및 숨은 비용 통제, 지속 가능한 데이터 플라이휠과 경쟁 우위를 구축할 수 있는가?

---

## 2.1 솔루션 조달 결정: Build vs Buy vs Partner Framework

| 조달 경로 (Approach) | 🇺🇸 English Strategic Rationale & Criteria | 🇰🇷 한국어 비즈니스 전략 및 선택 기준 | 🎯 Exam Answer Key |
| :--- | :--- | :--- | :--- |
| **Buy (상용 솔루션 구매)** | • Fastest Time-to-Market (TTM).<br>• Commodity/standard business functions (e.g., HR service desk, general email drafting).<br>• Minimal internal AI engineering overhead. | • 가장 빠른 출시 속도(Time to Market) 필요 시.<br>• 회사의 고유 경쟁력이 아닌 표준적/범용적 업무(HR, 일반 CRM).<br>• 사내 AI 엔지니어링 역량이 부족한 초기 단계. | **Amazon Q Business, 기성 SaaS 도입** |
| **Build (독자 자체 구축)** | • Core competitive differentiator.<br>• Proprietary datasets providing defensible commercial moat.<br>• Strict data sovereignty and air-gapped VPC network isolation requirements. | • 회사의 핵심 경쟁 우위가 되는 차별화 비즈니스 영역.<br>• 자사 고유의 독점 데이터로 경쟁사가 모방할 수 없는 해자 구축 시.<br>• 엄격한 보안 규제 및 전용 VPC 격리 요구 시. | **Amazon Bedrock / SageMaker 기반 자체 파이프라인 구축** |
| **Partner (전문 파트너 협력)** | • Hybrid acceleration model.<br>• Bridging interim talent shortages while internal capability is cultivated.<br>• Shared implementation risk for high-complexity strategic bets. | • 사내 역량이 성숙할 때까지 출시 속도를 내기 위한 하이브리드 협력.<br>• 복잡한 전략적 베팅 프로젝트의 초기 기술 위험 분산. | **AWS 전문 파트너십 및 공동 파일럿 프로젝트** |

---

## 2.2 유스케이스 발굴 및 우선순위 2x2 매트릭스 (Prioritization Matrix)

<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Prioritization Matrix Dimensions**: Every prospective AI use case must be plotted along two axes: **Business Impact (Value)** versus **Feasibility & Complexity (Effort)**.
* **Quick Wins (High Impact, Low Complexity)**: The mandatory starting point. Delivered rapidly with minimal friction to build organizational credibility, demonstrate tangible business ROI, and win executive sponsorship.
* **Strategic Bets (High Impact, High Complexity)**: Fundamental transformational initiatives requiring multi-quarter infrastructure investments, cross-functional re-engineering, and cultural readiness.
* **PoC Purgatory & Kill Criteria**: A critical executive failure is allowing dozens of PoCs to linger without transitioning to production. Define explicit Go/No-Go exit criteria prior to project kickoff; if a pilot fails its quantitative KPI gate, invoke disciplined project termination to avoid the **Sunk Cost Fallacy**.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 번역 및 비즈니스 전략 해설
* **우선순위 매트릭스 2대 축**: 모든 AI 아이디어는 **비즈니스 임팩트(가치)**와 **실현 가능성 및 복잡도(난이도)**의 2대 축을 기준으로 평가해야 합니다.
* **Quick Wins (단기 가시적 성과 - 고가치/저난이도)**: 반드시 가장 먼저 착수해야 하는 영역입니다. 빠른 시간 내에 가시적 성과를 입증하여 경영진의 신뢰와 전사적 모멘텀을 확보합니다.
* **Strategic Bets (전략적 베팅 - 고가치/고난이도)**: 장기적인 기업 경쟁 우위를 위해 대규모 인프라 투자와 조직 프로세스 혁신을 수반하는 핵심 프로젝트입니다.
* **PoC 연옥 탈출 및 프로젝트 중단 기준**: 파일럿 단계에서 무한 반복되다 폐기되는 **PoC 연옥(PoC Purgatory)**을 방지하기 위해 착수 전 명확한 성공 기준(KPI)을 정하고, 기준 미달 시 **매몰 비용의 오류(Sunk Cost Fallacy)**에 빠지지 않고 과감히 프로젝트를 종료(Kill)해야 합니다.

</div>
</div>

---

## 2.3 비즈니스 가치 측정: Baseline, 선행 vs 후행 지표 & ROI

<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Baseline Metric (As-Is vs To-Be)**: Before deploying any AI system, organizations must rigorously document baseline operational metrics (e.g., historical average handle time of 8 minutes). Without an unassailable baseline, post-deployment ROI calculation is mathematically impossible.
* **Leading vs Lagging Indicators**:
  * *Leading Indicators*: Early predictive operational metrics tracked during rollout (e.g., Daily Active Users, weekly query volume, employee prompt adoption rates).
  * *Lagging Indicators*: Trailing financial metrics observed months later (e.g., 30% reduction in annual operational expenses, quarterly operating margin gains).
* **Cost of Inaction (COI)**: The economic penalty and competitive decay incurred by delaying AI transformation while industry peers modernize, serving as a powerful justification framework for risk-averse executives.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 번역 및 비즈니스 전략 해설
* **기준 지표 (Baseline Metric)의 필수성**: AI 도입 전 현재(As-Is) 상태의 성과 지표(예: 기존 상담원 평균 처리 시간 8분)를 반드시 정량 측정해야만, 도입 후(To-Be) 성과 개선율과 ROI를 증명할 수 있습니다.
* **선행 지표 vs 후행 지표**:
  * *선행 지표 (Leading)*: 프로젝트 진행 중 초기 성패를 미리 알려주는 운영 지표 (일일 활성 사용자 수 DAU, 주당 AI 쿼리 수, 기능 채택률).
  * *후행 지표 (Lagging)*: 프로젝트 완료 후 분기/연 단위가 지나야 측정할 수 있는 최종 재무 결과 (연간 운영비 절감액, 분기 순이익 증가율).
* **행동하지 않는 비용 (Cost of Inaction, COI)**: AI 도입을 미루거나 보류함으로써 발생하는 시장 점유율 상실, 고객 이탈, 경쟁 열세 비용으로 보수적인 경영진을 설득하는 핵심 프레임워크입니다.

</div>
</div>

---

## 2.4 AI FinOps & 총 소유 비용(TCO) 최적화

<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Comprehensive AI TCO & Hidden Costs**: Real TCO extends far beyond raw cloud token bills. It encompasses ongoing data curation/labeling, MLOps monitoring pipelines, security compliance audits, and employee retraining costs.
* **Model Routing / Cascading**: Architectural cost optimization routing simple incoming requests to economical small models (e.g., Claude Instant / Haiku) and escalating only complex analytical reasoning to frontier large models, cutting token spend by 70%+.
* **Cost Allocation Tags & AWS Budgets**: Assigning granular departmental tags to all AI workloads, coupled with automated AWS Budgets alarms and Cost Anomaly Detection to prevent runaway cloud bills.
* **Provisioned Throughput**: Securing committed hourly throughput (Tokens Per Minute) in Amazon Bedrock to lock in volume discounts and ensure SLA latency during production scale.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 번역 및 비즈니스 전략 해설
* **숨은 TCO (Total Cost of Ownership) 관리**: AI 비용은 단순한 API 호출료에 그치지 않으며, 데이터 수집/정제, 지속적인 MLOps 모니터링, 법무 감사, 직원 재교육 비용이 모두 포함됩니다.
* **모델 라우팅 / 캐스케이딩 (Model Routing)**: 들어오는 질문 난이도를 분석하여 단순 질의는 저비용 경량 모델로, 복잡 질의는 고성능 대형 모델로 자동 분기 처리하여 품질 저하 없이 추론 비용을 70% 이상 절감합니다.
* **비용 할당 태그 (Cost Allocation Tags) & AWS Budgets**: 부서별로 AI 리소스 사용량을 태깅하고 예산 초과 시 실시간 경보를 울려 예측 불가능한 비용 폭증을 사전에 방지합니다.
* **프로비저닝 처리량 (Provisioned Throughput)**: 대규모 상시 트래픽 환경에서 확정된 분당 토큰 용량을 예약하여 비용 절감과 안정적인 응답 속도를 보장합니다.

</div>
</div>

---

## 2.5 지속 가능한 경쟁 우위: 데이터 플라이휠 (Data Flywheel Effect)

<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Data Flywheel Mechanics**: Superior user experiences attract more active users ➔ generating higher volumes of proprietary interaction telemetry ➔ enabling rapid model refinement ➔ delivering even better customer experiences.
* **Defensible AI Moat**: Commercial foundation models are commodities accessible to all market participants. A true enterprise moat stems from **proprietary workflow integration and closed-loop proprietary data flywheels** that competitors cannot duplicate.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 번역 및 비즈니스 전략 해설
* **데이터 플라이휠 효과**: 뛰어난 AI 경험 ➔ 사용자 유입 증가 ➔ 양질의 독점 데이터 축적 ➔ 모델 정밀도 향상 ➔ 사용자 경험 추가 개선의 선순환 구조입니다.
* **방어 가능한 AI 해자 (AI Moat)**: 누구나 쓸 수 있는 범용 모델 자체는 경쟁 우위가 될 수 없으며, **자사만의 독점적 데이터 플라이휠과 고유한 비즈니스 워크플로우 결합**만이 경쟁사가 복제할 수 없는 강력한 해자를 만듭니다.

</div>
</div>
