#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part D of the Exhaustive Master Glossary & Exam Expressions Encyclopedia for AWS AIB-C01.
Contains:
- Section 7: 데이터 아키텍처·데이터 메시·MLOps/LLMOps·클라우드/엣지 인프라 용어 45선
- Section 8: 전사 AI 전환 프레임워크(AWS CAF·성숙도 모델·조직 변화관리·CoE) 용어 45선
- Section 9: 16대 산업 도메인별 실전 빈출 표현 & KPI 80선
"""

GLOSSARY_PART_D = """
---

## 🗄️ [섹션 7] 데이터 아키텍처·데이터 메시·MLOps/LLMOps·클라우드/엣지 인프라 용어 45선

데이터 사일로 해소, 고품질 AI 데이터 공급망, 프로덕션 MLOps 자동화, 하이브리드/엣지 추론 인프라 설계 시 등장하는 핵심 용어입니다.

| 영문 용어 (English Term) | 한국어 명칭 | 실전 시험 출제 맥락 및 아키텍처 정답 공식 |
| :--- | :--- | :--- |
| **Data Silos & Data Hoarding** | 데이터 사일로 및 부서 이기주의적 데이터 독점 | 사업부별로 데이터가 각자의 레거시 DB에 갇혀 있고, 정치적 책임 회피나 권력 유지를 위해 타 부서와의 데이터 공유를 거부하는 현상. **기술만으로는 해결 안 되며 임원 스폰서십 + `Data Mesh (Data-as-a-Product)` + 성과급 인센티브 연동**이 정답. |
| **Domain-Oriented Data Mesh (`Data-as-a-Product`)** | 도메인 지향 데이터 메시 (제품으로서의 데이터) | 모든 데이터를 중앙 IT 팀 한 곳에서 정제하려다 병목이 생기는(`Centralized Data Lake Bottleneck`) 문제를 해결하기 위해, **데이터를 가장 잘 아는 각 현업 도메인(물류, 재무, 마케팅)이 자기 데이터를 '완성된 제품'처럼 품질·스키마를 보증해 발행(`Publish`)하고, 중앙에서는 통합 카탈로그(`Amazon DataZone`)와 보안 정책만 표준화**하는 분산 아키텍처. |
| **Data Contracts & Automated Schema Validation Gates** | 데이터 계약 및 자동 스키마 검증 관문 | 업스트림 ERP/앱 개발팀이 사전 예고 없이 DB 컬럼명을 바꾸거나 단위를 변경해 다운스트림 AI 모델이 붕괴되는 사고(`Silent Model Failure`)를 막기 위해, **생산자와 소비자 간에 데이터 스키마·결측치 허용률·지연시간 SLA를 코드로 명문화(`Data Contract`)하고 위반 시 파이프라인 초입에서 즉시 차단·알림(`AWS Glue Data Quality`)** 하는 체계. |
| **Data Lakehouse (`Apache Iceberg / Delta / Hudi` on S3)** | 데이터 레이크하우스 | 객체 스토리지(`Amazon S3`)의 저렴한 확장성과 데이터 웨어하우스(`Amazon Redshift`)의 트랜잭션 무결성(`ACID`), 스키마 진화, 타임트래블 스냅샷(특정 과거 시점 훈련 데이터 완벽 재현)을 결합한 현대적 AI 데이터 기반. |
| **Zero-ETL Integration** | 제로 ETL 통합 | 운영 데이터베이스(`Amazon Aurora / DynamoDB`)에서 분석/AI 스토리지(`Amazon Redshift / OpenSearch`)로 데이터를 옮길 때 복잡한 수동 ETL 배치 스크립트를 짜지 않고 거의 실시간으로 자동 복제하여 데이터 신선도(`Data Freshness`)를 높이는 기법. |
| **Fine-Grained Access Control (`Row-Level`, `Column-Level`, `Cell-Level`, `Tag-Based ABAC`)** | 세분화된 데이터 접근 제어 (`AWS Lake Formation`) | 데이터 사일로를 풀기 위해 모든 직원에게 전체 테이블 권한을 주면(오답: 보안 참사) 안 되므로, **단일 데이터 레이크 위에서 직무/속성 태그(`LF-TBAC`)에 따라 인사팀 외에는 연봉·주민번호 컬럼(`Column-Level`)과 타 국가 행(`Row-Level`)이 자동 마스킹/차단**되게 제어하는 기법. |
| **Centralized Feature Store (`Amazon SageMaker Feature Store`)** | 중앙 집중식 피처 스토어 | 부서마다 동일한 '최근 30일 고객 평균 결제액' 피처를 중복 개발하는 낭비를 막고, **실시간 추론용 저지연 온라인 스토어(`Online Store`)와 대규모 학습용 오프라인 스토어(`Offline Store`) 간 피처 정의를 100% 일치시켜 학습-서빙 불일치(`Training-Serving Skew`)를 원천 방지**하는 저장소. |
| **Training-Serving Skew (학습-서빙 불일치)** | 학습-서빙 스큐 | 모델 훈련 시 사용한 피처 계산 로직(예: Python Pandas 배치 집계)과 실시간 프로덕션 서빙 시의 피처 계산 로직(예: Java 실시간 스트림)이 미세하게 달라 프로덕션 예측 정확도가 급락하는 현상. **중앙 `Feature Store`와 시점 일치 조인(`Point-in-Time Travel Join`)** 이 정답. |
| **Data Residency & Digital Sovereignty (데이터 주권 및 역내 보관 의무)** | 데이터 레지던시 및 디지털 주권 | 특정 국가(독일, 한국, 사우디 등)의 금융·공공·의료 데이터가 물리적으로 해당 국가 국경 밖의 클라우드 리전으로 반출되는 것을 금지하는 법규. **해당 국가 내 AWS Region 고정, `AWS Outposts`, 또는 `AWS Dedicated Local Zones` + 지역별 거버넌스 가드레일**로 해결. |
| **Edge Computing vs. Cloud Inference Trade-off** | 엣지 컴퓨팅 vs. 클라우드 추론 트레이드오프 | • **Edge 배포 필수 상황**: 1) `Sub-10ms` 초저지연 제어(자율주행, 고속 컨베이어 비전), 2) 인터넷 단절/불안정 환경(원양 선박, 지하 광산, 폐쇄망 공장), 3) 고화질 4K 비디오 수백 채널의 클라우드 전송 대역폭(`Egress Bandwidth`) 비용 절감.<br>• **정답 패턴**: 대규모 학습과 관리는 클라우드에서 수행하고, 양자화/컴파일(`SageMaker Neo / IoT Greengrass`)된 경량 모델을 엣지로 배포하는 **Edge-Cloud Hybrid Flywheel**. |
| **MLOps / LLMOps Maturity Levels (Level 0 ➔ Level 1 ➔ Level 2)** | MLOps 성숙도 단계 | • **Level 0**: 데이터 과학자가 로컬 노트북에서 수동 학습 후 모델을 수동 전달 (재현 불가, 드리프트 방치)<br>• **Level 1**: 데이터 수집 ➔ 검증 ➔ 학습 ➔ 평가 파이프라인(`CT: Continuous Training`) 자동화 및 드리프트 트리거 재학습<br>• **Level 2**: CI/CD/CT 완전 자동화, 카나리 배포, 자동 롤백, 계보 추적, 전사 표준 템플릿화 |
| **Model Registry & Approval Workflow (`SageMaker Model Registry`)** | 모델 레지스트리 및 배포 승인 워크플로우 | 학습된 모든 모델 버전의 성능 지표, 편향/설명가능성 리포트(`Clarify`), 아티팩트 경로를 중앙 카탈로그에 등록하고, **`Pending ➔ Staging ➔ Approved / Rejected` 상태 관문을 통해 거버넌스 승인을 받은 모델만 프로덕션 CI/CD가 배포**하도록 통제하는 핵심 허브. |
| **Champion / Challenger Testing Framework** | 챔피언 / 챌린저 상시 경쟁 프레임워크 | 현재 프로덕션 주력 모델(`Champion`, 트래픽 90% 처리)과 새롭게 개선된 후보 모델(`Challenger`, 트래픽 10% 처리)을 실전에서 상시 경쟁시켜, 비즈니스 KPI 우위가 통계적으로 확정되면 챌린저를 새로운 챔피언으로 승격시키는 지속 개선 체계. |

