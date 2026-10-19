# AWS Services Cheat Sheet Deep Dive Generator

def get_aws_services_markdown():
    return """# 출제 범위 내 핵심 AWS 서비스 치트시트 (AIB-C01 In-Scope Services)

> **시험 공략 팁 (Exam Focus)**: AIB-C01 시험은 기술적인 API 코드 작성을 묻지 않습니다. 대신 **"어떤 비즈니스 시나리오에서 어떤 AWS 서비스를 선택하는 것이 최적인가?"**를 평가합니다.

---

## 📌 AWS 서비스 선택 의사결정 순서도 (Decision Tree)

```
[비즈니스 요구사항 분석]
  │
  ├─ 사내 40개 이상의 엔터프라이즈 저장소(Confluence, Jira, S3 등)를 연동하고 
  │  직원별 접근 권한(ACL)을 엄격히 통제하는 완성형 업무 어시스턴트가 필요한가?
  │  └─▶ [ Amazon Q Business ] (기성 상용 구매 / Buy 패턴)
  │
  ├─ 다양한 최신 파운데이션 모델(Claude, Llama, Titan)을 단일 API로 유연하게 호출하고,
  │  RAG(지식 기반), AI 에이전트, 안전 가드레일을 맞춤 조립(Build)해야 하는가?
  │  └─▶ [ Amazon Bedrock ]
  │       ├─ S3 사내 문서와 벡터 DB를 코딩 없이 자동 연동: [ Knowledge Bases for Bedrock ]
  │       ├─ 유해 콘텐츠 차단, PII 마스킹, 근거 기반 검증: [ Guardrails for Bedrock ]
  │       └─ 자연어 목표를 받아 외부 Lambda/API를 자율 호출: [ Agents for Bedrock ]
  │
  ├─ 코딩 지식이 없는 비즈니스 분석가가 직접 고객 이탈을 예측하고 시각적 머신러닝을 수행해야 하는가?
  │  └─▶ [ Amazon SageMaker Canvas ] (노코드 비즈니스 분석가 도구)
  │
  ├─ 모델의 알고리즘 편향(Bias)을 사전에 감사하고 SHAP 설명 가능성 리포트를 생성해야 하는가?
  │  └─▶ [ Amazon SageMaker Clarify ] (책임 있는 AI / 공정성 감사)
  │
  ├─ 프로덕션 환경에서 데이터 드리프트(Data Drift) 및 성능 저하를 지속 감시해야 하는가?
  │  └─▶ [ Amazon SageMaker Model Monitor ]
  │
  ├─ 고위험 의사결정 시 AI 신뢰도가 낮을 때 인간 전문가에게 자동으로 검토를 라우팅해야 하는가?
  │  └─▶ [ Amazon Augmented AI (Amazon A2I) ] (Human-in-the-Loop)
  │
  └─ 비개발자가 프롬프트만으로 몇 분 만에 AI 미니 앱을 만들고 동료와 공유해야 하는가?
     └─▶ [ AWS PartyRock ] (노코드 GenAI 플레이그라운드)
```

---

## 1. 생성형 AI 특화 핵심 서비스 (Generative AI Suite)

| 서비스명 (Service) | 🇺🇸 English Architecture & Key Role | 🇰🇷 한국어 핵심 역할 및 시험 출제 시나리오 | 🎯 Exam Match (정답 도출 키워드) |
| :--- | :--- | :--- | :--- |
| **Amazon Bedrock** | Fully managed API offering frontier FMs (Anthropic Claude, Meta Llama, AI21, Titan) with zero infrastructure management and zero model training on customer data. | 다양한 벤더의 파운데이션 모델을 단일 API로 제공하며, 고객 데이터를 절대 기본 모델 학습에 쓰지 않는 완전관리형 생성형 AI 서비스. | • 다양한 모델 비교 및 단일 API 연동<br>• 엔터프라이즈 맞춤형 GenAI 구축 (Build)<br>• 서버리스 FM 호출 |
| **Knowledge Bases for Bedrock** | Fully managed turnkey RAG pipeline connecting Amazon S3 document stores with vector databases (OpenSearch Serverless) automatically. | 사내 문서(PDF, Word)를 S3에 올리면 자동으로 청킹, 임베딩, 벡터 DB 인덱싱을 수행하여 최신 지식을 검색해 답변하는 완전관리형 RAG. | • 사내 최신 규정 반영<br>• 환각(Hallucination) 방지<br>• 출처 인용(Citations) 필수 시나리오 |
| **Guardrails for Bedrock** | Model-agnostic governance filter enforcing Denied Topics, Content Moderation, PII Redaction, and Contextual Grounding Checks. | 모든 파운데이션 모델에 일괄 적용되는 보안 가드로, 유해 콘텐츠 차단, PII 마스킹, 근거 없는 답변 필터링을 중앙에서 강제. | • 개인정보(PII) 자동 마스킹<br>• 금지된 주제(Denied Topics) 차단<br>• 환각 필터링 (Contextual Grounding) |
| **Agents for Bedrock** | Autonomous multi-step orchestration breaking high-level user directives into sequential sub-plans and invoking external APIs via Lambda. | 사용자의 자연어 목표를 분석하여 하위 계획을 세우고, OpenAPI 스키마로 정의된 비즈니스 API(Lambda)를 자율 호출하여 실제 업무 완수. | • 복합 업무 자율 수행 (예약, 결제 등)<br>• 외부 시스템 연동 (Action Groups)<br>• 다단계 의사결정 자동화 |
| **Amazon Q Business** | Enterprise conversational assistant connecting to 40+ corporate repositories while strictly honoring Access Control List (ACL) permissions. | 40개 이상의 기업 저장소(Salesforce, Jira, Confluence, S3)와 연동되며, 사용자의 접근 권한(ACL) 범위 내에서만 답변하는 기업용 AI. | • 기성 상용 솔루션 구매 (Buy 패턴)<br>• 기존 접근 권한(ACL) 엄격 준수<br>• 전사 직원 범용 업무 지식 검색 |
| **Amazon Q Developer** | Developer assistant generating code snippets, creating unit test suites, scanning security vulnerabilities, and upgrading legacy codebases. | 개발자의 코딩 생산성을 극대화하고 보안 취약점 검사 및 레거시 Java 코드 업그레이드를 자동 지원하는 개발자 전용 AI. | • 개발 생산성 향상<br>• 레거시 코드베이스 현대화<br>• 단위 테스트 자동 생성 |
| **AWS PartyRock** | Intuitive no-code generative AI app-building playground powered by Amazon Bedrock, fostering grassroots organizational literacy. | 비개발자도 프롬프트만으로 위젯을 조합하여 몇 분 만에 AI 미니 앱을 만들고 사내에 공유할 수 있는 노코드 실험 도구. | • 비개발자 대상 AI 리터러시 교육<br>• 풀뿌리(Grassroots) 프로토타이핑<br>• 노코드(No-Code) 앱 제작 |

---

## 2. 머신러닝 플랫폼 & 거버넌스 서비스 (ML Platform & Governance)

| 서비스명 (Service) | 🇺🇸 English Architecture & Key Role | 🇰🇷 한국어 핵심 역할 및 시험 출제 시나리오 | 🎯 Exam Match (정답 도출 키워드) |
| :--- | :--- | :--- | :--- |
| **Amazon SageMaker Canvas** | Visual point-and-click interface allowing business analysts to build predictive models (churn, demand forecasting) without code. | 데이터 사이언티스트의 도움 없이 현업 비즈니스 분석가가 마우스 클릭만으로 고객 이탈 예측 모델을 만들고 실행하는 노코드 ML 도구. | • 비즈니스 분석가 직접 예측 분석<br>• 노코드(No-Code) 머신러닝<br>• 고객 이탈률 및 수요 예측 |
| **Amazon SageMaker JumpStart** | Pre-trained model hub providing 1-click deployment and fine-tuning for hundreds of open-source and proprietary foundation models. | 오픈소스 및 상용 파운데이션 모델을 클릭 한 번으로 배포하거나 자체 데이터로 미세 조정(Fine-Tuning)할 수 있는 ML 모델 허브. | • 검증된 모델 기반 빠른 PoC 시작<br>• 전용 인프라 기반 자체 파인 튜닝<br>• 오픈소스 모델 프라이빗 호스팅 |
| **Amazon SageMaker Clarify** | Responsible AI engine auditing datasets and models for statistical bias while computing SHAP feature attribution explanations. | 데이터셋과 모델의 인구통계학적 편향을 감지하고, SHAP 값을 통해 어떤 변수가 예측에 기여했는지 설명 리포트를 자동 생성. | • 알고리즘 편향(Bias) 탐지<br>• 설명 가능성(Explainability / XAI)<br>• 규제 감사용 공정성 보고서 |
| **Amazon SageMaker Model Monitor** | Production monitoring tool tracking data drift, concept drift, and performance degradation in real-time deployed models. | 프로덕션에 배포된 모델의 입력 데이터 패턴 변화(Data Drift)와 성능 저하를 지속 모니터링하여 재학습을 트리거하는 도구. | • 모델 드리프트(Model Drift) 감지<br>• 실시간 프로덕션 모니터링<br>• 예측 정확도 저하 경고 |
| **Amazon Augmented AI (A2I)** | Turnkey Human-in-the-Loop workflow routing ambiguous or low-confidence inference predictions to human reviewer pools. | 모델의 신뢰도(Confidence)가 낮거나 중요한 고위험 의사결정 시 인간 검토자 풀에게 작업을 자동 전달하여 승인받는 HITL 서비스. | • 인간 참여형 검증 (HITL)<br>• 고위험 의사결정 안전망<br>• 신뢰도 미달 시 인간 전문가 에스컬레이션 |
| **Amazon DataZone** | Data governance portal enabling cross-functional data cataloging, business metadata discovery, and data mesh sharing across silos. | 부서 간 데이터 사일로를 타파하고 비즈니스 메타데이터 카탈로그를 통해 안전하게 데이터를 구독·공유하도록 돕는 포털. | • 데이터 사일로(Data Silos) 타파<br>• 전사 데이터 카탈로그 및 거버넌스<br>• 데이터 메시(Data Mesh) 아키텍처 |

---

## 3. 데이터 보안 및 엔터프라이즈 인프라 서비스 (Security & Infrastructure)

| 서비스명 (Service) | 🇺🇸 English Architecture & Key Role | 🇰🇷 한국어 핵심 역할 및 시험 출제 시나리오 | 🎯 Exam Match (정답 도출 키워드) |
| :--- | :--- | :--- | :--- |
| **AWS PrivateLink** | Secures private network connectivity between VPCs and AWS services without traffic traversing the public internet. | 데이터가 공용 인터넷을 거치지 않고 AWS 전용 사설망(VPC 내부) 안에서만 안전하게 Bedrock/SageMaker API와 통신하도록 보장. | • 데이터 주권 및 엄격한 규제 준수<br>• 공용 인터넷 노출 원천 차단<br>• 프라이빗 VPC 엔드포인트 격리 |
| **Amazon Macie** | Data security service discovering and protecting sensitive PII stored in Amazon S3 buckets using pattern matching and ML. | 사내 S3 버킷에 저장된 방대한 데이터 중 암호화되지 않은 주민번호, 신용카드 번호 등 PII를 자동으로 스캔·분류·보호하는 서비스. | • S3 버킷 내 민감 정보(PII) 자동 탐지<br>• 데이터 컴플라이언스 감사<br>• 데이터 유출 선제 방어 |
| **AWS Clean Rooms** | Secure multi-party data collaboration environment allowing partners to analyze collective data without sharing underlying raw records. | 여러 파트너사나 계열사가 원본 고객 개인정보를 서로에게 노출하지 않고 안전하게 연합 데이터 분석 및 머신러닝을 수행하는 환경. | • 원본 데이터 비공개 공동 분석<br>• 서드파티 파트너십 데이터 협업<br>• 프라이버시 보호 연합 분석 |
| **AWS Key Management Service (KMS)** | Managed encryption service generating and controlling cryptographic keys used to encrypt data at rest across AWS AI services. | S3 데이터 레이크, 벡터 DB, 모델 가중치 등 모든 저장 데이터를 기업 고객이 직접 제어하는 고객 마스터 키(CMK)로 암호화. | • 저장 데이터(Data at Rest) 암호화<br>• 고객 관리형 키(CMK) 통제<br>• 보안 감사 및 규제 요건 충족 |
| **AWS Budgets & Cost Allocation Tags** | Cloud financial management services tracking AI API expenditures by project and alerting on forecast overages. | 프로젝트/부서별로 태그를 붙여 AI 비용을 추적하고, 예산 초과 예상 시 실시간 알림을 발송하여 비용 폭증을 사전에 예방. | • AI FinOps 비용 거버넌스<br>• 부서별 비용 할당 및 책임성 부여<br>• 토큰 예산 초과 방지 |

---

## 4. 특화 도메인 AI 서비스 (Specialized Domain AI Services)

| 서비스명 (Service) | 🇺🇸 English Architecture & Key Role | 🇰🇷 한국어 핵심 역할 및 시험 출제 시나리오 | 🎯 Exam Match (정답 도출 키워드) |
| :--- | :--- | :--- | :--- |
| **Amazon Textract** | Optical Character Recognition (OCR) extracting printed text, handwriting, and tabular schemas from documents. | 스캔된 영수증, 계약서, 신분증에서 일반 텍스트뿐만 아니라 표(Table)와 키-값 쌍(Form)을 정확히 추출하는 지능형 문서 서비스. | • 비정형 문서의 표/양식 자동 추출<br>• 손글씨 및 스캔 문서 디지털화<br>• IDP(지능형 문서 처리) 1단계 |
| **Amazon Comprehend** | Natural Language Processing (NLP) extracting sentiment, entities, and key phrases, and performing PII redaction. | 고객 리뷰나 상담 텍스트에서 긍정/부정 감성, 주요 개체명(인물, 장소, 브랜드)을 추출하고 PII를 탐지·마스킹하는 NLP 서비스. | • 고객 피드백 감성 분석<br>• 텍스트 내 PII 개체명 탐지<br>• 대규모 비정형 문서 주제 분류 |
| **Amazon Rekognition** | Computer vision service analyzing imagery and video for object detection, facial analysis, and content moderation. | 이미지 및 영상에서 부적절한 콘텐츠(성인물, 폭력물)를 감지하고, 유명인 인식, 텍스트 추출, 사물 분류를 수행하는 비전 서비스. | • 사용자 업로드 이미지 유해성 검열<br>• 시각적 안전 거버넌스<br>• 컴퓨터 비전 객체 탐지 |
| **Amazon Transcribe** | Automatic Speech Recognition (ASR) converting spoken audio into accurate, punctuated text transcripts. | 고객센터 음성 통화 녹음 파일이나 회의 오디오를 텍스트로 자동 변환하며, 화자 분리(Diarization)를 지원하는 음성 인식 서비스. | • 콜센터 상담 음성 텍스트화<br>• 다국어 음성 자막 생성<br>• 음성 데이터 분석 파이프라인 |
"""
