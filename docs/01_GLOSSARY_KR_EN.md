# 📖 AWS Certified AI Business Strategist (AIB-C01) 마스터 용어사전 & 실전 시험 표현집 (Master Glossary & Exam Idioms)

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

---

## 👔 Part 2. C-Suite 임원진 의사결정 딜레마 & 거버넌스 핵심 표현 사전

실제 `AIB-C01` 시험은 **"CEO, CFO, CISO, CLO, CHRO, COO, CIO, CDO 중 누가 어떤 우려를 제기하며, 어떤 거버넌스 장치로 이해관계를 조율해야 하는가?"** 를 집중 출제합니다.

### 2-1. 임원별 핵심 우선순위·반대 논리(Pushback)·정답 해결책 매트릭스

| 임원 직책 (C-Suite Role) | 주요 관심사 및 단골 반대 논리 (Typical Exam Concerns & Pushback) | 시험 정답 조율 전략 및 핵심 영문 표현 (Winning Resolution Phrases) |
| :--- | :--- | :--- |
| **CEO (최고경영자)**<br>& **Board of Directors (이사회)** | • 경쟁사 대비 시장 선점 속도(`Speed-to-Market`) 압박<br>• 주주가치, 브랜드 평판 리스크(`Reputational Fallout`), 장기적 경쟁 해자(`Strategic Moat`) | • **Horizon 1-2-3 Portfolio Allocation** (단기 효율화 70% : 중기 확장 20% : 장기 혁신 10% 균형 배분)<br>• **AI Steering Committee Charter** (전사 AI 운영위원회 헌장 제정 및 최종 책임 명확화) |
| **CFO (최고재무책임자)** | • GPU/토큰 추론 비용 폭증(`Runaway Token Spend` / `Margin Erosion`)<br>• 불확실한 ROI, 숨겨진 운영비(`Hidden Lifecycle TCO`), 매몰 비용(`Sunk Cost`) | • **Stage-Gated Tranche Funding** (단계별 관문 통과 시 예산 분할 집행)<br>• **Unit Economics** (`Cost per Resolved Ticket`, `Gross Margin per Query`)<br>• **AI FinOps (`Showback / Chargeback`, `Semantic Caching`, `Tiered Model Routing`)** |
| **CISO (최고정보보안책임자)** | • 기밀 데이터·소스코드·PII 외부 유출(`Data Exfiltration`)<br>• 프롬프트 인젝션(`Prompt Injection`), 과도한 에이전트 권한(`Excessive Agency`), 비인가 `Shadow AI` | • **Zero Base-Model Training Guarantee** (`AWS PrivateLink` + 입출력 데이터 파운데이션 모델 재학습 절대 미사용 보장)<br>• **Automated PII Redaction** (`Amazon Macie` / `Comprehend` + `Bedrock Guardrails`)<br>• **Amnesty Funnel & Approved Enterprise AI Sandbox** |
| **CLO / General Counsel (최고법무책임자)** | • `EU AI Act` 역외 적용 과징금, 저작권 침해 소송(`IP Infringement`), 영업비밀 오염(`Trade Secret Contamination`), 설명의무 위반(`Adverse Action Notice`) | • **Vendor IP Indemnification** (상용 모델 저작권 면책 조항 확인)<br>• **Clean-Room Licensed Training Corpus** (적법 라이선스 데이터셋 검증)<br>• **Local Explainability (`SHAP` / `LIME`) & Immutable Audit Trail** |
| **COO (최고운영책임자)** | • 현장(공장·물류·콜센터) 업무 중단(`Operational Disruption`), 지연시간 SLA 초과, 레거시 ERP/MES 충돌 | • **Shadow Deployment / Canary Rollout** (무중단 병렬 검증 및 점진적 트래픽 전환)<br>• **Business Process Re-engineering (`BPR`)** (단순 자동화가 아닌 업무 흐름 재설계)<br>• **Edge-Cloud Hybrid Inference & Deterministic Fallback** |
| **CHRO (최고인사책임자)** | • 직원들의 일자리 대체 공포(`Job Displacement Anxiety`), 노조 반발, 업무 보이콧, 조용한 사직(`Quiet Quitting`), 변화 피로도(`Change Fatigue`) | • **Augmentation over Replacement** (인력 감축이 아닌 고부가가치 업무로의 역량 증강 선언)<br>• **Prosci ADKAR Change Management & Role-Based Upskilling**<br>• **Outcome-Based Incentive Realignment** (AI 협업 성과를 인사평가·보상에 긍정 반영) |
| **CIO (최고정보책임자)**<br>vs. **LOB VP (현업 본부장)** | • **CIO**: 중앙 통제·표준화·기술 부채 방지 선호 (병목 유발 위험)<br>• **LOB VP**: 현업 속도 우선, 독자적 AI 툴 도입 강행 (사일로·중복 투자 유발) | • **Federated Hub-and-Spoke Operating Model** (중앙 `AI CoE` 허브는 공통 플랫폼·보안 가드레일·재사용 템플릿만 제공하고, 현업 스포크 스쿼드가 도메인 과제를 자율 실행) |
| **CDO (최고데이터책임자)** | • 부서별 데이터 사일로(`Data Silos`), 데이터 독점(`Data Hoarding`), 스키마 불일치, 데이터 품질 저하(`Garbage In, Garbage Out`) | • **Domain-Oriented Data Mesh** (`Data-as-a-Product` 원칙)<br>• **Automated Data Contracts & Pipeline SLAs** (`Amazon DataZone` + `AWS Lake Formation` 세분화 권한 통제) |

---

## 🧠 Part 3. AI/ML 학습 방법론 & 모델 최적화 필수 용어·표현 사전

실제 시험에서 자주 출제되는 **기계학습 패러다임, 생성형 AI 다단계 학습 파이프라인, 도메인 적응, 경량화/최적화 기법**의 핵심 영문 표현과 선택 기준입니다.

### 3-1. 기초 기계학습 패러다임 & 모델 일반화 (Core ML Paradigms & Generalization)

| 핵심 용어 (English / Korean) | 실전 시험 출제 포인트 및 아키텍처 선택 기준 (When to Choose & Exam Triggers) |
| :--- | :--- |
| **Supervised Learning**<br>(지도 학습: Classification / Regression) | • **출제 키워드**: 과거 정답 라벨(`Historical Labeled Outcomes`)이 풍부할 때 미래 수치 예측(`Regression`: 수요량·매출 예측) 또는 범주 분류(`Classification`: 이탈 여부·불량 판정).<br>• **대표 알고리즘**: `XGBoost / LightGBM` (정형 테이블 데이터에서 설명가능성·가성비 최고), `Linear Learner`. |
| **Unsupervised Learning**<br>(비지도 학습: Clustering / Anomaly Detection) | • **출제 키워드**: 정답 라벨이 전혀 없는 상태(`Unlabeled Data`)에서 숨겨진 고객 군집 발굴(`Clustering: K-Means`) 또는 신종 이상 징후/설비 비정상 진동 탐지(`Anomaly Detection: Random Cut Forest`). |
| **Reinforcement Learning (RL)**<br>(강화 학습) | • **출제 키워드**: 정적 정답 데이터셋이 없고, 시뮬레이션/실시간 환경과 상호작용하며 **연속적 의사결정(`Sequential Decision-Making`)과 장기 누적 보상 극대화(`Cumulative Reward Maximization`)** 가 필요할 때 선택 (예: 동적 가격 책정, 물류 AGV 로봇 경로 제어, 스마트 그리드 전력 제어). |
| **Self-Supervised Learning (SSL)**<br>(자기지도 학습) | • **출제 키워드**: 사람이 수동 라벨링하지 않은 방대한 원시 텍스트/유전체/시계열 코퍼스에서 다음 토큰 예측(`Next-Token Prediction`)이나 마스킹 복원(`Masked Token Modeling`)을 통해 **Foundation Model을 사전 학습(Pre-training)** 하는 기법. |
| **Semi-Supervised & Active Learning**<br>(준지도 학습 & 능동 학습) | • **출제 키워드**: 라벨링 비용이 매우 비싼 도메인(전문의 의료 영상, 변호사 계약서)에서 **소량의 라벨 데이터 + 대량의 비라벨 데이터**를 결합하고, **모델이 가장 불확실해하는 고가치 샘플만 골라 전문가에게 라벨링을 요청(`Active Learning` via `SageMaker Ground Truth`)** 하여 라벨링 비용을 70% 이상 절감. |
| **Overfitting vs. Underfitting**<br>(과적합 vs. 과소적합) | • **Overfitting 징후**: 훈련 데이터 정확도는 99%인데 검증/실전 데이터(`Unseen Holdout Set`)에서는 성능이 급락함 (원인: 훈련 데이터 노이즈까지 암기, 데이터 부족, 과도한 모델 복잡도).<br>• **정답 처방**: `Stratified K-Fold Cross-Validation`(계층화 교차 검증), `Regularization (L1/L2, Dropout)`, `Early Stopping`(검증 손실 상승 시 조기 종료), `Feature Selection`(불필요 변수 제거), `Data Augmentation`. |
| **Data Leakage (Target Leakage)**<br>(데이터 누수 / 타겟 누수) | • **출제 함정**: 추론 시점에는 알 수 없는 미래 정보(예: 해지 확정 후 생성된 환불 코드)가 훈련 피처에 섞여 들어가 검증 정확도가 비정상적으로 높게(99.9%) 나오는 오류. **시간순 분할(`Temporal Split`)과 피처 스토어 시점 일치(`Point-in-Time Correctness`)** 로 방지해야 합니다. |

