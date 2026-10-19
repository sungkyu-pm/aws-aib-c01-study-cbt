#!/usr/bin/env python3
"""
AWS Certified AI Business Strategist (AIB-C01)
Dual-Track Bilingual Study Documents & Comprehensive Terminology System Builder
Generates rich, paragraph-by-paragraph English + Korean paired study guides
and updates docs/01~06 and portal-docs-data.js.
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
os.makedirs(DOCS_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. docs/01_GLOSSARY_KR_EN.md (Master Bilingual Glossary)
# -------------------------------------------------------------
GLOSSARY_MD = """# AIB-C01 마스터 한·영 비즈니스 AI 용어사전 (Master Glossary)

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
"""

# -------------------------------------------------------------
# 2. docs/02_DOMAIN_1_AI_FUNDAMENTALS.md (Dual-Track Domain 1)
# -------------------------------------------------------------
DOMAIN1_MD = """# 도메인 1: AI 기초 및 활용 능력 (AI Fundamentals and Literacy)

> **출제 비중 (Exam Weight)**: **20%**  
> **공식 시험 평가 목표 (Exam Objective)**: 비즈니스 문제에 적합한 AI/ML 솔루션 유형(정형 vs 비정형, 규칙 기반 vs AI, GenAI)을 구분하고, 프롬프트 엔지니어링, RAG, 파인 튜닝의 기술적 트레이드오프를 평가하며, AI 에이전트와 책임 있는 기초 AI 개념을 비즈니스 전략에 접목할 수 있는가?

---

## 1.1 핵심 AI 기술 및 개념 계층 (Core AI Taxonomy & Fundamentals)

<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Artificial Intelligence (AI)**: The broad discipline of computer science dedicated to simulating human cognitive functions such as learning, reasoning, and synthesis. Includes deterministic expert systems.
* **Machine Learning (ML)**: A specialized subset of AI where mathematical models learn predictive patterns directly from historical data without hardcoded procedural rules.
* **Generative AI (GenAI)**: A branch of deep learning models (such as Foundation Models and LLMs) capable of generating novel unstructured artifacts including natural text, synthetic code, and realistic media.
* **Structured vs Unstructured Data**: Structured data (tables, CSVs) is suited for classical discriminative algorithms (e.g., XGBoost). Unstructured data (PDF manuals, customer audio, email inquiries) accounts for over 80% of enterprise assets and represents the primary operating domain of GenAI.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 번역 및 비즈니스 전략 해설
* **인공지능 (AI)**: 인간의 학습, 추론, 지각 능력을 컴퓨터로 모방하는 가장 포괄적인 개념입니다. (규칙 기반 시스템도 AI에 포함됨)
* **머신러닝 (ML)**: 명시적인 IF-THEN 코딩 없이 대량의 데이터로부터 알고리즘이 스스로 패턴을 학습하여 예측이나 분류를 수행하는 하위 기술입니다.
* **생성형 AI (GenAI)**: 단순히 기존 레이블을 분류하는 것을 넘어 텍스트, 코드, 이미지 등 **새로운 원본 콘텐츠를 능동적으로 생성**하는 모델입니다.
* **정형 vs 비정형 데이터**: 정형 데이터(DB 테이블)는 전통적인 ML에 적합하며, 비정형 데이터(PDF 규정집, 상담 녹취록)는 기업 데이터의 80% 이상을 차지하며 **GenAI와 파운데이션 모델이 가장 큰 혁신을 만드는 영역**입니다.

</div>
</div>

---

## 1.2 솔루션 선택: 규칙 기반 vs 머신러닝 vs AI 에이전트 (Solution Architecture Selection)

<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Rule-Based Automation (RPA)**: Select when the business process is deterministic, governed by explicit compliance rules (IF-THEN), and requires 100% mathematical consistency with zero tolerance for ambiguity (e.g., tax calculation, payroll batches).
* **Machine Learning / GenAI**: Select when business inputs exhibit high ambiguity, unstructured complexity, or require dynamic adaptation to evolving consumer sentiment and fraud behaviors.
* **AI Agents & Multi-Step Orchestration**: Unlike simple passive chatbots that merely render text answers, **AI Agents** possess:
  1. *Autonomy*: Decomposing high-level enterprise goals into sequential sub-plans.
  2. *Tool Use (Action Groups)*: Interacting with enterprise databases and invoking external REST APIs via AWS Lambda and OpenAPI schemas.
  3. *Multi-Agent Orchestration*: Collaborating across specialized agents to execute complex transactions (e.g., checking flight availability, querying CRM records, and finalizing payments).

