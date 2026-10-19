#!/usr/bin/env python3
"""
AWS Certified AI Business Strategist (AIB-C01) Full 1,200 Question Bank Builder
Generates 300 high-quality bilingual questions per domain (1,200 questions total).
Preserves existing curated questions (Q01-Q30) and synthesizes Q031-Q300 for each domain.
"""

import json
import os
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_DIR = os.path.join(BASE_DIR, 'questions')

INDUSTRIES = [
    ("글로벌 금융/핀테크 기업", "global FinTech & banking firm", "신용 대출 심사 및 실시간 이상 거래 데이터", "credit underwriting and real-time fraud transaction data"),
    ("대형 전자상거래/리테일 플랫폼", "major e-commerce & retail platform", "수천만 건의 상품 리뷰 및 고객 장바구니 행동 로그", "tens of millions of product reviews and cart event logs"),
    ("종합 의료원 및 헬스케어 연구소", "university medical center and clinical research institute", "비정형 전자의무기록(EMR) 및 임상 시험 논문", "unstructured Electronic Medical Records (EMR) and clinical trial papers"),
    ("다국적 해운 및 스마트 물류사", "multinational ocean carrier and smart logistics provider", "글로벌 공급망 운송 경로 및 복합 화물 선적 데이터", "global supply chain shipping routes and cargo manifests"),
    ("글로벌 손해보험사", "global property and casualty insurance enterprise", "사고 손해사정 현장 보고서 및 보험금 청구 증빙 서류", "accident loss adjustment field reports and claim documents"),
    ("첨단 반도체/스마트 제조 공장", "high-tech semiconductor & smart manufacturing facility", "공장 설비 IoT 진동/온도 시계열 센서 데이터", "factory equipment IoT vibration and temperature time-series telemetry"),
    ("글로벌 미디어 및 엔터테인먼트 그룹", "global media & streaming entertainment corporation", "방대한 디지털 영상 아카이브 및 다국어 대본 자막", "massive digital video archives and multilingual subtitle scripts"),
    ("엔터프라이즈 B2B SaaS 기업", "enterprise B2B enterprise software company", "수백만 건의 고객 기술 지원 티켓 및 API 사용 로그", "millions of technical support tickets and API usage logs"),
    ("전국망 통신 서비스 사업자", "nationwide telecommunications carrier", "네트워크 기지국 혼잡도 지표 및 고객 해지 위험 로그", "cell tower congestion metrics and customer churn risk event logs"),
    ("공공 행정 및 지자체 민원 센터", "public municipal administration and civic portal", "시민 복지 상담 민원 내역 및 조례 행정 법률 문서", "citizen welfare petitions and municipal administrative legal codes"),
    ("글로벌 항공사 및 여행 플랫폼", "international airline and global travel booking platform", "실시간 항공편 예약 데이터 및 고객 수하물 추적 기록", "flight reservation streams and passenger baggage tracking data"),
    ("글로벌 자동차 제조 및 커넥티드카 기업", "global automotive OEM and connected vehicle firm", "차량 텔레매틱스 주행 데이터 및 운전자 보조 시스템 로그", "in-vehicle telematics driving telemetry and ADAS sensor logs")
]

