#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part E of the Exhaustive Master Glossary & Exam Expressions Encyclopedia for AWS AIB-C01.
Contains:
- Section 10: AWS AI/ML·데이터·보안·거버넌스 핵심 서비스 & 기능 매핑 마스터 사전 (50+ Services & Capabilities)
- Combines Part A, B, C, D, E + Original Domain 1~4 Reference Tables into docs/01_GLOSSARY_KR_EN.md
"""

from pathlib import Path
from glossary_builder_a import GLOSSARY_PART_A
from glossary_builder_b import GLOSSARY_PART_B
from glossary_builder_c import GLOSSARY_PART_C
from glossary_builder_d import GLOSSARY_PART_D

GLOSSARY_PART_E = """
---

## ☁️ [섹션 10] AWS AI/ML·데이터·보안·거버넌스 핵심 서비스 & 기능 매핑 마스터 사전 (55선)

시험 선지에서 **"특정 비즈니스·거버넌스 요구사항을 가장 적은 운영 부담(Minimum Operational Overhead)으로 충족하는 AWS 서비스 조합"** 을 고를 때 직결되는 마스터 매핑표입니다.

### 10-1. 생성형 AI 및 파운데이션 모델 계층 (`Amazon Bedrock` & `Amazon Q` 생태계)

| AWS 서비스 / 핵심 기능 | 시험 출제 트리거 키워드 (When to Pick in Exam Options) |
| :--- | :--- |
| **Amazon Bedrock (Core Platform)** | 서버리스 방식으로 다양한 서드파티 및 자체 파운데이션 모델(Anthropic Claude, Meta Llama, Amazon Nova/Titan, Mistral, Cohere 등)을 단일 API(`Converse API`)로 호출·실험·교체하고 입출력 데이터가 기본 모델 학습에 절대 쓰이지 않는 완전관리형 서비스. |
| **Amazon Bedrock Knowledge Bases** | S3 문서 수집 ➔ 청킹(Fixed, Semantic, Hierarchical Parent-Child) ➔ 임베딩 생성 ➔ 벡터 DB(`OpenSearch Serverless`, `Aurora pgvector`, `Pinecone`) 저장 ➔ **Hybrid Search & Reranking ➔ 출처 인용(`Citations`) 생성까지 완전 자동화하는 관리형 RAG 서비스**. |
| **Amazon Bedrock Guardrails** | 특정 모델 종류(Bedrock 내부 모델뿐만 아니라 외부/자체 호스팅 모델에도 `ApplyGuardrail API`로 단독 적용 가능!)에 상관없이 **금지 주제 차단, 유해 콘텐츠 필터링, PII 자동 마스킹, 문맥 기반 환각 차단(`Contextual Grounding`), 수학적 논리 규칙 검증(`Automated Reasoning`)** 을 일괄 적용하는 보안 통제 계층. |
| **Amazon Bedrock Agents** | 복잡한 사용자 요청을 다단계 계획(`Chain-of-Thought Reasoning`)으로 분해하고, `Knowledge Bases` 조회 및 `AWS Lambda / OpenAPI Action Groups`를 호출해 예약·발주·DB 업데이트를 자율 수행하는 관리형 에이전트(Multi-Agent Collaboration 지원). |
| **Amazon Bedrock Evaluations (Model Evaluation)** | 자동화된 지표(정확도, 독성, 강건성), **`LLM-as-a-Judge` 자동 평가**, 또는 자체 검수원/AWS 관리형 인력을 활용한 **인간 평가(`Human Evaluation`)** 를 통해 여러 파운데이션 모델과 프롬프트를 나란히 비교 벤치마킹하는 도구. |
| **Amazon Bedrock Prompt Management & Prompt Flows** | 프롬프트 템플릿의 버전 관리(`Versioning`)와 시각적 워크플로우 체이닝을 통해 코드 재배포 없이 프롬프트를 실험·관리하는 기능. |
| **Amazon Bedrock Intelligent Prompt Routing** | 동일한 모델 패밀리(예: Claude Sonnet vs. Haiku, Nova Pro vs. Micro) 내에서 프롬프트 난이도를 실시간 분석해 단순 질문은 저렴하고 빠른 소형 모델로, 복잡한 질문만 대형 모델로 자동 라우팅하여 품질 저하 없이 비용을 최대 30~50% 절감. |
| **Amazon Bedrock Model Distillation** | 대형 교사 모델(`Teacher Model`)로부터 합성 응답을 자동 생성·정제하여 소형 학생 모델(`Student Model`)을 파인튜닝함으로써 추론 속도는 최대 5배 높이고 비용은 최대 75% 낮추는 관리형 지식 증류 기능. |
| **Amazon Q Business** | 사내 40개 이상의 엔터프라이즈 데이터 소스(SharePoint, Salesforce, Jira, Slack, S3 등)와 즉시 연결되며, **기존 사내 사용자 권한(`ACL / IAM Identity Center`)을 그대로 상속받아 권한 있는 문서만 검색·요약·업무 자동화(`Q Apps`)** 해주는 현업 직원용 생성형 AI 비서. |
| **Amazon Q Developer** | 소프트웨어 개발자의 코딩, 레거시 코드 변환(예: 구버전 Java 8 ➔ Java 17 업그레이드, 메인프레임 현대화), 보안 취약점 스캔, AWS 아키텍처 트러블슈팅을 지원하는 개발자용 AI 에이전트. |
| **Amazon Q in QuickSight** | 경영진과 비즈니스 분석가가 SQL이나 BI 대시보드 제작법을 몰라도 자연어 질문만으로 즉시 시각적 차트 생성, 실적 변동 원인 요약(`Executive Summary`), 시나리오 예측을 수행하는 생성형 BI 기능. |
| **Amazon Q in Connect** | 콜센터 상담원이 고객과 통화/채팅하는 동안 실시간으로 고객 의도를 파악해 **해결책 문서와 권장 답변을 상담원 화면에 즉시 띄워주어 평균 처리 시간(`AHT`)과 신입 상담원 교육 기간을 대폭 단축**하는 코파일럿. |
| **Amazon PartyRock** | AWS 계정이나 코딩 지식 없이도 현업 직원들이 브라우저에서 생성형 AI 앱을 드래그 앤 드롭으로 빠르게 만들어보고 프롬프트 엔지니어링 감각을 익히는 노코드 플레이그라운드(Citizen Developer 입문 교육용). |

