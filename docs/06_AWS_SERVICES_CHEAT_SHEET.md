# 출제 범위 내 핵심 AWS 서비스 치트시트 (AIB-C01 In-Scope Services)

> **시험 공략 팁 (Exam Focus)**: AIB-C01 시험은 기술적인 API 코드 작성을 묻지 않습니다. 대신 **"어떤 비즈니스 시나리오에서 어떤 AWS 서비스를 선택하는 것이 최적인가?"**를 평가합니다.

---

## 1. 생성형 AI 특화 서비스 (Generative AI Services)

| 서비스명 (Service Name) | 🇺🇸 English Core Role & Exam Scenario | 🇰🇷 한국어 핵심 역할 및 전형적 출제 시나리오 |
| :--- | :--- | :--- |
| **Amazon Bedrock** | Fully managed foundation model API offering frontier models (Claude, Llama, Titan) via single API with zero model training on customer data. | 다양한 벤더의 최상위 모델을 서버 관리 없이 단일 API로 호출하며, 고객 데이터는 절대 모델 학습에 쓰이지 않는 완전관리형 FM 서비스. |
| **Knowledge Bases for Bedrock** | Fully managed RAG orchestrating document stores in Amazon S3 with vector databases to eliminate hallucinations and cite verifiable sources. | 사내 내부 문서(PDF 등)를 벡터 DB와 자동 동기화하여 환각 없이 정확한 출처와 함께 답변을 생성하는 완전관리형 RAG 솔루션. |
| **Guardrails for Bedrock** | Model-agnostic safety filter applying PII redaction, content moderation, denied topics, and contextual grounding verification. | 유해 콘텐츠 차단, 개인 식별 정보(PII) 마스킹, 특정 금지 주제 차단, 근거 기반 검증(Grounding Check)을 일괄 적용하는 보안 가드. |
| **Agents for Bedrock** | Autonomous multi-step orchestration breaking user queries into sub-tasks and invoking external APIs via Lambda and OpenAPI schemas. | 자연어 요청에 따라 외부 시스템 DB를 조회하고 실제 배송 변경이나 결제 API까지 스스로 실행하는 지능형 AI 에이전트. |
| **Amazon Q Business** | Enterprise generative AI assistant connecting to 40+ corporate repositories (Confluence, Jira, S3, Salesforce) while respecting ACL permissions. | 직원들이 사내 문서들을 안전하게 검색/요약받되, 본인이 접근 권한(ACL)이 없는 기밀 문서는 절대 볼 수 없도록 통제하는 기업용 AI 어시스턴트. |
| **Amazon Q Developer** | Developer productivity assistant generating code, creating unit tests, scanning vulnerabilities, and upgrading legacy codebases. | 개발자의 소프트웨어 개발 생산성을 높이고 레거시 코드베이스의 현대화를 가속화하는 개발자 전용 AI 어시스턴트. |
| **AWS PartyRock** | Intuitive no-code generative AI app-building playground fostering organizational AI literacy and rapid grassroots prototyping. | 비개발자도 프롬프트만으로 몇 분 만에 AI 미니 앱을 만들고 공유할 수 있는 노코드(No-Code) 실험 웹 도구. |

---

## 2. 머신러닝 플랫폼 & 데이터 거버넌스 (ML & Data Governance)

| 기능명 (Feature / Service) | 🇺🇸 English Core Role & Exam Scenario | 🇰🇷 한국어 핵심 역할 및 전형적 출제 시나리오 |
| :--- | :--- | :--- |
| **Amazon SageMaker Canvas** | Visual no-code machine learning enabling business analysts to generate churn and demand forecasts without coding. | 데이터 과학 팀의 도움 없이 현업 마케팅/비즈니스 분석가가 직접 고객 이탈을 예측하고 인사이트를 도출하는 노코드 ML 도구. |
| **Amazon SageMaker JumpStart** | Pre-trained model hub allowing machine learning teams to deploy and fine-tune open-source and proprietary models with 1-click. | 머신러닝 엔지니어가 처음부터 모델을 구축하지 않고 이미 검증된 모델을 가져와 빠르게 PoC를 시작하고자 할 때 사용하는 모델 허브. |
| **Amazon SageMaker Clarify** | Responsible AI engine detecting bias across data and trained models while computing SHAP feature attribution explanations. | 대출 심사 모델이 성별이나 인종에 차별적이지 않은지 검증하고, 규제 기관에 판단 근거를 설명해야 할 때 사용하는 도구. |
| **Amazon SageMaker Model Monitor** | Continuous telemetry monitoring tracking data drift, concept drift, and model degradation in production systems. | 프로덕션에 배포된 사기 탐지 모델의 성능이 시간 경과에 따른 시장 변화로 떨어지지 않는지 지속 감시하는 모니터링 도구. |
| **Amazon Augmented AI (A2I)** | Managed Human-in-the-Loop workflow routing low-confidence or high-risk inferences to human reviewer pools automatically. | 고위험 의사결정(대출 승인, 채용) 시 AI 신뢰도가 낮을 때 인간 전문가가 직접 검토하고 승인하도록 강제하는 워크플로우 서비스. |
| **Amazon DataZone** | Enterprise data governance portal enabling cross-departmental data discovery, cataloging, subscription, and data mesh sharing. | 부서별 데이터 사일로를 타파하고 각 팀이 데이터 소유권을 유지하면서 안전하게 전사적으로 데이터를 공유하도록 돕는 포털. |
| **AWS Lake Formation** | Centralized security service governing data lake permissions at granular database, table, column, and row levels. | 데이터 레이크에 여러 분석 팀이 접근할 때 최소 권한 원칙(PoLP)에 따라 민감한 열(Column)을 일괄 제한하는 보안 서비스. |
| **AWS Budgets & Cost Explorer** | AI financial management tools monitoring token consumption and firing alerts when expenditure exceeds budget thresholds. | 예측 불가능한 대규모 생성형 AI API 호출로 인한 TCO 폭증을 사전에 예방하고 통제하는 클라우드 재무 관리 도구. |