---

### 3-2. 생성형 AI 학습 파이프라인 & 커스터마이징 의사결정 (GenAI Training & Customization Spectrum)

| 학습/최적화 기법 (Methodology) | 목적 및 실전 시험 선택 기준 (Strategic Use Case & Cost/Latency Trade-off) |
| :--- | :--- |
| **1단계: Prompt Engineering & In-Context Learning (`Few-Shot`)** | • **최우선 검토(Lowest Cost/Fastest Time-to-Value)**: 모델 가중치 변경 없이 지시문과 몇 개의 예시(`Few-Shot Examples`)만으로 출력 형식과 톤앤매너를 제어. |
| **2단계: RAG (`Retrieval-Augmented Generation`)**<br>+ **Hybrid Search (`Dense Vector + Sparse BM25`)**<br>+ **Cross-Encoder Reranking & `GraphRAG`** | • **실시간 외부 지식·출처 표기 필수 시 정답**: 시시각각 변하는 사내 규정·재고·논문을 모델 재학습 없이 실시간 참조하고 **정확한 출처(`Citation`)와 문서 수준 권한(`ACL`)** 을 적용할 때 선택.<br>• **고유명사/부품번호/약물코드 검색 누락 해결**: 의미 기반 `Dense Embedding`과 키워드 정확 매칭 `BM25(Lexical)`를 결합한 **Hybrid Search + Reciprocal Rank Fusion(RRF) + Reranker** 가 정답.<br>• **다단계 관계 추론(`Multi-Hop Reasoning`)**: 여러 문서에 흩어진 엔티티 간 복합 인과관계 파악 시 **Knowledge Graph + Vector RAG (`GraphRAG`)** 선택. |
| **3단계: Instruction Fine-Tuning (`SFT`) & `PEFT` (`LoRA / QLoRA`)** | • **특수 출력 포맷·고유 문체·도메인 분류 일관성 내재화**: 수천~수만 건의 `(Prompt, Ideal Response)` 쌍으로 학습. 전체 가중치를 수정(`Full Fine-Tuning` = 고비용·과적합 위험)하지 않고, 원본 가중치는 동결(`Freeze`)한 채 **소수의 저랭크 어댑터 행렬(`LoRA Adapter`)만 학습**하여 비용·메모리를 90% 이상 절감.<br>• **Multi-Adapter Serving**: 단일 베이스 모델 위에 부서별/국가별 수십 개의 `LoRA Adapter`를 동적으로 교체 서빙하여 GPU 인프라 비용 극대화 절감. |
| **4단계: Continued Pre-Training (`CPT` / Domain-Adaptive Pretraining)** | • **고유 전문 언어·기호 체계 자체의 이해력 주입**: 일반 LLM이 전혀 모르는 희귀 바이오 서열, 특수 화학식, 고대 법률 용어 등 **수십억 토큰 규모의 비라벨 도메인 원시 코퍼스(`Unlabeled Domain Corpus`)로 추가 사전학습**할 때 선택 (단, 실시간 사실 조회 용도로 쓰면 오답!). |
| **5단계: Alignment (`RLHF` vs. `DPO` vs. `Constitutional AI` / `RLAIF`)** | • **인간 가치·안전성·선호도 정렬**: SFT 모델이 문법적으로는 맞지만 유해하거나 교묘하게 부정확한 답변을 할 때 교정.<br>• **`RLHF`**: 별도의 보상 모델(`Reward Model`) 학습 + `PPO` 강화학습 필요 (연산 무겁고 하이퍼파라미터 불안정).<br>• **`DPO (Direct Preference Optimization)`**: 별도 보상 모델 없이 `(Prompt, Chosen, Rejected)` 선호도 쌍 데이터만으로 직접 정책 최적화 ➔ **비용·안정성 면에서 RLHF 대비 실무 선호 정답**. |
| **6단계: Knowledge Distillation (`Teacher-Student`) & `Quantization`** | • **추론 지연시간(`Sub-50ms Latency`) 및 엣지/단위 비용 혁신**: 거대 `Teacher LLM`이 생성한 고품질 추론 데이터로 경량 `Student SLM(1B~8B)`을 전이 학습(`Knowledge Distillation`)하고, 가중치 정밀도를 `FP16 ➔ INT8/INT4`로 양자화(`Post-Training Quantization`)하여 **95% 이상의 성능을 유지하면서 추론 비용과 지연시간을 1/10로 압축**. |

---

## 🏭 Part 4. 산업 도메인별(바이오·제조·R&D·소매·유통·금융) 실전 빈출 영문 표현 & KPI 사전

실제 `AIB-C01` 시험은 단순 IT 기업이 아니라 **바이오/제약, 스마트 제조, 기업 R&D 연구소, 옴니채널 소매, 콜드체인 물류·유통, 금융/보험** 등 다양한 산업 현장의 고유 제약조건과 KPI를 지문에 등장시킵니다.