</div>
<div class="kr-col">

#### 🇰🇷 한국어 번역 및 비즈니스 전략 해설
* **규칙 기반 자동화 (RPA) 선택 기준**: 명확한 업무 규칙(IF-THEN)이 존재하고, 모호성이 없으며, 100% 오차 없는 결정론적(Deterministic) 결과가 필수적인 업무(세금 계산, 급여 이체)에 적합합니다.
* **AI/머신러닝 솔루션 선택 기준**: 데이터에 복잡한 비선형적 패턴이 있거나, 자연어/이미지 이해가 필요하며, 시장 변화에 지속적으로 적응해야 하는 경우(고객 감정 분석, 사기 탐지)에 선택합니다.
* **AI 에이전트 (AI Agents)의 핵심 차별점**: 단순 챗봇과 달리, 사용자의 포괄적 목표를 분석하여 하위 실행 계획을 세우고, **외부 API 도구(Action Groups, AWS Lambda)**를 스스로 호출하여 실제 예약이나 결제 같은 복합 업무를 완수합니다.

</div>
</div>

---

## 1.3 파운데이션 모델 추론 파라미터 제어 (Inference Hyperparameters)

<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Temperature**: Dictates output stochasticity. For deterministic, strictly factual, and reproducible outputs (e.g., contract summarization, medical guidelines), **set Temperature to 0.0 (Greedy Decoding)**. For creative marketing campaigns, increase to 0.7–1.0+.
* **Top-P (Nucleus Sampling)**: Dynamically filters the candidate pool to tokens whose cumulative probability reaches threshold P (e.g., 0.9), eliminating erratic long-tail vocabulary.
* **Top-K**: Caps candidate consideration strictly to the top K most probable tokens.
* **Token Streaming**: Emits generated tokens over an active HTTP stream as soon as they are computed, drastically decreasing Time-to-First-Token (TTFT) and elevating perceived responsiveness.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 번역 및 비즈니스 전략 해설
* **Temperature (온도)**: 출력의 무작위성(창의성)을 제어합니다. 보고서나 법률 문서 요약처럼 매번 100% 동일하고 사실에 기반한 결정론적 결과가 필요할 때는 **반드시 Temperature를 0.0으로 설정**해야 합니다.
* **Top-P (핵 샘플링)**: 누적 확률이 P(예: 0.9) 이내인 토큰 중에서만 다음 단어를 고르도록 하여 엉뚱한 단어 생성을 방지합니다.
* **Top-K**: 다음 단어 후보를 확률 상위 K개로 제한합니다.
* **토큰 스트리밍 (Token Streaming)**: 전체 답변이 완성될 때까지 기다리지 않고 첫 번째 토큰부터 화면에 실시간으로 표시하여 사용자의 체감 응답 대기 시간을 획기적으로 줄입니다.

</div>
</div>

---

## 1.4 모델 적응 아키텍처 비교: RAG vs Fine-Tuning vs Pre-training

| 비교 항목 (Comparison Axis) | 🇺🇸 Retrieval-Augmented Generation (RAG) | 🇺🇸 Supervised Fine-Tuning | 🇺🇸 Model Pre-training |
| :--- | :--- | :--- | :--- |
| **작동 원리 (Mechanism)** | Retrieves real-time enterprise documents from vector DBs and injects them into prompt context. | Adjusts model neural network weights using domain-specific labeled dataset pairs. | Trains multi-billion parameters from scratch on raw web-scale corpora. |
| **주요 목적 (Primary Objective)** | **Injecting dynamic enterprise knowledge**, preventing hallucinations, and citing verifiable sources. | **Specializing stylistic tone, fixed JSON schema output**, or unique organizational terminology. | Building sovereign or domain-exclusive foundational models from the ground up. |
| **비용 및 출시 속도 (TCO & TTM)** | Lowest TCO, fastest Time-to-Market. Built easily via **Knowledge Bases for Amazon Bedrock**. | Moderate-to-high cost (requires labeled data curation, GPU cycles, and retraining maintenance). | Astronomical cost (millions of USD, massive GPU clusters, deep research teams). |
| **지식 최신성 (Knowledge Recency)** | **Instantaneous**: Updating Amazon S3 documents reflects immediately without model downtime. | **Stale**: Requires complete dataset re-curation and model re-tuning for every update. | Static: Knowledge is completely frozen at training cutoff date. |
| **주요 위험 (Inherent Risks)** | Retrieval latency, context window token limits, **Lost in the Middle** if chunks are too large. | **Catastrophic Forgetting** (loss of general reasoning capability), high training overhead. | Massive capital burn, project abandonment risk. |
| **시험 추천 (Exam Recommendation)** | **1순위 정답**: 최신 사내 규정 반영 및 환각 방지 시나리오. | 특정 말투나 엄격한 출력 형식 강제가 필수적일 때만 선택. | 일반 기업 시나리오에서는 원칙적으로 오답. |