# Domain 1 Templates (AI Fundamentals & Literacy)
D1_THEMES = [
    (
        "Temperature 및 추론 파라미터 제어",
        "Temperature & Inference Parameters",
        "보고서나 법률 문서 요약처럼 매번 100% 동일하고 사실에 기반한 결정론적(Deterministic) 결과를 보장하기 위해 조정해야 하는 파운데이션 모델 추론 파라미터 설정은 무엇입니까?",
        "To ensure 100% consistent, deterministic, and strictly factual output without creative variance for formal summaries, which foundation model inference parameter setting must be configured?",
        "Temperature를 0.0으로 설정하고 Top-P를 최소화하여 모델이 항상 가장 확률이 높은 토큰(Greedy Decoding)만 선택하도록 합니다.",
        "Set Temperature to 0.0 and minimize Top-P, enforcing greedy decoding where the model strictly selects the highest-probability token.",
        [
            ("Temperature를 1.5로 올리고 Top-K를 100으로 설정합니다.", "Increase Temperature to 1.5 and set Top-K to 100 to maximize stochastic randomness."),
            ("GPU 클러스터의 디스크 캐시 크기를 2배로 늘립니다.", "Double the disk cache allocation on the GPU cluster."),
            ("Amazon S3 수명 주기 정책으로 프롬프트를 30일 후 자동 삭제합니다.", "Configure an S3 lifecycle policy to delete prompts after 30 days.")
        ],
        "• **Temperature**는 출력의 무작위성(창의성)을 제어합니다. 엄격한 일관성과 사실 기반 요약이 필요한 비즈니스 시나리오에서는 Temperature를 0.0으로 설정하여 항상 최고 확률 토큰을 선택하도록 해야 합니다."
    ),
    (
        "RAG (검색 증강 생성) vs 파인 튜닝 선택",
        "RAG vs Fine-Tuning Decision",
        "자주 업데이트되는 사내 지식 문서를 기반으로 정확한 출처(Source Citation)를 인용하며 환각을 방지해야 할 때, 모델 가중치 재학습 없이 가장 효율적으로 구축할 수 있는 솔루션은 무엇입니까?",
        "When business users require accurate answers citing exact sources from frequently updated internal documentation without retraining model weights, which solution architecture is most appropriate?",
        "Knowledge Bases for Amazon Bedrock을 활용한 완전관리형 검색 증강 생성(RAG) 파이프라인 구축",
        "Implement a fully managed Retrieval-Augmented Generation (RAG) pipeline using Knowledge Bases for Amazon Bedrock.",
        [
            ("새로운 문서가 추가될 때마다 전체 파운데이션 모델을 사전 학습(Pre-training)합니다.", "Pre-train a proprietary foundation model from scratch whenever new documents arrive."),
            ("모든 문서의 텍스트를 모델 가중치에 영구 반영하기 위해 매주 지도 파인 튜닝을 실행합니다.", "Run weekly supervised fine-tuning to permanently bake all text into model weights."),
            ("모든 문서를 1만 개의 하드코딩된 IF-ELSE 조건문 규칙으로 변환합니다.", "Convert all documentation into 10,000 hardcoded IF-ELSE deterministic branches.")
        ],
        "• **RAG(검색 증강 생성)**는 외부 데이터베이스에서 실시간으로 관련 문서를 검색하여 프롬프트 컨텍스트에 주입하므로, 잦은 지식 업데이트를 재학습 비용 없이 반영하고 출처 기반 답변으로 환각을 최소화합니다."
    ),
    (
        "자율 AI 에이전트 및 액션 그룹",
        "AI Agents & Action Groups",
        "사용자의 자연어 요청을 분석하여 다단계 실행 계획을 수립하고, 사내 REST API와 데이터베이스를 자율 호출하여 실제 비즈니스 트랜잭션을 완수하는 시스템에 필요한 핵심 기술은 무엇입니까?",
        "Which capability enables an AI system to parse natural language goals, generate multi-step execution plans, and autonomously invoke REST APIs to complete real-world transactions?",
        "OpenAPI 스키마와 AWS Lambda 함수로 액션 그룹(Action Groups)이 구성된 Agents for Amazon Bedrock",
        "Agents for Amazon Bedrock configured with Action Groups backed by OpenAPI schemas and AWS Lambda functions.",
        [
            ("단순 키워드 매칭 기반의 웹 브라우저 즐겨찾기 스크립트", "Simple keyword-matching browser bookmark scripts."),
            ("단일 정적 프롬프트만 하드코딩된 규칙 기반 챗봇 위젯", "A rule-based chatbot widget with a single hardcoded prompt string."),
            ("서버 CPU 사용률을 모니터링하는 CloudWatch 경보 규칙", "Amazon CloudWatch alarms tracking CPU utilization.")
        ],
        "• **Agents for Amazon Bedrock**은 파운데이션 모델의 추론(Reasoning) 능력과 액션 그룹(Action Groups)을 결합하여, OpenAPI 스키마에 정의된 API를 자율적으로 호출해 복합 작업을 완수합니다."
    ),
    (
        "중간 정보 누락 (Lost in the Middle) 현상",
        "Lost in the Middle & Chunking",
        "수백 페이지에 달하는 긴 문서를 단일 프롬프트에 통째로 입력했을 때, 문서 중간에 위치한 중요한 수치나 정보가 요약에서 누락되는 현상의 원인과 해결책은 무엇입니까?",
        "When an entire massive document is fed into an LLM prompt, critical facts in the middle of the text are frequently missed. What causes this and what is the recommended fix?",
        "LLM의 어텐션 저하 현상인 'Lost in the Middle'이며, 문서를 적절한 크기로 청킹(Chunking)하여 관련 조각만 검색 주입하는 벡터 검색 RAG로 해결합니다.",
        "The 'Lost in the Middle' attention degradation; resolve by chunking documents into optimal segments and retrieving relevant chunks via vector search RAG.",
        [
            ("모니터 해상도 부족이며, 4K 디스플레이로 교체합니다.", "Insufficient display resolution; upgrade to 4K monitors."),
            ("컴퓨터 램 부족이며, 로컬 노트북의 메모리를 증설합니다.", "Local workstation RAM exhaustion; install extra memory."),
            ("영문 글꼴 라이선스 만료이며, 시스템 글꼴을 변경합니다.", "System font license expiration; change default fonts.")
        ],
        "• LLM은 프롬프트의 시작과 끝부분에 더 강한 주의(Attention)를 기울이고 중간 정보를 놓치는 **Lost in the Middle** 특성이 있습니다. 이를 극복하려면 청킹(Chunking)과 벡터 RAG 검색이 필수적입니다."
    ),
    (
        "모델 드리프트 vs 개념 드리프트",
        "Model Drift & Concept Drift",
        "시장 경제 상황이나 소비자 행동 양식의 근본적인 변화로 인해 배포된 예측 AI 모델의 성능이 시간 경과에 따라 저하되는 현상과 그에 대한 운영 조치는 무엇입니까?",
        "When macroeconomic shifts or changing consumer habits degrade a deployed model's accuracy over time, what is this phenomenon and the appropriate remediation?",
        "개념 드리프트(Concept Drift); 최신 시장 데이터를 수집하여 모델을 재학습하고 SageMaker Model Monitor로 지속 감시합니다.",
        "Concept Drift; gather recent representative data, retrain the model, and implement continuous drift tracking via SageMaker Model Monitor.",
        [
            ("서버 팬 소음이며, 데이터 센터의 온도를 낮춥니다.", "Acoustic fan interference; lower room temperature."),
            ("프롬프트 문법 오류이며, 모든 쉼표를 마침표로 바꿉니다.", "Punctuation syntax errors; replace commas with periods."),
            ("네트워크 대역폭 한계이며, 이더넷 케이블을 교체합니다.", "Network bandwidth bottleneck; replace LAN cables.")
        ],
        "• **개념 드리프트(Concept Drift)**는 입력 변수와 목표 변수 사이의 관계 자체가 변화하는 현상입니다. 지속적인 모니터링(SageMaker Model Monitor)과 주기적 재학습 파이프라인 구축이 필수적입니다."
    ),
    (
        "정형 vs 비정형 데이터 모델 선택",
        "Structured vs Unstructured ML Selection",
        "관계형 테이블의 수치 데이터(결제 금액, 연령 등)와 비정형 텍스트(상담 녹취록, 고객 피드백)를 복합 처리할 때 가장 권장되는 아키텍처 조합은 무엇입니까?",
        "When handling both structured tabular numbers (e.g., tenure, transaction sums) and unstructured customer text, which combination of AI technologies is optimal?",
        "정형 데이터에는 트리 기반 지도학습(XGBoost 등)을 적용하고, 비정형 텍스트에는 대규모 언어 모델(LLM) 및 텍스트 임베딩 모델을 적용합니다.",
        "Tree-based supervised ML (e.g., XGBoost) for tabular data, and Large Language Models (LLMs) with text embeddings for unstructured text.",
        [
            ("정형 숫자 계산에 이미지 생성 확산 모델(Diffusion Model)을 적용합니다.", "Apply image diffusion models to compute numeric tables."),
            ("비정형 텍스트 분석에 단순 1차원 정수 계산기만 사용합니다.", "Use a scalar math calculator for semantic natural language."),
            ("모든 데이터베이스를 흑백 이미지 픽셀로 변환하여 OCR만 수행합니다.", "Convert all relational databases into black-and-white images.")
        ],
        "• 정형 데이터에는 XGBoost와 같은 트리 기반 알고리즘이 연산 효율과 정확도 면에서 뛰어나며, 문맥 이해가 필요한 비정형 텍스트에는 LLM과 임베딩 모델이 최적입니다."
    ),
    (
        "섀도 AI 위험 완화",
        "Shadow AI Mitigation",
        "직원들이 사내 기밀 문서나 고객 개인정보를 외부 퍼블릭 무료 챗봇에 무단 입력하여 사용하는 섀도 AI(Shadow AI) 위협에 대응하는 가장 바람직한 거버넌스 접근법은 무엇입니까?",
        "What is the most effective enterprise governance approach to mitigate Shadow AI risks where employees paste sensitive corporate data into unvetted public chatbots?",
        "외부 비인가 도구를 차단하는 동시에, 사내 데이터 보안 및 권한(ACL)이 보장된 엔터프라이즈 생성형 AI 어시스턴트(예: Amazon Q Business)를 공식 제공합니다.",
        "Block unvetted external consumer tools while officially providing an enterprise-grade AI assistant (e.g., Amazon Q Business) with strict data privacy and ACL security.",
        [
            ("전사 모든 임직원의 컴퓨터 및 인터넷 사용을 전면 금지합니다.", "Completely forbid computer and internet usage for all staff."),
            ("모든 업무 문서를 손글씨 종이 서류로만 작성하도록 강제합니다.", "Force all employees to write documents on physical stationery only."),
            ("보안 위험을 무시하고 직원들이 외부 공개 챗봇을 자유롭게 쓰도록 방치합니다.", "Ignore security concerns and let staff paste trade secrets into public tools.")
        ],
        "• 섀도 AI는 무조건적인 차단보다 엔터프라이즈 보안 및 데이터 비저장 정책이 적용된 공식 사내 도구(Amazon Q Business, Bedrock)를 제공하는 것이 가장 효과적인 해결책입니다."
    ),
    (
        "모델 양자화 (Quantization)",
        "Model Quantization",
        "대규모 파운데이션 모델의 추론(Inference) 비용과 지연 시간(Latency)을 줄이기 위해, 가중치 정밀도를 FP16에서 INT8/INT4로 축소하는 기법은 무엇입니까?",
        "Which technique reduces model weight numerical precision from FP16 to INT8 or INT4, slashing memory usage and accelerating inference latency with minimal accuracy loss?",
        "모델 양자화 (Model Quantization)",
        "Model Quantization",
        [
            ("데이터베이스 제3정규화 (3NF)", "Database Third Normal Form Normalization"),
            ("데이터 센터 물리적 이전", "Physically moving server racks to another building"),
            ("광통신 케이블 신호 증폭", "Fiber optic cable signal repeaters")
        ],
        "• **모델 양자화(Quantization)**는 부동소수점 가중치를 정수형(INT8/INT4)으로 압축하여 GPU 메모리 요구량을 줄이고 추론 속도를 획기적으로 개선하는 기술입니다."
    ),
    (
        "LLM-as-a-Judge 자동 평가",
        "LLM-as-a-Judge Evaluation",
        "매일 생성되는 수만 건의 AI 요약본 품질을 평가할 때, 인간 검수자의 비용 한계를 극복하고 일관된 루브릭에 따라 충실성과 정확성을 대규모로 자동 측정하는 방법은 무엇입니까?",
        "How can an organization continuously benchmark summary quality across tens of thousands of daily outputs without exorbitant manual evaluation costs?",
        "판사 모델 기반 평가 (LLM-as-a-Judge) 및 Amazon Bedrock 모델 평가 기능 활용",
        "LLM-as-a-Judge evaluation pattern utilizing automated Bedrock model evaluation capabilities.",
        [
            ("텍스트 파일의 바이트 용량만 단순 비교하기", "Comparing raw file sizes in bytes of text outputs."),
            ("문장의 글자 수가 짝수인지 홀수인지 검사하기", "Counting whether sentence length is an even integer."),
            ("모든 현장 직원에게 주말 수작업 채점 강제하기", "Forcing staff to spend weekends grading tens of thousands of transcripts manually.")
        ],
        "• **LLM-as-a-Judge**는 최상위 모델(예: Claude 3.5 Sonnet)에 체계적인 채점 기준표(Rubric)를 제공하여 대규모 생성물의 충실성과 정확성을 일관성 있게 자동 평가하는 모범 프랙티스입니다."
    ),
    (
        "사고의 사슬 (Chain-of-Thought) 프롬프팅",
        "Chain-of-Thought (CoT) Prompting",
        "복잡한 다단계 논리 추론이나 산술 계산 문제를 LLM이 해결할 때, '단계별로 나누어 생각해 봅시다(Think step-by-step)'라는 지침을 제공하여 오류를 줄이는 기법은 무엇입니까?",
        "Which prompting strategy guides an LLM to decompose complex multi-step reasoning or math logic into transparent sequential steps, significantly boosting accuracy?",
        "사고의 사슬 프롬프팅 (Chain-of-Thought, CoT)",
        "Chain-of-Thought (CoT) Prompting",
        [
            ("무작위 노이즈 프롬프팅 (Random Noise Injection)", "Random Noise Injection"),
            ("단일 단어 초단축 프롬프팅 (Zero-Context Prompting)", "Zero-Context Single Word Prompting"),
            ("이진 바이트 스트림 프롬프팅 (Raw Binary Prompting)", "Raw Binary Stream Prompting")
        ],
        "• **사고의 사슬(Chain-of-Thought, CoT)** 기법은 복잡한 추론 문제를 중간 단계별 논리로 분해하여 풀어내도록 유도함으로써 복합 논리 및 연산 문제의 정확도를 획기적으로 향상시킵니다."
    )
]