| 산업 도메인 (Industry Domain) | 시험 지문 빈출 핵심 영문 표현 (Domain-Specific Exam Terminology) | 핵심 비즈니스 가치 KPI & 아키텍처 정답 패턴 |
| :--- | :--- | :--- |
| **🧬 바이오 / 제약 / 임상**<br>(Bio / Pharma / Clinical Trials) | • **Target Identification & Lead Optimization** (신약 타겟 발굴 및 선도물질 최적화)<br>• **De Novo Molecular / Protein Design** (신규 분자·단백질 구조 생성)<br>• **Clinical Trial Patient Stratification** (임상시험 환자군 정밀 층화/선별)<br>• **GxP Compliance & FDA 21 CFR Part 11 Audit Trail** (의약품 제조·품질관리 기준 및 전자기록 무결성 감사 추적)<br>• **Pharmacovigilance / Adverse Event Detection** (약물감시 및 이상반응 탐지) | • **KPI**: `Phase-Transition Success Rate` (임상 단계 진입 성공률), `Time-to-IND Filing` (임상시험계획 승인 신청 단축 기간)<br>• **아키텍처 정답**: 환자 유전체/임상 데이터는 `HIPAA/GxP` 준수 환경에서 **Differential Privacy(차등 프라이버시) 합성 데이터** 활용, 모든 모델 버전·데이터 혈통을 `SageMaker Model Lineage`로 불변 기록, 임상 의사결정은 반드시 **전문의 HITL(Human-in-the-Loop)** 필수. |
| **⚙️ 스마트 제조 / 반도체 / 설비**<br>(Smart Manufacturing & Fab) | • **Predictive Maintenance (PdM) & Remaining Useful Life (RUL)** (예지보전 및 잔여 수명 예측)<br>• **Overall Equipment Effectiveness (OEE)** (설비종합효율 = 가동률 × 성능 × 양품률)<br>• **Sub-10ms Edge Computer Vision Defect Inspection** (10ms 미만 초저지연 엣지 비전 불량 검출)<br>• **OT (Operational Technology) Air-Gapped Network** (공장 폐쇄망 환경)<br>• **Digital Twin & PLC/SCADA Telemetry** (디지털 트윈 및 제어기 센서 텔레메트리) | • **KPI**: `Unplanned Downtime Reduction (%)` (비계획 설비 정지 감소율), `First-Pass Yield (FPY)` (초도 양품률), `Scrap Rate Reduction` (폐기율 감소), `False-Positive Line Stop Rate` (오탐지로 인한 라인 정지율)<br>• **아키텍처 정답**: 고속 생산라인(초당 수십 개 부품 이동)이나 네트워크 단절 위험이 있는 공장은 클라우드 왕복 지연(Latency)을 피하기 위해 **클라우드에서 학습·양자화(`SageMaker Edge / IoT Greengrass`)한 경량 비전 모델을 현장 Edge IPC에 배포**하고, 이상 샘플만 클라우드로 비동기 업로드하여 재학습(`Edge-Cloud Hybrid Loop`). |
| **🔬 기업 R&D (배터리·소재·화학)**<br>(Corporate R&D & Materials) | • **Electronic Lab Notebooks (ELN) & LIMS** (전자연구노트 및 실험실 정보관리 시스템)<br>• **Trade Secret & Proprietary Formulation Leakage** (핵심 영업비밀 및 독점 배합비 유출)<br>• **High-Throughput Virtual Screening** (고속 가상 물질 스크리닝)<br>• **Inverse Materials Design & Surrogate Simulation** (역설계 및 물리 시뮬레이션 대리 모델)<br>• **Prior Art Patent Search & Multi-Hop GraphRAG** (선행특허 조사 및 다단계 지식그래프 검색) | • **KPI**: `Experiment Cycle Time Reduction` (실험 주기 단축률), `Failed Wet-Lab Experiment Avoidance` (실패할 물리 실험 사전 회피 비용 절감), `R&D Engineer Retrieval Productivity`<br>• **아키텍처 정답**: 수십 년간 축적된 비정형 실험노트·특허·분자구조식은 외부 공개 모델 학습에 절대 유출되면 안 되므로 **`AWS PrivateLink` + Zero-Training Policy + 문서 등급별 ACL이 적용된 Hybrid GraphRAG** 로 구축. |
| **🛍️ 옴니채널 소매 / 이커머스**<br>(Omnichannel Retail & E-Commerce) | • **Hyper-Personalized Cross-Sell / Up-Sell** (초개인화 교차판매·상향판매)<br>• **Shopping Cart Abandonment & Churn Propensity** (장바구니 이탈 및 고객 이탈 성향)<br>• **Store Planogram Optimization & Markdown Pricing** (매대 진열 최적화 및 재고 소진 할인율 최적화)<br>• **Stockout Rate vs. Inventory Carrying Cost** (품절률 vs. 재고 유지비 트레이드오프)<br>• **Visual Search & Virtual Try-On** (시각 검색 및 가상 피팅) | • **KPI**: `Conversion Rate Uplift` (구매 전환율 상승), `Average Order Value (AOV) / Basket Size` (객단가), `Gross Margin Return on Inventory (GMROI)`, `Return Rate Reduction` (반품률 감소)<br>• **아키텍처 정답**: 실시간 개인화 추천은 `Amazon Personalize` 같은 관리형 서비스(Buy)로 빠르게 구축하여 `Time-to-Market`을 단축하고, 인과적 매출 증분은 반드시 **Holdout 대조군 기반 A/B 테스트(`Incremental Revenue Uplift`)** 로 증명. |
| **🚚 콜드체인 유통 / 글로벌 물류**<br>(Cold-Chain & Supply Chain Logistics) | • **SKU-Location Demand Forecasting** (품목·거점별 정밀 수요 예측)<br>• **Cold-Chain Spoilage & Temperature Excursion** (신선식품/백신 콜드체인 부패 및 온도 이탈)<br>• **Dynamic Last-Mile Route Optimization** (실시간 라스트마일 배송 경로 최적화)<br>• **Warehouse Management System (WMS) Slotting** (물류센터 적치 위치 최적화)<br>• **Bullwhip Effect Mitigation** (공급망 채찍 효과 완화) | • **KPI**: `MAPE (Mean Absolute Percentage Error)` 또는 `WAPE` (수요예측 오차율 감소), `Spoilage / Waste Rate (%)` (폐기율 감소), `On-Time In-Full (OTIF)` (정시·전량 납품률), `Fuel Cost per Delivery`<br>• **아키텍처 정답**: 기상 악화·항만 파업 등 외부 변수로 인해 과거 통계 패턴이 깨질 때는(`Concept Drift`), 외부 거시/기상 피처를 결합한 **앙상블 시계열 모델 + 이상 징후 감지 시 공급망 플래너 HITL 개입 구조**를 설계. |
| **🏦 금융 / 핀테크 / 보험**<br>(FinTech, Banking & Insurance) | • **Equal Credit Opportunity Act (ECOA) & Adverse Action Notice** (신용평등법 및 대출 거절 사유 통지 의무)<br>• **Real-Time Fraud Detection (Sub-50ms SLA)** (50ms 이내 실시간 이상거래 탐지)<br>• **False Positive Customer Friction vs. False Negative Fraud Loss** (오탐지로 인한 정상 카드 결제 차단 불편 vs. 미탐지로 인한 사기 손실)<br>• **Straight-Through Processing (STP) in Claims** (보험금 청구 무인 자동 심사 처리율) | • **KPI**: `Fraud Loss Reduction ($)`, `False Decline Rate` (정상 고객 오차단율), `Claims Processing Turnaround Time`, `Regulatory Audit Pass Rate`<br>• **아키텍처 정답**: 대출/보험 심사 모델은 규제 당국과 소비자에게 개별 거절 사유를 투명하게 제시해야 하므로 불투명한 거대 블랙박스 단독 사용을 피하고 **`XGBoost` 등 해석 가능한 모델 + `SageMaker Clarify (Local SHAP Values)`** 를 결합. |

---

# AIB-C01 마스터 한·영 비즈니스 AI 용어사전 (Master Glossary)

> **💡 영문 실전 시험 대비 안내 (Exam Dual-Track Guide)**  
> 실제 시험은 **100% 영문(English)**으로 출제됩니다. 본 마스터 사전은 1,200문항 문제은행 및 공식 가이드에 등장하는 **모든 핵심 개념, 정답 선지 및 오답 선지의 용어를 1:1 완벽 매칭**하여 정리한 학습 도구입니다.  
> 영문 지문에서 키워드가 등장했을 때 즉시 올바른 개념과 정답을 도출할 수 있도록 **[영문 용어 / 한국어 의미 / 🇺🇸 영문 핵심 정의 / 🇰🇷 한국어 비즈니스 해설 / 🎯 시험 출제 및 정답 매칭]**으로 구조화되어 있습니다.

---

## 1. 도메인 1: AI 기초 및 활용 능력 (AI Fundamentals & Literacy)