---

## 1.5 컨텍스트 윈도우, 청킹 및 검색 최적화 (Context, Chunking & Retrieval)

<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Context Window Degradation ("Lost in the Middle")**: When prompts are filled with massive raw text, foundation models exhibit an attention bias where facts located in the middle of the context are overlooked compared to information at the beginning or end.
* **Document Chunking Strategy**: Mitigates this phenomenon by parsing extensive documents into semantically coherent segments (e.g., 300–500 tokens) with 10–20% overlap, ensuring precise vector retrieval.
* **Vector Embeddings & Semantic Search**: Text is encoded into mathematical vectors where distance reflects conceptual meaning. Using services like **OpenSearch Serverless** allows semantic matching even when user queries do not contain exact keyword matches.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 번역 및 비즈니스 전략 해설
* **중간 정보 누락 ("Lost in the Middle") 현상**: 컨텍스트 윈도우에 수십 페이지의 방대한 문서를 한꺼번에 넣으면, 모델이 지문의 맨 앞과 맨 뒤 정보는 잘 기억하지만 **정작 중간에 위치한 중요한 사실을 놓치는 현상**이 발생합니다.
* **문서 청킹 (Document Chunking)**: 대형 문서를 적절한 토큰 크기(예: 300~500 토큰)로 쪼개고 앞뒤로 일정 부분(10~20%) 중첩시켜 검색 정확도와 컨텍스트 효율을 극대화합니다.
* **벡터 임베딩 및 의미론적 검색**: 텍스트를 의미 기반의 고차원 숫자 벡터로 변환하여, 사용자가 정확한 키워드를 입력하지 않아도 의도와 맥락이 일치하는 관련 문서를 정확하게 찾아냅니다.

</div>
</div>

---

## 1.6 프롬프트 엔지니어링 & 모델 평가 (Prompting & LLM Evaluation)

<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Zero-Shot vs Few-Shot (In-Context Learning)**: Zero-shot provides direct instructions without examples. Few-shot includes 2–3 exemplar demonstrations within the prompt, significantly boosting accuracy for complex classification or rigid schema outputs without changing model weights.
* **Chain-of-Thought (CoT)**: Instructing the model to "think step by step" forces sequential decomposition, drastically reducing arithmetic, logic, and multi-step reasoning errors.
* **LLM-as-a-Judge**: Employing a superior frontier foundation model to automatically evaluate candidate model outputs across factual correctness, groundness, and tone at enterprise scale, overcoming human evaluation bottlenecks.
* **Model Quantization**: Compressing model weights from 32-bit floating point (FP32) to 8-bit or 4-bit integers (INT8/INT4), drastically reducing memory and inference latency for deployment on edge devices or cost-constrained environments.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 번역 및 비즈니스 전략 해설
* **제로샷 vs 퓨샷 (인컨텍스트 학습)**: 예시 없이 지시만 내리는 방식(Zero-Shot)과 달리, 프롬프트 안에 2~3개의 모범 입출력 예시(Few-Shot)를 함께 제공하여 모델이 원하는 출력 양식을 완벽히 준수하도록 유도합니다.
* **사고의 사슬 (Chain-of-Thought, CoT)**: "단계별로 생각해보자"라는 지침을 통해 복합 문제를 순차적인 하위 단계로 나누어 풀도록 함으로써 논리적 추론 오류를 획기적으로 줄입니다.
* **LLM-as-a-Judge**: 인간 평가자의 병목을 해소하기 위해 고성능 파운데이션 모델을 심사위원으로 활용하여 수천 건의 프롬프트 응답 품질과 사실성을 대규모로 자동 채점합니다.
* **모델 양자화 (Model Quantization)**: 모델 가중치의 정밀도를 FP32에서 INT8/INT4로 압축하여 정확도 손실을 최소화하면서 메모리 사용량을 대폭 줄이고 추론 속도를 높여 엣지/모바일 배포를 가능하게 합니다.