# Generate synthetic variations to reach 300 per domain
def generate_questions_for_domain(domain_num, domain_name, base_themes, start_idx=31, target_total=300):
    questions = []
    current_id = start_idx
    theme_idx = 0
    industry_idx = 0

    while len(questions) < (target_total - start_idx + 1):
        theme = base_themes[theme_idx % len(base_themes)]
        ind = INDUSTRIES[industry_idx % len(INDUSTRIES)]

        org_kr, org_en, data_kr, data_en = ind
        topic_name, cat_en, stem_kr_raw, stem_en_raw, corr_kr, corr_en, distractors, exp_kr = theme

        # Format stems with industry contexts
        q_kr = f"[{org_kr}] {org_kr}에서 {data_kr}를 활용하여 AI 솔루션을 도입하고자 합니다. {stem_kr_raw}"
        q_en = f"[{org_en}] A {org_en} is adopting an AI solution leveraging {data_en}. {stem_en_raw}"

        # Build options
        opts_raw = [{"text_kr": corr_kr, "text_en": corr_en, "is_correct": True}]
        for d_kr, d_en in distractors:
            opts_raw.append({"text_kr": d_kr, "text_en": d_en, "is_correct": False})

        # Shuffle options deterministic per ID
        random.seed(current_id * 100 + domain_num)
        random.shuffle(opts_raw)

        options = []
        correct_letter = "A"
        letters = ["A", "B", "C", "D"]
        for idx, item in enumerate(opts_raw[:4]):
            letter = letters[idx]
            options.append({
                "key": letter,
                "text_en": item["text_en"],
                "text_kr": item["text_kr"]
            })
            if item["is_correct"]:
                correct_letter = letter

        qid = f"D{domain_num}-Q{current_id:03d}"
        q_obj = {
            "id": qid,
            "domain": f"Domain {domain_num}",
            "domain_name": domain_name,
            "question_en": q_en,
            "question_kr": q_kr,
            "options": options,
            "correct_answer": correct_letter,
            "explanation_kr": f"정답은 {correct_letter}입니다.\n\n{exp_kr}",
            "key_concept": f"{cat_en}, AWS Certified AI Business Strategist"
        }
        questions.append(q_obj)

        current_id += 1
        theme_idx += 1
        if theme_idx % len(base_themes) == 0:
            industry_idx += 1

    return questions

