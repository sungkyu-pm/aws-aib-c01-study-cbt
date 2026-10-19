# 도메인 3: AI 거버넌스 및 책임 있는 AI 리더십 (AI Governance & Responsible AI Leadership)

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