---

## 🏛️ [섹션 8] 전사 AI 전환 프레임워크(AWS CAF·성숙도 모델·조직 변화관리·CoE) 용어 45선

도메인 4(21% 비중)에서 집중 출제되는 **AWS Cloud Adoption Framework for AI(CAF-AI), 4단계 성숙도 전환, 변화관리, 인재 육성, 프로세스 재설계** 용어입니다.

| 영문 용어 (English Term) | 한국어 명칭 | 실전 시험 출제 맥락 및 전환 단계별 정답 전략 |
| :--- | :--- | :--- |
| **AWS CAF for AI — 6 Foundational Perspectives** | AWS AI 클라우드 도입 프레임워크 6대 관점 | 1. **Business (비즈니스)**: AI 투자를 전략적 비즈니스 성과 및 ROI와 직결<br>2. **People (피플/사람)**: 조직 구조, 리더십, 변화관리(`ADKAR`), 역할별 업스킬링<br>3. **Governance (거버넌스)**: 포트폴리오 우선순위, AI FinOps, 리스크/윤리/규제 통제<br>4. **Platform (플랫폼)**: 확장 가능한 데이터 레이크하우스, MLOps/GenAI 인프라 아키텍처<br>5. **Security (보안)**: 데이터 프라이버시, IAM 최소 권한, 암호화, 적대적 공격 방어<br>6. **Operations (운영)**: 프로덕션 SLA 모니터링, 드리프트 대응, 장애 복구 SOP |
| **AWS 4 Transformation Phases (`Envision ➔ Align ➔ Launch ➔ Scale`) / (`Envision ➔ Experiment ➔ Launch ➔ Scale`)** | AWS 4단계 전환 여정 | • **1단계 Envision (구상)**: 비즈니스 고충 식별, 가치 역산, 경영진 스폰서 확보, 고가치 파일럿 후보 선정<br>• **2단계 Align / Experiment (정렬 및 실험)**: 부서 간 이해관계/데이터/보안 격차 해소, 사전 중단 기준(`Kill Criteria`)을 갖춘 빠른 MVP/PoC 검증<br>• **3단계 Launch (출시)**: 프로덕션 파일럿 배포, MLOps/가드레일/HITL 연동, 실제 현업 프로세스 통합 및 초기 비즈니스 가치 입증<br>• **4단계 Scale (전사 확산)**: 검증된 아키텍처를 골든 템플릿으로 표준화하여 타 사업부/글로벌로 확산 및 단위 경제성(FinOps) 최적화 |
| **AI Maturity Model — Stage 1 to Stage 4** | 엔터프라이즈 AI 성숙도 4단계 | • **Stage 1 (Ad-Hoc / 산발적 탐색)**: 부서별 고립된 PoC, 거버넌스·표준 부재<br>• **Stage 2 (Opportunistic / 기회주의적 파일럿)**: 첫 프로덕션 성공 사례 등장, 초기 가드레일 및 데이터 파이프라인 구축 시작<br>• **Stage 3 (Systematic / 체계적 확장)**: 중앙 `AI CoE`와 `Hub-and-Spoke` 정착, 전사 MLOps/LLMOps 표준화, 수십 개 유스케이스 운영<br>• **Stage 4 (Transformational / AI-Native 혁신)**: AI가 전사 핵심 의사결정·신제품·비즈니스 모델 자체에 내재화되고 자율적 데이터 플라이휠이 작동 |
| **AI Center of Excellence (`AI CoE`) as an Enablement Engine** | 조력자(활성화 엔진)로서의 AI CoE | **오답 함정**: CoE가 모든 부서의 코드를 독점 개발하고 사사건건 결재를 막아서는 관료주의적 게이트키퍼(`Ivory Tower Bottleneck`)가 되는 것.<br>**정답**: CoE는 **사전 승인된 보안 아키텍처 블루프린트, 재사용 가능한 프롬프트/RAG 템플릿, 베스트 프랙티스 교육, 거버넌스 자동화 도구만 만들어 배포하고, 실제 개발은 현업 스포크 팀이 빠르게 수행하도록 돕는 조력자(`Enablement Engine`)** 여야 함. |
| **Cross-Functional AI Pods / Two-Pizza Squads** | 다학제 융합 AI 포드 (투피자 스쿼드) | 데이터 과학자들만 모아놓은 고립된 부서(`Siloed DS Lab` = 현업 맥락 몰라 배포 실패) 대신, **도메인 현업 전문가(SME) + 프로덕트 오너(PO) + 데이터/ML 엔지니어 + UX 디자이너 + 리스크/보안 담당자를 하나의 자율 스쿼드로 통합**해 비즈니스 KPI를 공동 책임지는 조직 구조. |
| **AI Champions / Change Ambassadors Network** | 현장 AI 챔피언(변화 홍보대사) 네트워크 | 인사팀이나 IT팀이 위에서 일방적으로 AI 사용을 강요(`Top-Down Mandate`)하면 현업이 거부감을 가짐. **각 현업 부서(영업, 간호, 물류, 법무) 내에서 동료들의 신망이 두터운 실무 리더를 선발해 먼저 AI를 숙달시키고, 동료의 언어로 성공 노하우를 전파(`Peer-to-Peer Coaching`)** 하게 하는 변화관리 핵심 기법. |
| **Role-Based Tiered Upskilling Curriculum** | 직무·계층별 맞춤형 AI 역량 교육 | 전 직원에게 똑같은 파이썬 코딩 강의를 듣게 하는 것은 대표적 오답! **1) 임원진: AI 전략·ROI·거버넌스·리스크 의사결정, 2) 현업 실무자: 도메인 프롬프트 엔지니어링·HITL 검증·기밀 데이터 보안 수칙, 3) 기술/ML 팀: LLMOps·가드레일·벡터 아키텍처 심화**로 세분화해야 함. |
| **Citizen Developers & Governed Low-Code/No-Code (`Amazon PartyRock` / `SageMaker Canvas` / `Amazon Q Apps`)** | 시티즌 디벨로퍼(현업 시민 개발자) 및 통제된 노코드/로코드 환경 | 코딩을 모르는 현업 직원이 IT 부서 대기열을 기다리지 않고 직접 업무 자동화 앱이나 예측 모델을 프로토타이핑하도록 지원하되, **데이터 유출 방지 가드레일과 프로덕션 승격 시 IT/보안 검수 관문(`Graduation Gate`)이 결합된 공식 샌드박스**를 제공하는 전략. |
| **Business Process Re-engineering (`BPR`) & End-to-End Workflow Redesign** | 비즈니스 프로세스 리엔지니어링 (업무 흐름 전면 재설계) | AI 도입 시 기존 7단계 수기 결재 양식을 그대로 둔 채 타이핑만 빠르게 해주는 것이 아니라(`Paving the Cow Path`), **AI 신뢰도 임계치 기반 자동 승인(`STP`)과 예외 건 중심 워크플로우로 업무 절차와 직무 역할 자체를 근본적으로 재설계**하는 작업. |
| **Outcome-Based Incentive & KPI Realignment** | 성과 기반 인센티브 및 인사평가 재정렬 | 예: 콜센터 상담원의 평가 기준이 여전히 '처리 건수'에만 묶여 있으면 AI가 단순 문의를 다 처리하고 남은 고난도 문의만 맡게 된 상담원이 불이익을 받아 AI를 보이콧함. **AI 전환에 맞춰 현업의 KPI와 보상 체계를 '복합 문제 해결 품질·AI 피드백 기여도'로 반드시 재조정**해야 함. |
| **Change Fatigue Mitigation & Wave-Based Phased Rollout** | 변화 피로도 완화 및 웨이브 기반 단계적 확산 | 한꺼번에 15개의 새로운 AI 툴을 현업에 쏟아부으면 직원들이 학습 과부하(`Cognitive Overload & Change Fatigue`)에 빠져 모든 툴을 외면함. **우선순위가 가장 높고 체감 고통(`Pain Point`)을 즉시 줄여주는 1~2개 핵심 워크플로우부터 단계적 웨이브(`Wave-based Rollout`)로 정착**시켜야 함. |