| Key Term (영문 / 국문) | 🇺🇸 English Exam Definition & Context | 🇰🇷 한국어 번역 및 비즈니스 핵심 설명 | 🎯 Exam Answer Match (출제 및 정답 매칭) |
| :--- | :--- | :--- | :--- |
| **Artificial Intelligence (AI)**<br>(인공지능) | The overarching discipline of computer science aimed at simulating human intellectual processes including learning, reasoning, and problem-solving. | 인간의 지능적 행동(학습, 추론, 지각, 문제 해결)을 시뮬레이션하는 가장 포괄적인 컴퓨터 과학 기술 범주. | 규칙 기반 전문가 시스템부터 딥러닝까지 포괄하는 최상위 개념 문제 |
| **Machine Learning (ML)**<br>(기계 학습) | A subset of AI that enables systems to autonomously learn patterns and statistical relationships from data without explicit procedural programming. | 명시적인 규칙 코딩 없이 대량의 데이터로부터 패턴을 스스로 학습하여 미래를 예측하거나 분류하는 기술. | 정형 데이터 분류, 회귀 예측, 고객 이탈 예측 시나리오의 정답 |
| **Generative AI (GenAI)**<br>(생성형 AI) | A branch of ML/deep learning that generates novel, original artifacts such as text, code, imagery, or audio rather than merely predicting labels. | 기존 데이터를 단순히 분류하는 데 그치지 않고, 텍스트, 코드, 이미지 등 새로운 원본 콘텐츠를 능동적으로 생성하는 기술. | 고객 서비스 챗봇, 마케팅 문구 생성, 문서 요약 솔루션 |
| **Foundation Model (FM)**<br>(파운데이션 모델) | Massive multi-billion parameter models pre-trained on vast unlabeled corpora, adaptable to diverse downstream enterprise tasks. | 방대한 비라벨 데이터로 사전 학습되어 요약, 질의응답, 번역 등 다양한 다운스트림 작업에 적응 가능한 범용 대형 모델. | Amazon Bedrock에서 단일 API로 제공하는 Claude, Llama, Titan 모델군 |
| **Large Language Model (LLM)**<br>(대규모 언어 모델) | Specialized foundation models trained on textual data to understand, summarize, synthesize, and generate human natural language. | 자연어 처리 및 생성에 특화된 수십억~수천억 파라미터 규모의 모델. | 기업 내부 지식 검색 및 자연어 대화형 인터페이스의 핵심 모델 |
| **Discriminative ML vs GenAI**<br>(판별형 ML vs 생성형 AI) | Predicting discrete numerical or categorical outcomes (Discriminative) versus synthesizing novel natural language content (Generative). | 기존 레이블 분류/수치 예측 vs 신규 콘텐츠 생성의 목적별 기술 구분. | 문제 해결 목적에 따른 적절한 AI 알고리즘 선정 문제 |
| **Structured Data**<br>(정형 데이터) | Data organized in predefined tabular schemas with explicit rows and columns (e.g., relational databases, CSV sheets). | 관계형 DB(RDBMS), 엑셀 시트처럼 고정된 스키마(행과 열)를 갖춘 규격화된 데이터. | XGBoost, 회귀 분석 등 기존 전통적 ML 알고리즘 적용 최적 |
| **Unstructured Data**<br>(비정형 데이터) | Data without predefined data models, including unstructured PDFs, emails, call logs, audio transcripts, and images. | 이메일, PDF 보고서, 상담 녹음본, 이미지 등 고정된 구조가 없는 데이터 (기업 데이터의 80% 이상). | LLM과 RAG(검색 증강 생성)가 가장 혁신적인 가치를 발휘하는 대상 |
| **Rule-Based Automation (RPA)**<br>(규칙 기반 자동화) | Deterministic IF-THEN logic executed without machine learning, guaranteeing 100% predictable outcomes with zero ambiguity. | 명확한 비즈니스 로직과 사전 정의된 조건에 따라 100% 결정론적으로 동작하는 프로세스. | 오차가 전혀 허용되지 않고 예외가 적은 단순 반복 업무(세금 계산 등) |
| **Hybrid Automation (IDP)**<br>(지능형 문서 처리) | Combining generative AI for unstructured document parsing with deterministic rule engines for compliance and numeric validation. | 비정형 서류의 텍스트 파싱은 GenAI/OCR로 수행하고, 최종 수치 검증과 승인은 규칙 기반 시스템으로 결합하는 모델. | 손해보험 청구 서류 심사, 세금 계산서 자동 처리 아키텍처 정답 |
| **Inference**<br>(추론 실행) | The operational phase where a trained model processes novel real-time inputs to generate outputs or classifications. | 학습이 완료된 모델에 새로운 입력 데이터를 주입하여 예측 결과나 생성된 텍스트 출력을 얻는 운영 과정. | 추론 비용(Inference Cost) 및 지연 시간(Latency) 최적화 시나리오 |
| **Temperature**<br>(온도 파라미터) | A hyperparameter controlling randomness: 0.0 enforces greedy deterministic token selection, while higher values (e.g., 0.8+) foster creative variance. | 모델 출력의 무작위성을 제어하는 파라미터. 0.0이면 최고 확률 토큰만 선택(Greedy Decoding), 1.0 이상이면 창의적 생성. | 법률/금융 요약처럼 사실에 기반한 일관된 결과가 필요할 때 **0.0 설정**이 정답 |
| **Top-P (Nucleus Sampling)**<br>(핵 샘플링) | Cumulative probability threshold that constrains token selection to the most probable subset whose sum equals P. | 누적 확률 합이 P(예: 0.9) 이내인 토큰 풀 안에서만 다음 단어를 선택하도록 제한하는 파라미터. | 엉뚱한 어휘 생성을 방지하고 답변의 안정성을 확보하는 설정 |
| **Top-K**<br>(Top-K 샘플링) | Restricts candidate selection strictly to the K highest-probability next tokens, pruning unlikely tail words. | 다음 단어 후보를 확률이 가장 높은 K개(예: 50개)로 엄격히 제한하는 파라미터. | 지나치게 확률이 낮은 비정상 토큰 생성을 차단하는 설정 |
| **Greedy Decoding**<br>(탐욕적 디코딩) | Always selecting the single highest-probability token at each decoding step (equivalent to Temperature 0.0). | 매 시점 가장 높은 확률을 가진 단 하나의 토큰만을 선택하는 디코딩 기법. | 결정론적이고 매번 100% 동일한 결과 출력을 보장하는 기법 |
| **Token Streaming**<br>(토큰 스트리밍) | Emitting tokens incrementally as they are computed rather than waiting for complete response generation, minimizing Time-to-First-Token (TTFT). | 전체 답변 생성을 기다리지 않고 첫 번째 토큰부터 사용자 화면에 실시간 전송하는 방식. | 체감 대기시간(Perceived Latency) 최소화 및 UX 최적화 솔루션 정답 |
| **Context Window & Token Limits**<br>(컨텍스트 윈도우 & 토큰 한도) | The total capacity of input and output tokens a foundation model can ingest and attend to in a single inference cycle. | 모델이 한 번의 프롬프트 처리 과정에서 기억하고 참조할 수 있는 최대 토큰 용량. | 대용량 문서 처리 시 한도 초과(Token Limit) 관리 및 비용 통제의 기준 |
| **Lost in the Middle**<br>(중간 정보 누락 현상) | Performance degradation where models attend accurately to information at the beginning and end of long prompts but overlook facts in the middle. | 컨텍스트 윈도우가 매우 길 때, 모델이 프롬프트의 맨 앞과 맨 뒤 정보만 기억하고 중간 문서를 간과하는 현상. | 문서 청킹(Chunking) 및 검색 결과 리랭킹(Reranking) 적용이 정답 |
| **Document Chunking**<br>(문서 청킹) | Splitting lengthy documents into discrete, semantically coherent segments with strategic overlap to maximize retrieval precision. | 대형 문서를 의미 단위의 작은 덩어리로 쪼개고 적절한 중첩(Overlap)을 두어 검색 정확도를 높이는 전처리. | RAG 파이프라인에서 검색 품질과 컨텍스트 효율을 극대화하는 기법 |
| **Vector Embeddings**<br>(벡터 임베딩) | High-dimensional numerical vectors that map semantic meaning, where proximity reflects conceptual similarity. | 텍스트의 의미적 유사성을 다차원 실수 벡터(숫자 배열)로 변환하는 기법 (예: Amazon Titan Embeddings). | 의미론적 검색(Semantic Search)을 가능하게 하는 핵심 변환 기술 |
| **Vector Database**<br>(벡터 데이터베이스) | Specialized data stores optimized for high-speed indexing and nearest-neighbor vector distance search (e.g., OpenSearch Serverless). | 고차원 임베딩 벡터 간의 거리(코사인 유사도 등)를 초고속으로 계산하여 관련 문서를 찾는 전용 DB. | RAG의 지식 저장소 구축 시 필수 컴포넌트 |
| **Retrieval-Augmented Generation (RAG)**<br>(검색 증강 생성) | Injecting external authoritative knowledge dynamically into prompt context without altering base model weights. | 모델 가중치 재학습 없이 외부 지식 DB에서 문서를 실시간 검색해 프롬프트에 주입하는 기법. | 최신 정보 반영, 환각(Hallucination) 방지, 출처 인용(Source Citation)의 최우선 정답 |
| **Knowledge Bases for Amazon Bedrock**<br>(베드록 지식 기반) | Fully managed RAG orchestration that synchronizes Amazon S3 document repositories with vector databases automatically. | S3 사내 문서와 벡터 DB를 클릭 몇 번으로 자동 연동하고 인덱싱하는 완전관리형 RAG 솔루션. | 인프라 관리 및 복잡한 코딩 없이 엔터프라이즈 RAG를 구축하는 최적 솔루션 |
| **Fine-Tuning**<br>(미세 조정) | Updating foundational model weights using supervised domain-specific labeled dataset pairs to alter behavior or formatting. | 사전 학습된 모델에 도메인 라벨링 데이터를 추가 학습시켜 모델 가중치를 영구 변경하는 기법. | 지식 주입보다는 특정 산업 어조(Tone), 특수 출력 포맷(JSON 등) 고정에 적합 |
| **Catastrophic Forgetting**<br>(치명적 망각) | The phenomenon where fine-tuning a model on specialized data degrades its previously learned generalized reasoning and broad knowledge. | 파인 튜닝 시 새로운 데이터에 과적합되면서 기존의 일반 상식이나 추론 능력이 급격히 상실되는 현상. | 파인 튜닝의 대표적 위험 요소 및 RAG 대비 한계점으로 출제 |
| **Pre-training**<br>(사전 학습) | Building foundation model weights from scratch using trillions of tokens and vast GPU clusters. | 처음부터 천문학적인 데이터와 GPU로 모델을 학습시키는 과정. | 천문학적인 비용과 데이터가 소요되므로 극소수 주권 AI 외에는 비즈니스 관점 오답 |
| **Prompt Engineering**<br>(프롬프트 엔지니어링) | Crafting input directives, context, and structural constraints to guide model generation without retraining weights. | 모델 재학습 없이 입력 지침 설계를 통해 출력을 최적화하는 가장 경제적인 기법. | 가장 빠른 출시 기간(TTM)과 최저 TCO로 모델 동작을 제어하는 1차 접근법 |
| **Zero-Shot vs Few-Shot**<br>(제로샷 vs 퓨샷 프롬프팅) | Unprompted directives (Zero-Shot) versus providing 2-3 exemplar input-output pairs (Few-Shot) within the prompt context. | 예시 없이 지시만 내리기 vs 프롬프트 내에 2~3개 모범 입출력 예시를 제공하여 형식 고정. | 복잡한 분류 작업이나 고정된 양식 출력을 강제할 때 Few-Shot이 정답 |
| **Chain-of-Thought (CoT)**<br>(사고의 사슬 프롬프팅) | Directing models to articulate step-by-step intermediate reasoning before rendering a final answer, mitigating logic errors. | "단계별로 생각해보자"와 같이 복합적인 문제를 순차적인 하위 추론 단계로 나누어 풀도록 지시. | 다단계 수학 연산, 비즈니스 로직 분석, 복합 추론 오류 해결의 정답 |
| **System Prompts**<br>(시스템 프롬프트) | Authoritative meta-directives establishing the model's persona, operational role, tone, and unbreakable safety constraints. | 모델의 페르소나, 역할, 응답 어조, 절대 해서는 안 되는 행동 제약 사항을 지정하는 최우선 지시문. | 모델의 일관된 브랜드 보이스 확립 및 1차 안전 가이드라인 부여 |
| **Prompt Injection & Jailbreak**<br>(프롬프트 주입 및 탈옥) | Malicious user input crafted to subvert system instructions, jailbreak safeguards, and extract confidential data or models. | 악의적인 사용자가 입력 지시문을 교묘하게 조작하여 시스템 프롬프트 제약을 무력화하려는 적대적 공격. | Amazon Bedrock Guardrails 입력 필터링으로 완화해야 할 핵심 보안 위협 |
| **AI Agent**<br>(AI 에이전트) | Autonomous systems capable of analyzing high-level goals, decomposing them into sequential plans, and calling external APIs to act. | 사용자의 상위 목표를 분석하여 자율적으로 계획을 세우고, 외부 도구를 호출하여 다단계 작업을 완수하는 시스템. | 여행 일정 조회부터 예약, 결제까지 자율 수행하는 시나리오의 정답 |
| **Action Groups & OpenAPI Schema**<br>(액션 그룹 및 OpenAPI 스키마) | The defined API integrations and Lambda business functions that Amazon Bedrock Agents invoke autonomously. | Bedrock Agents에서 에이전트가 호출할 수 있는 비즈니스 API 사양(OpenAPI)과 AWS Lambda 함수 매핑. | 에이전트가 외부 엔터프라이즈 시스템(ERP, CRM, 결제)과 연동하는 표준 방식 |
| **Multi-Agent Orchestration**<br>(멀티 에이전트 오케스트레이션) | Coordinating specialized agents handling distinct sub-tasks (e.g., triage, research, execution) to complete complex enterprise workflows. | 전문화된 복수의 AI 에이전트가 메시지를 주고받으며 엔드투엔드 워크플로우를 완수하는 구조. | 복잡한 엔터프라이즈 업무 프로세스를 모듈화하여 안정적으로 자동화하는 패턴 |
| **Model Quantization**<br>(모델 양자화) | Reducing floating-point precision (e.g., from FP32 to INT8/INT4) to compress model memory footprint and boost inference speed. | 모델 가중치의 정밀도를 축소하여 메모리 점유율을 낮추고 추론 속도를 높이는 최적화 기법. | 정확도 손실을 최소화하면서 엣지 디바이스나 제한된 GPU 메모리에 대형 모델 배포 |
| **LLM-as-a-Judge**<br>(LLM 평가자) | Utilizing a high-capability LLM to evaluate and score output quality, factual accuracy, and safety of candidate models automatically. | 고성능 파운데이션 모델을 심사위원으로 활용하여 생성 답변의 품질과 사실성을 자동 채점하는 방법론. | 대규모 프롬프트 테스트 결과를 빠르고 일관되게 벤치마킹하는 솔루션 정답 |
| **Model Drift & Concept Drift**<br>(모델 드리프트 & 개념 드리프트) | Statistical divergence where changing production data distributions or evolving real-world behaviors degrade predictive accuracy. | 시간 경과에 따라 실세계 데이터 패턴(Data Drift)이나 비즈니스 관계(Concept Drift)가 변해 성능이 떨어지는 현상. | Amazon SageMaker Model Monitor를 통한 지속적 모니터링 및 재학습 필요 |
| **Shadow AI**<br>(섀도 AI) | Unauthorized employee usage of unsanctioned consumer AI chatbots, exposing corporate IP and confidential customer PII. | 사내 승인이나 보안 통제 없이 직원들이 외부 상용 무료 AI 챗봇에 사내 기밀을 입력하여 사용하는 위험. | 무조건 차단 대신 엔터프라이즈 보안(Amazon Q Business) 공식 도구를 제공하여 해결 |

