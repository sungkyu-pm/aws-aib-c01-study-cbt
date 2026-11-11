#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part A of the Exhaustive Master Glossary & Exam Expressions Encyclopedia for AWS AIB-C01.
Contains:
- Header & Navigation Overview
- Section 1: 80+ Real Exam Green-Flag (정답 시그널) vs. Red-Flag (오답 함정 시그널) Idioms & Decision Phrases
- Section 2: 45+ C-Suite Executive Governance, FinOps, Legal & Operating Model Terms
"""

GLOSSARY_PART_A = """# 📖 AWS Certified AI Business Strategist (AIB-C01) 초대형 마스터 용어백과 & 실전 시험 표현 사전 (Comprehensive Master Glossary & Exam Idiom Encyclopedia)

> **본 백과사전의 목적**: 실제 `AWS Certified AI Business Strategist (AIB-C01)` 시험은 단순 약어 암기 시험이 아닙니다. 비즈니스 전략, 재무(FinOps), 법무/규제(EU AI Act/NIST/ISO), 머신러닝/생성형 AI 학습 아키텍처, 데이터 엔지니어링, 조직 변화관리(ADKAR/CAF), 그리고 16개 산업 도메인(바이오·제조·R&D·유통·소매·금융·공공 등)의 **고급 실무 영어 표현과 전략적 관용구(Strategic Idioms)** 를 정확히 독해하고 **미묘한 오답 함정(Distractor Traps)** 을 가려낼 수 있는지를 묻습니다.
>
> 본 문서는 **총 10개 핵심 섹션, 380개 이상의 실전 필수 용어·관용구·의사결정 표현**을 망라한 초대형 레퍼런스입니다. 상단 검색창 또는 브라우저 검색(`Ctrl+F` / `Cmd+F`)으로 원하는 영문·국문 표현을 즉시 찾아보세요.

---

## 🧭 목차 (Table of Contents)

1. **[섹션 1] 실전 시험 정답 시그널(🟢 Green Flags) vs. 오답 함정(🔴 Red Flags) 핵심 관용구 80선**
2. **[섹션 2] 임원진(C-Suite) 의사결정·투자 거버넌스·AI FinOps 재무 용어 50선**
3. **[섹션 3] AI/ML 학습 패러다임·통계적 검증·데이터 과학 심화 용어 55선**
4. **[섹션 4] 생성형 AI 커스터마이징·고급 RAG·파인튜닝·경량화·에이전트 용어 60선**
5. **[섹션 5] 책임 있는 AI(RAI)·편향 측정/완화·설명가능성(XAI)·보안 가드레일 용어 55선**
6. **[섹션 6] 글로벌 AI 규제(EU AI Act·NIST·ISO)·법무/IP·컴플라이언스 용어 40선**
7. **[섹션 7] 데이터 아키텍처·데이터 메시·MLOps/LLMOps·클라우드/엣지 인프라 용어 45선**
8. **[섹션 8] 전사 AI 전환 프레임워크(AWS CAF·성숙도 모델·조직 변화관리·CoE) 용어 45선**
9. **[섹션 9] 16대 산업 도메인별(바이오·제조·R&D·소매·유통·금융·의료·에너지 등) 실전 빈출 표현 & KPI 80선**
10. **[섹션 10] AWS AI/ML·데이터·보안·거버넌스 핵심 서비스 & 기능 매핑 마스터 사전**

---

## 🎯 [섹션 1] 실전 시험 정답 시그널(🟢 Green Flags) vs. 오답 함정(🔴 Red Flags) 핵심 관용구 80선

실제 시험 문제의 지문(Stem)과 4개 선지(Options A~D)에서 **출제위원들이 정답과 오답을 가르기 위해 사용하는 결정적 영어/한국어 상용구**입니다.

### 1-1. 전략 수립·조달(Build vs. Buy)·로드맵 단계별 관용구 (30선)