# Similar themes for Domain 2 (AI Strategy & Business Value)
D2_THEMES = [
    (
        "자체 구축 vs 솔루션 구매 vs 파트너 협력 (Build vs Buy vs Partner)",
        "Build vs Buy vs Partner Framework",
        "핵심 차별화 경쟁 우위가 아닌 일반적인 표준 업무(예: 직원 HR 온보딩)에 AI를 도입할 때, 가장 빠른 시장 출시(Time to Market)와 낮은 초기 TCO를 달성하기 위한 올바른 전략은 무엇입니까?",
        "When introducing AI to a standard non-differentiating back-office workflow (e.g., employee onboarding), which strategy achieves the fastest time-to-market and lowest upfront TCO?",
        "상용 솔루션 구매 (Buy): 검증된 SaaS 또는 완전관리형 상용 AI 서비스를 도입합니다.",
        "Buy: Procure an established commercial SaaS or managed turnkey AI application.",
        [
            ("처음부터 밑바닥 자체 개발 (Build): 독자적인 파운데이션 모델을 사전 학습합니다.", "Build from scratch: Pre-train a custom foundation model internally."),
            ("외부 파트너사에게 회사의 지분 50%를 양도하고 무기한 협력합니다.", "Surrender 50% equity to a consulting partner indefinitely."),
            ("해당 업무를 디지털 전환하지 않고 수작업 문서로만 처리하도록 동결합니다.", "Freeze the process into manual paper memos permanently.")
        ],
        "• 핵심 차별화(Core Differentiator)가 아닌 표준적인 백오피스 업무에는 **구매(Buy)** 전략이 가장 빠르고 유지보수 비용이 적게 듭니다. 반면 자사 고유의 경쟁 우위 영역에는 자체 구축(Build)을 고려합니다."
    ),
    (
        "우선순위 2x2 매트릭스 (Prioritization Matrix)",
        "Use Case Prioritization Matrix (Value vs Feasibility)",
        "다양한 AI 아이디어가 제안되었을 때, 조직 내 신뢰와 모멘텀을 확보하기 위해 최우선적으로 착수해야 하는 '단기 성공 과제(Quick Wins)'의 특성은 무엇입니까?",
        "When evaluating a portfolio of candidate AI projects, which quadrant represents 'Quick Wins' that should be prioritized first to build executive confidence and momentum?",
        "비즈니스 가치가 높고(High Value), 구현 복잡도/난이도가 낮은(Low Complexity) 과제",
        "Projects with High Business Value and Low Implementation Complexity (High Value, High Feasibility).",
        [
            ("비즈니스 가치가 거의 없고 구현 난이도가 극도로 높은 과제", "Projects with near-zero value and extreme technical complexity."),
            ("5년 동안 매출 발생이 전혀 없는 순수 이론 연구 과제", "Pure academic research with zero measurable ROI for 5 years."),
            ("경쟁사도 모두 포기한 성공 확률 1% 미만의 과제", "Projects with sub-1% feasibility that all competitors abandoned.")
        ],
        "• AI 프로젝트 포트폴리오에서는 **High Value & Low Complexity (Quick Wins)** 과제를 먼저 성공시켜 조기 가치를 입증하고, 이를 발판으로 대규모 전략적 투자(Strategic Bets)를 유치하는 것이 정석입니다."
    ),
    (
        "선행 지표 vs 후행 지표 (Leading vs Lagging Indicators)",
        "Leading vs Lagging Value Indicators",
        "엔터프라이즈 AI 어시스턴트 도입 초기 단계에서, 최종 연간 비용 절감액(후행 지표)이 나타나기 전에 프로젝트의 성공 가능성을 조기에 가늠할 수 있는 '선행 지표(Leading Indicator)'는 무엇입니까?",
        "During early enterprise AI rollout, which metric serves as a 'Leading Indicator' to predict future success before lagging financial ROI materializes?",
        "직원들의 일일 활성 사용자 수(DAU), 주당 AI 프롬프트 쿼리 수, 초기 사용자 채택률",
        "Daily Active Users (DAU), weekly query volume per user, and early employee adoption rate.",
        [
            ("3년 후 기업의 연간 총 영업이익률", "Consolidated 3-year trailing net operating margin."),
            ("회사 건물의 10년 감가상각 누계액", "10-year cumulative office depreciation."),
            ("국제 원자재 유가 변동 지수", "Global commodity crude oil futures price fluctuations.")
        ],
        "• **선행 지표(Leading Indicator)**는 채택률, 일일 활성 사용자 수(DAU), 사용 빈도처럼 조기에 관측 가능한 지표로, 후행 재무 지표(비용 절감, 순이익)의 성패를 미리 예측할 수 있게 해줍니다."
    ),
    (
        "기준 지표 (Baseline Metric)의 필수성",
        "Baseline Metric Definition",
        "AI 솔루션 도입 후 실제 비즈니스 ROI와 성과 개선율을 정량적으로 증명하기 위해 프로젝트 착수 전에 반드시 수행해야 하는 조치는 무엇입니까?",
        "To objectively validate ROI and performance improvements post-deployment, what must project leadership establish prior to initiating AI implementation?",
        "현재 상태(As-Is)의 업무 처리 시간, 오류율, 인건비 등의 기준 지표(Baseline Metric)를 사전에 정량적으로 측정 및 기록합니다.",
        "Quantitatively measure and document baseline metrics (As-Is processing duration, error rates, costs) before rollout.",
        [
            ("기존 시스템의 모든 과거 데이터를 삭제하여 비교를 불가능하게 만듭니다.", "Wipe historical logs so past performance cannot be compared."),
            ("모든 성과 측정을 배제하고 경영진의 직관적인 감에만 의존합니다.", "Rely entirely on subjective executive gut-feel without metrics."),
            ("도입 전에는 아무런 측정도 하지 않고 1년 후에 임의로 수치를 작성합니다.", "Skip pre-implementation measurement and fabricate numbers later.")
        ],
        "• **기준 지표(Baseline)**가 사전에 정의되지 않으면, AI 도입 후에 아무리 성능이 개선되어도 \"AI 덕분에 얼마나 개선되었는가?\"를 정량적으로 증명할 수 없습니다."
    ),
    (
        "숨은 TCO (Total Cost of Ownership) 관리",
        "Hidden TCO Components",
        "생성형 AI 프로젝트의 예산을 책정할 때, 단순한 클라우드 API 호출 토큰 비용 외에 간과하기 쉬운 주요 '숨은 TCO(총 소유 비용)' 항목은 무엇입니까?",
        "When estimating Generative AI Total Cost of Ownership (TCO), which critical hidden cost categories beyond raw API token fees must be budgeted?",
        "데이터 정제/라벨링 비용, MLOps 파이프라인 운영비, 지속적 드리프트 모니터링 및 직원 교육/변화 관리 비용",
        "Data curation/labeling, ongoing MLOps operations, drift monitoring, and staff change management/training costs.",
        [
            ("사무실 책상과 의자 가구 교체 비용", "Office furniture ergonomic replacement fees."),
            ("서버실 형광등 교체 전기료", "Server room fluorescent lighting bulbs."),
            ("회사 로고 브랜드 색상 인쇄비", "Marketing logo stationery reprint expenses.")
        ],
        "• 생성형 AI의 TCO는 API 토큰 비용뿐 아니라 **데이터 준비, 파이프라인 엔지니어링, 지속적인 모니터링, 재학습 및 전사 교육 비용**이 상당한 비중을 차지합니다."
    ),
    (
        "데이터 플라이휠 (Data Flywheel) 효과",
        "Data Flywheel Effect & Defensibility",
        "AI 솔루션에 더 많은 사용자가 유입될수록 고유 사용자 데이터가 축적되고, 이를 통해 모델이 정교화되어 다시 더 많은 사용자를 끌어들이는 지속 가능한 경쟁 우위 메커니즘은 무엇입니까?",
        "Which self-reinforcing competitive mechanism states that more users generate proprietary data, improving model quality, which attracts even more users?",
        "데이터 플라이휠 (Data Flywheel) 효과",
        "Data Flywheel Effect",
        [
            ("기술 부채 (Technical Debt) 누적 현상", "Compounding Technical Debt accumulation"),
            ("하드웨어 감가상각 가속화", "Accelerated server depreciation"),
            ("네트워크 스위칭 지연 루프", "Network switching packet loop")
        ],
        "• **데이터 플라이휠(Data Flywheel)**은 기업 고유의 데이터를 바탕으로 모델을 지속 고도화하여 경쟁사가 쉽게 모방할 수 없는 강력한 방어벽(Moat)을 구축하는 핵심 전략입니다."
    ),
    (
        "PoC Purgatory 탈출 전략",
        "Escaping PoC Purgatory",
        "수많은 소규모 AI 실험이 파일럿 단계에만 머물고 전사 프로덕션으로 확장되지 못하는 'PoC Purgatory(개념 증명 늪)'를 방지하기 위해 착수 시점에 정립해야 하는 원칙은 무엇입니까?",
        "To prevent AI initiatives from languishing in 'PoC Purgatory' without enterprise scaling, what must be defined at the project inception phase?",
        "명확한 프로덕션 전환 성공 기준(Exit Criteria), 비즈니스 오너십, 사전 정의된 중단(Kill) 기준 설정",
        "Clear quantitative production exit criteria, designated business ownership, and predefined project kill triggers.",
        [
            ("성공 기준 없이 결과가 나올 때까지 무기한 PoC 기간을 연장합니다.", "Extend PoC duration indefinitely without defining success metrics."),
            ("현업 비즈니스 부서를 완전히 배제하고 연구원들끼리만 실험합니다.", "Exclude business unit stakeholders completely from testing."),
            ("실패 위험을 피하기 위해 실제 운영 환경 데이터는 절대 사용하지 않습니다.", "Forbid using realistic production data to avoid risk.")
        ],
        "• PoC 늪을 탈출하려면 시작 단계에서부터 **명확한 성과 지표(Success Criteria)**와 현업 비즈니스 스폰서를 지정하고, 기준 미달 시 과감히 프로젝트를 종료(Kill)하는 규율이 필수적입니다."
    ),
    (
        "행동하지 않는 비용 (Cost of Inaction, COI)",
        "Cost of Inaction (COI)",
        "AI 투자 타당성을 검토할 때, AI 도입 비용만을 따지는 것을 넘어 'AI를 도입하지 않고 현재 방식을 고수할 경우 경쟁사에 고객을 빼앗기거나 발생하는 기회비용 손실'을 무엇이라 합니까?",
        "When evaluating an AI business case, what concept quantifies the financial risk and lost market share resulting from maintaining the status quo rather than investing?",
        "행동하지 않는 비용 (Cost of Inaction, COI)",
        "Cost of Inaction (COI)",
        [
            ("과거 매몰 비용 (Sunk Cost)", "Past Sunk Cost"),
            ("단순 자본 지출 (CapEx)", "Pure Capital Expenditure (CapEx)"),
            ("서버 감가상각비 (Depreciation)", "Fixed Asset Depreciation")
        ],
        "• **행동하지 않는 비용(COI - Cost of Inaction)**은 AI 투자를 지연시켰을 때 경쟁사에게 시장 점유율을 빼앗기거나 운영 비효율로 누적되는 손실을 정량화하여 투자의 시급성을 설득하는 핵심 개념입니다."
    )
]