---

### 10-2. 머신러닝 개발·학습·MLOps·거버넌스 계층 (`Amazon SageMaker AI` 생태계)

| AWS 서비스 / 핵심 기능 | 시험 출제 트리거 키워드 (When to Pick in Exam Options) |
| :--- | :--- |
| **Amazon SageMaker Canvas** | 코딩을 전혀 모르는 비즈니스 분석가/현업 담당자가 시각적 인터페이스만으로 정형 데이터 예측(이탈 예측, 수요 예측, 불량 분류) 및 파운데이션 모델 미세조정을 수행하는 **No-Code AutoML 도구**. |
| **Amazon SageMaker Autopilot** | 데이터 전처리, 알고리즘 선택(`XGBoost`, 선형 모델, 딥러닝), 하이퍼파라미터 튜닝을 자동 수행하면서도, **생성된 전체 파이썬 노트북 코드를 100% 투명하게 공개(`White-Box AutoML`)하여 데이터 과학자가 검수·수정**할 수 있는 기능. |
| **Amazon SageMaker JumpStart** | 수백 개의 오픈소스 파운데이션 모델 및 산업별 사전 구축 솔루션 템플릿을 클릭 한 번으로 자체 VPC 내에 배포하거나 파인튜닝할 수 있는 머신러닝 허브. |
| **Amazon SageMaker Clarify** | 1) **훈련 전 데이터 편향(`Pre-training Bias`) 및 훈련 후 모델 예측 편향(`Post-training Bias`) 통계 측정**, 2) **`SHAP` 기반 전역적/개별 건별(`Local`) 피처 기여도 설명가능성 리포트 생성**, 3) 프로덕션 배포 후 **실시간 편향 드리프트 및 피처 기여도 드리프트 지속 모니터링**. |
| **Amazon SageMaker Model Monitor** | 프로덕션 엔드포인트에서 실시간 추론 데이터를 캡처해 **데이터 품질 드리프트(`Data Drift`), 모델 품질 드리프트(`Model Accuracy Drift`), 편향 드리프트, 피처 기여도 드리프트**를 자동 감지하고 `CloudWatch Alarm` 및 재학습 파이프라인을 트리거. |
| **Amazon SageMaker Model Registry & Lineage Tracking** | 모델 버전 관리, 메타데이터/성능 지표 기록, **배포 승인 상태(`Approved/Rejected`) 워크플로우 통제**, 그리고 데이터부터 엔드포인트까지 전 과정의 **감사 추적 혈통(`Lineage`)** 을 자동 기록. |
| **Amazon SageMaker Model Cards & Role Manager** | 모델의 의도된 용도, 리스크 등급, 평가 결과를 표준화된 거버넌스 문서(`Model Card`)로 중앙 문서화하고, MLOps 역할별 최소 권한(`Role Manager`)을 쉽게 설정하는 거버넌스 도구. |
| **Amazon SageMaker Feature Store** | 온라인(실시간 저지연 추론용) 및 오프라인(학습 및 배치 추론용) 피처를 단일 저장소에서 통합 관리하여 부서 간 피처 재사용을 촉진하고 **학습-서빙 불일치(`Training-Serving Skew`)를 해결**. |
| **Amazon SageMaker Ground Truth (Plus)** | 인간 라벨러(자체 전문가, 벤더, 또는 크라우드)와 **`Active Learning` 자동 라벨링**을 결합하여 대규모 학습 데이터셋 및 RLHF/DPO 선호도 데이터를 구축할 때 **라벨링 비용과 기간을 최대 70% 절감**. |
| **Amazon Augmented AI (`Amazon A2I`)** | 추론 결과의 **신뢰도 점수(`Confidence Score`)가 임계치 미만이거나 무작위 감사 샘플링 조건에 해당할 때만 인간 검토자 워크플로우 UI로 자동 분기**시키는 관리형 `Human-in-the-Loop (HITL)` 서비스. |
| **Amazon SageMaker Pipelines** | 데이터 전처리 ➔ 학습 ➔ `Clarify` 편향/설명성 검증 ➔ `Model Registry` 등록 ➔ 조건부 배포로 이어지는 엔드투엔드 MLOps CI/CD/CT 워크플로우 오케스트레이션 서비스. |
| **Amazon SageMaker HyperPod** | 수천 개의 GPU/Trainium 클러스터에서 수주~수개월간 거대 파운데이션 모델을 사전학습(`Pre-training / CPT`)할 때, 하드웨어 노드 장애가 발생해도 자동으로 불량 노드를 교체하고 마지막 체크포인트부터 중단 없이 학습을 이어가는(`Resilient Distributed Training`) 인프라. |
| **AWS Trainium & AWS Inferentia (`EC2 Trn1 / Inf2`)** | AWS가 자체 설계한 AI 전용 가속 칩셋. 범용 GPU 대비 **대규모 딥러닝/LLM 학습 비용은 `AWS Trainium`으로 최대 50% 절감**하고, **대규모 실시간 추론 비용과 전력 소모(Green AI)는 `AWS Inferentia`로 최대 40% 절감**. |
| **AWS IoT Greengrass & SageMaker Edge / Neo** | 클라우드에서 학습·컴파일(`Neo`)한 경량 모델을 공장 설비, 자율주행차, 의료기기 등 현장 엣지 디바이스에 안전하게 배포하고 **인터넷 연결이 끊긴 폐쇄망(`Air-Gapped`)에서도 로컬 추론을 수행**하게 하는 엣지 런타임. |