| 영문 시험 표현 (Exact Exam Phrase) | 한국어 의미 | 판별 | 실전 시험 맥락 및 정답/오답 판별 공식 (Exam Decoding Logic) |
| :--- | :--- | :---: | :--- |
| **Undifferentiated Heavy Lifting** | 비차별화 중노동 (범용 반복 작업) | 🟢 **정답** | 기업의 고유 경쟁 우위(Core IP)를 만들지 못하는 범용 인프라 관리, 일반 번역/OCR/감성분석. **반드시 Managed AI Service(API)나 SaaS를 Buy하여 외주화/제거해야 함.** |
| **Core Competitive Differentiator / Strategic Moat** | 핵심 경쟁 차별화 요소 / 전략적 해자 | 🟢 **정답** | 경쟁사가 복제할 수 없는 당사 고유의 독점 데이터·핵심 알고리즘. **Custom Build 또는 독점 데이터 기반 RAG/PEFT로 내재화해야 함.** |
| **Stage-Gated Tranche Funding / Metered Funding** | 단계별 관문 기반 분할 펀딩 | 🟢 **정답** | 처음부터 수십억 원 일괄 예산(`Upfront Monolithic CapEx`)을 주지 않고, `Envision ➔ Experiment ➔ Launch ➔ Scale` 각 관문의 KPI 통과 시에만 다음 단계 예산을 집행하는 모범 투자 방식. |
| **Build-Operate-Transfer (BOT) with Contractual Knowledge Transfer** | 구축-운영-이전 파트너십 (지식이전 계약 포함) | 🟢 **정답** | 당장 내부 ML 인력이 부족하지만 장기적으로 핵심 IP를 내재화해야 할 때, 외부 전문 파트너와 **Co-Delivery(혼성 스쿼드)** 로 구축 후 단계적으로 운영권과 지식을 내부 팀에 이전받는 전략. |
| **Paving the Cow Path** | 비효율적 구식 업무 절차를 그대로 자동화함 | 🔴 **함정** | 불필요한 다단계 결재나 수기 병목을 재설계(`BPR: Business Process Re-engineering`)하지 않고 기존 비효율적 프로세스 위에 AI만 얹는 대표적 실패 패턴. |
| **Solution in Search of a Problem / Tech-First Mandate** | 문제를 찾아 헤매는 기술 / 기술 우선 강박 | 🔴 **함정** | 명확한 비즈니스 문제나 측정 가능한 KPI 정의 없이 "일단 우리도 최신 LLM/에이전트를 도입하라"는 식으로 시작하는 오답 패턴. 정답은 항상 **Business-Backward (비즈니스 역산)** 접근. |
| **Business-Backward Problem Framing** | 비즈니스 목표로부터 역산하는 문제 정의 | 🟢 **정답** | 먼저 해결할 비즈니스 병목과 재무적/운영적 목표 KPI를 정의한 뒤, 이를 달성할 가장 단순하고 경제적인 기술(규칙 기반 ➔ 고전 ML ➔ GenAI 순)을 선택하는 원칙. |
| **Minimum Viable Product (MVP) with Pre-Defined Kill/Pivot Criteria** | 사전 정의된 중단/방향전환 기준을 갖춘 최소기능제품 | 🟢 **정답** | 실험(`Experiment`) 착수 전에 **"정확도 X% 미달 또는 추론 단가 $Y 초과 시 과감히 중단(Kill)하거나 아키텍처를 전환(Pivot)한다"** 는 출구 전략을 미리 박아두는 거버넌스. |
| **Sunk Cost Fallacy / Escalation of Commitment** | 매몰 비용의 오류 / 실패하는 과제에 대한 집착 확대 | 🔴 **함정** | 이미 투입한 6개월의 시간과 예산이 아깝다는 이유로 비즈니스 가치가 입증되지 않은 PoC를 프로덕션으로 강행하거나 추가 예산을 쏟아붓는 오답. |
| **Pilot Purgatory / PoC Graveyard** | 파일럿 연옥 / PoC 무덤 | 🔴 **함정** | 데이터 파이프라인, 보안 가드레일, 운영 비용(FinOps), 현업 변화관리를 고려하지 않고 주피터 노트북 수준의 데모만 수십 개 만들어 프로덕션(`Launch/Scale`)으로 하나도 넘어가지 못하는 상태. |
| **Pre-Deployment Historical Baseline Capture** | 배포 전 기존 성과의 사전 기준선 측정 | 🟢 **정답** | AI 도입 효과를 증명하려면 **모델 배포 전에 반드시 기존 수작업/레거시 프로세스의 처리 시간·오류율·비용 기준선(Baseline)을 먼저 측정·고정**해 두어야 함. |
| **Holdout Control Group & Causal A/B Testing** | 홀드아웃 대조군 및 인과적 A/B 테스트 | 🟢 **정답** | 계절성이나 외부 프로모션 착시를 배제하고 AI 모델의 **순수 증분 가치(Incremental Uplift)** 를 입증하기 위해 무작위 대조군(기존 방식 유지 그룹)과 동시 비교하는 방법. |
| **Shadow Deployment / Dark Launch (Traffic Mirroring)** | 섀도우 배포 / 다크 런치 (실시간 트래픽 미러링) | 🟢 **정답** | 신규 AI 모델의 결과를 실제 고객/현장 설비에 바로 반영하지 않고, 프로덕션 실시간 입력을 복제해 백그라운드에서 추론만 수행하며 기존 시스템과 성능·지연시간을 무위험 비교하는 기법. |
| **Canary Rollout with Automated Rollback Triggers** | 자동 롤백 트리거를 갖춘 카나리 점진 배포 | 🟢 **정답** | 전체 트래픽의 1~5%에만 먼저 신규 모델을 적용하고, 오류율·지연시간·환각 지표가 임계치를 넘으면 즉시 기존 버전으로 자동 복구(`Automated Rollback`)하는 안전한 출시 방식. |
| **Big-Bang Cutover / Rip-and-Replace** | 전면 일괄 전환 / 레거시 일거 철거 | 🔴 **함정** | 검증 기간 없이 금요일 밤에 기존 ERP/콜센터 시스템을 완전히 끄고 월요일 아침부터 신규 AI로 100% 전환하는 무모한 방식(실전 시험에서 100% 오답). |
| **Strangler Fig Pattern for Legacy Modernization** | 교살자 무화과 패턴 (레거시 점진적 우회 현대화) | 🟢 **정답** | 거대 레거시 코어 시스템을 한 번에 건드리지 않고, API 게이트웨이/이벤트 브로커 앞단에서 특정 마이크로서비스 기능부터 하나씩 현대적 AI 서비스로 우회·대체해 나가는 아키텍처. |
| **Vanity Metrics vs. Actionable Business Value KPIs** | 허수 지표 vs. 실질적 비즈니스 가치 KPI | 🟢/🔴 | 단순 페이지뷰, 프롬프트 입력 횟수, 챗봇 로그인 수는 **Vanity Metric(오답)**. `First-Contact Resolution(FCR)`, `Cost per Resolved Ticket`, `Net Retention Uplift`가 **정답 KPI**. |
| **Leading Indicators vs. Lagging Indicators** | 선행 지표 vs. 후행 지표 | 🟢 **정답** | 분기 매출·연간 이탈률 같은 **후행 지표(Lagging)** 만 보면 조기 대응이 늦음. 일일 활성 채택률, 추천 수락률, 평균 응답 시간 단축 등 **선행 지표(Leading)** 를 함께 묶어(`Dual-Metric Scorecard`) 추적해야 함. |
| **Horizon 1 / Horizon 2 / Horizon 3 Balanced Portfolio** | 호라이즌 1·2·3 균형 포트폴리오 배분 | 🟢 **정답** | **H1(단기 코어 업무 효율화/비용 절감 70%)** 에서 창출한 현금흐름과 신뢰를 바탕으로 **H2(중기 인접 매출 확장 20%)** 와 **H3(장기 파괴적 비즈니스 모델 혁신 10%)** 에 재투자하는 자본 배분 전략. |
| **Cost of Inaction (COI) / Competitive Opportunity Cost** | 미도입 비용 / 경쟁 기회비용 | 🟢 **정답** | AI 투자 예산(TCO)만 계산하는 것이 아니라, **"AI를 도입하지 않았을 때 향후 3년간 경쟁사에게 빼앗길 시장점유율·고객 이탈·우수 인재 유출 손실액"** 을 정량화하여 이사회 설득에 활용하는 기법. |
| **Hidden Lifecycle TCO (Day-2 Operational Iceberg)** | 숨겨진 전 생애주기 총소유비용 (배포 후 운영 빙산 비용) | 🟢 **정답** | 초기 모델 개발/훈련비(전체의 15~20%) 외에 **지속적 데이터 정제, 드리프트 감시, 재학습, 가드레일 필터링, 벡터 DB 인덱싱, 감사 대응, 변화관리 교육비(나머지 80%)** 를 모두 포함한 진짜 TCO. |
| **Unit Economics (`Cost per Successful Business Outcome`)** | 단위 경제성 (성공적 비즈니스 성과 1건당 비용) | 🟢 **정답** | 단순 월간 클라우드 총액이 아니라, **"성공적으로 해결된 고객 문의 1건당 추론 비용($)"** 또는 **"구매 전환 1건당 AI 비용"** 이 창출 마진보다 낮은지 검증하는 핵심 재무 지표. |
| **Showback ➔ Chargeback FinOps Maturity** | 비용 가시화 ➔ 부서 예산 실청구 | 🟢 **정답** | 프로젝트·부서·유스케이스별 태그(`Cost Allocation Tags`)를 붙여 토큰 소비량을 대시보드로 보여주고(`Showback`), 이후 각 현업 부서의 실제 P&L 예산에서 차감(`Chargeback`)하여 주인의식을 부여하는 전략. |
| **Tiered Model Routing / Model Cascading** | 계층형 모델 라우팅 / 모델 캐스케이딩 | 🟢 **정답** | 앞단 경량 분류기(Router)가 질의 난이도를 판별해 **단순 FAQ/요약(70~80%)은 초저가 SLM(Haiku/Nova Micro)으로, 고난도 다단계 추론(20%)만 고성능 Frontier LLM으로 라우팅**하여 비용을 70% 절감하는 패턴. |
| **Semantic Caching & Prompt Prefix Caching** | 시맨틱 캐싱 및 프롬프트 프리픽스 캐싱 | 🟢 **정답** | 의미적으로 동일한 반복 질문은 벡터 캐시에서 즉시 응답(`Semantic Cache`)하고, 매 호출마다 반복되는 긴 시스템 프롬프트/문서 컨텍스트는 `Prompt Caching`으로 처리해 지연시간과 입력 토큰 비용을 대폭 절감. |
| **Asynchronous Batch Inference for Non-Urgent Workloads** | 비긴급 워크로드의 비동기 배치 추론 전환 | 🟢 **정답** | 야간 일괄 보고서 요약, 수백만 건 상품 카탈로그 태깅처럼 실시간 응답이 불필요한 작업을 실시간 온디맨드 API 대신 **Batch Inference(최대 50% 할인)** 로 분리 실행하는 FinOps 기법. |
| **Provisioned Throughput for Predictable High-Volume Steady Traffic** | 예측 가능한 대규모 상시 트래픽을 위한 프로비저닝 처리량 약정 | 🟢 **정답** | 트래픽이 불규칙한 초기 PoC는 `On-Demand(Pay-as-you-go)`가 정답이지만, **24/7 높은 베이스라인 트래픽과 엄격한 처리량 SLA가 요구되는 성숙 단계 워크로드**는 `Provisioned Throughput` 약정이 정답. |
| **Vendor Lock-In Mitigation via Model Abstraction Gateway** | 모델 추상화 게이트웨이를 통한 특정 벤더 종속 완화 | 🟢 **정답** | 애플리케이션 코드에 특정 모델의 고유 프롬프트/API를 하드코딩하지 않고, **`Amazon Bedrock Converse API` 등 통합 추상화 계층과 표준 평가 스위트**를 두어 언제든 타 모델로 무중단 교체(`Hot-Swap`) 가능하게 설계. |
| **Dark Data Monetization with Cost-Benefit Triage** | 비용-편익 선별 기반 다크 데이터 자산화 | 🟢 **정답** | 사내에 방치된 페타바이트급 비정형 데이터(콜센터 녹취, 설비 로그, 과거 PDF)를 무조건 전부 정제(오답)하지 않고, **비즈니스 의사결정 가치가 높은 고가치 데이터셋부터 선별적으로 카탈로그화·정제**하는 전략. |
| **Technical Debt Accumulation from Ad-Hoc Glue Code** | 임시방편 글루 코드로 인한 기술 부채 누적 | 🔴 **함정** | 표준 피처 스토어나 MLOps 파이프라인 없이 개발자 개인 스크립트와 수동 CSV 파일 복사(`Ad-hoc Glue Code & Pipeline Jungles`)로 모델을 배포해 유지보수가 불가능해지는 함정. |

