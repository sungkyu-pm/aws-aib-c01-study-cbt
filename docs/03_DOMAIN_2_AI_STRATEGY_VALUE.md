# 도메인 2: AI 전략 및 비즈니스 가치 창출 (AI Strategy & Business Value)

> **출제 비중 (Exam Weight)**: **31% (시험 내 최고 비중 영역!)**  
> **공식 시험 평가 목표 (Exam Objective)**: 비즈니스 임팩트와 기술적 실현 가능성을 바탕으로 AI 유스케이스 우선순위를 선정하고, Build vs Buy vs Partner 최적 경로를 도출하며, 총 소유 비용(TCO) 및 투자 수익률(ROI) 지표를 정량화하고, FinOps 비용 통제와 가치 실현 프레임워크를 수립할 수 있는가?

---

## 📌 도메인 2 출제 로드맵 및 30대 핵심 토픽 한눈에 보기
본 도메인은 AIB-C01 시험에서 **가장 많은 문항(약 19~20문항)**이 출제되는 절대 핵심 영역입니다. 엔지니어링이 아닌 **"비즈니스 의사결정권자로서의 재무적·전략적 판단"**을 평가합니다.

* **제1장: AI 솔루션 조달 전략: Build vs Buy vs Partner** (Cat 1~3)
* **제2장: 포괄적 AI 경제성 및 재무 타당성 모델링** (Cat 4~8)
* **제3장: 정량적 ROI 산출 및 성과 지표 체계** (Cat 9~12)
* **제4장: 유스케이스 우선순위 및 포트폴리오 관리** (Cat 13~18)
* **제5장: AI FinOps 및 클라우드 추론 비용 최적화** (Cat 19~25)
* **제6장: 벤더 종속성 회피 및 전사 가치 실현** (Cat 26~30)

---

## 제1장: AI 솔루션 조달 전략: Build vs Buy vs Partner (Sourcing Strategy)

### 2.1 Build vs Buy vs Partner 의사결정 트레이드오프
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Sourcing Framework**:
  * **Buy (Commercial Off-The-Shelf - e.g., Amazon Q Business)**: Optimal for standardized, non-differentiating commodity processes (internal HR Q&A, general document search). Delivers **fastest Time-to-Market (TTM)** and lowest immediate engineering overhead.
  * **Build (Custom In-House - e.g., Amazon Bedrock, SageMaker)**: Essential for **core proprietary differentiators** that define competitive enterprise moat, require full architectural control, or demand strict VPC data isolation.
  * **Partner (System Integrator / ISV)**: Bridge strategy to accelerate delivery while building internal technical competency.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* **구매 (Buy)**: 사내 인사 규정 챗봇, 회의록 요약처럼 시장에 이미 완성된 상용 제품이 있는 비핵심 업무에 최적입니다. 개발 인력 낭비 없이 **가장 빠른 출시 속도(TTM)**를 달성합니다.
* **자체 구축 (Build)**: 자사 고유의 핵심 알고리즘, 독점 지적재산권(IP), 차별화된 고객 경험을 창출하는 핵심 업무에는 독자 개발이 필수적입니다.
* **파트너십 (Partner)**: 사내 기술 역량이 부족할 때 외부 전문 SI나 AWS 파트너와 협력하여 과도기적으로 역량을 내재화합니다.

</div>
</div>

> **🎯 출제 예상 문제 분석 & 오답 함정**
> * **빈출 지문**: "기업이 표준화된 사내 지식 검색 시스템을 도입하려 한다. 고유한 비즈니스 로직 차별화가 필요 없고 가장 빠르게 사내에 배포하고자 할 때 최적의 전략은?"
> * **정답 도출**: **기성 상용 솔루션 구매 (Buy - e.g., Amazon Q Business)**
> * **오답 함정**: 수년간 자체 연구팀을 꾸려 기초 모델부터 개발(Build)하는 것은 시간과 비용 낭비로 오답입니다.

---

### 2.2 핵심 차별화 역량 vs 범용 상품 (Core Differentiator vs Commodity)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Core Differentiator**: Capabilities that directly distinguish the company from competitors in the eyes of revenue-generating customers. Demands **in-house engineering (Build)** to protect proprietary intellectual property and establish a defensible business moat.
* **Commodity Utility**: Undifferentiated back-office plumbing. Purchasing commercial SaaS frees valuable developer bandwidth for core initiatives.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* **핵심 차별화(Core)**: 고객이 우리 회사를 선택하는 결정적 이유가 되는 고유 영역 (예: 핀테크의 대출 심사 알고리즘, e커머스의 맞춤 추천 엔진).
* **범용 상품(Commodity)**: 어느 회사에나 동일하게 존재하는 일반 관리 업무. 범용 업무에 자체 구축(Build)을 고집하는 것은 리더십의 대표적 자원 낭비입니다.