</div>
</div>
"""

# -------------------------------------------------------------
# 3. docs/03_DOMAIN_2_AI_STRATEGY_VALUE.md (Dual-Track Domain 2)
# -------------------------------------------------------------
DOMAIN2_MD = """# 도메인 2: AI 전략 및 비즈니스 가치 창출 (AI Strategy & Business Value Creation)

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
"""

# -------------------------------------------------------------
# 4. docs/04_DOMAIN_3_GOVERNANCE_RESPONSIBLE_AI.md (Dual-Track Domain 3)
# -------------------------------------------------------------
DOMAIN3_MD = """# 도메인 3: AI 거버넌스 및 책임 있는 AI 리더십 (AI Governance & Responsible AI Leadership)

> **출제 비중 (Exam Weight)**: **27%**  
> **공식 시험 평가 목표 (Exam Objective)**: 책임 있는 AI 6대 핵심 차원(공정성, 설명가능성, 개인정보보호, 안전성, 투명성, 견고성)을 실천하고, Amazon Bedrock Guardrails 및 Human-in-the-Loop(HITL)을 구축하며, EU AI Act 및 ISO/IEC 42001 등 글로벌 규제를 준수할 수 있는가?

---

## 3.1 책임 있는 AI(RAI) 6대 핵심 차원 (Core Dimensions of Responsible AI)

| RAI 원칙 (Dimension) | 🇺🇸 English Definition & Operational Implementation | 🇰🇷 한국어 정의 및 엔터프라이즈 실천 방안 | 🎯 Core AWS Mechanism |
| :--- | :--- | :--- | :--- |
| **1. Fairness (공정성)** | Preventing systematic discrimination against protected demographic groups; detecting and mitigating historical bias in training data. | 성별, 인종 등 보호된 속성에 따라 특정 집단에 불리한 결정이 내려지지 않도록 데이터 편향을 검증하고 완화함. | **Amazon SageMaker Clarify (편향 감지)** |
| **2. Explainability (설명 가능성)** | Providing human-interpretable justifications for algorithmic outputs, illuminating the black box for customers and regulators. | AI가 내린 판단과 출력의 근거(피처 기여도)를 사용자와 규제 기관이 이해할 수 있도록 명확하게 제시함. | **SHAP Values & SageMaker Clarify** |
| **3. Privacy & Security (개인정보보호)** | Ensuring Personally Identifiable Information (PII) is safeguarded via encryption, redaction, and strict access controls. | 개인 식별 정보(PII)나 기업 기밀이 무단 활용되거나 유출되지 않도록 암호화 및 마스킹을 적용함. | **Amazon Bedrock Guardrails (PII Redaction)** |
| **4. Transparency (투명성)** | Disclosing AI interaction clearly to users; documenting system capabilities, provenance, and operational boundaries. | 사용자가 대화하는 상대가 AI임을 명확히 알리고, 모델 카드 및 디지털 워터마킹을 통해 출처를 공개함. | **C2PA Watermarking & Model Cards** |
| **5. Safety & Controllability (안전성 및 제어성)** | Preventing the generation of harmful, toxic, or illegal content; equipping systems with immediate operational **Kill-Switches**. | 유해 콘텐츠 및 사이버 공격 코드 생성을 차단하고, 비정상 동작 시 즉시 차단하는 비상 정지 메커니즘을 둠. | **Bedrock Guardrails & Kill-Switch Protocol** |
| **6. Robustness (견고성)** | Maintaining consistent and dependable performance in production despite noisy inputs, distribution shifts, or adversarial attacks. | 예상치 못한 비정상 입력이나 적대적 프롬프트 주입(Prompt Injection) 공격에도 일관된 안전 기준을 유지함. | **Adversarial Resilience & Input Filters** |