---

### 1-2. 거버넌스·리스크·보안·조직 변화관리 핵심 관용구 (50선)

| 영문 시험 표현 (Exact Exam Phrase) | 한국어 의미 | 판별 | 실전 시험 맥락 및 정답/오답 판별 공식 (Exam Decoding Logic) |
| :--- | :--- | :---: | :--- |
| **Shift-Left Governance / Governance-by-Design** | 거버넌스 좌측 이동 / 설계 단계 내재화 | 🟢 **정답** | 모델 개발이 다 끝난 배포 직전에 법무·보안 심사를 받으면 전면 재작업이 발생함. **기획(`Envision`) 및 데이터 수집 단계부터 보안·윤리·규제 요건을 아키텍처와 CI/CD 파이프라인에 자동 내재화**해야 함. |
| **Risk-Tiered Governance Triage (Fast-Track vs. Deep Review)** | 위험 등급별 차등 거버넌스 트리아지 | 🟢 **정답** | 모든 AI 과제를 동일한 6주짜리 위원회 심사에 태우면 혁신이 마비됨. **내부 회의록 요약 같은 저위험 과제는 자동 가드레일 기반 Fast-Track으로 즉시 승인**하고, **채용·신용평가·의료 등 고위험 과제에 심층 심사 역량을 집중**하는 정답 패턴. |
| **Fairness Through Unawareness (Blindness to Protected Attributes)** | 민감 속성 단순 제거를 통한 공정성 착시 | 🔴 **함정** | 성별·인종·연령 컬럼만 삭제하면 모델이 공정할 것이라 믿는 대표적 오답. **우편번호(`Zip Code`), 졸업학교, 소비 패턴 등 대리 변수(`Proxy Variables / Redlining`)** 를 통해 차별이 그대로 학습되므로 반드시 통계적 편향 측정이 필수임. |
| **Forced Post-Hoc Output Quota / Arbitrary Threshold Manipulation** | 사후 결과 할당량 강제 조작 | 🔴 **함정** | 실제 예측 근거와 무관하게 결과 비율을 인위적으로 50:50으로 강제 할당하는 오답. 정당한 자격을 갖춘 지원자/고객에 대한 역차별 및 규제 위반을 초래함. |
| **Pre-Processing / In-Processing / Post-Processing Bias Mitigation** | 전처리 / 인프로세싱 / 후처리 편향 완화 | 🟢 **정답** | • **Pre-processing**: 훈련 데이터 리샘플링·가중치 조정 (`SMOTE`, `Reweighing`)<br>• **In-processing**: 학습 손실 함수에 공정성 제약 조건(`Fairness Regularization`) 추가<br>• **Post-processing**: 집단별 진양성률 균등을 위한 보정된 결정 임계치(`Calibrated Threshold`) 조정 |
| **Demographic Parity vs. Equal Opportunity vs. Equalized Odds** | 인구통계학적 동등성 vs. 기회 균등 vs. 균등화된 오즈 | 🟢 **정답** | • **Demographic Parity**: 집단 간 긍정 판정 비율 자체를 동일하게 맞춤<br>• **Equal Opportunity**: 실제 자격 있는 사람(True Positive)이 선발될 확률(`TPR`)을 집단 간 동일하게 보장 (채용·대출 심사 빈출 정답)<br>• **Equalized Odds**: `TPR`과 오탐율(`FPR`) 모두 집단 간 동일하게 보장 |
| **Global Explainability vs. Local Explainability (`SHAP` / `LIME`)** | 전역적 설명가능성 vs. 국소적(개별 건) 설명가능성 | 🟢 **정답** | • **Global**: 모델 전체가 어떤 변수를 중요하게 보는지 파악 (`Global Feature Importance`)<br>• **Local**: **"왜 특정 고객 홍길동의 대출이 거절되었는가?"** 에 대한 개별 건별 변수 기여도 설명 (`Local SHAP / Counterfactuals`). 금융/의료 이의제기 대응 시 **Local Explainability** 가 필수 정답! |
| **White-Box (Glass-Box) Interpretable Model vs. Black-Box Model** | 화이트박스(본질적 해석 가능) 모델 vs. 블랙박스 모델 | 🟢 **정답** | 엄격한 금융 규제·임상 가이드라인에서 추론 과정 자체의 완전한 투명성이 법적으로 강제될 때는 딥러닝 블랙박스 대신 **Decision Tree, Linear/Logistic Regression, GAM 등 본질적 해석 가능 모델**을 선택해야 함. |
| **Confidence-Based Human-in-the-Loop (HITL) Routing (`Amazon A2I`)** | 신뢰도 임계치 기반 인간 개입 라우팅 | 🟢 **정답** | 모든 추론 건을 사람이 100% 전수 검수(확장성 파괴 = 오답)하지 않고, **모델 예측 신뢰도(`Confidence Score`)가 임계치(예: 85%) 미만이거나 고위험 예외 건만 인간 전문가 큐로 자동 라우팅**하는 아키텍처. |
| **Automation Bias & Rubber-Stamping Mitigation** | 자동화 편향 및 무비판적 도장 찍기 방지 | 🟢 **정답** | 인간 검수자가 피로도나 AI에 대한 맹신 때문에 AI 추천 결과를 읽지도 않고 1초 만에 승인(`Rubber-stamping`)하는 현상. **AI의 확신도를 일부러 숨기거나, 검수자가 핵심 근거를 직접 선택해야 승인 버튼이 활성화되는 인지적 마찰(Cognitive Friction) UI 및 블라인드 감사 샘플링**이 정답. |
| **Calibrated Trust UX (Citation Links & Uncertainty Badges)** | 신뢰 보정 UX (출처 하이라이트 및 불확실성 배지) | 🟢 **정답** | 사용자가 AI를 무조건 맹신(`Over-trust`)하거나 무조건 불신(`Under-trust`)하지 않도록, **원문 출처 문서의 정확한 단락 하이라이트 링크와 신뢰도/근거 수준 배지를 함께 표시**하는 인터페이스 설계. |
| **Contextual Grounding Check & Automated Reasoning Verification** | 문맥 기반 사실성 검증 및 자동화된 수학/논리 추론 검증 | 🟢 **정답** | `Amazon Bedrock Guardrails`를 통해 LLM의 답변이 검색된 참조 문서(`Source Chunks`)에서 벗어난 환각인지 차단(`Contextual Grounding`)하고, 보험 약관·수수료 정책 같은 엄격한 비즈니스 규칙을 수학적 논리로 검증(`Automated Reasoning`). |
| **Deterministic Execution Guardrails & Step-Up Authorization** | 결정론적 실행 가드레일 및 고위험 작업 단계별 격상 승인 | 🟢 **정답** | 자율형 AI 에이전트가 외부 API(환불, 발주, DB 수정)를 호출할 때 확률적 LLM 판단에만 맡기지 않고, **중간에 하드코딩된 결정론적 정책 엔진(예: $500 초과 환불 시 매니저 승인 토큰 강제 요구)이 실행을 가로채 검증**하는 보안 패턴. |
| **Excessive Agency & Principle of Least Privilege (PoLP)** | 과도한 에이전트 대행 권한 및 최소 권한 원칙 | 🟢 **정답** | 에이전트에게 DB `DROP/WRITE` 전체 권한을 부여하면 간접 프롬프트 인젝션 공격 시 참사가 발생함. **역할별로 세분화된 최소 IAM 권한(기본 Read-Only)과 샌드박스 격리 실행**이 필수. |
| **Indirect Prompt Injection via Poisoned External Documents** | 오염된 외부 문서를 통한 간접 프롬프트 인젝션 | 🟢 **정답** | 사용자가 직접 공격 프롬프트를 입력하지 않았더라도, AI가 요약/검색하기 위해 읽어 들인 **외부 이메일·웹페이지·이력서 PDF 안에 숨겨진 악성 명령어**가 실행되는 공격. **외부 데이터 영역 구분(`Spotlighting/Delimiters`), 입출력 가드레일, 에이전트 권한 격리**로 방어. |
| **Data Poisoning & Backdoor Trigger Injection** | 데이터 중독 및 백도어 트리거 주입 공격 | 🟢 **정답** | 오픈소스 데이터셋이나 크라우드소싱 라벨링 과정에 공격자가 악의적으로 조작된 샘플을 섞어 넣어 특정 트리거 문구 입력 시 모델이 오작동하게 만드는 공급망 공격. **데이터 출처 암호화 서명, 이상치 통계 필터링, Golden Validation Set 검증**이 정답. |
| **Model Inversion & Membership Inference Attacks** | 모델 역추적 복원 및 멤버십 추론 공격 | 🟢 **정답** | 모델 API에 반복 질의하여 훈련 데이터에 특정 개인의 의료/금융 기록이 포함되었는지 알아내거나(`Membership Inference`) 원본 얼굴/텍스트를 복원(`Model Inversion`)하는 공격. **Differential Privacy(차등 프라이버시 노이즈 주입), 출력 확률값(Logits) 반올림/제한, API Rate Limiting**이 정답. |
| **Zero Base-Model Training Assurance & Private Connectivity** | 파운데이션 모델 학습 미사용 보장 및 프라이빗 네트워크 연결 | 🟢 **정답** | 엔터프라이즈 기밀 데이터를 `Amazon Bedrock` 등에서 사용할 때 **고객의 입출력 프롬프트가 기본 파운데이션 모델 학습에 절대 사용되지 않으며, `AWS PrivateLink`와 `AWS KMS CMK` 암호화로 공용 인터넷을 타지 않도록 격리**하는 CISO 핵심 안심 장치. |
| **Non-Outsourceable Ultimate Accountability** | 외주화할 수 없는 최종 법적·윤리적 책임 | 🟢 **정답** | 클라우드 벤더나 서드파티 AI 모델을 쓰더라도(`Shared Responsibility`), **자사 서비스가 고객에게 끼친 차별·오진·규제 위반에 대한 최종 법적·윤리적 책임은 도입 기업(Deployer) 경영진에게 있으며 절대 벤더에게 떠넘길 수 없다**는 원칙. |
| **Kill-Switch & Automated Circuit Breaker** | 긴급 킬스위치 및 자동 서킷 브레이커 | 🟢 **정답** | 프로덕션 AI가 심각한 환각·기밀 유출·폭주 비용을 일으킬 때 **재배포 없이 1초 내에 AI 경로를 차단하고 기존의 안전한 결정론적 규칙 시스템이나 상담원 안내 화면으로 우회(`Graceful Degradation`)** 시키는 필수 안전장치. |
| **AI Red Teaming (Continuous Adversarial Stress-Testing)** | AI 레드티밍 (지속적 적대적 모의 해킹 검증) | 🟢 **정답** | 배포 전 및 주요 업데이트마다 보안·도메인·윤리 전문가(및 자동화된 공격 에이전트)가 탈옥(`Jailbreak`), 편향 유도, 권한 탈취를 의도적으로 시도하여 취약점을 사전 패치하는 활동. |
| **Amnesty Funnel & Safe-Harbor Enterprise AI Sandbox** | 섀도우 AI 사면(양성화) 통로 및 안전 샌드박스 | 🟢 **정답** | 직원들이 업무 효율을 위해 몰래 외부 무료 AI에 사내 데이터를 넣는 `Shadow AI`를 무조건 처벌·차단만 하면 음지화됨. **기존에 만든 유용한 프롬프트/워크플로우를 징계 없이 자진 신고(`Amnesty`)받아 공식 보안 가드레일이 적용된 사내 AI 환경으로 이관**해주는 변화관리 전략. |
| **Augmentation over Replacement & Prosci ADKAR Model** | 대체가 아닌 역량 증강 및 ADKAR 변화관리 모델 | 🟢 **정답** | 현업 직원들의 일자리 상실 공포와 사보타주를 극복하기 위해 **"AI는 인력 감축 수단이 아니라 반복 행정 업무를 덜어주는 코파일럿(Augmentation)"** 임을 천명하고, `Awareness(인식) ➔ Desire(욕구) ➔ Knowledge(지식) ➔ Ability(역량) ➔ Reinforcement(강화)` 5단계로 전환을 이끄는 전략. |
| **Federated Hub-and-Spoke AI Operating Model** | 연합형 허브 앤 스포크 AI 운영 모델 | 🟢 **정답** | • **Central Hub (`AI CoE`)**: 전사 공통 가드레일, 보안 아키텍처, 재사용 가능한 골든 템플릿, FinOps 정책 수립 (병목이 아닌 **Enablement Engine**)<br>• **Domain Spokes (현업 사업부)**: 도메인 전문가와 내재화된 분석가가 현업 과제를 자율적·민첩하게 실행 |
| **Blameless Post-Mortem & Psychological Safety for Experimentation** | 비난 없는 사후 분석 및 실험을 위한 심리적 안전감 | 🟢 **정답** | AI 실험(PoC)이 가설 기각으로 종료되었을 때 담당자를 문책하면 직원들이 실패 데이터를 숨기고 거짓 성공 보고를 올림. **빠른 가설 기각과 교훈 자산화(`Lessons Learned Repository`)를 장려하는 문화**가 정답. |
| **Whistleblowing Protection & Unilateral Stop-Work Veto Authority** | 내부 공익제보 보호 및 일방적 배포 중단 거부권 | 🟢 **정답** | 출시 일정 압박 속에서도 주니어 엔지니어나 리스크 담당자가 심각한 윤리적 결함·개인정보 유출 위험을 발견했을 때 **보복 없이 즉시 보고하고 해결 전까지 배포를 보류(`Stop-Work Veto`)시킬 수 있는 제도적 권한**. |
"""

if __name__ == "__main__":
    print("GLOSSARY_PART_A length:", len(GLOSSARY_PART_A))