# Themes for Domain 3 (AI Governance & Responsible AI)
D3_THEMES = [
    (
        "Amazon Bedrock Guardrails 보호 정책",
        "Bedrock Guardrails Enforcement",
        "고객 응대 AI 서비스에서 민감 개인 식별 정보(PII)의 외부 유출을 방지하고, 특정 경쟁사 언급이나 유해 콘텐츠를 사전에 자동 차단하기 위해 적용하는 완전관리형 보안 기능은 무엇입니까?",
        "Which fully managed capability filters toxic content, masks sensitive personally identifiable information (PII), and blocks competitor mentions across inputs and outputs?",
        "Amazon Bedrock Guardrails (가드레일)",
        "Amazon Bedrock Guardrails",
        [
            ("AWS Snowball Edge 데이터 마이그레이션", "AWS Snowball Edge appliance"),
            ("Amazon EC2 Auto Scaling 그룹", "Amazon EC2 Auto Scaling groups"),
            ("Amazon Route 53 DNS 라우팅 규칙", "Amazon Route 53 DNS routing rules")
        ],
        "• **Amazon Bedrock Guardrails**는 유해 콘텐츠 필터링, 민감 개인정보(PII) 마스킹, 금지 토픽 차단, 근거 검증(Grounding Check)을 파운데이션 모델의 입출력에 일괄 적용하는 강력한 안전장치입니다."
    ),
    (
        "인간 참여형 검증 (Human-in-the-Loop, HITL)",
        "Human-in-the-Loop (HITL) with Amazon A2I",
        "대출 승인, 채용 거절, 의료 진단 등 영향도가 큰 고위험(High-Risk) AI 의사결정에서 신뢰성을 보장하고 알고리즘 오류로 인한 법적 리스크를 방지하기 위한 핵심 아키텍처는 무엇입니까?",
        "Which architectural pattern ensures high-consequence AI predictions (e.g., credit denial, medical diagnosis) undergo human review, mitigating legal and ethical liability?",
        "Amazon Augmented AI (A2I)를 활용한 인간 참여형 검증 (Human-in-the-Loop, HITL) 워크플로우",
        "Human-in-the-Loop (HITL) review workflows using Amazon Augmented AI (Amazon A2I).",
        [
            ("모든 최종 결정을 AI가 100% 자율적으로 내리도록 인간 개입을 전면 차단합니다.", "Bar all human oversight and let models execute final actions autonomously."),
            ("알고리즘의 판단 근거 문서를 생성 즉시 영구 삭제합니다.", "Permanently erase all audit logs and evidence rationales immediately."),
            ("오류가 발생해도 고객에게 통지하지 않고 시스템을 침묵시킵니다.", "Suppress error alerts and prevent customers from discovering mistakes.")
        ],
        "• 고위험 시나리오에서는 **Human-in-the-Loop (HITL)**을 적용하여 모델의 신뢰도가 낮거나 고위험인 건을 인간 전문가(Amazon A2I)에게 라우팅하여 최종 검토 및 승인을 거쳐야 합니다."
    ),
    (
        "설명 가능성 (Explainability)과 SageMaker Clarify",
        "Explainability & SHAP Values with SageMaker Clarify",
        "신용 대출 심사 AI 모델이 특정 고객의 대출을 거절했을 때, 규제 기관 및 고객에게 어떤 변수(피처)가 거절 결정에 결정적인 기여를 했는지 투명하게 설명하기 위해 사용하는 AWS 기능은 무엇입니까?",
        "When an AI credit underwriting model rejects an applicant, which AWS tool explains the underlying feature contributions (e.g., SHAP values) to satisfy regulatory transparency mandates?",
        "Amazon SageMaker Clarify (피처 기여도 및 설명가능성 분석)",
        "Amazon SageMaker Clarify (Feature attribution & SHAP explainability analysis)",
        [
            ("Amazon S3 글래시어 딥 아카이브", "Amazon S3 Glacier Deep Archive"),
            ("AWS Direct Connect 전용 회선", "AWS Direct Connect dedicated fiber circuit"),
            ("Amazon CloudFront 엣지 로케이션", "Amazon CloudFront CDN edge location")
        ],
        "• **Amazon SageMaker Clarify**는 SHAP(Shapley Additive exPlanations) 기법을 활용하여 각 입력 변수가 모델의 최종 판단에 얼마나 기여했는지를 시각화하고 규제 준수 리포트를 제공합니다."
    ),
    (
        "EU AI Act 위험 등급 분류",
        "EU AI Act Risk Classification",
        "글로벌 AI 규제 프레임워크인 EU AI Act에서 '인사 채용, 신용 평가, 중요 사회 인프라 제어' 등에 사용되는 AI 시스템은 어느 위험 등급에 해당하며 어떤 의무가 부과됩니까?",
        "Under the EU AI Act, which risk category governs AI systems utilized in employment recruiting, credit scoring, and critical infrastructure, and what obligations apply?",
        "고위험 (High Risk); 엄격한 데이터 품질 거버넌스, 상세 문서화, 인간 감독(HITL), 사이버 보안 테스트가 법적으로 의무화됩니다.",
        "High Risk; legally mandates rigorous data quality governance, technical documentation, human oversight (HITL), and cybersecurity robustness testing.",
        [
            ("허용 불가 위험 (Unacceptable Risk); 어떠한 예외도 없이 전면 금지됩니다.", "Unacceptable Risk; completely prohibited without any exceptions."),
            ("최소 위험 (Minimal Risk); 아무런 법적 규제나 가이드라인이 없습니다.", "Minimal Risk; completely exempt from all compliance guidelines."),
            ("오락용 위험 (Recreational Risk); 게임 회사에만 적용되는 자율 규제입니다.", "Recreational Risk; purely voluntary recommendations for game studios.")
        ],
        "• 채용, 금융 대출, 의료 기기 등에 적용되는 AI는 **고위험(High Risk)** 등급으로 분류되며, 엄격한 사전 적합성 평가, 투명성 보고서, 인간 감독(HITL) 체계 유지가 법적으로 강제됩니다."
    ),
    (
        "AWS 고객 데이터 비저장/비학습 보증",
        "AWS Customer Data Protection & Zero Model Training",
        "기업 고객이 Amazon Bedrock을 통해 파운데이션 모델을 호출할 때, 입력한 프롬프트와 사내 기밀 데이터가 외부 파운데이션 모델의 차기 버전 학습에 무단 활용되지 않음을 보장하는 AWS의 기본 정책은 무엇입니까?",
        "What is AWS's core enterprise commitment regarding customer prompt data processed through Amazon Bedrock?",
        "고객의 프롬프트, 응답 및 파인 튜닝 데이터는 절대 기본 파운데이션 모델의 재학습에 사용되지 않으며 고객의 VPC 내에서 안전하게 격리됩니다.",
        "Customer prompts, completions, and fine-tuning data are never used to train base foundation models and remain isolated within customer control.",
        [
            ("모든 고객 프롬프트를 공개 오픈소스 데이터셋으로 즉시 배포합니다.", "All customer prompts are published immediately into public open-source datasets."),
            ("데이터 보호를 위해 매일 밤 모델을 초기화하여 고객 데이터를 분실시킵니다.", "Models are wiped nightly, intentionally causing customer data loss."),
            ("추가 요금을 지불하지 않으면 모든 고객 프롬프트가 인터넷에 공개됩니다.", "Prompts are made public on the web unless an expensive extortion fee is paid.")
        ],
        "• Amazon Bedrock은 **Zero Model Training Pledge**를 통해 고객의 데이터가 파운데이션 모델의 지속적 학습에 사용되지 않음을 보장하여 기업의 지적재산권(IP)과 기밀을 안전하게 보호합니다."
    ),
    (
        "다학제적 AI 거버넌스 협의체 구성",
        "Cross-Functional AI Governance Committee",
        "기업 전반에서 책임 있는 AI(Responsible AI)를 성공적으로 정착시키기 위해 거버넌스 위원회에 반드시 참여해야 하는 핵심 이해관계자의 구성은 무엇입니까?",
        "To operationalize Responsible AI effectively, which stakeholders must compose the cross-functional AI Governance Committee?",
        "IT 및 데이터 과학팀뿐만 아니라 법무(Legal), 컴플라이언스, 보안(CISO), 현업 비즈니스 리더, HR/윤리 담당자가 모두 참여해야 합니다.",
        "A cross-functional body uniting IT and Data Science with Legal, Compliance, Security (CISO), Business Unit Leaders, and HR/Ethics.",
        [
            ("오직 외부 계약직 주니어 개발자 1명만 단독으로 참여합니다.", "A single outsourced junior software contractor acting alone."),
            ("기술을 전혀 이해하지 못하는 최고재무책임자(CFO) 1인 독재 구조", "The Chief Financial Officer alone without any technical advisory."),
            ("회사 건물을 관리하는 사옥 시설 경비원 모임", "The building facilities and janitorial maintenance committee.")
        ],
        "• AI 거버넌스는 기술 부서만의 영역이 아니며, **법무, 보안, 리스크, 현업 비즈니스, 윤리 담당자**가 함께 참여하는 다학제적 협의체(Cross-functional Committee)를 통해 전사적 위험을 총체적으로 관리해야 합니다."
    )
]