---

## 3.2 안전성 필터링 및 가드레일 (Amazon Bedrock Guardrails)

<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Amazon Bedrock Guardrails Architecture**: A unified, model-independent policy layer that evaluates both user inputs and model outputs across four primary protections:
  1. *Content Filters*: Blocking hate speech, insults, sexual content, and violence.
  2. *Denied Topics*: Strictly forbidding discussions outside organizational boundaries (e.g., advising on competitor products or giving unofficial legal counsel).
  3. *Sensitive Information Filters*: Automated regex/ML detection and redaction of PII (Social Security numbers, credit cards).
  4. *Contextual Grounding Check*: Validating that generated responses are strictly factual and grounded in retrieved RAG source documents, intercepting hallucinations before delivery.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 번역 및 비즈니스 전략 해설
* **Amazon Bedrock Guardrails의 핵심 역할**: 파운데이션 모델의 종류와 관계없이 입력과 출력 양방향에서 다음과 같은 4대 보호 정책을 중앙 집중식으로 적용합니다:
  1. *유해 콘텐츠 필터*: 혐오 발언, 모욕, 음란물, 폭력적 지침 차단.
  2. *금지된 주제 (Denied Topics)*: 경쟁사 제품 추천 금지, 미승인 금융/법률 자문 등 지정된 금지 주제 차단.
  3. *민감 정보 필터 (PII Masking)*: 주민등록번호, 신용카드 번호 등 개인정보 자동 마스킹.
  4. *문맥적 근거 검사 (Contextual Grounding)*: 검색된 원본 문서에 없는 허위 주장(환각)을 실시간 감지하여 차단.

</div>
</div>

---

## 3.3 인간 참여형 검증 (Human-in-the-Loop, HITL) with Amazon A2I

<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Human-in-the-Loop Architecture**: Autonomous AI decisions must never be unmonitored in high-consequence business workflows (e.g., loan underwriting rejections, diagnostic triages, executive hiring).
* **Amazon Augmented AI (Amazon A2I)**: Automatically inspects inference confidence scores; when prediction confidence drops below a preconfigured threshold (e.g., < 85%) or touches sensitive compliance rules, the transaction is routed automatically to human expert review pools for adjudication and ongoing model auditing.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 번역 및 비즈니스 전략 해설
* **인간 참여형 검증 (HITL)의 필수성**: 대출 거절, 채용 탈락, 의료 진단 등 영향도가 큰 **고위험 시나리오**에서는 결정을 100% AI에 위임해서는 안 되며, 반드시 인간 전문가의 최종 검토 및 승인 단계를 거쳐야 합니다.
* **Amazon Augmented AI (Amazon A2I)**: 모델의 예측 신뢰도 점수가 사전 설정된 임계치(예: 85% 미만) 이하이거나 고위험 거래일 때 자동으로 인간 검토자 풀에게 작업을 전달하여 최종 확인을 받도록 합니다.

</div>
</div>

---

## 3.4 글로벌 AI 규제 준수: EU AI Act & ISO/IEC 42001

<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **EU AI Act Risk Classification**:
  * *Unacceptable Risk*: Social scoring, cognitive behavioral manipulation, real-time remote biometric surveillance in public ➔ **Strictly Prohibited**.
  * *High Risk*: Recruitment/HR scoring, creditworthiness evaluations, critical infrastructure, healthcare ➔ **Mandatory conformity assessments, strict data governance, explainability, and HITL**.
  * *Limited Risk*: Conversational chatbots, deepfakes ➔ **Transparency and disclosure obligations**.
  * *Minimal Risk*: Spam filters, AI in gaming ➔ **No regulatory burden**.