---

## 2. 도메인 2: AI 전략 및 비즈니스 가치 창출 (AI Strategy & Business Value Creation)

| Key Term (영문 / 국문) | 🇺🇸 English Exam Definition & Context | 🇰🇷 한국어 번역 및 비즈니스 핵심 설명 | 🎯 Exam Answer Match (출제 및 정답 매칭) |
| :--- | :--- | :--- | :--- |
| **Build vs Buy vs Partner**<br>(자체 개발 vs 구매 vs 파트너) | Strategic decision framework balancing TCO, Time-to-Market (TTM), core competitive differentiation, and data sovereignty. | TCO, 출시 속도(TTM), 핵심 역량 차별화 여부, 보안 요구사항을 고려하여 AI 솔루션 조달 방식을 결정하는 프레임워크. | 핵심 경쟁력이면 **Build**, 표준적 업무면 **Buy**, 역량 내재화 과도기면 **Partner** |
| **Core Differentiator vs Commodity**<br>(핵심 차별화 역량 vs 범용 상품) | Distinguishing proprietary competitive assets that define market moat from standardized undifferentiated commodity utilities. | 시장에서 기업의 독점적 경쟁 우위를 만드는 고유 역량(Core)과 어디서나 대체 가능한 표준 업무(Commodity)의 구분. | 자사 핵심 알고리즘은 자체 개발(Build), 일반 업무용 챗봇은 기성 솔루션(Buy) 도입 |
| **Total Cost of Ownership (TCO)**<br>(총 소유 비용) | Aggregate financial investment including API tokens, data engineering, ongoing MLOps, governance compliance, and organizational upskilling. | 초기 구축비 외에 인프라 운영비, 토큰 API 호출료, 데이터 수집/정제, MLOps, 보안 감사, 지속 유지보수를 합산한 총비용. | AI 투자 의사결정 시 단순 라이선스 비용이 아닌 TCO 전체를 산출해야 함 |
| **Hidden TCO Components**<br>(숨은 TCO 구성 요소) | Non-obvious expenditures beyond infrastructure bills: data labeling, ongoing prompt maintenance, legal reviews, and model retraining. | 클라우드 청구서 외에 발생하는 비가시적 비용: 데이터 정제, 법무/규제 감사, 직원 재교육, 모델 드리프트 모니터링 비용. | TCO 산정 시 간과하기 쉬운 항목으로 시험에서 단골 출제 |
| **Cost of Inaction (COI)**<br>(행동하지 않는 비용) | The economic penalty, market share erosion, and customer churn incurred by delaying AI investments while competitors modernize. | AI 투자를 지연시키거나 보류함으로써 발생하는 기회비용: 시장 점유율 상실, 고객 이탈, 경쟁 열세 비용. | 보수적인 경영진을 설득하여 AI 투자의 시급성을 입증하는 정당화 프레임워크 |
| **Sunk Cost Fallacy**<br>(매몰 비용의 오류) | Irrational persistence in funding failing or value-deficient AI projects merely because substantial resources were already expended. | 이미 투자된 시간과 자금이 아까워서 비즈니스 가치가 검증되지 않거나 실패한 AI 프로젝트에 계속 자금을 낭비하는 오류. | 비즈니스 성과 미달 시 즉시 프로젝트를 중단(Kill)하는 근거 |
| **Project Kill/Pause Decision**<br>(프로젝트 중단/보류 의사결정) | Disciplined governance shutting down pilots that fail predetermined quantifiable KPI thresholds to conserve capital and talent. | 사전 정의된 비즈니스 KPI 및 기술적 실현 가능성(Go/No-Go 게이트)에 미달할 경우 과감히 프로젝트를 종료하는 리더십 결정. | 실패한 PoC를 조기에 정리하고 성공 가능성이 높은 프로젝트로 리소스를 재배치 |
| **Baseline Metric**<br>(기준 지표) | Quantitative measurement of current As-Is performance taken prior to AI intervention, indispensable for verifying ROI. | AI 도입 전 현재(As-Is)의 비즈니스 성과 수준을 정량적으로 측정한 기준 수치 (예: 상담원 평균 처리 시간 8분). | AI 도입 후 성과 개선율과 ROI를 정량적으로 입증하기 위한 **필수 사전 작업** |
| **Return on Investment (ROI)**<br>(투자 수익률) | Formulaic verification: [(Net Economic Benefit - Total Cost of Ownership) / Total Cost of Ownership] x 100. | (AI 도입으로 창출된 순이익 ÷ 총 소유 비용) × 100. AI 투자의 재무적 타당성을 증명하는 핵심 지표. | 경영진 보고 시 가장 명확한 투자 근거 지표 |
| **Tangible Benefits**<br>(유형적 이익) | Direct, balance-sheet measurable impacts: labor hours saved, call center handle time reductions, and increased cart conversions. | 처리 시간 단축에 따른 인건비 절감, 전환율 상승으로 인한 직접 매출 증가 등 재무제표에 숫자로 바로 증명 가능한 성과. | 단기 재무 타당성 및 ROI 산정의 직접 분자 항목 |
| **Intangible Benefits**<br>(무형적 이익) | Strategic indirect dividends: Net Promoter Score (NPS) uplifts, improved employee morale, brand innovation perception, and talent attraction. | 고객 만족도(CSAT/NPS) 상승, 직원 직무 스트레스 감소, 기업 브랜드 혁신 이미지 제고 등 간접적 가치. | 장기적 전략 가치 평가 및 정성적 KPI로 반영 |
| **Leading Indicators**<br>(선행 지표) | Early operational metrics signaling future financial outcomes: Daily Active Users (DAU), weekly query volume, and feature adoption rates. | 최종 재무 성과가 나타나기 전에 프로젝트의 성공 가능성을 미리 예측할 수 있는 초기 운영 지표. | 파일럿 단계에서 조기 성패를 진단하고 피드백을 수렴하는 기준 |
| **Lagging Indicators**<br>(후행 지표) | Trailing outcome metrics evaluated months after release: annual operational expense reduction, quarterly profit margin expansions. | 프로젝트가 완료되고 일정 기간이 지난 후에야 측정할 수 있는 최종 결과 지표. | 프로젝트 완료 후 최종 비즈니스 성공을 결산하는 지표 |
| **Prioritization Matrix (2x2)**<br>(우선순위 평가 매트릭스) | Evaluative grid plotting Business Impact against Technical/Organizational Feasibility to sequence project roadmaps. | 비즈니스 가치(Business Value)와 실현 가능성/복잡도(Feasibility & Complexity)의 2대 축으로 유스케이스를 평가하는 도구. | 수많은 AI 아이디어 중 착수 순서를 결정하는 표준 도구 |
| **Quick Wins**<br>(단기 가시적 성과) | High-value, low-complexity initiatives delivered rapidly to establish credibility, demonstrate feasibility, and earn executive trust. | 높은 가치 + 낮은 복잡도를 가진 프로젝트. | 조직 내 AI 신뢰를 구축하고 초기 모멘텀을 확보하기 위해 **가장 먼저 실행해야 할 유스케이스** |
| **Strategic Bets**<br>(전략적 베팅) | High-value, high-complexity endeavors demanding substantial infrastructure and organizational transformation for market leadership. | 높은 가치 + 높은 복잡도를 가진 프로젝트. | 회사의 핵심 경쟁 우위를 위해 장기적 인프라 투자를 감수하고 추진하는 대형 프로젝트 |
| **PoC Purgatory**<br>(PoC 연옥) | Organizational paralysis where initiatives stall indefinitely in exploratory proof-of-concept stages without reaching production scale. | 수많은 PoC가 실제 운영 프로덕션으로 전환되지 못하고 실험실 단계에서 무한 반복되다 폐기되는 현상. | 명확한 비즈니스 KPI와 프로덕션 확장 기준을 사전 정의하여 탈출 |
| **Time to Market (TTM)**<br>(시장 출시 기간) | Elapsed duration from use case ideation to commercial production release, where commercial off-the-shelf software excels. | 아이디어 발굴부터 실제 고객에게 가치 있는 프로덕션 서비스를 릴리스하기까지 걸리는 시간. | 기성 상용 솔루션(Buy)을 선택하는 가장 강력한 비즈니스 동기 |
| **Data Flywheel Effect**<br>(데이터 플라이휠 효과) | Virtuous cycle where superior AI drives adoption, generating unique behavioral telemetry that refines models, entrenching market leadership. | 뛰어난 AI 사용자 경험 ➔ 사용자 유입 증가 ➔ 양질의 독점 데이터 축적 ➔ 모델 정밀도 향상 ➔ 더 많은 사용자 유치의 선순환. | 경쟁사가 쉽게 모방할 수 없는 지속 가능한 비즈니스 해자(Moat) 구축 |
| **AI FinOps**<br>(AI 재무 운영 프레임워크) | Operational practice combining cloud engineering and financial accountability to monitor, forecast, and optimize generative AI expenditure. | 변동성이 큰 클라우드 AI 추론 비용과 API 요금을 실시간으로 모니터링, 통제, 최적화하는 재무-엔지니어링 협업 체계. | 예상치 못한 AI 비용 폭증을 방지하고 ROI를 극대화하는 거버넌스 |
| **Cost Allocation Tags**<br>(비용 할당 태그) | Metadata labels assigned to AWS resources tracking consumption by business department, project code, or environment. | AWS 리소스에 프로젝트명, 부서명, 환경 메타데이터를 부여하여 부서별 AI 사용 비용을 추적하는 기능. | 부서별 AI 예산 책임성 부여 및 정확한 TCO 분배의 정답 |
| **Model Routing / Cascading**<br>(모델 라우팅 / 캐스케이딩) | Dynamic architectural tiering sending simple queries to economical small models and routing complex reasoning to frontier models. | 들어오는 질문의 난이도를 분석하여, 단순 질의는 저비용 경량 모델로, 복잡 질의는 고성능 대형 모델로 분기 전송하는 설계. | 성능 저하 없이 전체 AI 인프라 추론 비용을 70% 이상 절감하는 핵심 설계 |
| **Provisioned Throughput**<br>(프로비저닝 처리량) | Reserving committed model capacity (Tokens Per Minute) in Amazon Bedrock to secure predictable latency and lower unit costs at volume. | Amazon Bedrock에서 분당 토큰 처리량(TPM)을 약정 예약하여 안정적인 처리 성능과 볼륨 할인을 받는 과금 방식. | 대규모 상시 트래픽이 발생하는 엔터프라이즈 프로덕션 환경의 비용 최적화 정답 |