---

### 10-3. 관리형 AI 서비스 & 데이터·보안·통합 거버넌스 계층

| AWS 서비스 / 핵심 기능 | 시험 출제 트리거 키워드 (When to Pick in Exam Options) |
| :--- | :--- |
| **Amazon Textract** | 단순 OCR을 넘어 스캔된 대출 신청서, 영수증, 의료 양식, 복잡한 표(`Tables`)와 체크박스(`Key-Value Forms`)의 구조를 정확히 추출하는 문서 지능 서비스 (`AnalyzeDocument / Queries`). |
| **Amazon Comprehend & Comprehend Medical** | 텍스트에서 감성(`Sentiment`), 핵심 구문, 엔티티를 추출하고 **실시간/배치로 개인식별정보(`PII`) 및 의료 보호건강정보(`PHI` / `ICD-10-CM` / `RxNorm`)를 탐지·마스킹**하는 자연어 처리 서비스. |
| **Amazon Transcribe & AWS HealthScribe** | 콜센터 음성 녹취(`Transcribe Call Analytics`: 통화 감성, 침묵 시간, 상담원 규정 준수 분석 및 PII 음성/텍스트 마스킹) 및 의사-환자 진료 대화를 자동으로 임상 요약 노트(`SOAP Note`)로 변환하는 의료 특화 음성 서비스. |
| **Amazon Rekognition (Custom Labels)** | 이미지/비디오에서 얼굴, 객체, 유해 콘텐츠, 텍스트, 개인보호장구(`PPE`) 착용 여부를 즉시 탐지하거나, 수백 장의 소량 제조 부품 이미지만으로 커스텀 불량 판별 모델을 빠르게 구축(`Custom Labels`). |
| **Amazon Personalize** | 아마존닷컴의 실시간 추천 엔진 기술을 API로 제공하여, 수개월 걸리는 추천 알고리즘 개발 없이 클릭스트림·구매 이력만으로 초개인화 상품 추천 및 재순위화(`Reranking`)를 수일 내에 구축. |
| **Amazon Fraud Detector** | 과거 사기 이력 데이터와 AWS의 글로벌 사기 패턴 지식을 결합해 온라인 결제 사기, 가짜 계정 생성, 프로모션 악용을 실시간 감지하는 관리형 서비스. |
| **Amazon Kendra** | 엔터프라이즈 문서 저장소 전반에 걸친 고정밀 자연어 검색 엔진 (문서 수준 접근 권한 토큰 필터링 기본 지원). |
| **Amazon DataZone** | 전사 데이터 메시(`Data Mesh`) 구현의 핵심 허브. 각 부서가 생산한 데이터 자산을 비즈니스 용어집(`Business Glossary`)과 자동 생성된 메타데이터로 카탈로그화하고, **프로젝트 단위로 데이터 구독 신청·승인 거버넌스 워크플로우**를 제공. |
| **AWS Lake Formation** | S3 데이터 레이크 전반에 걸쳐 **데이터베이스, 테이블, 컬럼(`Column-level`), 행(`Row-level`), 셀(`Cell-level`) 단위의 초세분화 접근 권한 및 태그 기반 정책(`LF-TBAC`)** 을 중앙 집중식으로 통제. |
| **AWS Glue & AWS Glue DataBrew / Glue Data Quality** | 서버리스 데이터 통합(ETL) 서비스. 코딩 없이 시각적으로 250개 이상의 데이터 정제·변환을 수행하는 것은 `DataBrew`, 파이프라인 내 데이터 결측치·스키마 위반을 자동 검증·차단하는 것은 `Glue Data Quality`. |
| **AWS Clean Rooms (Differential Privacy & Clean Rooms ML)** | 두 개 이상의 기업(예: 병원과 제약사, 유통사와 광고주)이 **서로의 민감한 원시 고객 데이터를 직접 노출하거나 복사하지 않고도, 차등 프라이버시(`Differential Privacy`)와 암호화 연산을 통해 공동 통계 분석 및 연합 머신러닝 학습(`Lookalike Modeling`)** 을 수행하는 서비스. |
| **Amazon Macie** | 머신러닝과 패턴 매칭을 사용해 전사 수천 개의 **`Amazon S3` 버킷을 자동 스캔하여 어디에 민감한 개인정보(`PII`), 신용카드 번호, 암호화 키가 방치되어 있는지 발굴·경고**하는 데이터 보안 서비스 (AI 학습 전 S3 데이터 위생 점검 1순위 정답!). |
| **AWS KMS (`Customer Managed Keys - CMK`) & AWS PrivateLink** | • **KMS CMK**: 학습 데이터, 모델 가중치, Bedrock 프롬프트 캐시/로그를 고객이 직접 통제·회전·폐기할 수 있는 암호화 키로 보호<br>• **AWS PrivateLink (VPC Endpoints)**: 사내 VPC와 `Amazon Bedrock / SageMaker` 간의 모든 트래픽이 공용 인터넷을 절대 거치지 않고 AWS 내부 프라이빗 백본망으로만 통신하도록 격리 |
| **AWS CloudTrail & AWS Config / AWS Audit Manager** | • **CloudTrail**: 누가, 언제, 어떤 IP에서 어떤 AI API(`InvokeModel`, `UpdateGuardrail`, `ApproveModel`)를 호출했는지 모든 API 이벤트를 불변 기록하여 법무·보안 감사 추적 보장<br>• **AWS Audit Manager**: `NIST`, `ISO`, `GDPR`, `HIPAA` 등 규제 프레임워크에 맞춰 증적 자료 수집을 자동화 |