* **ISO/IEC 42001 (AIMS)**: The premier international certifiable management standard establishing organizational processes for managing AI risk and continuous governance.
* **Cross-Functional Governance Committee**: Effective AI governance cannot reside solely within IT. It requires equal partnership across Legal, Compliance, Line-of-Business, Security, and HR leadership.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 번역 및 비즈니스 전략 해설
* **EU AI Act 위험 4단계 등급**:
  * *허용 불가 위험 (Unacceptable)*: 사회적 신용 평가, 실시간 원격 생체 인식 등 ➔ **법적 전면 금지**.
  * *고위험 (High Risk)*: 채용 평가, 대출 심사, 핵심 인프라 등 ➔ **엄격한 위험 평가, 데이터 거버넌스, 설명 가능성, HITL 의무화**.
  * *제한적 위험 (Limited Risk)*: 챗봇, 딥페이크 등 ➔ **AI 사용 여부 투명 고지 의무**.
  * *최소 위험 (Minimal Risk)*: 스팸 필터 등 ➔ **자율 규제**.
* **ISO/IEC 42001**: 인공지능 경영시스템(AIMS)에 관한 최초의 국제 공인 인증 표준으로, 조직 전체의 책임 있는 AI 프로세스를 검증합니다.
* **다학제적(Cross-Functional) 거버넌스 협의체**: AI 거버넌스는 IT만의 업무가 아니며 법무, 컴플라이언스, 비즈니스 리더, 정보보안, 인사팀이 모두 참여해야 합니다.

</div>
</div>
"""

# -------------------------------------------------------------
# 5. docs/05_DOMAIN_4_TRANSFORMATION_READINESS.md (Dual-Track Domain 4)
# -------------------------------------------------------------
DOMAIN4_MD = """# 도메인 4: 비즈니스 준비성, 리더십, AI 혁신 (Business Readiness, Leadership & Transformation)

> **출제 비중 (Exam Weight)**: **22%**  
> **공식 시험 평가 목표 (Exam Objective)**: 조직의 AI 준비성 4대 차원과 성숙도 단계를 진단하고, 데이터 사일로 타파 및 Amazon DataZone 기반 거버넌스를 구축하며, Hub-and-Spoke AI CoE와 AI 챔피언 네트워크를 운영하고, '대체가 아닌 증강' 철학으로 조직 변화 관리를 주도할 수 있는가?

---

## 4.1 AI 준비성 4대 차원 & AI 성숙도 4단계 (Readiness & Maturity)

<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **4 Dimensions of AI Readiness**:
  1. *People*: Literacy, psychological safety, executive sponsorship, willingness to adopt.
  2. *Process*: Agile experimentation velocity, cross-functional collaboration, workflow flexibility.
  3. *Technology*: Modern cloud foundation, API modularity, scalable compute platforms (AWS).
  4. *Governance*: Data quality protocols, ethical RAI policies, regulatory compliance frameworks.
* **AI Maturity Stages**:
  * *Stage 1: Exploration*: Fragmented, uncoordinated ad-hoc experiments across isolated teams.
  * *Stage 2: Opportunistic (Piloting)*: Localized successes in specific business units, lacking central governance.
  * *Stage 3: Systematic (Operationalized)*: Establishment of an **AI Center of Excellence (CoE)**, standardized enterprise platforms, and formal RAI guardrails.
  * *Stage 4: Transformational (AI-Driven)*: Business models fundamentally reimagined around AI capabilities across all business units.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 번역 및 비즈니스 전략 해설
* **성공적인 AI 도입을 위한 4대 핵심 축**:
  1. *People (사람/문화)*: 직원들의 AI 리터러시, 심리적 안정감, 경영진의 적극적 스폰서십.
  2. *Process (프로세스)*: 애자일한 실험 프로세스, 부서 간 협업, 신속한 의사결정 체계.
  3. *Technology (기술/인프라)*: 확장 가능한 클라우드 인프라(AWS), API 연동 환경.
  4. *Governance (거버넌스)*: 데이터 품질 관리, 윤리적 가이드라인, 규제 준수 프레임워크.
* **AI 성숙도 4단계 발전 로드맵**:
  * *1단계 (탐색/실험)*: 부서별 파편화된 비공식 PoC 시도 단계.
  * *2단계 (기회 포착/시범)*: 특정 부서에서 초기 성공 사례가 나오나 전사 거버넌스는 미흡한 단계.
  * *3단계 (체계화/운영)*: **AI CoE**가 설립되고 표준 플랫폼과 전사 거버넌스가 확립되는 단계.
  * *4단계 (전사 혁신)*: 비즈니스 모델 자체가 AI 중심으로 재편되는 최고 단계.

</div>
</div>

---