</div>
</div>

---

### 2.3 데이터 주권 및 VPC 격리 (Data Sovereignty & VPC Isolation)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Data Sovereignty Mandates**: Under strict regulatory frameworks (HIPAA, PCI-DSS, GDPR), enterprise data must not cross multi-tenant public SaaS boundaries. Requires deploying models within dedicated Virtual Private Clouds (VPC) via **AWS PrivateLink** with Amazon Bedrock or SageMaker (Custom Build pattern).

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 금융/의료/공공 등 강력한 규제 산업에서는 데이터가 외부 퍼블릭 SaaS로 전송되는 것이 법적으로 금지됩니다. 이 경우 완전한 전용 VPC 격리와 AWS PrivateLink 사설 통신을 보장하는 자체 클라우드 구축(Build)이 강제됩니다.

</div>
</div>

---

## 제2장: 포괄적 AI 경제성 및 재무 타당성 모델링 (Financial Modeling & TCO)

### 2.4 포괄적 AI 총 소유 비용 (TCO) 모델링
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Total Cost of Ownership (TCO)**: Comprehensive financial calculation transcending superficial raw API token invoices.
  * **Direct Costs**: Model inference tokens, storage, provisioned throughput.
  * **Hidden TCO Drivers**: Data acquisition, continuous data labeling, MLOps monitoring pipelines, governance/legal audits, prompt maintenance, and employee change management upskilling.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 단순한 클라우드 토큰 요금(월 수백 달러)만 보고 AI 예산을 책정하면 심각한 예산 초과에 직면합니다. **데이터 정제, 지속적 MLOps 모니터링, 법무 감사, 직원 교육 비용이 합산된 진정한 TCO 전체를 산출해야 합니다.**

</div>
</div>

---

### 2.5 행동하지 않는 비용 (Cost of Inaction / COI)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Cost of Inaction (COI)**: Strategic financial justification framework quantifying the enterprise penalties incurred by stalling AI investments—including lost market share to AI-first disruptors, elevated customer churn, and widening employee productivity gaps.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 불확실성을 이유로 AI 도입을 주저하는 보수적인 경영진을 설득할 때 사용하는 전략 도구입니다. **"AI를 도입하지 않고 현재 상태를 유지할 때 경쟁사에 빼앗기게 될 시장 점유율과 고객 이탈 비용"**을 정량화하여 투자의 시급성을 입증합니다.

</div>
</div>

---

### 2.6 매몰 비용의 오류 극복 (Sunk Cost Fallacy in AI)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Sunk Cost Fallacy**: Flawed leadership behavior persisting in pouring capital into failing AI pilots simply because substantial engineering hours and budget were already expended. Disciplined leaders terminate unviable initiatives cleanly.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 이미 수억 원이 투입되었더라도 비즈니스 가치가 검증되지 않거나 실패한 프로젝트는 **과감하게 즉시 종료(Kill)하거나 피벗(Pivot)**해야 합니다. 과거의 매몰 비용에 얽매여 자원을 낭비하는 것은 시험에서 대표적 오답 행동입니다.

</div>
</div>

---

### 2.7 프로젝트 중단 및 보류 게이트 (Project Kill/Pause Gates)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Predetermined Go/No-Go Decision Gates**: Clear quantitative criteria established before pilot launch defining minimum acceptable accuracy, latency, and business ROI milestones. Prevents exploratory experiments from degenerating into perpetual zombie projects.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 프로젝트 착수 전 **"정확도 90% 미달 시 즉시 중단", "월간 비용 절감액 1,000만 원 미달 시 프로덕션 이관 보류"**와 같은 객관적 기준을 사전에 합의해 두어야 정치적 부담 없이 실패한 프로젝트를 정리할 수 있습니다.

</div>
</div>

---

### 2.8 기준 지표 확립 (Baseline Metric Definition)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Baseline Metric**: Rigorous quantitative measurement of current operational performance (As-Is state) recorded *prior* to AI deployment (e.g., current average call handle time: 8.5 minutes). Without baselines, calculating post-implementation improvement is statistically impossible.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* AI 도입 후의 성과 개선과 ROI를 증명하기 위해 **프로젝트 착수 전 반드시 선행되어야 하는 필수 작업**입니다. 현재 상태(As-Is)의 정량적 수치가 없으면 AI 도입의 효과를 결코 증명할 수 없습니다.

