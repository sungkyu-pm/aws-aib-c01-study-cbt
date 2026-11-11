#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part 2 of the Master Glossary & Exam Expressions Builder for AWS AIB-C01.
Generates:
- Part 2: C-Suite 임원진 의사결정 딜레마 & 핵심 역할·표현 사전
- Part 3: AI/ML 학습 방법론 & 모델 최적화 필수 용어·표현 사전
"""

PART2_MD = """
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
"""

if __name__ == "__main__":
    print("PART2_MD length:", len(PART2_MD))
