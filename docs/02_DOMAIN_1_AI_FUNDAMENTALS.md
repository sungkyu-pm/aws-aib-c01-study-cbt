# 도메인 1: AI 기초 및 활용 능력 (AI Fundamentals and Literacy)

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