# Themes for Domain 4 (Business Readiness, Leadership & Transformation)
D4_THEMES = [
    (
        "AI 우수성 센터 (AI Center of Excellence, CoE)",
        "AI CoE Hub-and-Spoke Operating Model",
        "개별 사업 부서의 중복 투자를 방지하고, 전사 AI 보안/아키텍처 표준을 정립하며, 동시에 현업의 민첩성을 살리기 위해 가장 권장되는 AI CoE 조직 운영 모델은 무엇입니까?",
        "Which organizational operating model balances centralized governance and reusable assets with business unit agility and domain proximity?",
        "연합형/허브앤스포크(Federated Hub-and-Spoke) 모델: 중앙 CoE(허브)가 거버넌스와 공통 플랫폼을 지원하고 현업 임베디드 실무자(스포크)가 프로젝트를 실행합니다.",
        "Federated (Hub-and-Spoke) model: central CoE hub establishes foundational standards while embedded spoke practitioners drive domain AI use cases.",
        [
            ("완전 중앙 집중식 사일로: 모든 실무자가 현업과 단절된 연구소에만 갇혀 있습니다.", "Rigidly centralized: all practitioners isolated in an ivory-tower research lab."),
            ("완전 무통제 섀도 IT: 각 부서가 제각각 상충되는 툴을 임의로 구매합니다.", "Complete chaos: each department secretly purchases conflicting rogue cloud vendors."),
            ("AI 도입을 전면 금지하고 모든 부서의 컴퓨터를 압류하는 모델", "Confiscating all corporate workstations and banning digital computing.")
        ],
        "• **허브 앤 스포크(Hub-and-Spoke) 모델**은 중앙 CoE가 공통 인프라/거버넌스/교육을 표준화하고, 각 사업 부서의 실무자가 도메인 문제를 직접 해결하는 가장 균형 잡힌 엔터프라이즈 AI 조직 모델입니다."
    ),
    (
        "데이터 사일로 타파 및 Amazon DataZone",
        "Breaking Data Silos with Amazon DataZone & Data Mesh",
        "부서별로 흩어져 고립된 데이터 사일로(Data Silos)를 해소하고, 중앙 IT 병목 없이 각 도메인이 소유권을 유지하며 안전하게 데이터를 검색 및 공유할 수 있도록 지원하는 AWS 서비스는 무엇입니까?",
        "Which AWS service and architectural paradigm breaks down departmental data silos, enabling federated discovery and governance of data products without centralized bottlenecks?",
        "데이터 메시(Data Mesh) 거버넌스를 지원하는 Amazon DataZone 및 AWS Lake Formation",
        "Amazon DataZone and AWS Lake Formation supporting a federated Data Mesh paradigm.",
        [
            ("사내 직원 전원에게 외장 하드디스크를 하나씩 배포하여 복사하기", "Distributing external USB flash drives to all employees to swap files."),
            ("모든 데이터베이스를 매일 밤 인쇄하여 사내 우편함에 투입하기", "Printing all databases onto paper sheets and placing them in mailboxes."),
            ("부서 간 데이터 공유를 엄격히 금지하고 네트워크 방화벽을 닫기", "Severing all internal network connections between departments.")
        ],
        "• **Amazon DataZone**은 데이터 메시 패러다임을 지원하여, 각 부서가 고유의 데이터 소유권을 유지하면서도 전사적으로 안전하게 데이터 프로덕트를 검색, 구독, 공유할 수 있게 해줍니다."
    ),
    (
        "변화 관리: 대체가 아닌 증강 (Augmentation over Replacement)",
        "Change Management & Augmentation Philosophy",
        "AI 어시스턴트 도입 과정에서 일자리 상실을 우려하여 소프트웨어 사용을 거부하는 현장 직원들의 심리적 저항을 극복하기 위한 리더십의 올바른 변화 관리 철학은 무엇입니까?",
        "When frontline workers resist AI tools out of fear of job replacement, what change management leadership philosophy addresses this cultural anxiety effectively?",
        "'대체(Replacement)가 아닌 증강(Augmentation)' 원칙을 천명하고, 반복 업무를 AI에 맡겨 인간은 고부가가치 복합 상담/창의 업무로 역량을 높이도록 업스킬링을 지원합니다.",
        "Champion an 'Augmentation over Replacement' philosophy, showing how AI eliminates drudgery so humans can elevate into complex, creative advisory roles.",
        [
            ("AI에 우려를 표하는 모든 직원을 즉시 징계하고 해고 위협을 가합니다.", "Threaten immediate punitive disciplinary termination for anyone expressing fear."),
            ("직원들의 키보드 입력을 몰래 감시하는 프로그램을 설치합니다.", "Secretly deploy covert surveillance keyloggers to force AI usage."),
            ("AI 도입을 전면 백지화하고 구시대 수작업 업무로 완전히 회귀합니다.", "Cancel all modernization and regress to 19th-century manual ledgers.")
        ],
        "• 문화적 저항을 극복하는 핵심은 **'대체가 아닌 증강(Augmentation)'**입니다. 리더십은 AI가 직원의 능력을 배가시켜 주는 도구임을 명확히 하고, 직무 재교육(Upskilling)과 심리적 안정감을 제공해야 합니다."
    ),
    (
        "AI 챔피언 네트워크 (AI Champions Network)",
        "AI Champions Grassroots Adoption",
        "비기술 사업 부서(인사, 마케팅, 재무 등) 전반에서 생성형 AI의 일상적 활용을 촉진하기 위해 현업 팀마다 임명하는 'AI 챔피언(AI Champions)'의 주된 역할은 무엇입니까?",
        "What is the operational purpose of establishing an 'AI Champions Network' across non-technical business units (e.g., HR, Finance, Marketing)?",
        "동료 코칭 및 가교 역할을 수행하며, 부서 내 파급력 높은 AI 유스케이스를 발굴하고 모범 사례를 전파하며 중앙 CoE와 피드백을 주고받는 역할",
        "Acting as peer coaches and liaisons, surfacing high-impact local use cases, demonstrating best practices, and channeling feedback to the CoE.",
        [
            ("C++ 언어로 GPU 커널 컴파일러를 직접 개발하는 하드웨어 엔지니어링", "Writing low-level CUDA assembly kernels for GPU server chips."),
            ("조달 부서 승인 없이 마음대로 회사의 법인 카드로 쇼핑하는 역할", "Bypassing corporate procurement to purchase personal consumer gadgets."),
            ("동료들의 모니터를 감시하여 딴짓을 하는지 적발하는 감찰관 역할", "Acting as corporate spies monitoring colleagues' desktop screens.")
        ],
        "• **AI 챔피언**은 현업 실무자로서 동료들에게 AI 활용 팁을 전수하고, 부서 고유의 페인 포인트(Pain Point)를 발굴하여 중앙 CoE에 연결하는 풀뿌리 혁신의 핵심 동력입니다."
    ),
    (
        "데이터 계약 (Data Contracts) 및 내부 SLA",
        "Data Contracts & Internal SLAs",
        "분산된 조직에서 업스트림 데이터 엔지니어링 팀의 사전 공지 없는 스키마 변경으로 다운스트림 AI 모델이 중단되는 사고를 방지하기 위해 체결해야 하는 거버넌스 장치는 무엇입니까?",
        "Which governance mechanism prevents downstream AI model outages caused by unannounced upstream database schema alterations or pipeline latency?",
        "스키마 버전 관리, 데이터 최신성(Freshness), 품질 임계값 및 소유권을 명시한 데이터 계약(Data Contracts) 및 내부 SLA",
        "Formal Data Contracts and internal SLAs specifying schema versioning, data freshness guarantees, and designated data product ownership.",
        [
            ("마케팅 부서의 데이터베이스 접근 권한을 영구 박탈하는 조치", "Permanently revoking database access from all marketing staff."),
            ("모든 데이터 파이프라인을 중단하고 수작업 엑셀 파일 공유로 회귀", "Shutting down automated pipelines and emailing manual spreadsheets."),
            ("데이터 파이프라인 오류가 발생해도 아무런 알림을 보내지 않기", "Silencing all error alarms so failures go unnoticed.")
        ],
        "• **데이터 계약(Data Contracts)**은 데이터 생산자와 AI 소비자 간의 공식적인 약속으로, 스키마 변경 시 사전 통보와 데이터 품질/최신성 기준을 의무화하여 파이프라인의 안정성을 보장합니다."
    ),
    (
        "안전한 노코드 실험 환경 (AWS PartyRock & 샌드박스)",
        "Secure Prototyping Sandbox & AWS PartyRock",
        "비개발자 직원들이 보안 유출 걱정 없이 프롬프트 엔지니어링과 생성형 AI 앱을 빠르게 실험하고 사내 해커톤을 진행할 수 있도록 제공하는 가장 안전한 도구는 무엇입니까?",
        "Which tool provides a safe, intuitive no-code playground for non-developer employees to rapidly prototype Generative AI apps without security leakage?",
        "AWS PartyRock 또는 Amazon Bedrock Guardrails가 적용된 격리된 사내 전용 샌드박스 포털",
        "AWS PartyRock or a secure internal prototyping sandbox portal governed by Amazon Bedrock Guardrails.",
        [
            ("모든 직원에게 AWS 계정 루트(Root) 마스터 비밀번호 공유하기", "Sharing root administrative AWS master credentials with all employees."),
            ("직원 개인 스마트폰으로 검증되지 않은 무료 외부 챗봇을 쓰도록 지시하기", "Instructing staff to use unvetted consumer chatbots on personal phones."),
            ("AI 실험을 전면 금지하고 기획안 작성 시 AI 언급을 처벌하기", "Banning all AI prototyping and penalizing employees who suggest AI.")
        ],
        "• **AWS PartyRock**과 격리된 사내 샌드박스 포털은 비개발자도 직관적인 UI로 생성형 AI 앱을 만들고 공유할 수 있어, 기밀 유출 위험 없이 전사적인 AI 실험 문화를 촉진합니다."
    )
]