</div>
</div>

---

## 제3장: 정량적 ROI 산출 및 성과 지표 체계 (ROI & Value Metrics)

### 2.9 AI 투자 수익률 (ROI) 수학적 산출 공식
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **AI ROI Formula**:
  $$\text{ROI (\%)} = \left[ \frac{\text{Net Economic Benefits} - \text{Total Cost of Ownership}}{\text{Total Cost of Ownership}} \right] \times 100$$
  * *Net Benefits*: Quantifiable labor savings + incremental revenues directly attributable to AI.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* AI 도입으로 창출된 순 경제적 이익(인건비 절감액 + 신규 매출액)에서 총 소유 비용(TCO)을 뺀 순이익을 TCO로 나누어 백분율로 계산합니다. 경영진 보고 시 가장 설득력 있는 재무 지표입니다.

</div>
</div>

---

### 2.10 유형적 이익 vs 무형적 이익 (Tangible vs Intangible Benefits)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Tangible Benefits**: Direct balance-sheet measurable impacts: reduced customer support labor hours, decreased fraud write-offs, elevated checkout conversion percentages.
* **Intangible Benefits**: Strategic dividends: improved Net Promoter Score (NPS), employee workplace morale, reduced cognitive burnout, enhanced brand perception as an innovative market leader.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* **유형적 이익**: 재무제표에 숫자로 즉시 증명 가능한 성과 (직접적 ROI 산출의 분자).
* **무형적 이익**: 고객 만족도, 브랜드 신뢰, 직원 직무 스트레스 감소 등 장기적이고 전략적인 가치. 두 가지를 종합적으로 평가하는 균형 성과표(Balanced Scorecard)가 권장됩니다.

</div>
</div>

---

### 2.11 선행 지표 (Leading Indicators of AI Success)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Leading Indicators**: Early operational signals predicting future financial success during initial pilot and rollout phases: Daily Active Users (DAU), weekly prompt volume, feature utilization rate, user feedback thumbs-up ratios.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 최종 재무 성과(연간 영업이익)가 나타나기 전에 **프로젝트의 조기 성공 가능성을 가늠할 수 있는 초기 운영 지표**입니다. 도구 사용량, 일일 활성 사용자 수 등이 대표적입니다.

</div>
</div>

---

### 2.12 후행 지표 (Lagging Indicators of Long-term Value)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Lagging Indicators**: Trailing outcome metrics confirmed only months or quarters post-launch: annual operational expense (OpEx) reduction, quarterly earnings margin expansion, reduced annual customer churn rates.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 시스템이 구축되어 일정 기간 이상 실제 운영된 후에야 결산할 수 있는 최종 성과 지표입니다.

</div>
</div>

---

## 제4장: 유스케이스 우선순위 및 포트폴리오 관리 (Prioritization Portfolio)

### 2.13 우선순위 2x2 매트릭스 (Prioritization Matrix)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **2x2 Prioritization Matrix**: Grid mapping prospective AI use cases along **Business Value (Impact)** on the vertical axis versus **Feasibility & Complexity** on the horizontal axis. Categorizes initiatives into Quick Wins, Strategic Bets, Low-Hanging Fruits, and Deprioritized distractions.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 수많은 부서에서 쏟아지는 수십 개의 AI 아이디어 중 착수 순서를 합리적으로 결정하는 표준 포트폴리오 도구입니다.

</div>
</div>

---

### 2.14 단기 가시적 성과 우선 착수 전략 (Quick Wins First)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Quick Wins (High Value, Low Complexity)**: The first initiatives to launch. Rapidly prove feasibility, generate immediate business value, build executive trust, and secure momentum for future investments.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 높은 비즈니스 가치를 가지면서도 기술적 복잡도가 낮은 프로젝트입니다. **조직 내 AI 회의론을 극복하고 경영진의 신뢰를 확보하기 위해 가장 먼저 착수해야 하는 1순위 유스케이스**입니다.

</div>
</div>

---

### 2.15 전략적 베팅 장기 로드맵 (Strategic Bets)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Strategic Bets (High Value, High Complexity)**: Multi-year transformations (e.g., enterprise-wide autonomous supply chain planning). Demands substantial capital, architectural modernization, and organizational maturity earned from Quick Win successes.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 회사의 핵심 미래 경쟁 우위를 만드는 대형 프로젝트로, Quick Win을 통해 조직의 역량과 신뢰가 축적된 후 체계적으로 추진합니다.