---

## 🏭 [섹션 9] 16대 산업 도메인별 실전 빈출 영문 표현 & KPI 마스터 사전 (80선)

실제 시험 지문에서 배경 시나리오로 등장하는 **16개 핵심 산업 도메인의 전문 용어, 치명적 규제/현장 제약조건, 그리고 정답 아키텍처 패턴**입니다.

| 산업 도메인 (Industry) | 실전 시험 지문 빈출 영문 키워드 (Domain Trigger Keywords) | 산업 고유 제약조건 & 시험 정답 아키텍처 공식 |
| :--- | :--- | :--- |
| **1. 🧬 바이오·제약 신약개발**<br>(Bio / Pharma R&D) | `Target Identification`, `Lead Compound Optimization`, `De Novo Protein Folding`, `Preclinical Toxicity`, `Clinical Trial Patient Stratification`, `GxP Compliance`, `FDA 21 CFR Part 11 Electronic Audit Trail`, `IND Filing` | • **제약**: 임상 데이터 프라이버시(`HIPAA`), 규제 당국의 100% 재현성 및 데이터 혈통(`Lineage`) 감사 요구.<br>• **정답**: 단백질 구조 예측(`AlphaFold/BioNeMo` 계열 워크로드) + `SageMaker Lineage/Model Registry` 불변 기록 + `Differential Privacy` 합성 데이터 + 임상 의사결정 전문의 `HITL`. |
| **2. ⚙️ 스마트 제조·반도체 팹**<br>(Smart Manufacturing & Fab) | `Predictive Maintenance (PdM)`, `Remaining Useful Life (RUL)`, `Overall Equipment Effectiveness (OEE)`, `First-Pass Yield (FPY)`, `Wafer Defect Vision Inspection`, `PLC / SCADA Telemetry`, `OT Air-Gapped Network`, `Digital Twin` | • **제약**: 초당 수십 개 부품이 지나가는 고속 라인(`Sub-10ms Latency`), 외부 인터넷과 단절된 공장 폐쇄망(`OT Network`), 오탐지로 라인이 멈추면 시간당 수억 원 손실(`False-Positive Line Stop Cost`).<br>• **정답**: 클라우드 학습 후 양자화/컴파일(`SageMaker Neo / IoT Greengrass`)하여 **현장 Edge IPC 배포** + 비동기 드리프트 수집 루프. |
| **3. 🔬 기업 R&D (배터리·소재·화학)**<br>(Corporate Materials & Chemical R&D) | `Electronic Lab Notebooks (ELN)`, `LIMS`, `Solid-State Battery Electrolyte Formulation`, `Inverse Materials Design`, `Surrogate Physics Simulation`, `Prior Art Patent Landscaping`, `Trade Secret Leakage` | • **제약**: 수십 년 축적된 독점 배합비·실험 실패 데이터 유출 시 기업 존립 위기(`Trade Secret Contamination`), 화학식·특허 번호·복합 물성 간의 다단계 관계 추론 필요.<br>• **정답**: `AWS PrivateLink` + `Zero-Training Assurance` + 문서 보안 등급 ACL이 적용된 **Hybrid Search (`BM25 + Dense`) + `GraphRAG`**. |
| **4. 🛍️ 옴니채널 소매·백화점**<br>(Omnichannel Retail) | `Hyper-Personalized Cross-Sell / Up-Sell`, `Store Planogram Optimization`, `Dynamic Markdown Pricing`, `Clienteling Copilot`, `Stockout Rate vs. Inventory Carrying Cost`, `GMROI`, `Basket Size / AOV` | • **제약**: 오프라인 POS와 온라인 앱 고객 ID 파편화, 시즌성 트렌드 급변(`Concept Drift`).<br>• **정답**: 통합 고객 프로필(`Entity Resolution`) + 실시간 개인화 추천(`Amazon Personalize`) + 무작위 홀드아웃 대조군 기반 **Incremental Revenue Uplift** 측정. |
| **5. 🚚 콜드체인 물류·도매 유통**<br>(Cold-Chain & Wholesale Distribution) | `SKU-Location Demand Forecasting`, `Perishable Spoilage Rate`, `Temperature Excursion Alert`, `WMS Slotting Optimization`, `Dynamic Last-Mile Routing`, `OTIF (On-Time In-Full)`, `MAPE / WAPE`, `Bullwhip Effect` | • **제약**: 신선식품·백신의 유통기한 폐기 손실(`Spoilage`)과 품절(`Stockout`)의 비대칭 비용, 기상 악화·유가 급등 등 외부 변수 영향.<br>• **정답**: 외부 기상/캘린더 변수를 결합한 확률적 분위수 수요예측(`Quantile Forecasting`: 과소/과대 발주 비용 비대칭 반영) + 공급망 플래너 예외 승인 `HITL`. |
| **6. ☕ 식음료 프랜차이즈·CPG**<br>(F&B Franchise & CPG) | `Drive-Thru Voice Ordering AI`, `Trade Promotion Optimization (TPO)`, `Store-Level Prep Forecasting`, `Menu Engineering`, `Consumer Sentiment Drift`, `New Product Cannibalization` | • **제약**: 매장 소음 환경에서의 음성 인식 정확도, 신제품 출시 시 기존 주력 상품 매출 잠식(`Cannibalization`) 예측.<br>• **정답**: 도메인 용어(메뉴명) 커스텀 어휘가 적용된 `Speech-to-Text` + 경량 `SLM` 주문 파싱 + 매장 POS 재고 실시간 연동. |
| **7. 🛒 초대형 이커머스·마켓플레이스**<br>(Mega E-Commerce Marketplace) | `Multimodal Catalog Auto-Tagging`, `Counterfeit / Fraudulent Seller Detection`, `Search Relevance Ranking`, `Review Summarization`, `Return Abuse Prevention`, `Flash-Sale Traffic Spike` | • **제약**: 수억 개 신규 상품 이미지·텍스트의 처리 단가(`Unit Economics`), 가짜 리뷰 및 위조품 판매자 실시간 차단.<br>• **정답**: 비긴급 카탈로그 태깅은 **Batch Inference + SLM** 으로 단가 절감, 실시간 검색은 **Hybrid Search + Cross-Encoder Reranking**. |
| **8. 🏦 리테일 금융·핀테크·신용**<br>(FinTech & Retail Banking) | `Credit Underwriting`, `Equal Credit Opportunity Act (ECOA)`, `Adverse Action Notice`, `Sub-50ms Real-Time Payment Fraud`, `AML / KYC Transaction Monitoring`, `False Decline Customer Friction` | • **제약**: 대출 거절 시 법적으로 구체적 사유 통지 의무(`ECOA / GDPR Art. 22`), 결제 사기 탐지는 50ms 이내 응답 필수.<br>• **정답**: 신용심사는 **해석 가능한 트리 모델(`XGBoost`) + `SageMaker Clarify (Local SHAP + Disparate Impact 검증)`**, 결제 사기는 초저지연 인메모리 피처 스토어 연동. |
| **9. 🏥 임상 헬스케어·대형 병원**<br>(Clinical Healthcare & Hospital Network) | `Ambient Clinical Voice Scribe`, `EHR / FHIR Integration`, `ICD-10 Medical Coding`, `Diagnostic Radiology Triage`, `Sepsis Early Warning`, `HIPAA PHI Protection`, `Clinician Burnout` | • **제약**: 환자 건강정보(`PHI`) 절대 보호, AI의 단독 확정 진단 금지, 의료진의 `Automation Bias` 방지.<br>• **정답**: `AWS HealthScribe / Comprehend Medical` + `HIPAA Eligible` 아키텍처 + 판독 우선순위 트리아지 후 **반드시 의사 최종 서명(`Mandatory Physician Sign-off HITL`)**. |
| **10. 🛡️ 손해보험·언더라이팅·보상**<br>(P&C Insurance & Claims) | `Straight-Through Processing (STP)`, `Auto Damage Computer Vision Assessment`, `Actuarial Risk Pricing`, `Subrogation Recovery`, `Fraudulent Claim Ring Detection (Graph Analytics)`, `Loss Ratio` | • **제약**: 소액 단순 사고는 즉시 지급(`STP`)하여 고객 만족도를 높이고, 고액·조직적 보험사기 의심 건만 정밀 조사관(`SIU`)에게 배정해야 함.<br>• **정답**: **신뢰도 임계치 기반 `Amazon A2I` 라우팅** + 공모 네트워크 탐지를 위한 **`Amazon Neptune` 그래프 분석**. |
| **11. 🚗 모빌리티·자율주행·전장 R&D**<br>(Automotive & Autonomous Mobility) | `ADAS Sensor Fusion (LiDAR + Camera + Radar)`, `Corner-Case Scenario Mining`, `Over-the-Air (OTA) Model Update`, `ISO 26262 Functional Safety`, `In-Cabin Voice Assistant` | • **제약**: 차량 내부에서의 실시간 무결성 판단(통신 두절 시에도 안전 제동 필수), 희귀 돌발 상황(`Long-Tail Corner Cases`: 폭설 속 역주행 오토바이 등) 확보 난이도.<br>• **정답**: 온보드 엣지 추론 칩셋 탑재 + 희귀 엣지 케이스만 클라우드로 수집해 **합성 시뮬레이션 데이터(`Synthetic Corner-Case Generation`)** 로 재학습. |
| **12. ⚡ 에너지·스마트 그리드·유틸리티**<br>(Energy & Smart Grid Utilities) | `Renewable Generation Forecasting (Solar/Wind Intermittency)`, `Grid Load Balancing`, `Substation Thermal Drone Inspection`, `SCADA Critical Infrastructure Protection`, `Carbon Footprint Optimization` | • **제약**: 국가 기간망 보안 규제, 기상 급변에 따른 재생에너지 발전량 변동성, 송전탑 원격지 비전 검사.<br>• **정답**: 물리 법칙이 반영된 시계열 예측 + 드론 촬영 영상 배치/엣지 결함 분석 + 결정론적 안전 한계치(`Safety Bounds`) 가드레일. |
| **13. 💻 B2B 엔터프라이즈 SaaS·보안**<br>(B2B Enterprise SaaS & CyberSec) | `Multi-Tenant Data Isolation`, `Noisy Neighbor Prevention`, `SOC Alert Fatigue Triage`, `Net Dollar Retention (NDR)`, `Customer Churn Early Warning`, `BYOK (Bring Your Own Key)` | • **제약**: 고객사 A의 데이터가 고객사 B의 RAG 검색이나 파인튜닝 어댑터에 절대 섞이면 안 됨(`Strict Tenant Isolation`).<br>• **정답**: 테넌트별 네임스페이스/메타데이터 암호화 격리 + `Multi-Adapter LoRA` 분리 + 테넌트별 토큰 쿼터 제한(`Rate Limiting`). |
| **14. 🎮 미디어·게임·콘텐츠 스튜디오**<br>(Media, Gaming & Entertainment) | `Dynamic NPC Dialogue Generation`, `Real-Time Toxicity & Voice Chat Moderation`, `Multilingual Localization & Lip-Sync`, `Copyright / Artist Style Infringement`, `C2PA Content Provenance` | • **제약**: 게임 내 실시간 NPC 대화의 극단적 저지연·저비용 요구, 미성년자 보호를 위한 실시간 유해 발언 차단, 아티스트 저작권 분쟁.<br>• **정답**: **Clean-Room 라이선스 자산으로만 파인튜닝** + `C2PA` 워터마킹 + 경량 증류 모델(`Distilled SLM`) 서빙. |
| **15. 🏛️ 공공·스마트시티·행정 서비스**<br>(Public Sector & Smart City) | `Multilingual Citizen Welfare Copilot`, `Public Procurement Compliance`, `Digital Divide Accessibility`, `FOIA / Public Records Redaction`, `Strict Statutory Eligibility Rules` | • **제약**: 복지 수급 자격 판정이나 세금 계산에서는 0.1%의 확률적 환각도 허용되지 않으며 법령 조항에 100% 부합해야 함, 디지털 취약계층 접근성 보장.<br>• **정답**: 자연어 이해는 LLM이 돕되, **실제 자격 판정·수급액 계산은 결정론적 규칙 엔진(`Deterministic Rule Engine`)과 `Automated Reasoning` 검증으로 처리**. |
| **16. 📡 통신(Telco)·네트워크 인프라**<br>(Telecommunications & 5G Network) | `Base Station Predictive Anomaly Detection`, `Self-Organizing Network (SON)`, `Subscriber Churn Retention Offer`, `Call Center AHT (Average Handle Time)`, `First-Contact Resolution (FCR)` | • **제약**: 전국 수만 개 기지국에서 초당 수백만 건 쏟아지는 시계열 로그 처리, 상담원 이직률 및 통화 대기시간 단축.<br>• **정답**: 스트리밍 이상 탐지(`Kinesis + Random Cut Forest`) + 상담원 실시간 지식 추천 코파일럿(`Amazon Connect + Amazon Q in Connect`). |
"""

if __name__ == "__main__":
    print("GLOSSARY_PART_D length:", len(GLOSSARY_PART_D))