## 4.2 데이터 사일로 타파 및 엔터프라이즈 데이터 거버넌스 (Data Foundation)

<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Breaking Data Silos with Data Mesh**: Departmental data isolation prevents AI models from learning end-to-end customer contexts. Modern enterprise architecture shifts from centralized data bottlenecks to a **Data Mesh** model where domain units curate "Data Products" under federated governance.
* **Amazon DataZone**: A business data management portal enabling federated data cataloging, discovery, subscription, and secure governance across organizational boundaries.
* **Data Contracts & Internal SLAs**: Explicit formal agreements between upstream data engineering teams and downstream AI consumers governing schema stability, data freshness, and quality thresholds, eliminating unexpected pipeline outages.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 번역 및 비즈니스 전략 해설
* **데이터 사일로 타파 및 데이터 메시 (Data Mesh)**: 부서별로 데이터가 고립되어 있으면 AI가 전체 고객 여정을 파악할 수 없습니다. 중앙 데이터팀의 병목을 없애고 각 현업 부서가 자신의 데이터를 '데이터 프로덕트'로 소유하고 공유하는 데이터 메시로 전환해야 합니다.
* **Amazon DataZone**: 부서 간에 데이터를 안전하게 검색, 카탈로그화, 구독, 공유할 수 있도록 지원하는 완전관리형 데이터 거버넌스 포털 서비스입니다.
* **데이터 계약 (Data Contracts) 및 내부 SLA**: 데이터 생산자와 AI 소비자 간에 스키마 변경 사전 공지, 데이터 최신성, 품질 기준을 명시한 공식 협약으로 다운스트림 AI 모델의 중단 사고를 방지합니다.

</div>
</div>

---

## 4.3 조직 모델: AI 센터 오브 엑설런스 (AI CoE) & AI 챔피언 네트워크

<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Hub-and-Spoke CoE Operating Model**: The industry-standard enterprise AI organization:
  * *The Central Hub (CoE)*: Establishes enterprise architecture standards, curates shared foundation models and prompt libraries, manages compliance guardrails, and negotiates vendor pricing.
  * *The Decentralized Spokes (Business Units)*: Domain product managers, business analysts, and domain engineers addressing local business friction points directly.
* **AI Champions Network**: Embedded grassroots peer-coaches in non-technical departments (HR, Finance, Legal) who surface high-impact use cases, mentor peers in daily prompt literacy, and relay feedback back to the central CoE.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 번역 및 비즈니스 전략 해설
* **허브 앤 스포크 (Hub-and-Spoke) 조직 모델**: 중앙 CoE(Hub)가 인프라, 공통 도구, 보안 거버넌스 표준을 총괄하고, 각 사업 부서 실무자(Spoke)가 현업의 비즈니스 문제를 직접 해결하는 **가장 이상적인 엔터프라이즈 AI 조직 모델**입니다.
* **AI 챔피언 네트워크 (AI Champions)**: 인사, 재무, 마케팅 등 비기술 부서마다 AI 챔피언을 지정하여 동료들에게 AI 활용 팁을 코칭하고, 부서 내 페인 포인트를 발굴하여 중앙 CoE에 연결하는 풀뿌리 혁신의 핵심 동력입니다.

</div>
</div>

---

## 4.4 변화 관리 철학: 대체가 아닌 증강 (Augmentation over Replacement)

<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **"Augmentation over Replacement" Philosophy**: Employee resistance and cultural friction stem from job insecurity. Leadership must clearly communicate that AI is designed to eliminate mundane cognitive drudgery, liberating human workers to elevate into high-value strategic, creative, and empathetic advisory roles.
* **Psychological Safety & Culture of Experimentation**: Fostering an agile "fail-fast" learning culture where employees are encouraged to experiment boldly without fear of punitive measures.
* **AWS PartyRock & Prototyping Sandboxes**: Empowering non-technical employees with intuitive no-code generative AI playgrounds governed by Bedrock Guardrails, enabling safe grassroots prototyping and enterprise hackathons.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 번역 및 비즈니스 전략 해설
* **'대체가 아닌 증강(Augmentation over Replacement)' 원칙**: 직원들의 저항은 일자리 상실 우려에서 비롯됩니다. 리더십은 AI가 직원을 해고하기 위한 대체자가 아니라 단순 반복 업무를 대신해 주어 인간이 고부가가치 창의/전략 업무로 역량을 높이도록 돕는 보조자임을 명확히 선포해야 합니다.
* **심리적 안전감 및 실험 문화**: 작은 실패를 비난하지 않고 빠른 가설 검증과 학습의 기회로 장려하는 애자일한 조직 문화를 조성합니다.
* **AWS PartyRock 및 안전한 사내 샌드박스**: 비개발자도 프롬프트만으로 생성형 AI 앱을 손쉽게 만들어볼 수 있는 노코드 도구와 격리된 사내 샌드박스를 제공하여 기밀 유출 위험 없이 전사적인 AI 실험 문화를 확산합니다.

