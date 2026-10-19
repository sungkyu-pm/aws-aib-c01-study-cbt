# 도메인 4: 비즈니스 준비성, 리더십, AI 혁신 (Business Readiness, Leadership & Transformation)

> **출제 비중**: **22%**  
> **핵심 키워드**: AI 성숙도 모델, People/Process/Technology/Governance 격차 분석, 데이터 사일로(Data Silos), AI Center of Excellence (CoE), AI 챔피언, 변화 관리(Change Management), 4단계 스케일링(Envision-Experiment-Launch-Scale)

---

## 4.1 AI 비즈니스 준비 상태 및 성숙도 평가 (Readiness & Maturity)

### 1. 성공적인 AI 도입을 위한 4대 핵심 축 (4 Dimensions of AI Readiness)
* **People (사람/문화)**: 조직원들의 AI 리터러시, 변화에 대한 개방성, 경영진의 적극적 스폰서십.
* **Process (프로세스)**: 애자일한 실험 프로세스, 신속한 의사결정 체계, AI와 기존 업무 프로세스의 매끄러운 통합.
* **Technology (기술 & 인프라)**: 클라우드 인프라 기반, 확장 가능한 AI/ML 플랫폼(AWS), API 연동 환경.
* **Governance (거버넌스)**: 데이터 품질 관리 정책, 보안 및 개인정보 보호 규정 준수, 위험 관리 프레임워크.

### 2. AI 성숙도 4단계 (AI Maturity Stages)
1. **탐색/실험 단계 (Exploration & Experimentation)**: 소규모 팀이 개별적으로 챗봇이나 PoC를 시도하는 단계. 데이터가 파편화되어 있음.
2. **시범 도입 단계 (Opportunistic/Piloting)**: 특정 비즈니스 부서에서 성공 사례가 나오기 시작함. 전사 거버넌스는 아직 미흡.
3. **체계화 단계 (Systematic/Operationalized)**: AI CoE가 설립되고 표준 플랫폼(AWS)과 거버넌스 가이드라인이 정립됨.
4. **전사적 혁신 단계 (Transformational/AI-Driven)**: 전 직원이 AI를 일상 도구로 활용하며, 비즈니스 모델 자체가 AI 중심으로 재편됨.

---

## 4.2 AI를 위한 데이터 및 인프라 기반 구축 (Data & Infra Foundation)

### 1. 데이터 사일로 (Data Silos) 타파
* **문제점**: 마케팅, 영업, 물류 등 부서마다 데이터가 고립되어 있으면, AI 모델이 전체 고객 여정을 파악할 수 없어 정확도가 크게 떨어짐.
* **해결책**: 데이터 레이크(Data Lake, 예: Amazon S3) 및 중앙 집중식 데이터 공유/거버넌스(예: AWS DataZone, Lake Formation) 구축.

### 2. 데이터 준비성 (Data Readiness)의 4대 요소
* **접근성 (Accessibility)**: 보안 권한을 갖춘 AI 애플리케이션이 필요 시 실시간으로 데이터에 접근할 수 있는가?
* **품질 및 정합성 (Quality & Consistency)**: 중복, 결측치, 형식 불일치가 정제되어 있는가?
* **보안 및 규정 준수 (Security & Compliance)**: 암호화 및 민감 정보 마스킹 정책이 적용되어 있는가?
* **소유권 및 라벨링 (Ownership & Labeling)**: 데이터의 소유 주체(Data Owner)가 명확하고 비즈니스 메타데이터가 잘 정리되어 있는가?

---

## 4.3 전사적 변화 관리 및 인력 역량 구축 (Change Management & People)

### 1. 경영진 후원 (Executive Sponsorship) 및 AI 챔피언 (AI Champions)
* **경영진 후원**: AI 프로젝트가 부서 간 이기주의에 부딪히지 않도록 C-레벨 리더의 명확한 비전 선포와 예산 지원이 필수적임.
* **AI 챔피언**: 각 현업 부서(영업, 재무, 인사 등)에서 AI 도구를 가장 먼저 익히고 동료들을 코칭하는 '전도사' 역할. 탑다운 지시보다 훨씬 빠른 현장 확산 효과를 냄.

### 2. 직원의 우려 해소 및 문화적 저항 극복
* **직원들의 불안**: "AI가 내 일자리를 대체할 것인가?"
* **변화 관리 커뮤니케이션 전략**:
  * AI는 **대체자(Replacement)가 아니라 보조자/증강자(Copilot/Augmenter)**임을 명확히 전달.
  * 반복적이고 지루한 업무(데이터 취합, 회의록 요약 등)를 AI에 맡기고, 인간은 **고부가가치 창의적 업무와 공감 중심의 소통**에 집중하도록 유도.
  * 투명한 도입 일정 공유 및 전사적 재교육(Upskilling/Reskilling) 프로그램 제공.

### 3. AI 리터러시 확산을 위한 실천적 접근
* **해커톤(Hackathons)**: 비즈니스 현업과 IT가 팀을 이뤄 실제 사내 문제를 해결하는 프로토타입 제작.
* **안전한 모래사장(Sandbox)**: 사내 기밀 유출 걱정 없이 마음껏 실험해볼 수 있는 안전한 환경(예: AWS PartyRock, 사내 격리 Bedrock 플레이그라운드) 제공.

---

## 4.4 파일럿에서 전사적 배포로의 스케일링 (Pilot to Production Scaling)

### 1. AWS의 4단계 AI 혁신 프레임워크
```
[1. Envision (구상)] ➔ [2. Experiment (실험)] ➔ [3. Launch (출시)] ➔ [4. Scale (확장)]
```
* **Envision**: 비즈니스 목표 설정, 유스케이스 발굴, 우선순위화.
* **Experiment**: PoC(개념 증명)를 통해 기술적 실현 가능성 및 비즈니스 가치 검증. (Fail Fast)
* **Launch**: 초기 사용자 그룹(파일럿)을 대상으로 최소 기능 제품(MVP) 배포 및 피드백 수집.
* **Scale**: 전사 조직으로 배포 확장, 자동화된 MLOps/LLMOps 적용, AI CoE를 통한 거버넌스 총괄.

### 2. AI 우수성 센터 (AI Center of Excellence, AI CoE)의 핵심 역할
* 전사 표준 AI 프레임워크 및 클라우드 아키텍처 수립
* 부서 간 중복 투자 방지 및 공통 에셋(라이브러리, 프롬프트 템플릿, 데이터셋) 재사용 촉진
* 전사 거버넌스 및 윤리적 가이드라인 감독