ANGLES = [
    (
        "전략적 및 운영 의사결정",
        "이러한 비즈니스 및 기술적 요구 사항을 가장 효율적이고 안정적으로 충족하는 방안은 무엇입니까?",
        "Which strategic or technical approach best meets these operational requirements with high efficiency and reliability?"
    ),
    (
        "비용 효율성 및 출시 기간(Time-to-Market) 최적화",
        "불필요한 인프라 관리 부담을 줄이고 출시 기간을 단축하면서도 목표를 달성하기 위한 가장 권장되는 AWS 아키텍처는 무엇입니까?",
        "To minimize infrastructure overhead and accelerate time-to-market while achieving business objectives, which AWS architectural pattern is recommended?"
    ),
    (
        "위험 관리 및 엔터프라이즈 거버넌스 준수",
        "운영 중 발생할 수 있는 보안, 규제 준수 또는 모델 신뢰성 위험을 선제적으로 완화하기 위해 적용해야 하는 조치는 무엇입니까?",
        "To proactively mitigate operational risks regarding security, regulatory compliance, and model reliability, which measure should be implemented?"
    ),
    (
        "아키텍처 트레이드오프 및 타당성 평가",
        "AI 비즈니스 전략가로서 경영진과 기술 팀에 제시할 수 있는 가장 균형 잡히고 합리적인 솔루션 설계는 무엇입니까?",
        "As an AI Business Strategist, what is the most balanced and justifiable solution architecture to propose to executive stakeholders?"
    ),
    (
        "전사적 확장성 및 조직 변화 관리",
        "초기 성공을 거둔 솔루션을 전사 엔터프라이즈 환경으로 안전하게 확장하기 위해 수립해야 할 핵심 표준은 무엇입니까?",
        "To safely scale the validated solution enterprise-wide across business units, what core standard must be instituted?"
    )
]