---

## 3. 도메인 3: AI 거버넌스 및 책임 있는 AI 리더십 (AI Governance & Responsible AI)

| Key Term (영문 / 국문) | 🇺🇸 English Exam Definition & Context | 🇰🇷 한국어 번역 및 비즈니스 핵심 설명 | 🎯 Exam Answer Match (출제 및 정답 매칭) |
| :--- | :--- | :--- | :--- |
| **Responsible AI (RAI)**<br>(책임 있는 AI) | The holistic governance framework ensuring AI systems operate ethically, fairly, transparently, safely, and compliant with laws throughout their lifecycle. | AI 시스템을 전 생애주기에 걸쳐 안전하고, 윤리적이며, 공정하고 신뢰할 수 있게 설계, 구축, 운영하는 전사적 프레임워크. | 기업 평판 보호, 규제 준수, 사용자 신뢰 확보를 위한 최상위 거버넌스 원칙 |
| **Fairness & Algorithmic Bias**<br>(공정성 및 알고리즘 편향) | Guaranteeing AI systems do not produce discriminatory or systematically disadvantageous outcomes across legally protected demographic groups. | 성별, 인종, 종교 등 보호된 속성에 따라 특정 집단에 부당하게 차별적이거나 불리한 예측 결과를 내놓지 않도록 통제하는 원칙. | 대출 심사, 채용 평가 모델에서 편향을 완화하는 핵심 요건 |
| **Demographic Parity**<br>(인구통계학적 동등성) | Fairness metric verifying that the proportion of positive decisions rendered is statistically balanced across sub-populations. | 보호 집단과 비보호 집단 간에 긍정적 결정(예: 채용 합격률, 대출 승인율)을 받을 확률이 통계적으로 균등해야 한다는 기준. | 알고리즘의 차별 여부를 수학적으로 검증하는 정량 지표 |
| **Historical Bias**<br>(과거 데이터 편향) | Systemic inequities embedded in historical training datasets that algorithms learn and perpetuate if uncorrected. | 과거 데이터 수집 당시 존재했던 사회적 편견이나 차별 관행이 데이터셋에 그대로 반영되어 AI가 이를 정상 패턴으로 오인하는 현상. | "과거 10년치 성공적인 채용자 이력서" 학습 시 발생하는 성별 편향의 근본 원인 |
| **Explainability & Interpretability**<br>(설명 가능성 및 해석 가능성) | The technical ability to communicate why an AI model reached a specific conclusion in terms understandable to human stakeholders and auditors. | AI 모델이 왜 그러한 판단이나 예측을 내렸는지 그 이유와 피처 기여도를 인간 사용자와 규제 당국이 이해할 수 있도록 제시하는 역량. | 대출 거절 사유 통보, 의료 진단 근거 제시 의무 준수의 정답 |
| **SHAP Values**<br>(샤플리 기여도 값) | Cooperative game-theoretic measure quantifying each feature's marginal contribution to a model's prediction. | 게임 이론에 기반하여 각 입력 변수(나이, 소득 등)가 최종 모델 예측 결과에 기여한 수학적 영향도를 정량화하는 기법. | Amazon SageMaker Clarify에서 설명 리포트를 생성할 때 사용하는 표준 방식 |
| **Amazon SageMaker Clarify**<br>(세이지메이커 클래리파이) | AWS service detecting bias during data preparation and model monitoring while generating SHAP-based feature attribution explanations. | 데이터셋 및 모델의 잠재적 편향을 감지하고, SHAP 값 기반의 피처 중요도 및 설명 가능성 리포트를 자동 생성하는 도구. | 고위험 AI 모델의 공정성 검증 및 규제 보고서 작성을 위한 AWS 서비스 정답 |
| **Personally Identifiable Information (PII)**<br>(개인 식별 정보) | Any data that can distinguish or trace an individual's identity (e.g., Social Security Numbers, names, medical records). | 이름, 주민등록번호, 신용카드 번호 등 특정 개인을 식별할 수 있는 모든 민감 정보. | 모델 입력 전 반드시 마스킹하거나 차단해야 하는 데이터 |
| **PII Masking / Redaction**<br>(PII 마스킹 / 비식별화) | Automated identification and anonymization of sensitive personal records prior to model ingestion or output rendering. | 텍스트 내의 개인 식별 정보를 탐지하여 `[REDACTED]`나 임의의 기호로 자동 대체하는 보안 조치. | Amazon Bedrock Guardrails의 민감 정보 필터 기능을 통해 구현 |
| **AWS Data Privacy Pledge**<br>(AWS 고객 데이터 보호 서약) | Contractual guarantee that customer prompts, inputs, and knowledge bases are never utilized to train AWS foundation models. | 고객이 Amazon Bedrock이나 Amazon Q에 입력한 프롬프트 및 사내 데이터는 **절대 AWS 기본 파운데이션 모델 학습에 사용되지 않는다**는 서약. | 엔터프라이즈 고객의 데이터 유출 우려를 불식시키는 공식 보안 보증 |
| **Transparency & AI Disclosure**<br>(투명성 및 AI 사용 고지) | Mandate to explicitly inform consumers that they are interacting with an AI system and disclose its capabilities and operational boundaries. | 사용자가 현재 대화하고 있는 대상이 인공지능임을 명확히 안내하고, 모델의 작동 원리와 한계를 투명하게 공개하는 원칙. | 고객 상담 챗봇 도입 시 사용자 신뢰 확보 및 법적 의무 준수 요건 |
| **Synthetic Media Watermarking**<br>(합성 미디어 디지털 워터마킹) | Embedding cryptographic metadata (e.g., C2PA standard) into AI-generated media to prove origin and detect tampering. | AI가 생성한 이미지, 영상에 보이지 않는 암호화된 메타데이터를 삽입하여 진위 여부를 증명할 수 있게 하는 기술. | 딥페이크 악용 방지 및 저작물 출처 투명성 확보의 정답 |
| **Kill-Switch Mechanism**<br>(비상 정지 메커니즘) | Emergency protocol and architectural circuit breaker terminating AI inference endpoints instantaneously during critical failures or breach. | AI 시스템이 심각한 오작동을 일으키거나 공격을 받았을 때, 즉시 추론 트래픽을 차단하고 롤백할 수 있는 긴급 차단 프로토콜. | 중대 보안/규제 사고 발생 시 피해를 즉시 통제하는 필수 운영 장치 |
| **Amazon Bedrock Guardrails**<br>(베드록 가드레일) | Managed policy engine enforcing denied topics, content filters, PII redaction, and contextual grounding across all foundation models. | 유해 콘텐츠 필터링, 금지된 주제 차단, PII 마스킹, 근거 기반 검증(Grounding Check)을 일괄 적용하는 완전관리형 보안 가드. | 엔터프라이즈 책임 있는 AI 보호 정책을 모델 독립적으로 중앙 적용하는 최적 솔루션 |
| **Denied Topics**<br>(금지된 주제 차단) | Configurable guardrail restrictions preventing models from entertaining unauthorized discussions (e.g., competitor comparisons, legal advice). | 기업 정책상 AI가 언급하거나 답변해서는 안 되는 특정 주제(경쟁사 제품 추천, 비공식 금융 투자 권유)를 지정하여 원천 차단하는 기능. | Bedrock Guardrails의 핵심 설정으로 출제 |
| **Contextual Grounding Check**<br>(문맥적 근거 검사) | Bedrock Guardrails capability verifying that generated text is mathematically factual and grounded strictly in retrieved source documentation. | 모델의 생성 응답이 검색된 원본 참조 문서에 명확히 근거하는지 검증하여 거짓 정보를 걸러내는 Guardrails 기능. | RAG 환경에서 모델의 사실무근 환각(Hallucination)을 차단하는 정답 |
| **Human-in-the-Loop (HITL)**<br>(인간 참여형 검증) | Mandatory routing mechanism escalating low-confidence predictions or high-consequence decisions to human experts for adjudication. | 최종 결과의 위험도가 높거나 모델의 신뢰도가 기준치 미만일 때, 인간 전문가의 최종 검토 및 승인 단계를 필수 배치하는 구조. | 대출 거절, 채용 탈락, 의료 진단 등 고위험 시나리오의 필수 아키텍처 |
| **Amazon Augmented AI (Amazon A2I)**<br>(세이지메이커 A2I) | AWS service automating human review workflows when model inference confidence drops below predetermined thresholds. | 모델의 신뢰도가 낮거나 감사 대상인 추론 결과를 인간 검토자 풀에게 자동으로 라우팅하여 검토받도록 하는 완전관리형 HITL 서비스. | 고위험 의사결정의 정확도를 보장하고 모델을 지속 평가하는 AWS 서비스 정답 |
| **EU AI Act Risk Tiers**<br>(EU AI Act 위험 등급) | Four-level classification: Unacceptable (banned), High (strictly regulated), Limited (transparency mandated), Minimal (unregulated). | 위험 크기에 따라 AI를 4등급(허용 불가, 고위험, 제한적 위험, 최소 위험)으로 분류하여 차등 규제하는 법안. | 글로벌 비즈니스를 영위하는 기업의 핵심 준수 표준 |
| **ISO/IEC 42001**<br>(인공지능 경영시스템 표준) | The inaugural international certifiable standard establishing enterprise requirements for establishing and operating an AI Management System (AIMS). | 조직이 책임감 있게 AI를 기획, 개발, 도입, 운영하고 있음을 제3자가 심사하여 공인하는 최초의 글로벌 AI 표준 인증. | 전사적 AI 거버넌스 체계 구축 및 대외 신뢰도 입증의 국제 표준 |
| **Cross-Functional Governance Council**<br>(다학제적 거버넌스 협의체) | Oversight committee comprising IT, Legal, Compliance, Line-of-Business, Security, and HR leaders to balance innovation with risk. | IT 엔지니어뿐만 아니라 법무(Legal), 컴플라이언스, 비즈니스 리더, 정보보안, HR이 모두 참여하는 전사 AI 총괄 위원회. | AI 프로젝트의 비즈니스 가치와 법적/윤리적 리스크를 균형 있게 심의하는 조직 |
| **Model Cards & System Cards**<br>(모델 카드 및 시스템 카드) | Standardized documentation delineating a model's architectural characteristics, intended use cases, performance bounds, and known limitations. | 모델의 개발 목적, 아키텍처, 성능 벤치마크, 학습 데이터 분포, 사용상 제약 사항과 한계를 투명하게 기술한 표준화된 규격 문서. | 투명성 확보, 규제 감사 대응, 사내 모델 거버넌스의 표준 문서 |
| **Copyright Indemnification**<br>(저작권 및 지적재산권 면책) | Cloud vendor contractual defense protecting enterprise customers against third-party intellectual property infringement claims arising from GenAI outputs. | 상용 GenAI 모델이 생성한 콘텐츠가 저작권을 침해하여 소송이 제기될 경우, 클라우드 벤더(AWS 등)가 고객을 대신해 법적 책임을 방어해주는 보증. | 엔터프라이즈가 상용 파운데이션 모델을 안심하고 도입할 수 있게 하는 법적 보호 장치 |

