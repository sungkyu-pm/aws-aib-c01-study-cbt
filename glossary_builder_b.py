#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part B of the Exhaustive Master Glossary & Exam Expressions Encyclopedia for AWS AIB-C01.
Contains:
- Section 2: 임원진(C-Suite) 의사결정·투자 거버넌스·AI FinOps 재무 용어 50선
- Section 3: AI/ML 학습 패러다임·통계적 검증·데이터 과학 심화 용어 55선
- Section 4: 생성형 AI 커스터마이징·고급 RAG·파인튜닝·경량화·에이전트 용어 60선
"""

GLOSSARY_PART_B = """
---

## 👔 [섹션 2] 임원진(C-Suite) 의사결정·투자 거버넌스·AI FinOps 재무 용어 50선

실제 시험에서 **CEO, CFO, CISO, CLO, CHRO, COO, CIO, CDO 및 투자심의위원회(Investment Review Board)** 가 사용하는 재무·전략·거버넌스 핵심 용어입니다.

| 영문 용어 (English Term) | 한국어 명칭 | 실전 비즈니스·시험 정의 및 의사결정 활용 포인트 |
| :--- | :--- | :--- |
| **AI Steering Committee / Executive Sponsor** | 전사 AI 운영위원회 / 임원 스폰서 | CEO·CFO·CISO·CLO·사업본부장이 참여하여 전사 AI 우선순위 조정, 예산 관문 승인, 부서 간 데이터 사일로 중재, 고위험 과제 최종 승인을 수행하는 최상위 의사결정 기구. |
| **CapEx (Capital Expenditure) vs. OpEx (Operating Expenditure)** | 자본적 지출 vs. 운영 비용 | 자체 GPU 클러스터 구매(`CapEx`) 대신 클라우드 종량제/약정 기반 AI 서비스(`OpEx`)를 활용하여 초기 자본 묶임과 하드웨어 노후화 위험을 제거하는 재무 전환 전략. |
| **Total Cost of Ownership (TCO) — Full Lifecycle** | 전 생애주기 총소유비용 | 모델 초기 구축비(15~20%)뿐만 아니라 데이터 수집·정제·라벨링, 벡터 DB 운영, 추론 토큰/인프라, 드리프트 모니터링, 정기 재학습, 보안 가드레일, 규제 감사, 현업 교육비(80%)를 모두 합산한 비용. |
| **Net Present Value (NPV) & Internal Rate of Return (IRR)** | 순현재가치 및 내부수익률 | 다년도 AI 전환 프로젝트의 미래 현금 창출액을 할인율(자본비용)로 할인하여 현재 가치로 환산한 재무 타당성 지표. |
| **Risk-Adjusted ROI** | 위험 조정 투자수익률 | 단순 낙관적 기대 수익이 아니라, 모델 정확도 미달 확률·규제 과징금 위험·구현 지연 리스크를 확률 가중치로 차감하여 보수적으로 산출한 실질 ROI (CFO 설득 필수 지표). |
| **Payback Period / Breakeven Point** | 투자 회수 기간 / 손익분기점 | 초기 AI 구축 및 변화관리 투자 비용이 월간 운영비 절감액 또는 증분 마진으로 완전히 상쇄되는 시점. |
| **Cost of Inaction (COI)** | 미도입 비용 (행동하지 않음으로써 발생하는 손실) | AI 투자를 미뤘을 때 경쟁사 대비 잃게 되는 시장점유율, 고객 이탈 손실, 수작업 유지로 인한 누적 비효율 비용. |
| **Opportunity Cost** | 기회비용 | 한정된 데이터 과학자 인력과 GPU 예산을 저가치 과제 A에 묶어둠으로써 고수익 과제 B를 추진하지 못해 포기하게 되는 가치. |
| **Unit Economics (`Cost per Transaction / Outcome`)** | 단위 경제성 | 추론 API 호출 1건당 비용이 아니라, **비즈니스 성과 1건(예: 해결된 상담 티켓 1건, 성사된 주문 1건)당 소요된 총 AI 비용**과 해당 거래가 창출한 한계 이익(`Marginal Profit`)의 비율. |
| **Margin Erosion from Unbounded Token Consumption** | 무제한 토큰 소비로 인한 마진 잠식 | 정액제(예: 월 $20) AI 기능을 출시했으나 헤비 유저들의 장문 프롬프트·무한 에이전트 루프로 인해 추론 원가가 구독료를 초과하여 팔수록 적자가 나는 현상. |
| **Cost Allocation Tags (`Project / BU / UseCase`)** | 비용 배부 태그 | AWS 리소스 및 Bedrock API 호출마다 부서·프로젝트·환경(`dev/prod`) 태그를 강제 부여하여 누구 때문에 비용이 발생했는지 100% 추적하는 FinOps 기초. |
| **Showback vs. Chargeback** | 비용 가시화 리포팅 vs. 부서 예산 실청구 | • **Showback**: 부서별 AI 소비 금액을 대시보드로 공개하여 자발적 절감 유도<br>• **Chargeback**: 사용한 토큰·GPU 비용을 해당 현업 본부의 실제 손익(P&L) 예산에서 직접 차감 |
| **Token Budget Quota & Rate Limiting** | 토큰 예산 쿼터 및 호출 속도 제한 | 특정 사용자·부서·에이전트가 일일/월간 허용된 토큰 한도를 초과하지 못하도록 API 게이트웨이 수준에서 차단·쓰로틀링하는 비용 보호 장치. |
| **On-Demand Pricing (Pay-As-You-Go)** | 온디맨드 종량제 과금 | 약정 없이 입출력 토큰 수(또는 초당 추론 시간)만큼만 지불. 트래픽을 예측할 수 없는 **초기 PoC/파일럿이나 간헐적 스파이크 워크로드**에 최적. |
| **Provisioned Throughput (Committed Capacity)** | 프로비저닝된 처리량 (약정 용량) | 시간/월 단위로 고정된 모델 처리 용량(`Model Units`)을 사전 약정. **연중무휴 예측 가능한 대규모 상시 트래픽이나 커스텀 파인튜닝 모델 서빙 시 단가 절감 및 처리량 SLA 보장**에 필수. |
| **Batch Inference Pricing** | 배치 추론 할인 과금 | 즉각적인 실시간 응답이 필요 없는 대량 문서 요약·야간 카탈로그 분류를 비동기 일괄 작업으로 제출하여 **온디맨드 대비 약 50% 저렴하게 처리**하는 방식. |
| **Amazon EC2 Spot Instances for Fault-Tolerant Training** | 내결함성 학습을 위한 스팟 인스턴스 활용 | 클라우드 유휴 GPU 용량을 온디맨드 대비 최대 70~90% 할인된 가격에 사용. 중단될 수 있으므로 **주기적 체크포인팅(`Managed Spot Training Checkpointing`)이 구현된 비긴급 모델 훈련**에 사용 (실시간 고객 추론에는 부적합). |
| **AWS Savings Plans / Reserved Instances** | 세이빙 플랜 / 예약 인스턴스 | 1년 또는 3년 기간 약정을 통해 `SageMaker` 및 `EC2` 컴퓨팅 비용을 대폭 할인받는 재무 약정 모델. |
| **Build vs. Buy vs. Partner Decision Matrix** | 자체 구축 vs. 구매 vs. 파트너십 의사결정 매트릭스 | 전략적 차별성(`Differentiation`), 시급성(`Time-to-Market`), 내부 역량(`Internal Talent`), 데이터 민감도, 장기 TCO를 축으로 조달 방식을 결정하는 프레임워크. |
| **Commercial Off-The-Shelf (COTS) / Turnkey SaaS** | 상용 기성품 소프트웨어 / 턴키 SaaS | 인사·회계·일반 고객지원 등 범용 업무에 즉시 도입 가능한 완성형 AI 솔루션 (가장 빠른 Time-to-Value). |
| **Co-Delivery / Joint Squad Model** | 공동 수행 / 혼성 스쿼드 모델 | 외부 컨설팅/SI 파트너에게 블랙박스 외주(`Turnkey Outsourcing` = 내부 역량 축적 실패)를 주지 않고, 사내 엔지니어와 외부 전문가를 한 팀으로 묶어 구축하며 기술을 내재화하는 방식. |
| **Service Level Agreement (SLA) vs. SLO vs. SLI** | 서비스 수준 협약 vs. 목표 vs. 지표 | • **SLI**: 실제 측정된 지연시간(예: `p99 Latency = 420ms`) 및 가용성 수치<br>• **SLO**: 내부 엔지니어링 팀이 사수하려는 목표치 (예: `p99 < 500ms`)<br>• **SLA**: 고객/현업과 맺은 공식 계약 기준 및 위반 시 페널티 조항 |
| **p50 / p95 / p99 Tail Latency** | 백분위수 지연시간 (중앙값 / 상위 5% / 상위 1% 꼬리 지연) | 평균 응답 시간(`Mean Latency`)은 양호해 보여도 가장 느린 상위 1%(`p99 Tail Latency`)가 15초씩 걸리면 고객 이탈이 발생하므로, 엔터프라이즈 SLA는 반드시 `p95/p99` 기준으로 관리해야 함. |
| **Time-to-First-Token (TTFT) & Tokens Per Second (TPS)** | 첫 토큰 도달 시간 및 초당 생성 토큰 수 | 생성형 AI 챗봇의 체감 속도를 좌우하는 핵심 지표. **스트리밍 응답(`Response Streaming`)** 을 적용하면 전체 답변 완성 시간은 같아도 `TTFT`가 0.5초로 줄어들어 체감 UX가 극적으로 개선됨. |
| **Incremental Uplift / Causal Attribution** | 순수 증분 효과 / 인과적 기여도 귀속 | 마케팅·영업 매출 상승분 중 외부 경기 회복이나 가격 할인의 영향을 빼고 **오직 신규 AI 모델 도입 때문에 순증한 매출/전환율**을 통계적으로 분리해내는 것. |
| **Goodhart's Law in AI KPIs** | 굿하트의 법칙 (측정 지표가 목표가 되는 순간 왜곡됨) | 예: 챗봇 KPI를 '평균 대화 종료 시간 단축'으로만 잡으면 AI가 고객 문제를 해결하지 않고 대화를 강제로 빨리 끊어버리는 부작용 발생 ➔ 반드시 **해결률(`FCR`)과 고객만족도(`CSAT`)를 결합한 균형 지표(`Counter-Balance Metric`)** 를 써야 함. |
| **RACI Matrix (`Responsible, Accountable, Consulted, Informed`)** | RACI 책임 할당 매트릭스 | • **R (실행 책임)**: 데이터 과학자 / MLOps 엔지니어<br>• **A (최종 결과 책임 — 단 1명)**: 비즈니스 오너 / 임원 스폰서<br>• **C (사전 협의)**: 법무(CLO) / 보안(CISO)<br>• **I (결과 통보)**: 유관 부서 |
| **Product-Centric AI Funding vs. Project-Centric Funding** | 제품 중심 상시 펀딩 vs. 일회성 프로젝트 펀딩 | AI 모델은 배포 후 데이터 드리프트 관리와 지속적 개선이 필수이므로, 구축 후 팀을 해체하는 일회성 프로젝트 예산(`Project Funding`)이 아니라 **장기 프로덕트 오너십 기반 상시 예산(`Product-Centric Lifecycle Funding`)** 으로 운영해야 함. |