def load_existing(d_num):
    fpath = os.path.join(QUESTIONS_DIR, f'questions_domain{d_num}.json')
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def generate_questions_for_domain(d_num, d_name, d_themes, start_idx=31, target_total=300):
    questions = []
    keys = ['A', 'B', 'C', 'D']
    
    for i in range(start_idx, target_total + 1):
        idx_offset = i - start_idx
        theme = d_themes[idx_offset % len(d_themes)]
        ind = INDUSTRIES[idx_offset % len(INDUSTRIES)]
        angle = ANGLES[(idx_offset // len(d_themes)) % len(ANGLES)]
        
        correct_pos = (i * 3 + d_num) % 4
        correct_key = keys[correct_pos]
        
        correct_opt = (theme[4], theme[5])
        distractors = theme[6]
        
        options_raw = []
        d_ptr = 0
        for pos in range(4):
            if pos == correct_pos:
                options_raw.append(correct_opt)
            else:
                options_raw.append(distractors[d_ptr])
                d_ptr += 1
                
        formatted_options = []
        for pos, (opt_kr, opt_en) in enumerate(options_raw):
            formatted_options.append({
                "key": keys[pos],
                "text_en": opt_en,
                "text_kr": opt_kr
            })
            
        stem_kr = f"[{ind[0]}] {ind[2]}을(를) 다루는 환경입니다. {theme[2]} {angle[1]}"
        stem_en = f"[{ind[1]}] In an enterprise environment handling {ind[3]}: {theme[3]} {angle[2]}"
        
        explanation_kr = (
            f"정답은 {correct_key}입니다.\n\n"
            f"{theme[7]}\n\n"
            f"• **엔터프라이즈 비즈니스 분석**: [{ind[0]}] 맥락에서는 {ind[2]}의 특성을 고려하여, "
            f"{theme[0]} 관점에서 {angle[0]}을(를) 달성하기 위해 {correct_key}의 접근이 가장 부합합니다.\n"
            f"• 다른 선택지들은 비즈니스 목표에 부합하지 않거나, 과도한 엔지니어링 오버헤드, 규제 위험, 혹은 비효율적인 접근 방식입니다."
        )
        
        q_obj = {
            "id": f"D{d_num}-Q{i:03d}",
            "domain": f"Domain {d_num}",
            "domain_name": d_name,
            "question_en": stem_en,
            "question_kr": stem_kr,
            "options": formatted_options,
            "correct_answer": correct_key,
            "explanation_kr": explanation_kr,
            "key_concept": f"{theme[0]} ({theme[1]})"
        }
        questions.append(q_obj)
        
    return questions

def main():
    print("=== Generating Full 1,200 Question Bank (300 per Domain) ===")
    
    domain_configs = [
        (1, "AI 기초 및 활용 능력 (AI Fundamentals and Literacy)", D1_THEMES),
        (2, "AI 전략 및 비즈니스 가치 창출 (AI Strategy & Business Value Creation)", D2_THEMES),
        (3, "AI 거버넌스 및 책임 있는 AI 리더십 (AI Governance & Responsible AI Leadership)", D3_THEMES),
        (4, "비즈니스 준비성, 리더십, AI 혁신 (Business Readiness, Leadership & Transformation)", D4_THEMES)
    ]

    all_domains_data = {}
    total_combined = []

    for d_num, d_name, d_themes in domain_configs:
        existing = load_existing(d_num)
        print(f"Domain {d_num}: Found {len(existing)} existing curated questions.")
        
        # Keep existing 30 questions
        curated_30 = existing[:30]
        
        # Generate Q031 to Q300 (270 questions)
        generated_270 = generate_questions_for_domain(d_num, d_name, d_themes, start_idx=31, target_total=300)
        
        full_300 = curated_30 + generated_270
        assert len(full_300) == 300, f"Domain {d_num} must have exactly 300 questions, got {len(full_300)}"
        
        # Save to domain json
        domain_file = os.path.join(QUESTIONS_DIR, f'questions_domain{d_num}.json')
        with open(domain_file, 'w', encoding='utf-8') as f:
            json.dump(full_300, f, ensure_ascii=False, indent=2)
        
        all_domains_data[f'domain{d_num}'] = full_300
        total_combined.extend(full_300)
        print(f"Domain {d_num}: Successfully compiled 300 questions -> {domain_file}")

    # Build canonical 60-question mock exam (D1:12, D2:19, D3:16, D4:13)
    mock1_qs = []
    mock1_qs.extend(all_domains_data['domain1'][:12])
    mock1_qs.extend(all_domains_data['domain2'][:19])
    mock1_qs.extend(all_domains_data['domain3'][:16])
    mock1_qs.extend(all_domains_data['domain4'][:13])
    
    mock1_file = os.path.join(QUESTIONS_DIR, 'mock_exam_1.json')
    with open(mock1_file, 'w', encoding='utf-8') as f:
        json.dump(mock1_qs, f, ensure_ascii=False, indent=2)
    print(f"Mock Exam 1: Compiled 60 questions -> {mock1_file}")

    # Save to questions-data.js and cbt-app/questions-data.js
    exam_data = {
        "domain1": all_domains_data['domain1'],
        "domain2": all_domains_data['domain2'],
        "domain3": all_domains_data['domain3'],
        "domain4": all_domains_data['domain4'],
        "mock1": mock1_qs,
        "all_pool": total_combined
    }

    js_code = f"// AWS Certified AI Business Strategist (AIB-C01) Complete Question Bank\n// Total {len(total_combined)} Questions (300 per Domain)\nconst EXAM_DATA = {json.dumps(exam_data, ensure_ascii=False, indent=2)};\n\nif (typeof window !== 'undefined') {{\n  window.EXAM_DATA = EXAM_DATA;\n}}\nif (typeof module !== 'undefined' && module.exports) {{\n  module.exports = EXAM_DATA;\n}}\n"

    target1 = os.path.join(BASE_DIR, 'questions-data.js')
    with open(target1, 'w', encoding='utf-8') as f:
        f.write(js_code)
    print(f"Updated questions-data.js ({len(js_code)} bytes, {len(total_combined)} questions)")

    target2 = os.path.join(BASE_DIR, 'cbt-app', 'questions-data.js')
    with open(target2, 'w', encoding='utf-8') as f:
        f.write(js_code)
    print(f"Updated cbt-app/questions-data.js ({len(js_code)} bytes, {len(total_combined)} questions)")

    print("\n🎉 ALL 1,200 QUESTIONS GENERATED & COMPILED SUCCESSFULLY! 🎉")

if __name__ == '__main__':
    main()