</div>
</div>

---

### 2.16 PoC 연옥 탈출 (Avoiding PoC Purgatory)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **PoC Purgatory**: Organizational paralysis where AI initiatives languish in perpetual sandbox experimentation without ever transitioning into production. Remedied by defining production acceptance criteria and business KPIs *before* initiating prototypes.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 수많은 AI 실험이 실제 프로덕션 서비스로 확장되지 못하고 실험실에서 맴돌다 폐기되는 현상입니다. 착수 전 명확한 프로덕션 이관 기준과 비즈니스 KPI를 합의하여 탈출해야 합니다.

</div>
</div>

---

### 2.17 출시 속도 (Time to Market / TTM)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Time to Market (TTM)**: Elapsed duration from concept approval to enterprise deployment. When market window or competitive parity is the primary constraint, **purchasing commercial solutions (Buy)** consistently trumps multi-year custom engineering.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 시장 선점이나 경쟁사 대응이 시급한 상황에서 상용 솔루션(Buy)을 선택하는 가장 결정적인 비즈니스 동기입니다.

</div>
</div>

---

### 2.18 데이터 플라이휠과 지속 가능한 해자 (Data Flywheel Effect)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Data Flywheel**: Self-reinforcing cycle where an intuitive AI application attracts active users $\rightarrow$ generates proprietary user behavioral logs and domain telemetry $\rightarrow$ continuously refines model accuracy $\rightarrow$ attracts more users, establishing an insurmountable commercial moat against competitors.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 뛰어난 AI 경험이 더 많은 사용자를 모으고, 이들이 생성한 고유한 행동 데이터가 다시 모델을 고도화하여 경쟁사가 쉽게 복제할 수 없는 지속 가능한 비즈니스 해자(Moat)를 만드는 선순환 구조입니다.

</div>
</div>

---

## 제5장: AI FinOps 및 클라우드 추론 비용 최적화 (AI FinOps & Cost Controls)

### 2.19 AI FinOps 운영 프레임워크
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **AI FinOps**: Collaborative financial management discipline uniting engineering, finance, and business leaders to provide continuous visibility, unit cost tracking, and algorithmic optimization of generative AI expenses.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 변동성이 큰 생성형 AI 토큰 비용을 실시간 모니터링하고 부서별 사용 책임을 명확히 하여 클라우드 재무 건전성을 확보하는 프레임워크입니다.

</div>
</div>

---

### 2.20 비용 할당 태그 (Cost Allocation Tags)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **AWS Cost Allocation Tags**: Metadata tags assigned to Bedrock and SageMaker resources tracking API expenditures by department, project code, or cost center. Enables financial transparency and eliminates "free rider" budget abuse.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 각 부서나 프로젝트별로 태그를 붙여 AI 사용 요금을 정확히 분배하고 부서장의 재무적 책임성을 강화하는 표준 AWS 기능입니다.

</div>
</div>

---

### 2.21 모델 라우팅 및 캐스케이딩 (Model Routing & Cascading)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Model Routing / Cascading**: Architectural tiering directing simple factual inquiries to economical lightweight models (e.g., Claude 3 Haiku, Amazon Titan Express) while intelligently escalating complex multi-step reasoning to frontier models (e.g., Claude 3.5 Sonnet). Reduces overall inference OpEx by 60~80%.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 모든 질문을 값비싼 최고 사양 모델로 처리하지 않고, 단순 질의는 저비용 소형 모델로, 고난도 추론은 대형 모델로 자동 분기시켜 비용을 획기적으로 절감하는 지능형 아키텍처입니다.

</div>
</div>

---

### 2.22 프로비저닝 처리량 vs 온디맨드 과금 (Provisioned Throughput)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Provisioned Throughput**: Reserving committed model capacity (Model Units / TPM) in Amazon Bedrock for predictable latency SLAs and substantial volume discounts during sustained, heavy enterprise production traffic.
* **On-Demand**: Best for exploratory PoCs, variable development, and unpredictable traffic bursts.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* **온디맨드(On-Demand)**: 트래픽이 들쑥날쑥한 개발/테스트 단계에 적합.
* **프로비저닝 처리량(Provisioned Throughput)**: 대규모 상시 트래픽이 발생하는 엔터프라이즈 운영 환경에서 응답 지연(SLA)을 보장받고 단위 토큰 비용을 대폭 낮추는 정답입니다.

</div>
</div>

---

