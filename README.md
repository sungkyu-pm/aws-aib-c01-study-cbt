# AWS Certified AI Business Strategist (AIB-C01) 학습 & CBT 플랫폼

> **한국어 사용자를 위한 AIB-C01 시험 대비 올인원(All-in-One) 학습 공간 및 CBT 가상 실습 시스템**  
> 공식 가이드 기준 도메인 1~4 완벽 반영 | 한·영 듀얼 트랙 학습 | 실전 CBT 모의고사 지원

🌐 **온라인 실시간 포털 바로가기**: **[https://sungkyu-pm.github.io/aws-aib-c01-study-cbt/](https://sungkyu-pm.github.io/aws-aib-c01-study-cbt/)**

---

## 🔗 공식 시험 및 접수 링크 (Official Links)
* **AWS 공식 시험 가이드 (한국어)**: [AWS Certified AI Business Strategist 공식 가이드 (한국어) ↗](https://docs.aws.amazon.com/ko_kr/aws-certification/latest/ai-business-strategist-01/ai-business-strategist-01.html)
* **AWS 공식 시험 가이드 (영문)**: [AWS Certified AI Business Strategist Official Exam Guide (English) ↗](https://docs.aws.amazon.com/aws-certification/latest/ai-business-strategist-01.html)
* **AWS 자격증 시험 접수 포털**: [AWS Training & Certification (Pearson VUE) ↗](https://www.aws.training/certification)
* **AWS Skill Builder 시험 준비 코스**: [AIB-C01 Official Exam Prep Course ↗](https://skillbuilder.aws/category/exam-prep/ai-business-strategist-business-AIB-C01)

---

## 🚀 빠른 시작 (Quick Start)

### 🌐 방법 1: 온라인 웹에서 바로 학습 (추천! 별도 설치 불필요)
브라우저에서 바로 접속하여 모바일/PC 어디서나 시험 응시 및 학습이 가능합니다:  
👉 **[https://sungkyu-pm.github.io/aws-aib-c01-study-cbt/](https://sungkyu-pm.github.io/aws-aib-c01-study-cbt/)**

---

### 💻 방법 2: 로컬 서버 실행
시험 응시 이력 저장, 실시간 채점, 오답 노트 누적 기록을 지원하는 전용 로컬 경량 백엔드 서버입니다 (추가 라이브러리 설치 불필요).

터미널에서 아래 명령어를 실행하면 서버가 켜지며 브라우저가 자동으로 열립니다:
```bash
./run.sh
```
또는 직접 파이썬으로 실행:
```bash
python3 server.py
```
접속 주소: **`http://localhost:8000`**

---

### 📂 방법 2: 브라우저 직접 열기 (파일 모드)
서버 실행 없이 브라우저로 바로 확인하고 싶다면:
* Finder에서 루트 폴더의 [`index.html`](file:///Users/sungkyu/Study/AI%20BS_AWS/index.html)을 더블 클릭하여 크롬이나 사파리로 엽니다.

---

## 📂 프로젝트 구성 안내

```
AI BS_AWS/
├── docs/                                  # 📚 체계적인 이론 및 가이드 자료실
│   ├── 00_AIB-C01_EXAM_GUIDE.md           # 시험 개요, 도메인 비중 및 3단계 합격 로드맵
│   ├── 01_GLOSSARY_KR_EN.md               # [핵심] 필수 비즈니스 AI 한·영 용어사전
│   ├── 02_DOMAIN_1_AI_FUNDAMENTALS.md     # 도메인 1: AI 기초 및 활용 능력 (20%)
│   ├── 03_DOMAIN_2_AI_STRATEGY_VALUE.md   # 도메인 2: AI 전략 및 비즈니스 가치 창출 (31%)
│   ├── 04_DOMAIN_3_GOVERNANCE_RESPONSIBLE_AI.md # 도메인 3: AI 거버넌스 & 책임 있는 AI (27%)
│   ├── 05_DOMAIN_4_TRANSFORMATION_READINESS.md  # 도메인 4: 비즈니스 준비성 & 조직 혁신 (22%)
│   └── 06_AWS_SERVICES_CHEAT_SHEET.md     # 출제 범위 내 핵심 AWS 서비스 치트시트
│
├── questions/                             # 📝 실전 수준 문제은행 (JSON 포맷)
│   ├── questions_domain1.json             # 도메인 1 전용 문제 & 상세 한국어 해설
│   ├── questions_domain2.json             # 도메인 2 전용 문제 & 상세 한국어 해설
│   ├── questions_domain3.json             # 도메인 3 전용 문제 & 상세 한국어 해설
│   ├── questions_domain4.json             # 도메인 4 전용 문제 & 상세 한국어 해설
│   └── mock_exam_1.json                   # 전 도메인 통합 실전 모의고사 세트 (20문항)
│
└── cbt-app/                               # 💻 실전 CBT 가상 실습 웹 애플리케이션
    ├── index.html                         # CBT 웹앱 메인 화면
    ├── app.js                             # CBT 엔진 (타이머, 채점, 모드 전환, 오답노트)
    ├── style.css                          # AWS 공식 스타일 테마 & 반응형 UI
    └── questions-data.js                  # 브라우저 즉시 구동용 문제 데이터
```

---

## 🎯 핵심 학습 전략 (한·영 듀얼 트랙)

실제 시험은 **영문**으로 출제되기 때문에, 단순히 한국어 번역본만 읽고 가면 시험장에서 영문 전문 용어(예: *Hallucination, Guardrails, Shadow AI, Baseline Metric, Bias Drift, AI Champions, HITL*)를 마주했을 때 당황할 수 있습니다.

1. **이론 학습 시**:
   * [`docs/01_GLOSSARY_KR_EN.md`](file:///Users/sungkyu/Study/AI%20BS_AWS/docs/01_GLOSSARY_KR_EN.md)에서 영문 키워드와 한글 개념을 먼저 매핑합니다.
   * [`docs/02` ~ `05`](file:///Users/sungkyu/Study/AI%20BS_AWS/docs/02_DOMAIN_1_AI_FUNDAMENTALS.md) 도메인별 요약 노트에서 전략적 배경을 이해합니다.
   * [`docs/06_AWS_SERVICES_CHEAT_SHEET.md`](file:///Users/sungkyu/Study/AI%20BS_AWS/docs/06_AWS_SERVICES_CHEAT_SHEET.md)로 Bedrock, Q, SageMaker의 비즈니스 역할을 확인합니다.

2. **CBT 실습 시**:
   * **1단계 (학습 모드 - Study Mode)**:
     * 영문 지문을 먼저 읽어보고, 이해가 안 될 땐 **[🌐 한국어 번역 보기]** 버튼을 눌러 확인합니다.
     * 문제를 푼 직후 **[정답 확인]**을 눌러 왜 정답인지, 왜 오답인지 상세한 한국어 해설을 습득합니다.
   * **2단계 (실전 모드 - Exam Mode)**:
     * 실전 시험 환경과 동일하게 타이머 카운트다운을 켜고, 영문 지문 위주로 신속하게 문제를 풉니다.
     * 아리송한 문제는 **[🚩 나중에 검토(Flag)]**로 표시해두고 마지막에 재검토합니다.
   * **3단계 (결과 분석 & 오답 노트)**:
     * 제출 후 **도메인별 성취도(%)**를 확인하여 취약한 도메인을 파악합니다.
     * **[틀린 문제만 오답노트 복습]** 버튼을 눌러 틀린 문제만 다시 풀며 완벽히 숙지합니다.

---

## 🛠️ 문제 추가 및 커스터마이징 방법
새로운 기출 변형 문제나 학습하고 싶은 문제를 추가하려면:
1. `questions/questions_domain{1~4}.json` 파일에 문제 객체를 추가합니다.
2. 아래 스크립트를 터미널에서 실행하여 CBT 앱 데이터에 반영합니다:
   ```bash
   python3 -c "
   import json
   files = ['questions/questions_domain1.json', 'questions/questions_domain2.json', 'questions/questions_domain3.json', 'questions/questions_domain4.json']
   all_q = []
   data = {}
   for i, f in enumerate(files, 1):
       with open(f, 'r', encoding='utf-8') as fp:
           d = json.load(fp)
           data[f'domain{i}'] = d
           all_q.extend(d)
   data['mock1'] = all_q
   with open('questions/mock_exam_1.json', 'w', encoding='utf-8') as out:
       json.dump(all_q, out, ensure_ascii=False, indent=2)
   with open('cbt-app/questions-data.js', 'w', encoding='utf-8') as f:
       f.write('const EXAM_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n')
   print('Updated successfully!')
   "
   ```