</div>
</div>
"""

# -------------------------------------------------------------
# 6. docs/06_AWS_SERVICES_CHEAT_SHEET.md (Dual-Track AWS Services)
# -------------------------------------------------------------
SERVICES_MD = """# 출제 범위 내 핵심 AWS 서비스 치트시트 (AIB-C01 In-Scope Services)

> **시험 공략 팁 (Exam Focus)**: AIB-C01 시험은 기술적인 API 코드 작성을 묻지 않습니다. 대신 **\"어떤 비즈니스 시나리오에서 어떤 AWS 서비스를 선택하는 것이 최적인가?\"**를 평가합니다.

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
"""

def main():
    print("=== Writing Bilingual Dual-Track Study Documents ===")
    
    files = {
        '01_GLOSSARY_KR_EN.md': GLOSSARY_MD.strip(),
        '02_DOMAIN_1_AI_FUNDAMENTALS.md': DOMAIN1_MD.strip(),
        '03_DOMAIN_2_AI_STRATEGY_VALUE.md': DOMAIN2_MD.strip(),
        '04_DOMAIN_3_GOVERNANCE_RESPONSIBLE_AI.md': DOMAIN3_MD.strip(),
        '05_DOMAIN_4_TRANSFORMATION_READINESS.md': DOMAIN4_MD.strip(),
        '06_AWS_SERVICES_CHEAT_SHEET.md': SERVICES_MD.strip()
    }
    
    for filename, content in files.items():
        fpath = os.path.join(DOCS_DIR, filename)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content + '\n')
        print(f"✓ Written {filename} ({len(content)} chars)")
        
    # Read exam guide as well
    exam_guide_path = os.path.join(DOCS_DIR, '00_AIB-C01_EXAM_GUIDE.md')
    with open(exam_guide_path, 'r', encoding='utf-8') as f:
        exam_guide_content = f.read()

    portal_docs = {
        'overview': exam_guide_content,
        'glossary': files['01_GLOSSARY_KR_EN.md'],
        'domain1': files['02_DOMAIN_1_AI_FUNDAMENTALS.md'],
        'domain2': files['03_DOMAIN_2_AI_STRATEGY_VALUE.md'],
        'domain3': files['04_DOMAIN_3_GOVERNANCE_RESPONSIBLE_AI.md'],
        'domain4': files['05_DOMAIN_4_TRANSFORMATION_READINESS.md'],
        'aws_services': files['06_AWS_SERVICES_CHEAT_SHEET.md']
    }
    
    js_code = (
        "// AWS Certified AI Business Strategist (AIB-C01) Complete Bilingual Study Materials\n"
        "// Exhaustive vocabulary & exam answers alignment with Dual-Track English/Korean layout\n"
        f"const PORTAL_DOCS = {json.dumps(portal_docs, ensure_ascii=False, indent=2)};\n\n"
        "if (typeof window !== 'undefined') {\n  window.PORTAL_DOCS = PORTAL_DOCS;\n}\n"
        "if (typeof module !== 'undefined' && module.exports) {\n  module.exports = PORTAL_DOCS;\n}\n"
    )
    
    portal_js_path = os.path.join(BASE_DIR, 'portal-docs-data.js')
    with open(portal_js_path, 'w', encoding='utf-8') as f:
        f.write(js_code)
    print(f"✓ Synchronized portal-docs-data.js ({len(js_code)} bytes)")
    
    print("\n🎉 ALL 6 BILINGUAL DUAL-TRACK STUDY GUIDES BUILT SUCCESSFULLY! 🎉")

if __name__ == '__main__':
    main()