### 2.23 비동기 배치 추론 (Batch Inference)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Amazon Bedrock Batch Inference**: Asynchronous processing of massive document sets (e.g., millions of archived contracts) within 24 hours at a **50% discount** compared to real-time synchronous on-demand endpoints.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 즉각적인 실시간 응답이 필요 없는 대용량 야간 문서 요약이나 로그 분석 작업은 배치 추론을 활용하여 **비용을 50% 절감**합니다.

</div>
</div>

---

### 2.24 프롬프트 및 임베딩 캐싱 (Prompt & Embedding Caching)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Caching**: Storing frequently generated vector embeddings and repetitive system prompt tokens in in-memory stores (Amazon ElastiCache). Eliminates redundant accelerator computations and slashes repetitive API costs.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 동일한 질문이나 고정된 시스템 프롬프트를 매번 모델에 보내지 않고 캐시에서 즉시 반환하여 응답 속도를 높이고 API 요금을 절약합니다.

</div>
</div>

---

### 2.25 토큰 소비 예산 쿼터 (Budget Quotas & AWS Budgets)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **AWS Budgets & CloudWatch Alerts**: Setting strict monetary thresholds that trigger automated SNS notifications and pause inference throttling when consumption exceeds allocated monthly quotas.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 무한 루프나 트래픽 폭증으로 인한 요금 폭탄을 방지하기 위해 예산 임계값을 설정하고 초과 시 알림 및 자동 차단을 수행합니다.

</div>
</div>

---

## 제6장: 벤더 종속성 회피 및 전사 가치 실현 (Vendor Portability & Alignment)

### 2.26 벤더 락인 방지 및 모델 이식성 (Vendor Lock-in & Portability)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Model Agnosticism**: Abstracting application code from vendor-specific proprietary APIs. **Amazon Bedrock** provides a single unified Converse API across Anthropic Claude, Meta Llama, AI21, and Amazon Titan, allowing frictionless model swapping.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 특정 AI 벤더에 종속되지 않도록 단일 통합 API(Amazon Bedrock)를 사용하여 코드 수정 없이 필요에 따라 더 성능 좋고 저렴한 모델로 손쉽게 교체할 수 있는 유연성을 확보합니다.

</div>
</div>

---

### 2.27 오픈소스 vs 독점 상용 모델 (Open-Source vs Proprietary)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Trade-off Evaluation**:
  * **Proprietary (Claude 3.5 Sonnet)**: Frontier reasoning, zero self-hosting maintenance, state-of-the-art coding and agentic capabilities.
  * **Open-Source (Meta Llama 3)**: Full weights access, ability to host in totally air-gapped private sovereign enclaves, freedom from vendor API pricing changes.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 최고 성능과 무관리 편의성을 원하면 상용 파운데이션 모델을, 완전한 폐쇄망 자체 호스팅과 가중치 소유권을 원하면 Llama 등 오픈소스 모델을 선택합니다.

</div>
</div>

---

### 2.28 SaaS 통합 및 Amazon Q Apps (Rapid Grassroots Modernization)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Amazon Q Apps**: Feature allowing business users to generate secure, shareable enterprise generative AI applications directly from a conversational prompt within seconds, tapping into existing corporate data connections seamlessly.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 현업 실무자가 개발자의 도움 없이 대화 몇 마디로 사내 데이터를 연동한 업무용 AI 앱을 즉시 만들고 부서원들과 공유하는 기능입니다.

</div>
</div>

---

### 2.29 비즈니스 케이스 내러티브 작성 (Business Case & Executive Alignment)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Executive Proposal Craft**: Framing AI proposals around quantifiable business outcomes (revenue growth, margin preservation, regulatory risk reduction) rather than technical jargon (parameters, transformer layers, benchmark scores).

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 경영진 보고서에는 복잡한 딥러닝 기술 용어 대신, **"비용이 얼마나 절감되고, 고객 유지율이 얼마나 향상되며, 회사의 전략적 목표에 어떻게 기여하는가"**를 정량적 비즈니스 언어로 제시해야 합니다.

</div>
</div>

---

### 2.30 전사 비즈니스 가치 실현 협의체 (Cross-Functional Realization)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Joint Accountability**: Structuring AI project ownership with joint leadership between IT engineering and Line-of-Business (LoB) executives, ensuring technology deployments strictly align with bottom-line corporate P&L goals.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* IT 부서 단독으로 프로젝트를 추진하면 현업에서 외면받기 쉽습니다. 현업 사업부(LoB)와 IT가 공동의 성과 목표(KPI)와 재무적 책임을 공유해야 진정한 비즈니스 가치가 실현됩니다.

</div>
</div>