---

## 🧠 [섹션 3] AI/ML 학습 패러다임·통계적 검증·데이터 과학 심화 용어 55선

실제 시험에서 **문제 유형별 최적의 학습 방법론 선택, 과적합/데이터 누수 방지, 모델 평가 지표 해석**을 물을 때 등장하는 핵심 용어입니다.

| 영문 용어 (English Term) | 한국어 명칭 | 실전 시험 출제 맥락 및 핵심 판별 포인트 |
| :--- | :--- | :--- |
| **Supervised Learning (`Classification` & `Regression`)** | 지도 학습 (분류 및 회귀) | 입력 피처(X)와 정답 라벨(Y)이 쌍으로 존재할 때 학습. 범주 예측(사기/정상, 질병 유무)은 **Classification**, 연속형 수치 예측(내일 전력 수요량, 주택 가격, 잔여 수명 시간)은 **Regression**. |
| **Binary vs. Multi-Class vs. Multi-Label Classification** | 이진 분류 vs. 다중 클래스 분류 vs. 다중 라벨 분류 | • **Binary**: 스팸 여부 (택1)<br>• **Multi-Class**: 불량 유형 A/B/C/D 중 정확히 하나로 분류 (상호배타적)<br>• **Multi-Label**: 영화 한 편에 [액션, SF, 스릴러] 등 여러 태그를 동시에 부여 |
| **Tree-Based Ensemble (`XGBoost`, `LightGBM`, `Random Forest`)** | 트리 기반 앙상블 모델 | **정형 테이블 데이터(`Structured Tabular Data`: 행·열 DB, 재무제표, 센서 통계)** 에서 딥러닝/LLM보다 학습·추론 비용이 훨씬 저렴하고 정확도와 변수 중요도 설명가능성(`SHAP`)이 가장 뛰어난 실무 1순위 모델. |
| **Unsupervised Learning (`Clustering`, `Dimensionality Reduction`, `Anomaly Detection`)** | 비지도 학습 (군집화, 차원 축소, 이상 탐지) | 정답 라벨(Y)이 없는 상태에서 데이터 내재 구조 발굴. 고객 세분화는 `K-Means / DBSCAN`, 고차원 시각화는 `PCA / t-SNE / UMAP`, 미지의 설비 이상/제로데이 침입 탐지는 `Random Cut Forest / Isolation Forest`. |
| **Semi-Supervised Learning & Pseudo-Labeling** | 준지도 학습 및 의사 라벨링 | 소량의 고품질 전문가 라벨 데이터(예: 5%)와 대량의 비라벨 데이터(95%)를 결합하여, 초기 모델이 고신뢰도로 예측한 비라벨 샘플에 의사 라벨(`Pseudo-Label`)을 붙여 재학습하는 기법. |
| **Active Learning (`Human-in-the-Loop Data Labeling`)** | 능동 학습 (불확실성 기반 선별 라벨링) | 수백만 건의 비라벨 데이터 중 모델이 가장 헷갈려하는(결정 경계 근처의 엔트로피가 높은) 샘플만 골라 인간 전문가(`SageMaker Ground Truth`)에게 라벨링을 요청하여 **라벨링 비용과 시간을 70~80% 절감**. |
| **Weak Supervision / Programmatic Labeling (`Snorkel` style)** | 약지도 학습 / 프로그래밍 방식 라벨링 | 도메인 전문가의 휴리스틱 규칙, 정규표현식, 외부 사전(`Labeling Functions`)을 조합해 대량의 노이즈 라벨을 빠르게 자동 생성한 뒤 확률 모델로 디노이징하는 기법. |
| **Self-Supervised Learning (SSL)** | 자기지도 학습 | 인간의 수동 라벨링 없이 원시 텍스트/이미지/유전체 자체의 일부를 가리고(`Masked Language Modeling`) 맞추거나 다음 토큰을 예측(`Causal Language Modeling`)하며 파운데이션 모델을 사전학습하는 패러다임. |
| **Reinforcement Learning (RL: `Agent, Environment, State, Action, Reward Policy`)** | 강화 학습 | 정적 정답이 없는 동적 환경에서 에이전트가 행동(`Action`)을 취하고 환경으로부터 보상(`Reward`) 또는 페널티를 받으며 **장기 누적 보상을 극대화하는 정책(`Policy`)** 을 학습 (자율 로봇 제어, 동적 가격 결정, 실시간 입찰). |
| **Exploration vs. Exploitation Trade-off (`Multi-Armed Bandit`)** | 탐색 vs. 활용 딜레마 (멀티 암드 밴딧) | 이미 효과가 검증된 추천/배너만 계속 보여줄 것인가(`Exploitation`), 아니면 잠재적으로 더 나을 수 있는 새로운 옵션을 실험해 볼 것인가(`Exploration`)의 균형. 실시간 개인화 추천의 콜드스타트 해결에 핵심. |
| **Transfer Learning & Domain Adaptation** | 전이 학습 및 도메인 적응 | 대규모 범용 데이터(예: ImageNet, 웹 코퍼스)로 이미 학습된 모델의 하위 특징 추출 층(`Feature Extractor`)을 재사용하고, 상단 레이어만 자사 소량 도메인 데이터로 미세조정하여 적은 데이터로도 고성능 달성. |
| **Overfitting (High Variance) vs. Underfitting (High Bias)** | 과적합(높은 분산) vs. 과소적합(높은 편향) | • **Overfitting**: 훈련셋 점수는 99%이나 테스트셋 점수가 65%로 폭락 (훈련 노이즈까지 암기) ➔ **해결**: 데이터 증강, 정규화(`L1/L2/Dropout`), 피처 축소, 조기 종료(`Early Stopping`)<br>• **Underfitting**: 훈련셋·테스트셋 모두 60%로 낮음 (모델이 너무 단순함) ➔ **해결**: 모델 용량/복잡도 확대, 유의미한 파생 피처 추가(`Feature Engineering`), 정규화 완화 |
| **Stratified K-Fold Cross-Validation** | 계층화 K-겹 교차 검증 | 데이터가 적거나 클래스 불균형(예: 사기 1%, 정상 99%)이 심할 때, 각 폴드(Fold)마다 양성/음성 비율을 동일하게 유지하며 K번 번갈아 훈련·검증하여 평가의 신뢰도를 높이는 필수 기법. |
| **Temporal Split (Time-Based Train/Test Split)** | 시간순 데이터 분할 | 시계열 데이터(주가, 수요 예측, 사기 탐지)를 무작위로 섞어서(`Random Split` = **오답!** 미래 정보가 과거 학습에 섞이는 누수 발생) 나누지 않고, **반드시 특정 시점 이전 데이터로 학습하고 이후 미래 데이터로 검증**하는 원칙. |
| **Data Leakage / Target Leakage** | 데이터 누수 / 타겟 누수 | 추론 시점에는 절대 알 수 없는 결과 변수(예: '대출 연체 추심 담당자 배정 여부' 컬럼)가 훈련 피처에 실수로 포함되어 개발 중에는 정확도가 99.9%로 나왔으나 실제 프로덕션 배포 즉시 무용지물이 되는 치명적 오류. |
| **Class Imbalance & `SMOTE` / Class-Weighted Loss** | 클래스 불균형 및 소수 클래스 오버샘플링 / 가중 손실 함수 | 불량이나 희귀질환 데이터가 전체의 0.1%뿐일 때 단순 정확도(`Accuracy`)는 99.9%가 나오는 착시 발생. **`SMOTE`(합성 소수 샘플링) 또는 소수 클래스 오분류에 큰 페널티를 주는 `Class-Weighted Loss`와 `PR-AUC / F1-Score` 평가**가 정답. |
| **Confusion Matrix (`TP, FP, TN, FN`)** | 혼동 행렬 (진양성, 위양성[오탐], 진음성, 위음성[미탐]) | 비즈니스 의사결정의 핵심: **위양성(`False Positive`: 정상 고객을 사기범으로 오차단해 고객 이탈 유발)** 과 **위음성(`False Negative`: 실제 암 환자나 중대 설비 결함을 정상으로 놓쳐 생명/대형 사고 유발)** 의 비용 비대칭성을 분석해야 함. |
| **Precision (정밀도) vs. Recall (재현율/민감도) Trade-off** | 정밀도 vs. 재현율 트레이드오프 | • **Precision 중시 (`TP / (TP+FP)`)**: 오탐(`FP`) 비용이 클 때 (예: VIP 고객 계좌 자동 동결, 스팸 메일함 자동 삭제)<br>• **Recall 중시 (`TP / (TP+FN)`)**: 미탐(`FN`) 비용이 치명적일 때 (예: 암 조기 스크리닝, 항공기 엔진 균열 탐지, 자금세탁 의심 플래깅) |
| **F1-Score & `F-beta` Score / `PR-AUC` vs. `ROC-AUC`** | 조화평균 F1 점수 및 PR-AUC vs. ROC-AUC | 극심한 클래스 불균형(예: 이상거래 0.05%)에서는 다수 음성(`TN`) 때문에 `ROC-AUC`가 부풀려지므로, 반드시 **`PR-AUC (Precision-Recall AUC)`와 비즈니스 비용 가중치를 반영한 `F-beta Score`** 를 사용해야 함. |
| **Regression Metrics: `MAE`, `RMSE`, `MAPE`, `WAPE`** | 회귀 평가지표 (평균절대오차, 평균제곱근오차, 평균절대백분율오차, 가중절대백분율오차) | • **RMSE**: 큰 오차(Outlier)에 제곱 페널티를 크게 부여할 때<br>• **MAE**: 이상치에 강건한 평균 오차 파악 시<br>• **MAPE / WAPE**: 유통·소매 수요예측에서 품목 간 판매량 스케일 차이를 보정하여 백분율(%) 오차를 보고할 때 표준 KPI. |
| **Probability Calibration (`Platt Scaling` / `Isotonic Regression`)** | 예측 확률 보정 | 모델이 출력한 신뢰도 점수(`Confidence = 0.90`)가 실제로도 90%의 정답 확률을 의미하도록 보정하는 작업. **`Confidence-Based HITL` 임계치 라우팅을 설계할 때 선행되어야 하는 핵심 단계.** |
| **Data Drift (Covariate Shift) vs. Concept Drift** | 데이터 드리프트(입력 분포 변화) vs. 컨셉 드리프트(인과 관계 변화) | • **Data Drift**: 입력 피처의 분포 자체가 변함 (예: 신규 연령대 고객 대거 유입, 카메라 센서 노후화로 이미지 밝기 변화)<br>• **Concept Drift**: 입력은 같아도 정답과의 관계가 변함 (예: 금리 폭등·팬데믹으로 인해 동일한 소득 수준 고객의 소비/연체 행동 양식 자체가 바뀜) |
| **Differential Privacy (DP) & Synthetic Data Generation** | 차등 프라이버시 및 프라이버시 보존 합성 데이터 생성 | 실제 환자·금융 고객 원시 데이터를 직접 공유하거나 외부 개발환경에 반출할 수 없을 때, 수학적으로 개인 식별이 불가능하도록 프라이버시 예산(ε, Epsilon) 노이즈를 적용해 **원본의 통계적 분포만 보존한 가상 합성 데이터(`Synthetic Data`)** 를 생성하는 기법. |
| **Federated Learning (분산 연합 학습)** | 연합 학습 | 병원·은행·스마트폰 엣지 기기들이 각자의 민감한 원본 데이터를 중앙 클라우드로 모으지 않고, **로컬 기기 안에서만 모델을 학습한 뒤 가중치 변화량(`Gradients`)만 암호화해 중앙 서버에서 집계(`Federated Averaging`)** 하는 프라이버시 보존 학습법. |
"""

if __name__ == "__main__":
    print("GLOSSARY_PART_B length:", len(GLOSSARY_PART_B))
