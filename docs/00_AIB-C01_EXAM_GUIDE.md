# AWS Certified AI Business Strategist (AIB-C01) 시험 안내 및 학습 전략

## 1. 시험 개요 (Exam Overview)
* **시험 코드**: AIB-C01 (AWS Certified AI Business Strategist)
* **목표 대상**: 기술 엔지니어가 아닌, 조직 내에서 **AI 이니셔티브를 평가·기획·주도·확장하는 비즈니스 리더, 기획자, PM, 컨설턴트, 의사결정권자**
* **시험 특징**: 복잡한 딥러닝 코드 구현 대신 **비즈니스 가치 창출(ROI/KPI), 우선순위 선정(Build vs Buy), 책임 있는 AI(윤리/규제/가드레일), 조직 변화 관리(Change Management)** 위주 출제
* **문항 형식**: 객관식 단일 선택(Multiple Choice) 및 다중 선택(Multiple Response)
* **언어 전략**: 시험 문항이 영문으로 출제되는 환경을 대비해 **"한국어로 원리를 확실히 이해하고, 문제 키워드와 선지는 영문 표현에 완벽히 익숙해지는 한·영 듀얼 트랙"**으로 대비합니다.

---

## 2. 도메인별 출제 비중 (Domain Weighting)

| 도메인 | 도메인 명칭 (Domain Name) | 출제 비중 | 핵심 평가 역량 |
| :---: | :--- | :---: | :--- |
| **Domain 1** | **AI 기초 및 활용 능력**<br>*(AI Fundamentals and Literacy)* | **20%** | • AI / ML / GenAI 차이점<br>• 정형 vs 비정형 데이터 및 데이터 품질<br>• 규칙 기반 vs AI 솔루션 구분 및 AI 에이전트 개념<br>• 프롬프트 엔지니어링, RAG, Fine-tuning 차이 |
| **Domain 2** | **AI 전략 및 비즈니스 가치 창출**<br>*(AI Strategy & Business Value Creation)* | **31%** | • 고임팩트 비즈니스 유스케이스 발굴<br>• Build vs Buy vs Partner 의사결정<br>• 유형적/무형적 KPI 및 ROI 측정 프레임워크<br>• 기준 지표(Baseline) 및 비용 통제 전략 |
| **Domain 3** | **AI 거버넌스 및 책임 있는 AI 리더십**<br>*(AI Governance & Responsible AI Leadership)* | **27%** | • 공정성, 설명가능성, 투명성, 개인정보보호, 안전성<br>• Human-in-the-loop 및 가드레일(Guardrails)<br>• 크로스펑셔널(부서 간) 거버넌스 협의체 구성<br>• 환각(Hallucination), 편향(Bias Drift), 섀도 AI 위험 완화 |
| **Domain 4** | **비즈니스 준비성, 리더십, AI 혁신**<br>*(Business Readiness, Leadership, and AI Transformation)* | **22%** | • People, Process, Tech, Governance 성숙도 평가<br>• 데이터 사일로 해소 및 데이터 거버넌스<br>• 전사적 변화 관리, AI 챔피언, 문화적 저항 극복<br>• Envision ➔ Experiment ➔ Launch ➔ Scale 및 AI CoE |

---

## 3. 한국어 사용자를 위한 합격 3단계 로드맵

```
[1단계: 이론 & 한-영 용어 매핑]
  - docs/01_GLOSSARY_KR_EN.md 로 핵심 영문 키워드와 한국어 개념 매핑
  - docs/02 ~ 05 도메인별 요약 노트 완독
  - docs/06 AWS 서비스 치트시트로 Bedrock, Q, SageMaker 역할 숙지

[2단계: 도메인별 문제은행 학습]
  - questions/ 폴더의 도메인별 문제 풀이
  - 영문 지문을 읽고 키워드를 포착하는 훈련
  - 한국어 상세 해설을 통해 오답 선지가 왜 틀렸는지 분석

[3단계: 실전 CBT 가상 모의고사 반복]
  - cbt-app/ 웹앱 실행
  - 1회차: [학습 모드] 한/영 번역 토글과 즉시 해설을 보며 실전 문제 풀이
  - 2회차: [실전 모드] 영문 전용 + 제한 시간 타이머를 켜고 100% 실전 환경 적응
  - 오답 리포트를 확인하고 취약 도메인 보완
```