---
"""


def main():
    glossary_path = Path("/Users/sungkyu/Study/AI BS_AWS/docs/01_GLOSSARY_KR_EN.md")
    existing_text = glossary_path.read_text(encoding="utf-8")

    marker = "## 1. 도메인 1: AI/ML 및 생성형 AI의 비즈니스 전략적 기초"
    if marker in existing_text:
        domain_tables_part = existing_text[existing_text.index(marker):]
        domain_tables_part = (
            "## 📚 [부록] 도메인 1~4 기본 개념 한·영 요약 테이블 (Quick Domain Reference)\n\n"
            + domain_tables_part
        )
    else:
        domain_tables_part = ""

    full_markdown = (
        GLOSSARY_PART_A.strip()
        + "\n\n"
        + GLOSSARY_PART_B.strip()
        + "\n\n"
        + GLOSSARY_PART_C.strip()
        + "\n\n"
        + GLOSSARY_PART_D.strip()
        + "\n\n"
        + GLOSSARY_PART_E.strip()
        + "\n\n"
        + domain_tables_part.strip()
        + "\n"
    )

    glossary_path.write_text(full_markdown, encoding="utf-8")
    print(f"[SUCCESS] Built Massive Master Glossary Encyclopedia: {len(full_markdown):,} chars, {len(full_markdown.splitlines()):,} lines")


if __name__ == "__main__":
    main()
