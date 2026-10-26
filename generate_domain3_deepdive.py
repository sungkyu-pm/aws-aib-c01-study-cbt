# Domain 3 Deep Dive Content Generator (AI Governance & Responsible AI Leadership - 27%)
# Covers all 30 Categories

def get_domain3_markdown():
    return """# 도메인 3: AI 거버넌스 및 책임 있는 AI 리더십 (AI Governance & Responsible AI)

> **출제 비중 (Exam Weight)**: **27% (핵심 고배점 영역!)**  
> **공식 시험 평가 목표 (Exam Objective)**: 책임 있는 AI(공정성, 설명가능성, 프라이버시, 투명성, 안전성) 프레임워크를 수립하고, 편향 완화 및 PII 보호 정책을 구현하며, Amazon Bedrock Guardrails와 Human-in-the-Loop(HITL) 체계를 구축하고, EU AI Act 및 글로벌 규제 준수 거버넌스를 지휘할 수 있는가?

---

## 📌 도메인 3 출제 로드맵 및 30대 핵심 토픽 한눈에 보기
비즈니스 리더십 관점에서 기업의 법적 리스크와 브랜드 평판을 보호하는 핵심 거버넌스 영역입니다.

* **제1장: 책임 있는 AI 6대 핵심 원칙과 알고리즘 공정성** (Cat 1~4)
* **제2장: 설명 가능성(XAI)과 데이터 프라이버시 보호** (Cat 5~10)
* **제3장: 투명성 고지 및 안전성 운영 메커니즘** (Cat 11~13)
* **제4장: Amazon Bedrock Guardrails 심층 거버넌스** (Cat 14~16, 28)
* **제5장: Human-in-the-Loop(HITL) 및 고위험 의사결정 에스컬레이션** (Cat 17~19)
* **제6장: 글로벌 AI 규제 법제 및 전사 거버넌스 조직** (Cat 20~27, 29~30)

---

## 제1장: 책임 있는 AI 6대 핵심 원칙과 알고리즘 공정성 (RAI Pillars & Fairness)

### 3.1 책임 있는 AI (Responsible AI / RAI) 6대 핵심 기둥
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **6 Foundational Pillars of Responsible AI**:
  1. *Fairness*: Systems treat all demographics equitably without systematic bias.
  2. *Explainability & Interpretability*: Communicating decision rationale clearly to auditors and users.
  3. *Privacy & Security*: Safeguarding confidential IP and customer personal data.
  4. *Transparency*: Disclosing AI capabilities, limitations, and operational boundaries.
  5. *Controllability & Safety*: Enforcing guardrails, fallback kill-switches, and error containment.
  6. *Veracity & Grounding*: Minimizing hallucinations and anchoring assertions strictly to factual sources.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 책임 있는 AI는 단순한 윤리 선언이 아닌, 기업의 법적 책임 회피와 고객 신뢰 유지를 위한 **전사적 운영 프레임워크**입니다. 6대 기둥(공정성, 설명가능성, 프라이버시, 투명성, 안전성, 사실성)은 모든 거버넌스 설계의 출발점입니다.

</div>
</div>

---

### 3.2 알고리즘 편향 완화 (Algorithmic Bias Mitigation)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Algorithmic Bias**: Systematically skewed outcomes disfavoring legally protected groups (race, gender, age, disability) in automated credit scoring, talent recruitment, or insurance underwriting. Addressed via representative dataset re-balancing and algorithmic auditing tools like **Amazon SageMaker Clarify**.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* AI 모델이 특정 성별이나 인종에 대해 불리한 예측 결과를 내놓는 현상으로, 심각한 소송과 규제 처벌을 초래합니다. 데이터 수집 단계부터 대표성을 검증하고 **Amazon SageMaker Clarify**를 통해 지속적으로 편향을 완화해야 합니다.

</div>
</div>

---

### 3.3 인구통계학적 동등성 및 공정성 지표 (Demographic Parity)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Demographic Parity**: Mathematical fairness standard stipulating that the acceptance or approval rate of an algorithm should be statistically identical across all protected sub-populations, regardless of sensitive group membership.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 알고리즘의 공정성을 수학적으로 검증하는 대표적 정량 지표입니다. (예: 남성과 여성 지원자 간의 서류 합격률 비율이 동등해야 함)

</div>
</div>

---

### 3.4 과거 데이터 편향 (Historical Bias in Training Data)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Historical Bias**: Inequities already embedded in historical human decision records that machine learning models inadvertently memorize and perpetuate as ground truth if uncorrected (e.g., past 10 years of male-dominated tech hiring records).

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* "과거 데이터는 거짓말을 하지 않는다"는 착각에서 비롯되는 문제입니다. 과거 사회적 차별 관행이 데이터에 반영되어 있다면, AI는 이를 학습하여 미래에도 차별을 고착화합니다. 데이터 큐레이션 시 과거 편향 보정이 필수적입니다.

</div>
</div>

---

## 제2장: 설명 가능성(XAI)과 데이터 프라이버시 보호 (Explainability & Privacy)

### 3.5 설명 가능성 및 해석 가능성 (Explainability & Interpretability)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Explainability (XAI)**: The technical and communicative capability to articulate *why* an AI system rendered a specific decision in terms comprehensible to lay human users and regulatory compliance auditors (e.g., explaining why a loan application was rejected).

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 블랙박스 딥러닝 모델의 판단 근거를 사람이 이해할 수 있는 언어로 설명하는 역량입니다. 금융 대출 거절 통보, 의료 진단 등 고위험 의사결정에서 법적 의무 사항입니다.

</div>
</div>

---

### 3.6 SHAP 기여도 값 분석 (SHAP Values & Feature Attribution)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **SHAP (SHapley Additive exPlanations)**: Game-theoretic mathematical framework quantifying the exact marginal contribution of each input feature (e.g., debt-to-income ratio, credit history length) to the terminal model prediction score.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 각 입력 변수(소득, 부채 비율 등)가 최종 대출 승인/거절 결정에 얼마나 기여했는지를 수학적으로 정량화하여 규제 당국에 증명하는 업계 표준 설명 기법입니다.

</div>
</div>

---

### 3.7 Amazon SageMaker Clarify 편향 및 설명 감사
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Amazon SageMaker Clarify**: Fully managed AWS service that detects bias across datasets and trained models, computes SHAP feature attributions, and automatically generates compliance-ready transparency reports for external audits.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 머신러닝 데이터셋과 모델의 편향을 탐지하고 SHAP 기반의 설명 보고서를 자동으로 만들어주는 AWS의 핵심 거버넌스 서비스입니다. **공정성 검증 및 규제 보고서 작성의 1순위 정답**입니다.

</div>
</div>

---

### 3.8 개인 식별 정보 (PII) 보호 및 법적 준수
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Personally Identifiable Information (PII)**: Sensitive consumer data (SSNs, credit card numbers, home addresses, biometric records) governed by GDPR, CCPA, and HIPAA. Ingesting raw PII into foundation models creates severe regulatory liability.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 주민등록번호, 카드 번호 등 개인을 식별할 수 있는 모든 민감 정보는 모델에 주입되기 전에 반드시 마스킹되거나 차단되어야 합니다.

</div>
</div>

---

### 3.9 PII 마스킹 및 비식별화 (PII Redaction via Guardrails)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Automated Redaction**: Configuring **Amazon Bedrock Guardrails Sensitive Information Filters** to automatically detect and redact or block PII entities across prompts and completions in real time.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 개발자가 정규식을 일일이 코딩하지 않고, **Amazon Bedrock Guardrails**의 민감 정보 필터를 활성화하여 주민번호나 카드번호를 자동으로 `[REDACTED]` 처리하는 것이 가장 안전한 표준 아키텍처입니다.

</div>
</div>

---

### 3.10 AWS 고객 데이터 보호 서약 (AWS Data Privacy Pledge)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **AWS Zero-Data Retention & Privacy Guarantee**: Contractual promise that customer prompts, inputs, and knowledge bases processed via Amazon Bedrock or Amazon Q **are NEVER used to train base AWS foundation models** or shared across tenants.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 고객이 입력한 프롬프트와 사내 기밀 문서는 **절대 AWS의 파운데이션 모델 학습에 사용되지 않는다**는 공식 보안 서약입니다. 보안팀을 안심시키는 결정적 근거입니다.

</div>
</div>

---

## 제3장: 투명성 고지 및 안전성 운영 메커니즘 (Transparency & Operational Safety)

### 3.11 투명성 및 AI 사용 고지 의무 (Transparency & Mandatory Disclosure)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Mandatory AI Disclosure**: Ethical and legal requirement to explicitly inform human users when they are interacting with an artificial intelligence system (e.g., customer service chatbots), communicating its scope, capabilities, and limitations.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 고객이 대화하고 있는 상대가 사람이 아닌 AI임을 투명하게 밝히고 시스템의 한계를 사전에 고지해야 합니다. (EU AI Act 등 글로벌 법제에서 필수 요구 사항)

</div>
</div>

---

### 3.12 합성 미디어 디지털 워터마킹 (Synthetic Media Watermarking)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Cryptographic Watermarking (e.g., C2PA Standard, Amazon Titan Image Generator)**: Embedding invisible, tamper-evident cryptographic metadata into AI-generated images and media to verify provenance and counteract deepfakes.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* AI가 생성한 이미지나 영상에 육안으로는 보이지 않는 암호화된 메타데이터를 삽입하여 출처를 증명하고 가짜 뉴스/딥페이크 악용을 방지합니다.

</div>
</div>

---

### 3.13 비상 정지 메커니즘 (Kill-Switch Circuit Breakers)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Kill-Switch Architecture**: Automated architectural circuit breakers capable of instantaneously halting AI model inference endpoints and reverting to fallback rule-based or human workflows during catastrophic failures or security breaches.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 모델이 심각한 환각을 일으키거나 공격을 받았을 때, **한 번의 클릭이나 자동화 트리거로 즉시 AI 추론 트래픽을 차단하고 기존 업무 체계로 롤백**할 수 있는 긴급 차단 장치입니다.

</div>
</div>

---

## 제4장: Amazon Bedrock Guardrails 심층 거버넌스 (Guardrails Deep Dive)

### 3.14 Amazon Bedrock Guardrails 포괄적 거버넌스 정책
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Amazon Bedrock Guardrails**: Fully managed, model-agnostic governance filter that standardizes corporate safety policies across all foundation models (Claude, Llama, Titan). Centrally manages Denied Topics, Content Filters, Sensitive Information Redaction, and Contextual Grounding.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 모델 종류에 종속되지 않고 애플리케이션 전체에 일괄 적용되는 완전관리형 보안 가드입니다. 금지 주제, 유해 콘텐츠, PII 마스킹, 근거 검사를 한곳에서 중앙 제어합니다.

</div>
</div>

---

### 3.15 금지된 주제 필터링 (Denied Topics Filtering)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Denied Topics**: Natural language policy definitions prohibiting models from entertaining unauthorized discussions (e.g., giving financial investment advice, providing medical diagnoses, comparing corporate competitors).

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 기업 정책상 AI가 절대 답변해서는 안 되는 민감한 주제(비공식 법률/세무 상담, 경쟁사 제품 비교)를 자연어 규칙으로 지정하여 원천 차단하는 기능입니다.

</div>
</div>

---

### 3.16 근거 기반 검증 (Contextual Grounding Check)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Contextual Grounding Check**: Bedrock Guardrails feature evaluating whether generated answers are strictly grounded in retrieved reference documentation and filtering out ungrounded factual hallucinations before responses reach users.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* RAG 환경에서 모델이 생성한 답변이 검색된 사내 문서에 실제로 존재하는지 수학적으로 대조 검증하여, 근거 없는 거짓 답변(환각)을 사용자에게 전달되기 전에 자동 차단합니다.

</div>
</div>

---

## 제5장: Human-in-the-Loop(HITL) 및 고위험 의사결정 에스컬레이션 (HITL & A2I)

### 3.17 계층적 인간 참여형 검증 (Human-in-the-Loop / HITL)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **HITL Architecture**: Mandatory operational pattern routing low-confidence model predictions or high-consequence business decisions (credit rejections, cancer screenings, employment candidate disqualifications) to qualified human experts for final binding approval.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* AI가 100% 자율 결정하게 두지 않고, 모델의 확신도(Confidence)가 낮거나 법적/재무적 리스크가 매우 큰 고위험 결정에는 **반드시 인간 전문가의 최종 승인을 거치도록 설계하는 필수 아키텍처**입니다.

</div>
</div>

---

### 3.18 완전관리형 검토 워크플로우: Amazon Augmented AI (Amazon A2I)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Amazon Augmented AI (Amazon A2I)**: AWS service automating human review workflows. Seamlessly routes inference results from Amazon Textract, Rekognition, or custom SageMaker models to internal employees or external workforce pools when confidence drops below defined thresholds.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 신뢰도가 기준치 미만인 모델 예측 결과를 사람이 직접 검토하고 수정할 수 있도록 검토 인터페이스와 작업자 라우팅을 자동화하는 AWS 완전관리형 서비스입니다.

</div>
</div>

---

### 3.19 고영향 자동화 의사결정 에스컬레이션 (High-Consequence Escalation)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Automated Escalation Protocol**: Enterprise rule dictating that adverse decisions impacting an individual's legal rights, livelihood, or health must never be rendered solely by an algorithm without human oversight and appeal mechanisms.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 개인의 권리나 생계에 중대한 영향을 미치는 결정(대출 부적격, 채용 탈락)은 결코 AI 단독으로 확정해서는 안 되며, 이의 신청 및 인간 재심 절차가 반드시 마련되어야 합니다.

</div>
</div>

---

## 제6장: 글로벌 AI 규제 법제 및 전사 거버넌스 조직 (Global Regulations & Oversight)

### 3.20 EU AI Act 4대 위험 등급 (EU AI Act Four Risk Tiers)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **EU AI Act Risk Classification**:
  1. *Unacceptable Risk (Banned)*: Social scoring, cognitive behavioral manipulation, real-time public biometric surveillance.
  2. *High Risk (Strictly Regulated)*: Critical infrastructure, medical devices, recruitment, credit scoring. Requires mandatory risk management, high-quality data governance, and HITL.
  3. *Limited Risk*: Transparency obligations (chatbots, deepfakes).
  4. *Minimal Risk*: Unregulated (spam filters, AI video games).

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 글로벌 비즈니스를 영위하는 기업의 핵심 준수 표준입니다. 위험 크기에 따라 차등 규제하며, 채용 및 신용 평가는 **고위험(High Risk)**으로 분류되어 엄격한 감사와 인간 감독(HITL)이 법적으로 강제됩니다.

</div>
</div>

---

### 3.21 ISO/IEC 42001 인공지능 경영시스템 (AI Management System)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **ISO/IEC 42001**: The premier certifiable international standard establishing requirements for an enterprise Artificial Intelligence Management System (AIMS), demonstrating structured governance across the AI lifecycle.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 조직이 책임감 있게 AI를 개발, 도입, 운영하고 있음을 공인하는 최초의 글로벌 AI 국제 표준 인증입니다.

</div>
</div>

---

### 3.22 NIST AI 위험 관리 프레임워크 (NIST AI RMF)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **NIST AI Risk Management Framework (AI RMF)**: Structured framework built upon four core functions: **GOVERN, MAP, MEASURE, and MANAGE** to cultivate trustworthy, safe AI systems.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 미국 국립표준기술원(NIST)의 신뢰할 수 있는 AI 구축 가이드라인으로, GOVERN(거버넌스) ➔ MAP(매핑) ➔ MEASURE(측정) ➔ MANAGE(관리)의 4단계 프레임워크를 제공합니다.

</div>
</div>

---

### 3.23 다학제적 전사 거버넌스 협의체 (Cross-Functional Governance Council)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Cross-Functional Governance Council**: Executive oversight committee uniting Legal, Compliance, IT Engineering, Cybersecurity, HR, and Line-of-Business leaders. Balances rapid technological innovation with ethical and statutory risk controls.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* AI 프로젝트를 IT 기술자들끼리만 결정하지 않고, **법무(Legal), 컴플라이언스, 정보보안, 인사(HR), 사업부 리더**가 함께 참여하여 비즈니스 가치와 위험을 균형 있게 심의하는 전사 협의체입니다.

</div>
</div>

---

### 3.24 모델 카드 및 시스템 카드 (Model & System Cards)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Model Cards & System Cards**: Standardized documentation disclosing a model's intended use cases, training corpus characteristics, architectural limitations, evaluation benchmarks, and ethical caveats.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 모델의 사용 목적, 한계, 평가 결과, 학습 데이터 구성을 투명하게 정리한 표준 설명서로 규제 감사 및 내부 거버넌스의 기본 문서입니다.

</div>
</div>

---

### 3.25 저작권 및 지적재산권 면책 (Copyright Indemnification)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Cloud Vendor IP Indemnification**: Contractual defense provided by major cloud providers (including AWS for Amazon Bedrock and Amazon Q) defending enterprise customers against third-party copyright infringement lawsuits arising from generative outputs.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 생성형 AI 산출물이 제3자의 저작권을 침해했다는 법적 분쟁이 발생했을 때 클라우드 벤더(AWS)가 고객을 대신해 법적 방어와 배상을 책임져주는 엔터프라이즈 보호 조항입니다.

</div>
</div>

---

### 3.26 서드파티 벤더 리스크 평가 (Vendor Risk Assessment)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Third-Party AI Auditing**: Thorough compliance vetting of external AI SaaS vendors—inspecting data retention policies, model fine-tuning clauses, and SOC 2 / ISO certifications before corporate onboarding.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 외부 AI 솔루션을 도입할 때 해당 벤더가 고객 데이터를 모델 학습에 재사용하지 않는지, 데이터 보존 및 보안 규정을 준수하는지 엄격히 감사해야 합니다.

</div>
</div>

---

### 3.27 섀도 AI 통제 정책 (Shadow AI Governance Policy)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Proactive Shadow AI Policy**: Establishing clear acceptable use guidelines combined with providing enterprise-approved AI tools (Amazon Q Business) with data DLP controls rather than relying purely on blunt network blocks.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 직원들의 무단 챗봇 사용을 방화벽으로 차단만 하면 우회 경로를 찾게 됩니다. 사내 보안 가이드라인을 제정하고 안전한 공식 기업용 AI 도구를 제공하는 것이 올바른 거버넌스입니다.

</div>
</div>

---

### 3.28 프롬프트 주입 방어 (Prompt Injection Defense via Guardrails)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Multi-Layer Defense**: Employing **Amazon Bedrock Guardrails** to inspect inbound user prompts for adversarial injection attempts and inspecting outbound model responses before delivery.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 입력 단계와 출력 단계 양방향에서 Guardrails 필터를 적용하여 적대적 프롬프트 주입 공격을 원천 차단합니다.

</div>
</div>

---

### 3.29 데이터 출처 및 계보 추적 (Data Provenance & Lineage)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Data Lineage (Amazon DataZone, AWS Glue Data Catalog)**: Tracking the historical journey, transformations, and custody of training and RAG data from raw source to model ingestion, indispensable for regulatory audits.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* AI 모델 학습 및 RAG에 사용된 데이터가 어디서 수집되었고 어떻게 가공되었는지 전 생애주기 이력을 추적하여 규제 감사에 투명하게 제시합니다.

</div>
</div>

---

### 3.30 지속적 편향 및 유해성 모니터링 (Continuous Bias & Toxicity Monitoring)
<div class="bilingual-grid">
<div class="en-col">

#### 🇺🇸 English Exam Context
* **Continuous Monitoring**: Ongoing production surveillance utilizing **Amazon SageMaker Model Monitor** and **Bedrock Model Evaluation** to detect toxic outputs, safety drift, and emerging bias over time.

</div>
<div class="kr-col">

#### 🇰🇷 한국어 전략 해설 & 비즈니스 판단 기준
* 모델은 배포 시점에 안전했더라도 시간이 지나며 성능 저하나 편향이 발생할 수 있으므로, 프로덕션 환경에서 지속적으로 유해성과 편향을 모니터링해야 합니다.

</div>
</div>
"""