---

## 4. 도메인 4: 비즈니스 준비성, 리더십, AI 혁신 (Readiness & Transformation)

| Key Term (영문 / 국문) | 🇺🇸 English Exam Definition & Context | 🇰🇷 한국어 번역 및 비즈니스 핵심 설명 | 🎯 Exam Answer Match (출제 및 정답 매칭) |
| :--- | :--- | :--- | :--- |
| **4 Dimensions of AI Readiness**<br>(AI 준비성 4대 차원) | Foundational readiness audit: People (skills/culture), Process (agility/workflows), Technology (cloud platform), Governance (data ethics). | 성공적인 AI 도입을 위해 반드시 점검해야 하는 조직의 4대 핵심 축: **People(인력/문화), Process(프로세스), Technology(기술), Governance(거버넌스)**. | 전사 AI 도입 타당성 및 준비 상태 갭 분석의 표준 프레임워크 |
| **AI Maturity Stages**<br>(AI 성숙도 4단계) | Progression: 1. Exploration (ad-hoc), 2. Opportunistic (pilots), 3. Systematic (CoE & standards), 4. Transformational (AI-native business models). | 조직의 AI 역량 발전 단계: **1. Exploration(탐색) ➔ 2. Opportunistic(시범) ➔ 3. Systematic(체계화) ➔ 4. Transformational(전사 혁신)**. | 현재 조직의 위치를 진단하고 다음 단계로의 로드맵을 수립하는 기준 |
| **AWS Cloud Adoption Framework (CAF)**<br>(AWS 클라우드 채택 프레임워크) | Comprehensive methodology examining Business, People, Governance, Platform, Security, and Operations perspectives for cloud & AI adoption. | 기업의 클라우드 및 AI 전환을 비즈니스, 피플, 거버넌스, 플랫폼, 보안, 운영의 6대 관점(Perspectives)에서 체계적으로 가이드하는 프레임워크. | 전사적 AI 준비 상태 진단 및 로드맵 수립의 AWS 공식 방법론 |
| **Data Silos**<br>(데이터 사일로) | Isolated, fragmented departmental data repositories preventing unified enterprise data access and impeding cross-functional AI efficacy. | 조직 내 각 부서마다 데이터가 고립되어 서로 공유되지 못하고 파편화되어 있는 상태. | AI 모델이 통합적 비즈니스 맥락을 학습하지 못하게 가로막는 **최대 장애물** |
| **Data Mesh**<br>(데이터 메시) | Decentralized architecture treating domain data as analytical products owned by business units under federated computational governance. | 중앙 집중식 데이터팀의 병목을 해소하기 위해, 각 도메인 부서가 자신의 데이터를 '데이터 프로덕트'로 직접 소유·관리하는 아키텍처. | 부서 간 데이터 사일로를 타파하고 안전한 공유를 촉진하는 현대적 아키텍처 |
| **Amazon DataZone**<br>(아마존 데이터존) | Fully managed data management service enabling business users to discover, catalog, govern, and share data across enterprise boundaries. | 비즈니스 사용자와 기술팀이 도메인 간 데이터를 검색, 카탈로그화, 공유, 거버넌스할 수 있도록 지원하는 완전관리형 데이터 관리 서비스. | 데이터 메시 패러다임을 AWS 상에서 구현하는 핵심 서비스 정답 |
| **AWS Lake Formation**<br>(AWS 레이크 포메이션) | Centralized service streamlining data lake creation while enforcing granular column- and row-level access permissions. | 데이터 레이크 구축을 간소화하고, 테이블, 열(Column), 행(Row) 수준의 세분화된 접근 권한을 중앙에서 일괄 제어하는 서비스. | 규제 준수 및 안전한 데이터 공유의 보안 인프라 정답 |
| **Data Contracts**<br>(데이터 계약) | Explicit agreements between data producers and downstream AI consumers governing schema changes, latency, and freshness thresholds. | 업스트림 데이터 생산자(엔지니어링)와 다운스트림 AI 소비자 간에 체결하는 공식 스키마 및 품질 협약. | 스키마 변경 사전 공지 및 품질 SLA를 명시하여 다운스트림 AI 모델 중단 사고를 방지하는 거버넌스 장치 |
| **AI Center of Excellence (CoE)**<br>(AI 우수성 센터) | Centralized leadership body formulating enterprise AI strategy, curating reusable assets, establishing guardrails, and guiding business units. | 전사 AI 전략 수립, 클라우드 아키텍처 표준화, 기술 지원, 모범 사례 전파 및 거버넌스 감독을 총괄하는 중앙 전문 조직. | 전사적 AI 도입을 체계화하고 중복 투자를 방지하는 핵심 조직 구조 |
| **Hub-and-Spoke Operating Model**<br>(허브 앤 스포크 조직 모델) | Hybrid organization: Central CoE (Hub) sets platform standards, tooling, and governance while embedded teams (Spokes) execute local business use cases. | 중앙 CoE(Hub)가 인프라, 공통 도구, 보안 거버넌스 표준을 총괄하고, 각 사업 부서 실무자(Spoke)가 도메인 특화 문제를 직접 해결하는 모델. | 중앙 통제력과 현업 민첩성의 균형을 달성하는 **가장 이상적인 엔터프라이즈 AI 조직 모델** |
| **AI Champions Network**<br>(AI 챔피언 네트워크) | Grassroots network of embedded departmental advocates peer-coaching colleagues, identifying friction points, and bridging to the CoE. | 각 현업 비기술 부서에서 AI를 앞장서 학습하고 동료들을 코칭하며 현업 유스케이스를 발굴하는 풀뿌리 혁신 리더 네트워크. | 탑다운 지시의 한계를 극복하고 현장 실무자들의 자발적 AI 채택을 이끄는 핵심 동력 |
| **Augmentation over Replacement**<br>(대체가 아닌 증강 철학) | Leadership philosophy emphasizing that AI automates repetitive cognitive drudgery to elevate human creativity and empathy, dispelling job loss anxiety. | AI는 직원을 해고하기 위한 대체자가 아니라, 반복 업무를 제거하여 인간이 고부가가치 창의/전략 업무로 역량을 높이도록 돕는 보조자라는 원칙. | AI 도입 시 직원들의 고용 불안과 문화적 저항을 극복하는 최우선 리더십 메시지 |
| **Psychological Safety**<br>(심리적 안전감) | Cultural climate where employees feel secure experimenting with new AI tools, asking questions, and reporting defects without fear of reprisal. | 직원들이 처벌 걱정 없이 새로운 AI 기술을 자유롭게 실험하고, 한계점을 솔직하게 보고할 수 있는 조직 문화. | AI 혁신과 창의적 실험을 촉진하는 필수 조직 환경 |
| **AWS PartyRock**<br>(AWS 파티락) | Intuitive no-code generative AI app-building playground enabling non-technical staff to experiment with prompt engineering safely. | 비개발자도 자연어 프롬프트만으로 단 몇 분 만에 위젯 기반의 생성형 AI 앱을 만들고 공유할 수 있는 노코드(No-Code) 웹 도구. | 사내 해커톤이나 AI 리터러시 교육에서 비기술 직무의 아이디어를 빠르게 시제품화하는 최적 도구 |
| **Secure Prototyping Sandbox**<br>(안전한 프로토타이핑 샌드박스) | Isolated internal environment governed by Bedrock Guardrails allowing employees to experiment freely without leaking proprietary enterprise data. | 사내 기밀 유출이나 데이터 외부 유출 우려 없이 Amazon Bedrock Guardrails가 적용된 격리된 사내 전용 AI 실험 포털. | 현업 직원들의 안전한 자유 실험을 보장하는 인프라 환경 |
| **4-Stage Transformation Framework**<br>(4단계 AI 혁신 프레임워크) | AWS innovation pathway: **1. Envision (strategy) ➔ 2. Experiment (PoC) ➔ 3. Launch (pilot/MVP) ➔ 4. Scale (enterprise-wide integration)**. | AWS가 권장하는 체계적 확산 단계: **1. Envision(구상) ➔ 2. Experiment(실험/PoC) ➔ 3. Launch(출시/MVP) ➔ 4. Scale(전사 확장/운영)**. | 파일럿의 일회성 성공을 넘어 전사적 가치로 스케일업하는 표준 라이프사이클 |
| **Business Process Re-engineering (BPR)**<br>(비즈니스 프로세스 재설계) | Radically redesigning fundamental end-to-end workflows around AI capabilities rather than merely superimposing automated chatbots on legacy bureaucracy. | 기존의 낡은 수작업 절차에 단순히 AI 챗봇을 덧붙이는 것이 아니라, AI의 자율성과 속도에 맞춰 전체 업무 흐름을 근본적으로 재설계하는 혁신. | AI 도입을 통한 10배 이상의 극적인 생산성 혁신을 달성하는 방법 |
