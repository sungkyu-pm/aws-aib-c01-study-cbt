#!/usr/bin/env python3
"""
AWS Certified AI Business Strategist (AIB-C01)
Complete 120-Category Deduplicated Question Bank Generator
- 30 distinct topic categories per domain (Total 120 categories).
- 10 diverse enterprise questions per category (Total 300 questions per domain, 1,200 questions overall).
- Explicit `topic_category` on every question for 100% duplicate-free CBT sampling.
"""

import json
import os

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

# We import D1_TAXONOMY from build_deduplicated_question_bank
from build_deduplicated_question_bank import D1_TAXONOMY

# 30 Distinct Categories for Domain 2 (Strategy & Business Value)
D2_TAXONOMY = [
    ("Build vs Buy vs Partner Trade-offs", "솔루션 조달 3대 축 결정",
     "핵심 차별화 역량이 아니며 시장에 이미 검증된 상용 솔루션이 존재하는 비핵심 업무에 가장 적합한 AI 조달 방식은 무엇입니까?",
     "When an organization seeks an AI solution for standard commodity business processes with mature off-the-shelf market offerings, which strategy minimizes TTM and TCO?",
     "기성 상용 솔루션 구매 (Buy - e.g., Amazon Q Business)", "Purchasing commercial off-the-shelf software (Buy - e.g., Amazon Q Business)",
     [("5년간의 독자적인 기초 연구를 통한 자체 구축(Build)", "Multi-year bespoke ground-up engineering (Build)"),
      ("클라우드 도입을 전면 거부하고 외주 용역만 유지하기", "Rejecting cloud and maintaining manual agency outsourcing"),
      ("오픈소스 소스코드를 검증 없이 사내 서버에 복사하기", "Pasting unverified open-source scripts into root servers")],
     "상용 솔루션 구매(Buy)는 검증된 표준 업무에서 개발 오버헤드를 없애고 가장 빠른 출시 속도(Time to Market)를 제공합니다."),

    ("Core Differentiator vs Commodity Utility", "핵심 차별화 역량 vs 범용 상품",
     "기업의 독점적 데이터와 고유 비즈니스 로직이 결합되어 시장에서 모방 불가능한 경쟁 우위를 만드는 핵심 영역에 권장되는 조달 방식은 무엇입니까?",
     "Which sourcing paradigm is required for core proprietary business capabilities where unique enterprise data delivers a defensible commercial moat?",
     "완전한 통제권과 맞춤화를 보장하는 독자 자체 구축 (Build)", "Custom in-house engineering (Build) securing proprietary IP and full differentiation",
     [("경쟁사와 동일한 무료 공개 챗봇 위젯 임베딩", "Embedding the identical free public chatbot widget as competitors"),
      ("모든 독점 데이터를 경쟁사 포럼에 공개 업로드하기", "Publicly uploading proprietary training datasets"),
      ("AI 프로젝트를 즉시 전면 취소하기", "Cancelling all analytical modernization")],
     "기업의 핵심 경쟁 우위(Core Differentiator)가 되는 고유 영역은 자체 구축(Build)을 통해 독점 지적재산권(IP)과 차별화를 확보해야 합니다."),

    ("Data Sovereignty in Build vs Buy", "데이터 주권 및 VPC 격리",
     "엄격한 금융/의료 규제로 인해 고객 데이터가 외부 퍼블릭 SaaS 환경으로 유출되어서는 안 되는 기업에 권장되는 아키텍처는 무엇입니까?",
     "When strict regulatory compliance mandates that customer records must never traverse public multi-tenant SaaS endpoints, which approach is required?",
     "전용 VPC 내에서 프라이빗 엔드포인트(PrivateLink)로 격리 구동되는 Bedrock/SageMaker 자체 구축 (Build)", "Private VPC network isolation via AWS PrivateLink with Amazon Bedrock or SageMaker (Build)",
     [("소비자용 무료 퍼블릭 AI 웹사이트로 데이터 전송", "Transmitting data to free unvetted consumer web portals"),
      ("인터넷 방화벽을 완전히 해제하여 외부 접근 허용", "Disabling enterprise network firewalls"),
      ("데이터 암호화 키를 외부에 공개 배포하기", "Publishing KMS master encryption keys publicly")],
     "데이터 주권(Data Sovereignty)과 엄격한 규제가 요구될 때는 자체 VPC 내에서 프라이빗하게 격리된 클라우드 파이프라인(Build)을 구축해야 합니다."),

    ("Comprehensive AI TCO Modeling", "포괄적 AI TCO 모델링",
     "생성형 AI 프로젝트의 총 소유 비용(TCO)을 산정할 때, 단순 클라우드 API 호출료 외에 반드시 포함해야 하는 '숨은 TCO' 항목은 무엇입니까?",
     "When formulating enterprise AI Total Cost of Ownership (TCO), which hidden expenditures beyond raw API token invoices must be included?",
     "데이터 수집 및 정제, MLOps 모니터링, 보안/거버넌스 감사 및 직원 재교육 비용", "Data labeling and curation, continuous MLOps, governance audits, and organizational change management",
     [("사내 카페테리아 음료 할인 쿠폰 비용", "Corporate cafeteria beverage discount subsidies"),
      ("사무실 책상의 목재 페인트 재도색 비용", "Office desk furniture refurbishment costs"),
      ("임원진의 해외 골프 회원권 구매 비용", "Executive recreation membership subscriptions")],
     "AI TCO는 API 호출료 외에도 데이터 엔지니어링, 지속적인 모니터링(MLOps), 법무 감사, 조직 변화 관리 등 상당한 숨은 비용을 수반합니다."),

    ("Cost of Inaction (COI) Strategic Value", "행동하지 않는 비용 (COI)",
     "경영진이 불확실성을 이유로 AI 투자를 무기한 지연할 때, 시장 점유율 상실과 고객 이탈이라는 기회비용을 정량화하여 설득하는 프레임워크는 무엇입니까?",
     "Which economic justification framework quantifies the enterprise penalty, market share erosion, and customer churn incurred by delaying AI transformation?",
     "행동하지 않는 비용 (Cost of Inaction / COI)", "Cost of Inaction (COI)",
     [("복권 구매 기대 수익률 분석", "Lottery ticket expected value calculations"),
      ("단순 과거 회계 장부 수기 입력", "Manual historical ledger ledger keeping"),
      ("감가상각비 0원 처리 가정", "Zero depreciation mathematical assumptions")],
     "COI(행동하지 않는 비용)는 AI 도입을 미룰 때 발생하는 경쟁 열세, 고객 이탈, 생산성 격차를 정량화하여 투자의 시급성을 입증합니다."),

    ("Sunk Cost Fallacy in AI Governance", "매몰 비용의 오류 극복",
     "이미 수억 원의 예산이 투입되었으나 비즈니스 가치가 검증되지 않고 실패한 AI 프로젝트에 대해 리더십이 취해야 하는 올바른 자세는 무엇입니까?",
     "When an AI pilot fails to deliver business value despite substantial capital already expended, what leadership mindset prevents further resource waste?",
     "매몰 비용의 오류(Sunk Cost Fallacy)를 극복하고 과감히 프로젝트를 조기 종료(Kill)하거나 피벗(Pivot)함", "Overcoming the Sunk Cost Fallacy by decisively terminating (Kill) or pivoting the failed pilot",
     [("실패를 숨기기 위해 추가로 100억 원을 더 투입하기", "Pouring millions more into the failed project to conceal the error"),
      ("성과 지표를 조작하여 가짜 성공 보고서 만들기", "Falsifying operational metrics to simulate phantom success"),
      ("프로젝트 담당자를 아무 이유 없이 징계하고 방치하기", "Punishing junior staff without analyzing root systemic failure")],
     "매몰 비용(Sunk Cost)은 회수할 수 없는 과거의 비용이므로, 미래 가치가 없는 프로젝트는 과감히 중단하여 자원을 유망한 과제로 재배치해야 합니다."),

    ("Project Kill/Pause Decision Gates", "프로젝트 중단/보류 게이트",
     "AI 파일럿 프로젝트의 성공 여부를 객관적으로 판단하고 자원 낭비를 방지하기 위해 착수 전 반드시 수립해야 하는 거버넌스 장치는 무엇입니까?",
     "To enforce disciplined project governance and avoid endless experimentation, what mechanism must be defined prior to pilot kickoff?",
     "정량적 비즈니스 KPI 및 기술적 실현 가능성 기준을 명시한 Go/No-Go 중단 게이트(Kill Criteria)", "Predetermined quantitative Go/No-Go decision gates and objective termination criteria",
     [("프로젝트 종료 날짜를 무기한 무제한으로 설정하기", "Granting indefinite timeline extensions without performance milestones"),
      ("성과 측정을 일체 하지 않겠다는 서약서 작성", "Signing waivers exempting teams from performance evaluation"),
      ("팀장의 직관과 주관적인 기분에만 전적으로 의존하기", "Relying purely on subjective executive intuition")],
     "Go/No-Go 게이트와 조기 중단 기준(Kill Criteria)을 사전에 정의해 두어야 실패한 프로젝트를 신속히 정리하고 전사 혁신 속도를 높일 수 있습니다."),

    ("Baseline Metric Definition", "기준 지표 (Baseline Metric)",
     "AI 솔루션 도입 후의 성과 개선과 투자 수익률(ROI)을 정량적으로 증명하기 위해 프로젝트 착수 전 반드시 선행되어야 하는 작업은 무엇입니까?",
     "What mandatory step must be completed prior to AI deployment to objectively verify post-implementation business improvements and ROI?",
     "현재 상태(As-Is)의 비즈니스 성과를 정량 수집한 기준 지표 (Baseline Metric) 확립", "Establishing quantitative Baseline Metrics measuring current As-Is operational performance",
     [("도입 후 개선율을 주관적 느낌으로 추측하기", "Guessing post-launch improvements based on vague intuition"),
      ("과거 데이터를 모두 삭제하여 비교를 불가능하게 만들기", "Deleting all historical operational records"),
      ("다른 회사의 재무제표를 그대로 베껴오기", "Copying financial statements from unrelated competitors")],
     "기준 지표(Baseline Metric)가 사전에 정량적으로 측정되어 있지 않으면, AI 도입 후 성능 개선이나 ROI를 결코 증명할 수 없습니다."),

    ("ROI Mathematical Calculation & Modeling", "AI ROI 계산 및 재무 모델링",
     "AI 솔루션 도입의 투자 타당성을 입증하기 위해 경영진 보고서에 제시해야 하는 올바른 ROI 산출 공식은 무엇입니까?",
     "Which financial formula correctly substantiates the investment viability of an enterprise AI initiative to executive stakeholders?",
     "[(AI로 창출된 순 경제적 이익 - 총 소유 비용) / 총 소유 비용] × 100", "[(Net Economic Benefits - Total Cost of Ownership) / Total Cost of Ownership] x 100",
     [("총 매출액을 직원 수로 나눈 단순 수치", "Total gross corporate revenues divided by headcount"),
      ("클라우드 인프라 청구서의 총 페이지 수", "The total page count of AWS billing invoices"),
      ("프로젝트 팀원들의 평균 경력 연수", "The average years of experience of software engineers")],
     "AI ROI는 창출된 순 경제적 가치(비용 절감 + 신규 매출)에서 TCO를 뺀 순이익을 TCO로 나누어 백분율로 산출합니다."),

    ("Tangible vs Intangible Benefits", "유형적 이익 vs 무형적 이익",
     "상담원 통화 시간 40% 단축으로 인한 인건비 절감(유형적 이익)과 고객 만족도 NPS 상승(무형적 이익)을 균형 있게 평가하는 프레임워크는 무엇입니까?",
     "Which measurement framework balances direct balance-sheet savings (tangible) with strategic dividends like NPS and brand trust (intangible)?",
     "유형적 이익과 무형적 이익을 종합 반영한 균형 성과표 (Balanced Scorecard)", "A Balanced Scorecard integrating both tangible cost savings and intangible strategic benefits",
     [("무형적 가치를 100% 무시하고 단기 회계 비용만 계산하기", "Completely ignoring customer satisfaction and brand reputation"),
      ("모든 성과를 재무제표 대신 직원 설문조사로만 대체하기", "Replacing financial audits with anonymous employee gossip polls"),
      ("비용 절감액을 10배로 부풀려 허위 보고하기", "Artificially inflating cost reduction estimates ten-fold")],
     "유형적 이익(비용 절감, 매출 증대)과 무형적 이익(고객 만족도, 직원 만족도, 브랜드 가치)을 모두 포괄해야 진정한 AI 가치를 측정할 수 있습니다."),

    ("Leading Indicators of AI Success", "선행 지표 (Leading Indicators)",
     "AI 프로젝트가 본격적인 재무적 성과를 내기 전에 초기 성공 여부와 사용자 정착을 미리 예측할 수 있는 선행 지표(Leading Indicator)는 무엇입니까?",
     "Which metric serves as a leading indicator predicting future AI business success during the initial rollout phase?",
     "일일 활성 사용자 수(DAU), 주당 AI 쿼리 발생량 및 기능 채택률(Adoption Rate)", "Daily Active Users (DAU), weekly query volume, and active feature adoption rates",
     [("3년 후 달성될 것으로 예상되는 연간 순이익", "Annual net operating profit measured three years post-deployment"),
      ("연말 세무 회계 감사 보고서의 감가상각 누계액", "Year-end statutory financial audit tax depreciation balances"),
      ("사내 서버실의 물리적 평수 크기", "Physical floor area square footage of data center racks")],
     "선행 지표(Leading Indicator)는 최종 재무 성과가 나타나기 전 사용자들의 실제 도구 채택률과 활용 빈도를 측정하여 조기 피드백을 제공합니다."),

    ("Lagging Indicators of Long-term Value", "후행 지표 (Lagging Indicators)",
     "AI 시스템 구축이 완료되고 수개월 이상 운영된 후에야 비로소 신뢰성 있게 측정할 수 있는 대표적인 후행 지표(Lagging Indicator)는 무엇입니까?",
     "Which metric functions as a lagging indicator, quantifiable only after sustained production operation over multiple fiscal quarters?",
     "연간 고객 서비스 운영비 30% 절감액 및 분기별 영업 이익률 개선", "Annual customer service operating expense reduction and quarterly operating margin gains",
     [("첫날 생성된 테스트 프롬프트 단어 수", "The word count of prompts written on launch day"),
      ("사내 킥오프 미팅 참석자들의 출석률", "Attendance rates at the internal kickoff pizza party"),
      ("개발자가 작성한 파이썬 코드의 글꼴 크기", "The desktop monitor font size of the software engineers")],
     "후행 지표(Lagging Indicator)는 프로젝트의 최종적인 비즈니스 결실(비용 절감액, 매출 증가액)을 확인하는 지표입니다."),

    ("Prioritization 2x2 Matrix", "우선순위 2x2 매트릭스",
     "수십 개의 잠재적 AI 아이디어 중에서 어떤 프로젝트를 먼저 착수할지 결정하기 위해 사용하는 '비즈니스 가치 vs 실현 가능성' 평가 도구는 무엇입니까?",
     "Which structured portfolio management framework evaluates prospective AI initiatives along Business Impact versus Feasibility?",
     "우선순위 2x2 매트릭스 (Prioritization Matrix)", "Prioritization 2x2 Matrix (Value vs Feasibility)",
     [("가위바위보 게임을 통한 무작위 결정", "Playing rock-paper-scissors to select production projects"),
      ("가장 목소리가 큰 부서장의 의견만 따르기", "Defaulting to the most aggressive executive in the room"),
      ("모든 프로젝트를 동시에 착수하여 리소스 분산시키기", "Starting 50 complex projects concurrently with no prioritization")],
     "우선순위 2x2 매트릭스는 비즈니스 가치와 기술적/조직적 실현 가능성을 평가하여 프로젝트 로드맵의 순서를 합리적으로 정합니다."),

    ("Quick Wins Execution Strategy", "단기 가시적 성과 (Quick Wins)",
     "전사적인 AI 불신을 해소하고 경영진의 지속적인 투자와 예산 지원을 이끌어내기 위해 가장 먼저 실행해야 하는 프로젝트 유형은 무엇입니까?",
     "To overcome institutional skepticism and secure continued executive budget sponsorship, which project quadrant must be executed first?",
     "높은 비즈니스 가치와 낮은 구현 복잡도를 가진 Quick Wins (단기 가시적 성과)", "High-value, low-complexity Quick Wins demonstrating rapid tangible ROI",
     [("성공 확률이 1% 미만인 고위험 미증명 기초 연구", "Unproven moonshots with a 99% probability of complete technical failure"),
      ("가치는 없으나 구현만 매우 복잡한 Money Pit 프로젝트", "Low-value, high-complexity projects that consume all capital"),
      ("아무도 쓰지 않는 사내 게시판 배경화면 변경", "Cosmetic modifications to unused intranet bulletin boards")],
     "Quick Wins는 빠르게 성과를 입증하여 조직 내 신뢰를 얻고, 후속 대형 프로젝트를 추진할 수 있는 모멘텀을 형성합니다."),

    ("Strategic Bets Long-term Investment", "전략적 베팅 (Strategic Bets)",
     "구현 복잡도와 인프라 투자가 매우 크지만, 성공할 경우 회사의 독점적 시장 지배력을 보장하는 고임팩트 프로젝트를 일컫는 용어는 무엇입니까?",
     "What portfolio category describes transformational AI initiatives requiring multi-quarter infrastructure investments that define industry leadership?",
     "전략적 베팅 (Strategic Bets)", "Strategic Bets",
     [("매일 아침 커피 주문을 돕는 단순 챗봇", "A basic coffee ordering reminder bot"),
      ("단순 수작업 엑셀 데이터 복사 작업", "Routine spreadsheet manual copy-paste"),
      ("외부 외주사에 모든 핵심 사업을 넘기는 조치", "Outsourcing the entire core commercial business to third parties")],
     "전략적 베팅(Strategic Bets)은 단기 성과를 넘어 기업의 미래 먹거리가 되는 핵심 경쟁 우위를 창출하는 대규모 투자 과제입니다."),

    ("PoC Purgatory Exit Strategies", "PoC 연옥 탈출 전략",
     "기업 내 수많은 AI PoC(개념 증명)가 실제 프로덕션으로 전환되지 못하고 실험실 단계에서 맴돌다 폐기되는 'PoC 연옥'을 탈출하는 최선의 방법은 무엇입니까?",
     "How can enterprise leadership prevent initiatives from stalling indefinitely in 'PoC Purgatory' without ever reaching production scale?",
     "PoC 착수 전 명확한 비즈니스 성공 기준(KPI)과 프로덕션 확장 요건을 사전에 정의하고 강제함", "Defining explicit production readiness criteria, scalable architectures, and business KPIs before PoC kickoff",
     [("PoC 기간을 10년으로 연장하여 결론을 계속 미루기", "Extending PoC timelines to ten years to avoid making production decisions"),
      ("프로덕션 배포 없이 PoC 결과만 사내 게시판에 자랑하기", "Publishing marketing press releases while keeping systems in lab prototype stage"),
      ("비즈니스 현업 부서의 참여를 전면 배제하기", "Banning business end-users from evaluating prototype tools")],
     "PoC 연옥을 방지하려면 시작부터 비즈니스 현업과 협력하여 배포 기준(KPI, 비용, 보안)을 사전에 정의하고 단계별 승인을 거쳐야 합니다."),

    ("Time-to-Market (TTM) Optimization", "출시 기간(TTM) 최적화",
     "경쟁사가 새로운 AI 서비스를 출시하기 전에 우리 회사가 시장을 선점하기 위해 상용 솔루션(Buy)을 도입하는 가장 핵심적인 이유는 무엇입니까?",
     "Why is purchasing commercial AI software (Buy) often preferred over custom in-house development (Build) in fast-moving consumer markets?",
     "개발 및 검증 시간을 수개월 단축하여 가장 빠른 시장 출시 기간 (Time-to-Market)을 달성할 수 있기 때문", "Achieving the fastest Time-to-Market (TTM) by eliminating lengthy ground-up engineering cycles",
     [("자체 개발보다 소프트웨어 버그가 100배 더 많기 때문에", "Because commercial software always contains 100 times more bugs"),
      ("회사 내부 엔지니어들을 모두 해고하기 위해서", "To immediately eliminate the entire engineering department"),
      ("클라우드 인프라 제공업체에 대한 모든 종속성을 없애기 위해", "To eliminate all reliance on cloud providers")],
     "기성 상용 솔루션(Buy)의 최대 강점은 이미 검증된 인프라를 활용하여 시장 출시 기간(Time-to-Market)을 극적으로 단축하는 데 있습니다."),

    ("Data Flywheel Defensible Moat", "데이터 플라이휠과 기업 해자",
     "누구나 접근할 수 있는 범용 상용 파운데이션 모델(LLM) 환경에서, 특정 기업이 지속 가능하고 방어 가능한 비즈니스 해자(Moat)를 구축하는 원천은 무엇입니까?",
     "In an era where commodity foundation models are accessible to all competitors, what creates an enduring, defensible enterprise moat?",
     "독점적인 자사 고객 인터랙션 데이터 축적과 모델 고도화가 선순환하는 데이터 플라이휠 (Data Flywheel)", "Proprietary customer data flywheels tightly coupled with deep operational workflows",
     [("오픈소스 모델의 가중치를 외부에 무료 배포하기", "Publicly giving away proprietary datasets to market rivals"),
      ("가장 값비싼 그래픽 카드를 창고에 쌓아두기만 하기", "Hoarding expensive GPUs in a physical storage closet without using them"),
      ("경쟁사의 로고를 자사 웹사이트에 무단 복제하기", "Copying the trademark logos of competing startups")],
     "경쟁사가 복제할 수 없는 진정한 해자는 **'사용자 증가 ➔ 독점 데이터 축적 ➔ 모델 및 경험 개선'**으로 이어지는 독자적인 데이터 플라이휠에서 나옵니다."),

    ("AI FinOps Operating Framework", "AI FinOps 운영 체계",
     "예측 불가능한 대규모 생성형 AI API 호출 비용을 실시간으로 추적, 통제하고 예산 초과를 사전에 방지하는 재무-엔지니어링 거버넌스는 무엇입니까?",
     "Which cross-functional operating discipline combines engineering, finance, and procurement to manage and optimize generative AI expenditures?",
     "AI 재무 운영 프레임워크 (AI FinOps)", "AI FinOps Operating Framework",
     [("월말에 청구서가 오기 전까지 지출을 전혀 확인하지 않기", "Ignoring all billing dashboards until invoices arrive in the mail"),
      ("비용이 많이 나온 달에는 클라우드 계정을 폐쇄하기", "Deleting the corporate AWS account whenever monthly bills are high"),
      ("모든 소프트웨어 개발자에게 결제 신용카드를 무제한 지급하기", "Distributing corporate credit cards with unlimited spending limits to all interns")],
     "AI FinOps는 엔지니어링과 재무 부서가 협업하여 사용량 태깅, 예산 경보, 모델 라우팅을 통해 클라우드 AI 비용을 실시간 통제하는 체계입니다."),

    ("Cost Allocation Tags & Chargeback", "비용 할당 태그 및 부서별 정산",
     "전사적으로 공유되는 Amazon Bedrock 환경에서 마케팅팀, 고객지원팀, HR팀이 사용한 AI API 비용을 각각 분리하여 측정하고 정산하기 위한 AWS 기능은 무엇입니까?",
     "In a shared multi-tenant AWS environment, which feature attributes AI token consumption back to specific business units for accurate chargeback?",
     "AWS 비용 할당 태그 (Cost Allocation Tags)", "AWS Cost Allocation Tags",
     [("서버실 출입문의 비밀번호 변경", "Changing the physical electronic door codes of server rooms"),
      ("직원들의 출퇴근 지문 인식 기록", "Employee biometric time-clock attendance logs"),
      ("이메일 서명란에 부서 이름 적기", "Writing departmental names in Outlook email signatures")],
     "AWS 비용 할당 태그는 리소스 호출에 부서 및 프로젝트 메타데이터를 연결하여 정확한 비용 추적과 부서별 예산 책임성을 보장합니다."),

    ("AWS Budgets & Cost Anomaly Alerts", "AWS 예산 및 비용 이상 감지",
     "생성형 AI 챗봇에 예기치 못한 트래픽 급증이나 무한 루프 호출이 발생하여 월 예산 한도를 초과하기 전에 담당자에게 실시간 경보를 보내는 서비스는 무엇입니까?",
     "Which AWS governance service monitors cloud expenditure in real time and triggers automated alerts before budgets are breached?",
     "AWS Budgets 및 AWS Cost Anomaly Detection", "AWS Budgets and AWS Cost Anomaly Detection",
     [("Amazon Route 53 트래픽 라우팅", "Amazon Route 53 DNS routing policies"),
      ("AWS Snowmobile 초대형 데이터 이송 트럭", "Ordering an AWS Snowmobile 45-foot shipping container truck"),
      ("Amazon Simple Email Service 스팸 필터", "Amazon SES outbound email bounce suppression lists")],
     "AWS Budgets와 Cost Anomaly Detection은 비정상적인 지출 급증이나 예산 임계치 도달을 조기에 감지하여 재무적 위험을 차단합니다."),

    ("Model Routing & Cascading TCO Savings", "모델 라우팅 및 캐스케이딩",
     "단순 인사나 FAQ 질문은 저렴한 소형 모델로 처리하고, 복잡한 다단계 계약서 분석만 고성능 대형 모델로 보내어 TCO를 70% 이상 절감하는 아키텍처는 무엇입니까?",
     "Which architectural tiering pattern routes low-complexity queries to economical small models and escalates only complex reasoning to frontier models?",
     "지능형 모델 라우팅 / 모델 캐스케이딩 (Model Routing / Cascading)", "Intelligent Model Routing and Cascading Architecture",
     [("모든 단순 인사 질문에도 최고가 대형 모델을 풀가동하기", "Routing trivial single-word greetings to the most expensive frontier model"),
      ("모든 사용자 요청을 무조건 임의로 거절하기", "Configuring web servers to randomly reject 50% of user traffic"),
      ("서버 CPU 클럭 속도를 절반으로 줄여 속도 늦추기", "Underclocking server CPU cycles to artificially slow down responses")],
     "모델 라우팅(Model Routing)은 질문 난이도에 따라 최적의 가성비를 가진 모델로 동적 분기하여 사용자 경험을 유지하면서 비용을 극적으로 낮춥니다."),

    ("Provisioned Throughput vs On-Demand", "프로비저닝 처리량 vs 온디맨드",
     "대규모 전사 서비스 오픈 시 상시적으로 발생하는 대량의 트래픽을 처리하며, 지연 시간 SLA를 보장받고 토큰당 단가를 낮추기 위해 선택하는 Bedrock 과금 모델은 무엇입니까?",
     "To ensure consistent sub-second latency SLAs and secure bulk pricing for massive ongoing production workloads on Amazon Bedrock, which model is optimal?",
     "Amazon Bedrock 프로비저닝 처리량 (Provisioned Throughput)", "Amazon Bedrock Provisioned Throughput",
     [("건당 최고 요금을 지불하는 완전 비예약 온디맨드 모델", "Paying maximum retail rates on pure uncommitted On-Demand requests"),
      ("무료 체험판 쿠폰을 반복해서 재발급받기", "Creating thousands of trial accounts to exploit initial credits"),
      ("모든 트래픽을 해외 무료 서버로 우회 전송하기", "Routing enterprise data through unvetted overseas proxy nodes")],
     "프로비저닝 처리량(Provisioned Throughput)은 일정한 분당 처리 용량(TPM)을 약정함으로써 안정적인 응답 속도와 대규모 할인 혜택을 제공합니다."),

    ("Multi-Model Strategy & Lock-in Mitigation", "멀티 모델 전략 및 벤더 종속 방지",
     "특정 단일 AI 모델 벤더의 가격 인상, 서비스 장애, 성능 저하 위험으로부터 엔터프라이즈를 보호하기 위한 아키텍처 전략은 무엇입니까?",
     "Which architectural strategy insulates organizations against vendor price hikes, API outages, or proprietary model obsolescence?",
     "Amazon Bedrock과 같은 통합 API를 통해 복수의 파운데이션 모델을 유연하게 교체 사용하는 멀티 모델 전략", "A Multi-Model Strategy leveraging unified APIs like Amazon Bedrock to switch models seamlessly",
     [("단일 특정 스타트업 모델에만 모든 회사 코드를 하드코딩 결합", "Hardcoding all enterprise applications exclusively to a single vendor's closed API"),
      ("AI 소프트웨어 사용을 중단하고 수작업으로 회귀하기", "Cancelling all AI initiatives and returning to physical ledger entry"),
      ("모델 소스코드를 해킹하여 강제로 복제하기", "Attempting illegal reverse-engineering of proprietary weights")],
     "멀티 모델 전략(Multi-Model Strategy)은 통합 추상화 레이어를 통해 언제든 더 우수하고 경제적인 최신 모델로 쉽게 전환할 수 있는 유연성을 보장합니다."),

    ("Unit Economics in Scaled Inference", "스케일업 단계의 단위 경제학",
     "AI 서비스를 전사 또는 수백만 고객으로 확장하기 전에, 사용자 1인당 또는 트랜잭션 1회당 발생하는 AI 비용과 매출 기여도를 분석하는 재무 지표는 무엇입니까?",
     "Before scaling generative AI to millions of consumers, what metric validates whether variable token inference costs permit a profitable business model?",
     "단위 경제학 (Unit Economics)", "Unit Economics (Cost per active user / Cost per completed transaction)",
     [("서버실 건물 전체의 부동산 감정 평가액", "Real estate market appraisal of the corporate headquarters building"),
      ("회사 로고 브랜드의 색상 선호도 점수", "Consumer graphic design color preferences for company logos"),
      ("사내 식당의 일일 쌀 소비량", "Daily grain consumption statistics in the cafeteria")],
     "단위 경제학(Unit Economics)은 거래당 AI 추론 비용을 정밀하게 분석하여, 서비스 규모가 커질수록 적자가 아닌 흑자가 발생하는지 검증합니다."),

    ("Customer Retention & NPS Valuation", "고객 유지율 및 NPS 가치 평가",
     "AI 기반 개인화 추천과 24/7 신속한 고객 상담 자동화가 기업 재무에 미치는 긍정적인 무형 및 간접적 영향은 무엇입니까?",
     "What primary indirect business value is generated when AI delivers personalized customer experiences and instant 24/7 service resolution?",
     "고객 만족도(CSAT/NPS) 상승 및 고객 이탈률(Churn) 감소에 따른 고객 생애 가치(CLV) 증대", "Increased Customer Satisfaction (NPS/CSAT) and churn reduction, expanding Customer Lifetime Value (CLV)",
     [("소프트웨어 개발자의 키보드 타이핑 속도 증가", "Faster typing speeds of back-office database administrators"),
      ("사내 사무용지의 월간 인쇄량 급증", "Increased consumption of physical printer paper sheets"),
      ("회사 주차장의 주차면수 부족 현상", "Parking lot congestion at corporate headquarters")],
     "AI를 통한 고객 경험 혁신은 직접적인 인건비 절감뿐 아니라, 이탈 방지와 고객 생애 가치(CLV) 극대화라는 막대한 간접 가치를 창출합니다."),

    ("Developer Productivity ROI", "개발자 생산성 향상과 ROI",
     "개발팀에 Amazon Q Developer를 도입했을 때 소프트웨어 엔지니어링 리더가 측정해야 하는 핵심적인 유형적 성과 지표는 무엇입니까?",
     "When deploying Amazon Q Developer across engineering organizations, what tangible KPI demonstrates strategic developer productivity ROI?",
     "코드 작성 및 단위 테스트 작성 시간 단축, 레거시 마이그레이션 소요 기간 단축", "Reduction in task completion time, faster unit test authoring, and accelerated legacy code upgrades",
     [("개발자들의 커피 소비량 증가율", "Caffeine consumption per software engineering team"),
      ("사내 슬랙 메신저의 이모티콘 사용 횟수", "The total count of custom emoji reactions in internal chat rooms"),
      ("개발용 모니터의 화면 밝기 설정값", "Desktop display brightness settings in software labs")],
     "Amazon Q Developer는 코드 자동 완성, 테스트 코드 자동 작성, 버전 업그레이드를 통해 개발 주기를 단축하여 직접적인 엔지니어링 ROI를 증명합니다."),

    ("AI Business Model Innovation", "비즈니스 모델 혁신",
     "단순한 사내 비용 절감(내부 효율화)을 넘어, AI를 활용하여 신규 유료 구독 서비스나 지능형 부가 가치 프로덕트를 출시하는 전략적 단계를 무엇이라 합니까?",
     "Which strategic phase transcends internal cost optimization to create entirely new commercial monetization streams and intelligent product tiers?",
     "비즈니스 모델 혁신 (Business Model Innovation)", "Business Model Innovation",
     [("단순한 기존 업무 외주화", "Routine vendor staff augmentation"),
      ("사내 복사용지 구매 축소", "Reducing corporate stationary budgets"),
      ("사무실 형광등 소등 캠페인", "Turning off office lightbulbs early to save electricity")],
     "AI 혁신의 최고 단계는 내부 운영 효율화(비용 절감)에서 나아가, AI 기반의 새로운 수익 모델과 제품을 창출하는 비즈니스 모델 혁신입니다."),

    ("A/B Testing & Causal Attribution", "A/B 테스트 및 인과관계 검증",
     "AI 솔루션 도입 후 매출 증대가 단순한 계절적 성수기 요인 때문이 아니라 순수하게 AI의 기여 때문임을 과학적으로 증명하기 위한 방법론은 무엇입니까?",
     "To prove that post-launch conversion increases are causally attributable to AI rather than macro market seasonality, which method is mandatory?",
     "무작위 대조군을 격리하여 비교하는 A/B 테스트 (A/B Testing with Control Groups)", "Rigorous A/B Testing isolating randomized Control and Treatment groups",
     [("매출이 오른 날에는 무조건 AI 덕분이라고 주장하기", "Claiming credit for all positive sales increases without data"),
      ("매출이 떨어진 날에는 경쟁사의 탓으로 돌리기", "Blaming all revenue declines entirely on market competitors"),
      ("통계 분석을 전면 거부하고 감으로 판단하기", "Banning statistical variance modeling across all departments")],
     "대조군(Control Group)을 둔 A/B 테스트는 계절적 외부 변수를 통제하여 AI가 순수하게 창출한 증분 가치(Incremental Lift)를 증명합니다."),

    ("Fail Fast & Agile Experimentation", "빠른 실패와 애자일 실험",
     "불확실성이 높은 생성형 AI 시장에서 기업이 자본 낭비를 최소화하고 혁신 속도를 높이기 위해 채택해야 하는 실험 철학은 무엇입니까?",
     "In rapidly evolving AI markets, which organizational principle maximizes innovation velocity while capping downside financial exposure?",
     "작은 가설을 세워 신속히 검증하고 가치가 없으면 즉시 중단하는 'Fail Fast(빠른 실패)' 문화", "An agile 'Fail Fast' culture testing small hypotheses rapidly to conserve capital",
     [("결과가 안 좋아도 10년 동안 끝까지 밀어붙이기", "Persisting stubbornly in failed initiatives for ten years"),
      ("실패한 프로젝트의 모든 팀원을 형사 고발하기", "Filing civil lawsuits against engineers whose hypotheses fail"),
      ("실패를 두려워하여 아무런 신기술도 시도하지 않기", "Freezing all innovation to avoid ever making an operational mistake")],
     "생성형 AI는 불확실성이 크므로, 소규모 파일럿으로 빠르게 가설을 검증하고 실패 시 즉시 학습하여 방향을 트는 'Fail Fast' 문화가 필수적입니다.")
]

# We also build similar 30 categories for Domain 3 and Domain 4...
print("Loaded D1 (30) and D2 (30) taxonomies.")

# 30 Distinct Categories for Domain 3 (Governance & Responsible AI)
D3_TAXONOMY = [
    ("Responsible AI (RAI) Core Principles", "책임 있는 AI 핵심 원칙",
     "AI 시스템을 기획부터 배포, 운영까지 전 생애주기에 걸쳐 안전하고, 윤리적이며, 공정하게 통제하기 위한 전사적 프레임워크는 무엇입니까?",
     "Which overarching enterprise framework governs the ethical, secure, fair, and legally compliant operation of AI systems throughout their lifecycle?",
     "책임 있는 AI (Responsible AI / RAI) 거버넌스 프레임워크", "Responsible AI (RAI) governance framework",
     [("순수 수익 극대화를 위해 모든 윤리 규제를 폐지하는 정책", "Policy abolishing all ethics to maximize short-term revenue"),
      ("개발자 개인의 양심에만 전적으로 일임하는 무통제 모델", "Uncontrolled model relying solely on individual developer discretion"),
      ("AI 감사 로그를 매일 영구 삭제하는 정책", "Policy permanently deleting all audit logs nightly")],
     "책임 있는 AI(RAI)는 공정성, 설명가능성, 개인정보보호, 안전성, 투명성을 보장하는 전사적 거버넌스 체계입니다."),

    ("Fairness & Historical Bias Mitigation", "공정성 및 과거 데이터 편향 완화",
     "과거 수십 년간의 불평등한 관행이나 편견이 데이터셋에 내재되어 AI 모델이 이를 학습하여 차별적 결정을 내리지 않도록 통제하는 원칙은 무엇입니까?",
     "Which Responsible AI principle mitigates algorithms from perpetuating pre-existing societal prejudices embedded in historical training datasets?",
     "공정성 확보 및 데이터 편향 완화 (Fairness & Bias Mitigation)", "Fairness and historical bias mitigation",
     [("데이터셋에 존재하는 모든 인종/성별 정보를 더 크게 가중하기", "Amplifying demographic disparities in training loss functions"),
      ("차별적 결과가 나와도 모델의 통계적 사실이라며 방치하기", "Ignoring discriminatory outcomes as natural statistical facts"),
      ("공정성 테스트를 일체 금지하는 보안 서약", "Enforcing non-disclosure agreements banning fairness audits")],
     "공정성(Fairness)은 과거 데이터의 역사적 편향(Historical Bias)을 선제적으로 감지하고 수정하여 공정한 평가를 보장하는 핵심 원칙입니다."),

    ("Demographic Parity & Disparate Impact", "인구통계학적 동등성 및 이종 영향",
     "대출 심사나 채용 AI에서 특정 보호 집단(예: 여성, 소수자)의 합격률이 비보호 집단에 비해 통계적으로 부당하게 낮지 않은지 검증하는 수학적 지표는 무엇입니까?",
     "Which mathematical fairness metric verifies that positive outcome ratios (e.g., approval rates) are statistically balanced across protected sub-populations?",
     "인구통계학적 동등성 (Demographic Parity / Disparate Impact 검증)", "Demographic Parity and Disparate Impact evaluation",
     [("GPU 프로세서의 클럭 주파수 동등성", "GPU clock frequency parity across cloud availability zones"),
      ("데이터베이스 서버실의 온도 및 습도 균등 지수", "Server room HVAC temperature humidity balance metrics"),
      ("직원들의 주간 사내 식당 이용 빈도", "Cafeteria lunch card usage balance among employees")],
     "인구통계학적 동등성(Demographic Parity)은 알고리즘이 특정 집단에 차별적 영향(Disparate Impact)을 주지 않는지 검증하는 정량 지표입니다."),

    ("Explainability & Black-Box Transparency", "설명 가능성 및 블랙박스 해소",
     "고객의 대출 신청이 거절되었을 때 금융 규제 기관과 고객에게 모델이 왜 그러한 판단을 내렸는지 납득할 만한 이유를 제시해야 하는 원칙은 무엇입니까?",
     "When an AI system denies a commercial credit application, which principle mandates providing human-understandable justifications to regulators?",
     "설명 가능성 및 해석 가능성 (Explainability & Interpretability)", "Explainability and Interpretability",
     [("모델이 복잡한 블랙박스이므로 설명을 거부할 권리 주장", "Asserting the legal right to hide behind black-box neural networks"),
      ("거절 사유로 난수 생성기의 임의 숫자를 제시하기", "Providing random numbers as explanations to customers"),
      ("모든 거절 고객을 형사 고소하기", "Filing police complaints against rejected loan applicants")],
     "설명 가능성(Explainability)은 AI의 블랙박스 예측 과정을 투명하게 밝혀 규제 준수와 고객 권리를 보장하는 핵심 역량입니다."),

    ("SHAP Values & Feature Attribution", "SHAP 기여도 값 분석",
     "모델의 최종 예측에 각 입력 변수(소득, 부채, 연체 이력 등)가 얼마나 긍정적 또는 부정적 영향을 미쳤는지 정량적으로 설명하는 게임 이론 기반 기법은 무엇입니까?",
     "Which game-theoretic attribution method quantifies each input feature's marginal mathematical contribution to an individual AI prediction?",
     "샤플리 기여도 값 (SHAP Values / Shapley Additive Explanations)", "SHAP Values (Shapley Additive Explanations)",
     [("텍스트 단어의 알파벳 철자 개수 세기", "Counting the alphabet character lengths of input words"),
      ("단순 무작위 동전 던지기 가중치 부여", "Assigning random coin-flip weights to variables"),
      ("데이터 파일의 크기(KB)로만 기여도 측정", "Measuring contribution purely by file size in kilobytes")],
     "SHAP 값은 게임 이론을 바탕으로 각 피처의 기여도를 공정하게 배분하여 모델의 설명 가능성 리포트를 생성하는 표준 기법입니다."),

    ("Amazon SageMaker Clarify Operations", "세이지메이커 클래리파이 편향 감지",
     "데이터 준비 단계와 모델 학습 후 단계에서 잠재적 편향을 자동으로 감지하고, SHAP 값 기반의 설명 리포트를 생성하는 AWS 서비스는 무엇입니까?",
     "Which AWS service automates bias detection across training datasets and deployed models while generating SHAP-based feature attribution reports?",
     "Amazon SageMaker Clarify", "Amazon SageMaker Clarify",
     [("Amazon Simple Storage Service (S3) 버킷 생성기", "Amazon S3 bucket creation wizard"),
      ("AWS Direct Connect 전용선 연결 도구", "AWS Direct Connect physical fiber optic provisioning"),
      ("Amazon Elastic File System (EFS) 파일 공유", "Amazon EFS network file share mount scripts")],
     "Amazon SageMaker Clarify는 데이터셋의 불균형 감지, 모델의 편향 분석, SHAP 기반 피처 중요도 분석을 원클릭으로 제공하는 RAI 핵심 도구입니다."),

    ("Personally Identifiable Information (PII) Protection", "개인 식별 정보(PII) 보호",
     "이름, 주민등록번호, 여권번호, 카드번호 등 개인을 특정할 수 있는 민감 정보가 AI 모델 입력창이나 학습에 무단 활용되지 않도록 하는 거버넌스 조치는 무엇입니까?",
     "Which compliance measure prevents sensitive personal identifiers like Social Security numbers and phone numbers from model ingestion?",
     "개인 식별 정보 (Personally Identifiable Information / PII) 보호 및 마스킹", "Personally Identifiable Information (PII) protection and masking",
     [("모든 개인정보를 사내 게시판에 텍스트로 공개 게시", "Posting raw customer SSNs on public intranet noticeboards"),
      ("개인정보 암호화 키를 외부에 무료 공개하기", "Publishing customer encryption keys on external blogs"),
      ("보안 정책을 폐지하고 완전 자율에 맡기기", "Abolishing all corporate data privacy policies")],
     "PII(개인 식별 정보)는 GDPR, 개인정보보호법에 따라 모델에 입력되기 전에 반드시 마스킹되거나 암호화되어야 합니다."),

    ("Automated PII Masking & Redaction", "자동화된 PII 마스킹",
     "고객이 상담창에 신용카드 번호나 주민번호를 실수로 입력하더라도, 모델이 이를 보기 전에 자동으로 `[REDACTED]` 처리하는 기능은 무엇입니까?",
     "Which security filter automatically detects and redacts credit card digits and government IDs into placeholders before prompt transmission?",
     "Amazon Bedrock Guardrails의 민감 정보 필터 (Sensitive Information Filters)", "Amazon Bedrock Guardrails Sensitive Information Filters (PII Redaction)",
     [("사용자에게 개인정보를 입력하지 말라고 구두 경고만 하기", "Relying purely on verbal warnings asking users not to enter PII"),
      ("상담원의 모니터 전원을 끄는 조치", "Turning off the customer service agent's monitor screen"),
      ("모든 고객 문의를 무조건 즉시 삭제하기", "Deleting all customer support inquiries immediately")],
     "Amazon Bedrock Guardrails의 민감 정보 필터는 정규식과 ML을 활용하여 PII를 실시간 감지하고 자동 마스킹(Redaction)합니다."),

    ("AWS Customer Data Protection Pledge", "AWS 고객 데이터 보호 서약",
     "엔터프라이즈 고객이 Amazon Bedrock이나 Amazon Q에 입력한 프롬프트 및 비즈니스 데이터에 대해 AWS가 공식 계약으로 보장하는 핵심 보안 원칙은 무엇입니까?",
     "What contractual privacy commitment does AWS provide regarding customer prompts, inputs, and knowledge bases processed via Amazon Bedrock?",
     "고객의 데이터는 절대 AWS 기본 파운데이션 모델의 학습이나 개선에 사용되지 않음", "Customer data is never used to train or improve AWS base foundation models",
     [("고객의 모든 기밀 데이터를 제3자 광고주에게 판매함", "Selling enterprise customer prompts to third-party ad networks"),
      ("고객의 소스코드를 오픈소스 깃허브에 자동 공개함", "Automatically publishing customer proprietary code to public GitHub"),
      ("고객 데이터를 주말마다 인터넷에 무료 배포함", "Freely distributing customer database snapshots on weekends")],
     "AWS는 고객의 프롬프트와 지식 베이스 데이터가 기본 모델 재학습에 결코 사용되지 않으며, 고객 계정 내에서 안전하게 격리됨을 보증합니다."),

    ("Transparency & AI Disclosure Mandates", "투명성 및 AI 사용 고지 의무",
     "소비자가 고객 상담 챗봇이나 전화 상담을 이용할 때, 자신이 대화하는 상대가 인간이 아닌 AI 시스템임을 명확히 알 수 있도록 하는 원칙은 무엇입니까?",
     "Which regulatory mandate obligates enterprises to inform consumers explicitly that they are conversing with an autonomous AI system?",
     "투명성 및 AI 상호작용 명시적 고지 의무 (Transparency & AI Disclosure)", "Transparency and mandatory AI disclosure",
     [("챗봇을 인간 상담원인 것처럼 완벽히 속이기", "Deliberately deceiving consumers into believing an AI is a real human"),
      ("AI 이용 약관을 보이지 않는 투명 글씨로 숨겨두기", "Hiding terms of service in transparent invisible HTML font"),
      ("고객의 질문에 아무런 답변도 하지 않기", "Configuring chatbots to remain completely silent")],
     "투명성(Transparency) 원칙 및 EU AI Act에 따라, 기업은 소비자가 AI와 상호작용하고 있음을 명확하게 사전에 고지해야 합니다."),

    ("Synthetic Media & Digital Watermarking", "합성 미디어 디지털 워터마킹",
     "생성형 AI가 제작한 마케팅 이미지나 영상에 비가시적 메타데이터(C2PA 표준)를 삽입하여 출처를 증명하고 딥페이크 위조를 방지하는 기술은 무엇입니까?",
     "Which technological standard embeds imperceptible, cryptographically verifiable metadata into AI-generated media to guarantee provenance?",
     "디지털 워터마킹 및 출처 증명 (Digital Watermarking & C2PA Standards)", "Digital Watermarking and C2PA Provenance Standards",
     [("이미지 파일의 이름을 대문자로 바꾸기", "Renaming image file extensions to uppercase letters"),
      ("모든 이미지를 흑백으로만 강제 변환하기", "Converting all enterprise marketing assets strictly to monochrome"),
      ("이미지의 해상도를 극단적으로 낮추어 흐리게 만들기", "Downsampling image resolutions to 10x10 pixels")],
     "디지털 워터마킹(Digital Watermarking)은 AI 생성물에 암호화된 출처 정보를 각인하여 딥페이크 위조를 방지하고 투명성을 보장합니다."),

    ("Safety & Controllability Guardrails", "안전성 및 제어성 가드레일",
     "AI 모델이 유해 콘텐츠, 폭력적 지침, 증오 발언, 사이버 공격 코드를 생성하지 못하도록 차단하는 최우선 보호 장치는 무엇입니까?",
     "Which protection mechanism blocks generative AI systems from synthesizing toxic, offensive, violent, or cyber-attack instructions?",
     "안전성 및 제어성 가드레일 (Safety Guardrails)", "Safety and Controllability Guardrails",
     [("모델의 입출력 필터를 완전히 비활성화하기", "Disabling all input/output content inspection filters"),
      ("유해 프롬프트를 입력한 사용자에게 보상금 지급하기", "Rewarding users who submit illegal prompts with discount coupons"),
      ("서버의 전력 공급을 차단하여 전원 끄기", "Cutting physical power lines to the cloud provider")],
     "안전성 및 제어성(Safety & Controllability)은 부적절한 유해 생성을 원천 차단하여 기업의 브랜드와 사회적 책임을 보호합니다."),

    ("Kill-Switch Mechanism & Circuit Breakers", "비상 정지 메커니즘 (Kill-Switch)",
     "운영 중인 생성형 AI 시스템이 예상치 못한 치명적 오작동을 일으키거나 기밀을 유출할 때, 즉시 추론 트래픽을 차단하고 롤백하는 프로토콜은 무엇입니까?",
     "Which emergency circuit breaker protocol terminates AI model inference traffic instantaneously during a catastrophic failure or breach?",
     "비상 정지 메커니즘 (Kill-Switch Mechanism / Emergency Circuit Breaker)", "Kill-Switch Mechanism and Emergency Circuit Breakers",
     [("오작동을 보면서 3년간 아무런 조치도 취하지 않기", "Observing catastrophic failures for three years without intervening"),
      ("오작동하는 모델의 API 호출 한도를 10배로 늘리기", "Increasing rate limits ten-fold on corrupted model endpoints"),
      ("모든 관리자의 로그인 비밀번호를 삭제하기", "Deleting all administrator login credentials during an incident")],
     "Kill-Switch 메커니즘은 중대 보안/규제 사고 발생 시 시스템을 즉시 안전 모드로 격리하여 2차 피해를 차단하는 필수 안전장치입니다."),

    ("Robustness against Adversarial Attacks", "적대적 공격 대응 및 견고성",
     "사용자가 모델을 속여 안전 지침을 우회하려는 프롬프트 탈옥(Jailbreak) 시도에도 시스템이 흔들리지 않고 보안 정책을 유지하는 역량은 무엇입니까?",
     "Which attribute reflects an AI system's ability to maintain policy compliance and security integrity against malicious jailbreak attacks?",
     "적대적 공격에 대한 견고성 (Robustness against Adversarial Attacks)", "Robustness against Adversarial Attacks",
     [("사용자의 모든 악성 요구를 100% 무조건 수용하기", "Complying with 100% of malicious user requests without resistance"),
      ("보안 팀원들을 모두 해고하고 보안 부서를 해체하기", "Disbanding the enterprise cyber security department entirely"),
      ("방화벽 포트를 전 세계에 활짝 열어두기", "Opening all database ports to the global public internet")],
     "견고성(Robustness)은 적대적 프롬프트 주입 공격을 실시간 감지하여 정책 우회를 차단하고 안정적인 성능을 유지하는 능력입니다."),

    ("Amazon Bedrock Guardrails Architecture", "베드록 가드레일 아키텍처",
     "파운데이션 모델의 종류와 관계없이 중앙에서 일괄적으로 유해 콘텐츠 필터링, 민감 정보 마스킹, 금지 주제 차단을 적용하는 AWS 기능은 무엇입니까?",
     "Which unified AWS policy layer enforces content filters, denied topics, and PII masking across multiple foundation models independently?",
     "Amazon Bedrock Guardrails", "Amazon Bedrock Guardrails",
     [("Amazon Route 53 DNS 도메인 등록기", "Amazon Route 53 DNS domain registrar"),
      ("AWS Snowball 물리적 하드웨어 디스크", "AWS Snowball edge computing appliances"),
      ("Amazon Simple Queue Service (SQS) 메시지 큐", "Amazon SQS asynchronous message queues")],
     "Amazon Bedrock Guardrails는 모델에 구애받지 않고 엔터프라이즈 보안 정책을 단일 인터페이스로 중앙 통제하는 완전관리형 가드레일입니다."),

    ("Denied Topics Enforcement", "금지된 주제 (Denied Topics) 차단",
     "기업의 정책상 AI 어시스턴트가 '경쟁사 제품 추천', '공식 승인되지 않은 법률/세무 자문' 등에 대해 답변하지 못하도록 원천 차단하는 Bedrock 기능은 무엇입니까?",
     "Which Amazon Bedrock Guardrails feature strictly forbids models from entertaining discussions on unauthorized subjects like competitor products?",
     "금지된 주제 차단 (Denied Topics)", "Denied Topics Enforcement",
     [("컴퓨터 바탕화면 아이콘 숨기기", "Hiding desktop icons on client machines"),
      ("사내 키보드의 스페이스바 키보드 분리", "Physically removing spacebars from employee keyboards"),
      ("질문할 때마다 이용료를 부과하는 유료화", "Charging mandatory micro-transactions for each user prompt")],
     "Denied Topics는 기업이 허용하지 않은 주제에 대해 명시적인 거절 메시지를 출력하도록 강제하여 브랜드 위험을 방지합니다."),

    ("Contextual Grounding Check for Hallucinations", "문맥적 근거 검사 (Grounding Check)",
     "RAG 시스템에서 모델의 답변이 검색된 사내 문서에 사실적으로 근거하고 있는지 검증하여 지어낸 허위 사실(환각)을 실시간 차단하는 Guardrails 기능은 무엇입니까?",
     "Which capability within Bedrock Guardrails mathematically scores and blocks hallucinations that lack grounding in retrieved reference sources?",
     "문맥적 근거 검사 (Contextual Grounding Check)", "Contextual Grounding Check",
     [("인터넷 소설 사이트의 글을 프롬프트에 자동 주입하기", "Injecting fictional internet web novels into prompt context"),
      ("검색된 모든 문서를 즉시 폐기하고 추측으로 답변하기", "Discarding retrieved facts and guessing answers randomly"),
      ("환각이 발생할 때마다 박수를 치도록 스피커 설정하기", "Playing sound effects whenever models hallucinate")],
     "Contextual Grounding Check는 생성된 문장이 원본 검색 문서의 내용과 일치하는지 검증하여 거짓 정보를 사전에 걸러냅니다."),

    ("Human-in-the-Loop (HITL) High-Risk Escalation", "고위험 시나리오 인간 참여형 검증",
     "대출 심사 거절, 고액 보험금 지급 거부, 채용 서류 탈락 등 개인의 권리에 중대한 영향을 미치는 고위험 결정 시 반드시 구축해야 하는 아키텍처는 무엇입니까?",
     "In high-consequence enterprise workflows impacting individual rights (e.g., loan denials), what governance architecture is mandatory?",
     "인간 전문가가 최종 검토 및 승인을 수행하는 인간 참여형 검증 (Human-in-the-Loop / HITL)", "Human-in-the-Loop (HITL) with mandatory human expert review and sign-off",
     [("100% 자율 AI에게 모든 거절 권한을 전적으로 위임하기", "Delegating 100% of final rejection authority strictly to autonomous algorithms"),
      ("신청서를 검토하지 않고 모두 무작위로 거절하기", "Randomly rejecting all applications without reading"),
      ("심사 결과를 10년 후에 통보하기", "Delaying application results for a decade")],
     "HITL(인간 참여형 검증)은 고위험 의사결정의 오차를 방지하고 윤리적/법적 책임을 확보하기 위해 인간 전문가의 최종 승인을 의무화합니다."),

    ("Amazon Augmented AI (Amazon A2I) Workflows", "Amazon A2I 워크플로우",
     "머신러닝 모델의 예측 신뢰도 점수가 사전 설정된 임계치(예: 80%) 미만일 때, 인간 검토자 풀에게 작업을 자동 라우팅하는 AWS 서비스는 무엇입니까?",
     "Which AWS service automates human review workflows when model inference confidence falls below predetermined operational thresholds?",
     "Amazon Augmented AI (Amazon A2I)", "Amazon Augmented AI (Amazon A2I)",
     [("AWS CloudShell 웹 브라우저 터미널", "AWS CloudShell browser command-line interface"),
      ("Amazon DynamoDB NoSQL 데이터베이스", "Amazon DynamoDB key-value tables"),
      ("AWS Glue ETL 데이터 카탈로그", "AWS Glue data crawler pipelines")],
     "Amazon A2I는 모델의 신뢰도가 낮거나 무작위 감사 대상인 데이터를 인간 검토자 풀에 전달하여 정확도를 담보하는 완전관리형 HITL 서비스입니다."),

    ("EU AI Act Four-Tier Risk Classification", "EU AI Act 위험 등급 분류",
     "유럽연합 인공지능법(EU AI Act)에서 AI 시스템을 규제하기 위해 분류한 4단계 위험 등급 체계는 무엇입니까?",
     "What four-tier risk classification taxonomy does the European Union AI Act establish to determine regulatory obligations?",
     "허용 불가 위험(Unacceptable), 고위험(High), 제한적 위험(Limited), 최소 위험(Minimal)", "Unacceptable Risk, High Risk, Limited Risk, and Minimal Risk",
     [("위험 없음, 중간 위험, 매우 위험의 3단계", "Three tiers: No Risk, Medium Risk, Very High Risk"),
      ("초급, 중급, 고급의 사용자 등급 체계", "Novice, Intermediate, and Advanced user tiers"),
      ("무료, 유료, 엔터프라이즈의 가격 등급 체계", "Free, Pro, and Enterprise pricing tiers")],
     "EU AI Act는 위험도에 따라 AI를 4등급으로 나누어, 허용 불가 위험은 전면 금지하고 고위험 AI에는 엄격한 규제를 적용합니다."),

    ("Unacceptable Risk Banned AI", "EU AI Act 허용 불가 위험",
     "EU AI Act에 따라 인간의 존엄성과 기본권을 침해하여 법적으로 전면 금지(Banned)되는 AI 시스템 유형은 무엇입니까?",
     "Under the EU AI Act, which AI systems are classified as Unacceptable Risk and strictly banned from deployment?",
     "정부의 사회적 신용 평가(Social Scoring) 및 공공장소 실시간 원격 생체 인식", "Governmental Social Scoring and real-time remote biometric identification in public spaces",
     [("전자상거래 상품 추천 알고리즘", "E-commerce product recommendation carousels"),
      ("고객 서비스 안내 챗봇", "Customer service conversational chatbots"),
      ("스팸 이메일 자동 분류 필터", "Spam email classification filters")],
     "사회적 신용 점수 평가, 행동 조작, 실시간 안면 인식 등은 기본권을 심각하게 침해하므로 허용 불가 위험(Unacceptable Risk)으로 전면 금지됩니다."),

    ("High-Risk AI Mandatory Conformity", "EU AI Act 고위험 AI 의무",
     "채용 및 인사 선발, 대출 신용 평가, 핵심 인프라 운영에 AI를 도입할 때 EU AI Act에 따라 반드시 준수해야 하는 의무는 무엇입니까?",
     "What mandatory legal obligations are imposed by the EU AI Act on High-Risk AI deployments such as recruitment and credit underwriting?",
     "적합성 평가, 엄격한 데이터 품질 거버넌스, 설명 가능성 및 인간 감독(Human Oversight) 의무", "Conformity assessments, rigorous data governance, transparency, and human oversight",
     [("모든 규제를 면제받고 완전 자율 운영", "Complete exemption from all regulatory audits and inspections"),
      ("외국 법률을 준수할 필요가 없다는 확인서 작성", "Certifying immunity from all international regulations"),
      ("사내 모든 소프트웨어 코드를 삭제하기", "Deleting all software codebases")],
     "고위험 AI(High Risk)는 적합성 평가(Conformity Assessment), 철저한 데이터 거버넌스, 로깅 및 인간 감독(HITL)이 법적으로 강제됩니다."),

    ("Limited & Minimal Risk Regulatory Obligations", "제한적 및 최소 위험 AI 의무",
     "고객 서비스 챗봇이나 딥페이크 생성 도구와 같은 '제한적 위험(Limited Risk)' AI에 법적으로 요구되는 유일한 핵심 의무는 무엇입니까?",
     "For AI applications falling into the Limited Risk tier under the EU AI Act (e.g., customer chatbots), what primary legal duty is mandated?",
     "사용자가 AI와 상호작용하고 있음을 명확히 알 수 있도록 하는 '투명성 및 고지 의무'", "Transparency obligations ensuring users are explicitly informed they are interacting with an AI",
     [("수억 원의 벌금을 납부하고 사업을 중단하기", "Paying heavy administrative fines and shutting down the business"),
      ("모든 소프트웨어를 정부에 헌납하기", "Transferring ownership of the software to government ministries"),
      ("인터넷 사용을 영구 중단하기", "Banning all employees from using web browsers")],
     "제한적 위험(Limited Risk) AI는 사용자가 AI와 대화하고 있음을 명확히 인지할 수 있도록 하는 '투명성 고지 의무'만 준수하면 됩니다."),

    ("ISO/IEC 42001 (AIMS) Global Standard", "ISO/IEC 42001 인공지능 경영시스템",
     "조직이 책임감 있게 AI 시스템을 개발, 도입, 관리하고 있음을 제3자가 공인하는 최초의 국제 표준 인증은 무엇입니까?",
     "Which inaugural international certifiable standard establishes enterprise requirements for an AI Management System (AIMS)?",
     "ISO/IEC 42001 (인공지능 경영시스템 인증)", "ISO/IEC 42001 (Artificial Intelligence Management System)",
     [("ISO 9001 일반 제조업 품질 인증", "ISO 9001 classical manufacturing quality certifications"),
      ("사내 동호회 친목 회칙 인증", "Internal corporate sports club charter bylaws"),
      ("운전면허증 제1종 보통 인증", "Commercial vehicle driving licenses")],
     "ISO/IEC 42001은 기업의 AI 위험 관리, 윤리적 거버넌스, 투명한 운영 체계를 종합 심사하여 공인하는 글로벌 AI 인증 표준입니다."),

    ("NIST AI Risk Management Framework", "NIST AI 위험 관리 프레임워크",
     "미국 국립표준기술원(NIST)이 제정한 엔터프라이즈 AI 위험 관리 가이드라인의 4대 핵심 기능은 무엇입니까?",
     "What are the four core functions delineated by the NIST AI Risk Management Framework (NIST AI RMF)?",
     "거버넌스(Govern), 매핑(Map), 측정(Measure), 관리(Manage)", "Govern, Map, Measure, and Manage",
     [("구입(Buy), 판매(Sell), 보관(Store), 폐기(Trash)", "Buy, Sell, Store, and Trash"),
      ("설계(Plan), 코딩(Code), 빌드(Build), 배포(Deploy)", "Plan, Code, Build, and Deploy"),
      ("조회(Select), 삽입(Insert), 수정(Update), 삭제(Delete)", "Select, Insert, Update, and Delete")],
     "NIST AI RMF는 조직이 AI 위험을 거버넌스(Govern)하고, 식별(Map)하며, 분석(Measure)하고, 완화(Manage)하도록 돕는 프레임워크입니다."),

    ("Cross-Functional AI Governance Committee", "다학제적 AI 거버넌스 위원회",
     "AI 거버넌스를 IT/엔지니어링 부서에만 맡겨두지 않고, 전사적 리스크와 가치를 균형 있게 심의하기 위해 위원회에 반드시 참여해야 하는 핵심 구성원은 누구입니까?",
     "To ensure AI systems align with corporate ethics and legal compliance, what cross-functional stakeholders must populate the AI Governance Council?",
     "비즈니스 리더, IT/데이터 엔지니어, 법무(Legal), 컴플라이언스, 정보보안, HR/윤리 담당자", "Line-of-Business executives, IT engineers, Legal, Compliance, Cyber Security, and HR/Ethics leaders",
     [("오직 소프트웨어 주니어 인턴 개발자들로만 구성", "Exclusively junior software engineering interns"),
      ("회사에 출입하는 외부 택배 기사님들로만 구성", "External logistics delivery personnel"),
      ("경쟁사 회사의 임원진으로만 구성", "Executive leadership of market competitor firms")],
     "AI 거버넌스 위원회는 기술적 타당성뿐 아니라 법률, 컴플라이언스, 평판, 윤리적 리스크를 종합 심의하기 위해 다학제적(Cross-Functional)으로 구성되어야 합니다."),

    ("Model Cards & System Cards Documentation", "모델 카드 및 시스템 카드",
     "모델의 훈련 데이터 분포, 성능 벤치마크 점수, 의도된 용도, 알려진 한계점과 사용상 제약 사항을 투명하게 문서화하는 표준 규격은 무엇입니까?",
     "Which standardized artifact documents a foundation model's architectural traits, intended use cases, performance benchmarks, and known limitations?",
     "모델 카드 (Model Cards) 및 시스템 카드 (System Cards)", "Model Cards and System Cards",
     [("사내 메신저의 비밀 일기장", "Personal diaries written in internal messaging tools"),
      ("식당 영수증 뒷면에 적은 볼펜 메모", "Notes written on paper restaurant receipts"),
      ("소프트웨어 바이너리 파일의 16진수 덤프", "Raw hexadecimal memory dump files")],
     "모델 카드와 시스템 카드는 모델의 기능과 한계를 투명하게 공개하여 사용자가 올바른 맥락에서 안전하게 모델을 사용하도록 돕는 표준 문서입니다."),

    ("Model Lineage & Audit Trail Tracking", "모델 계보 및 감사 추적",
     "규제 기관의 감사 시 특정 모델이 어떤 원본 데이터셋 버전, 어떤 전처리 파이프라인, 어떤 하이퍼파라미터로 학습되었는지 불변 로그로 증명하는 역량은 무엇입니까?",
     "Which capability tracks data origins, preprocessing pipelines, code revisions, and hyperparameters to provide immutable regulatory auditability?",
     "모델 계보 추적 (Model Lineage Tracking via Amazon SageMaker Lineage)", "Model Lineage Tracking via Amazon SageMaker Lineage",
     [("과거 학습 코드를 모두 휴지통에 넣고 비우기", "Emptying the operating system recycling bin"),
      ("학습 로그 파일의 날짜를 임의로 조작하기", "Manually editing timestamp dates in log text files"),
      ("감사 요청이 오면 서버 전원 스위치를 끄기", "Powering down server hardware upon receiving audit subpoenas")],
     "모델 계보 추적(Model Lineage)은 학습 데이터부터 배포된 아티팩트까지의 전 과정을 추적하여 재현성과 규제 감사 대응력을 확보합니다."),

    ("Copyright Infringement & Cloud Indemnification", "저작권 침해 및 클라우드 면책 보증",
     "생성형 AI 모델이 원작자의 저작권을 침해했다는 이유로 제3자로부터 소송이 제기될 경우, 클라우드 벤더(AWS)가 고객을 법적으로 보호하고 배상해주는 제도는 무엇입니까?",
     "Which cloud contractual safeguard defends and indemnifies enterprise customers against third-party IP infringement claims arising from GenAI outputs?",
     "저작권 면책 보증 (Copyright / IP Indemnification Pledge)", "Copyright and Intellectual Property Indemnification",
     [("소송 비용을 고객사가 전액 부담한다는 조항", "Clause requiring customers to pay all legal fees of the cloud provider"),
      ("저작권 소송이 발생하면 고객 계정을 즉시 폐쇄하는 조항", "Clause terminating customer accounts upon receiving third-party complaints"),
      ("소송 결과를 무시하고 도망치도록 권유하는 조항", "Legal advice suggesting executives flee jurisdictional boundaries")],
     "AWS 등 주요 클라우드 벤더는 고객이 가드레일을 준수하며 정상적으로 상용 서비스를 사용할 때 저작권 침해 소송에 대해 법적 면책(Indemnification)을 제공합니다."),

    ("Operational Incident Response Protocol", "AI 보안 사고 대응 절차",
     "운영 중인 챗봇이 유해 콘텐츠를 생성하거나 프롬프트 주입 공격을 당해 기밀이 유출되었을 때, 팀이 즉시 격리, 로깅, 보고, 롤백을 수행하는 표준 지침은 무엇입니까?",
     "Which operational SOP outlines immediate isolation, forensic telemetry preservation, stakeholder notification, and remediation during an AI security failure?",
     "AI 보안 사고 대응 프로토콜 (AI Security Incident Response Protocol)", "AI Security Incident Response Protocol",
     [("사고를 숨기고 언론에 거짓 해명 자료를 배포하기", "Concealing the breach and publishing fraudulent denials to media"),
      ("사고 발생 원인을 모두 고객의 탓으로 돌리기", "Blaming the security failure entirely on end-user prompts"),
      ("사고가 발생해도 평소처럼 아무런 조치 없이 방치하기", "Ignoring alerts and taking zero remediation actions")],
     "AI 사고 대응 프로토콜은 사고 발생 시 피해를 최소화하고 증거를 보존하며 신속한 시스템 복구를 지원하는 표준 운영 절차입니다.")
]

# 30 Distinct Categories for Domain 4 (Business Readiness, Leadership & Transformation)
D4_TAXONOMY = [
    ("4 Dimensions of AI Readiness", "AI 준비성 4대 차원 진단",
     "기업이 전사적 AI 도입을 추진하기 전에 반드시 종합적으로 진단해야 하는 조직의 4대 핵심 역량 축은 무엇입니까?",
     "What four foundational organizational dimensions must enterprise leadership evaluate to audit comprehensive readiness for AI adoption?",
     "People(인력/문화), Process(프로세스/민첩성), Technology(기술/인프라), Governance(거버넌스/데이터)", "People (culture/skills), Process (agility/workflows), Technology (cloud/infra), and Governance (data/ethics)",
     [("책상, 의자, 컴퓨터 모니터, 마우스의 4대 비품", "Office desks, ergonomic chairs, desktop monitors, and mice"),
      ("봄, 여름, 가을, 겨울의 4계절 기후", "Spring, Summer, Autumn, and Winter climate variables"),
      ("조식, 중식, 석식, 야식의 4대 식사 메뉴", "Breakfast, Lunch, Dinner, and Midnight snack cafeteria schedules")],
     "성공적인 AI 전환은 단순히 모델(Tech)만 도입한다고 되지 않으며, 사람(People), 프로세스(Process), 데이터 거버넌스(Governance)가 균형을 이루어야 합니다."),

    ("AI Maturity Stage 1: Exploration", "AI 성숙도 1단계: 탐색 및 실험",
     "소규모 팀이나 개별 직원이 비공식적으로 챗봇을 테스트해 보거나 소규모 PoC를 시도하지만, 전사 표준이나 가이드라인이 전혀 없는 성숙도 단계는 무엇입니까?",
     "Which initial AI maturity phase is characterized by fragmented, uncoordinated grassroots experiments without centralized oversight or standards?",
     "1단계: 탐색 및 실험 단계 (Exploration & Experimentation)", "Stage 1: Exploration and Experimentation",
     [("전 직원이 AI를 주도하는 전사 혁신 단계", "Stage 4: Transformational AI-Driven Enterprise"),
      ("전사 AI CoE가 통제하는 체계화 단계", "Stage 3: Systematic Operationalized Stage"),
      ("클라우드 도입을 전면 거부하는 구석기 단계", "Paleolithic Stage refusing all digital technology")],
     "탐색 단계(Exploration)는 부서별로 산발적인 PoC가 시작되는 초기 단계로, 지식 공유와 전사 거버넌스가 결여되어 있는 상태입니다."),

    ("AI Maturity Stage 2: Opportunistic", "AI 성숙도 2단계: 기회 포착 및 시범",
     "특정 선도 사업 부서(예: 마케팅팀)에서 AI 파일럿의 성공 사례가 나오기 시작하지만, 여전히 타 부서와 사일로가 존재하고 거버넌스가 미흡한 단계는 무엇입니까?",
     "Which AI maturity stage features localized pilot successes within specific departments but still lacks centralized governance and cross-unit scale?",
     "2단계: 기회 포착 및 시범 도입 단계 (Opportunistic / Piloting)", "Stage 2: Opportunistic and Piloting Stage",
     [("모든 비즈니스 모델이 AI 중심으로 재편된 단계", "Stage 4: Complete AI Transformation"),
      ("AI에 대해 아무도 모르는 완전 무지 단계", "Stage 0: Total Corporate Ignorance"),
      ("사내 모든 컴퓨터를 압류한 단계", "Asset Liquidation Stage")],
     "기회 포착 단계(Opportunistic)는 개별 부서의 성공은 존재하지만, 전사적인 표준 플랫폼과 데이터 공유 체계가 확립되지 않은 상태입니다."),

    ("AI Maturity Stage 3: Systematic", "AI 성숙도 3단계: 체계화 및 운영",
     "중앙에 AI Center of Excellence(CoE)가 설립되고, AWS 기반의 전사 표준 AI 플랫폼과 거버넌스 가이드라인이 정립되어 안정적으로 확장되는 단계는 무엇입니까?",
     "Which maturity level is marked by the formal establishment of an AI CoE, standardized cloud platforms, and centralized RAI guardrails?",
     "3단계: 체계화 및 운영 단계 (Systematic / Operationalized)", "Stage 3: Systematic and Operationalized Stage",
     [("개별 직원들이 각자 몰래 챗봇을 쓰는 단계", "Stage 1: Fragmented Ad-hoc Exploration"),
      ("AI 도입을 법적으로 포기한 단계", "Surrender Stage abandoning modern technology"),
      ("회사의 문을 닫고 폐업하는 단계", "Corporate Insolvency Stage")],
     "체계화 단계(Systematic)는 중앙 CoE가 플랫폼과 거버넌스를 표준화하여 부서 간 중복 투자를 없애고 안전하게 스케일업하는 단계입니다."),

    ("AI Maturity Stage 4: Transformational", "AI 성숙도 4단계: 전사 혁신",
     "전 직원이 일상 업무에서 AI를 보조 도구로 자연스럽게 활용하며, 기업의 비즈니스 모델 자체가 AI를 중심으로 새롭게 재편된 최고 성숙도 단계는 무엇입니까?",
     "What pinnacle maturity tier represents an organization where business models are fundamentally AI-driven and culture embraces continuous augmentation?",
     "4단계: 전사적 혁신 단계 (Transformational / AI-Driven)", "Stage 4: Transformational and AI-Driven Enterprise",
     [("파일럿 하나도 성공하지 못한 초기 단계", "Stage 1: Unsuccessful initial lab prototype"),
      ("AI 프로젝트를 모두 취소하고 옛날로 돌아간 단계", "Regressive Stage returning to paper forms"),
      ("회사 주식을 모두 매각하고 해체된 단계", "Liquidation Stage")],
     "전사 혁신 단계(Transformational)는 단순한 비용 절감을 넘어 비즈니스 모델 전체가 AI 기반으로 작동하며 시장을 선도하는 최종 단계입니다."),

    ("AWS Cloud Adoption Framework (CAF) AI/ML Lens", "AWS CAF AI/ML 렌즈 프레임워크",
     "기업의 클라우드 및 AI 전환 준비 상태를 비즈니스, 피플, 거버넌스, 플랫폼, 보안, 운영의 6대 관점(Perspectives)에서 체계적으로 진단하는 프레임워크는 무엇입니까?",
     "Which AWS methodology evaluates readiness across Business, People, Governance, Platform, Security, and Operations perspectives for AI adoption?",
     "AWS Cloud Adoption Framework (AWS CAF) - AI/ML Lens", "AWS Cloud Adoption Framework (AWS CAF) - AI/ML Lens",
     [("단순한 컴퓨터 부품 가격 견적서", "Hardware price quotation catalog"),
      ("사내 축구 동호회 경기 규칙집", "Internal employee soccer tournament rulebook"),
      ("사무실 청소 당번 순번표", "Office janitorial duty rotation schedule")],
     "AWS CAF AI/ML Lens는 6대 핵심 관점에서 기업의 현재 준비 상태를 진단하고 실행 가능한 로드맵을 수립하도록 돕는 공식 방법론입니다."),

    ("Data Silos Organizational Friction", "데이터 사일로와 전사 확장 저해",
     "마케팅, 영업, 물류 부서마다 데이터베이스가 단절되어 있어, AI 모델이 전체 고객 여정을 학습하지 못하고 성능이 떨어지는 근본적 조직 문제는 무엇입니까?",
     "What organizational defect describes departmental data repositories isolated in silos, preventing comprehensive enterprise AI integration?",
     "데이터 사일로 (Data Silos)", "Data Silos",
     [("사내 초고속 광랜 인터넷 속도", "Gigabit fiber internet connectivity"),
      ("서버실의 완벽한 24시간 냉방 장치", "24/7 server room air conditioning"),
      ("개발자들의 친절한 사내 미팅 태도", "Polite communication manners during standup meetings")],
     "데이터 사일로(Data Silos)는 전사적 협업과 데이터 융합을 가로막아 AI 프로젝트의 확장을 저해하는 가장 큰 병목입니다."),

    ("Data Mesh Decentralized Architecture", "데이터 메시 탈중앙화 아키텍처",
     "중앙 IT 데이터팀의 처리 병목을 해소하기 위해, 각 도메인 부서가 자신의 데이터를 '데이터 프로덕트'로 직접 소유하고 관리하는 아키텍처는 무엇입니까?",
     "Which architectural paradigm organizes analytical data around autonomous domain business teams treating data as a product under federated governance?",
     "데이터 메시 (Data Mesh)", "Data Mesh Architecture",
     [("모든 데이터를 단 하나의 외장 하드에 복사해 두기", "Copying all company files to a single USB flash drive"),
      ("모든 데이터 공유를 전면 금지하고 방화벽 닫기", "Severing all network connections between departments"),
      ("매일 모든 데이터베이스를 종이로 출력하기", "Printing entire relational databases onto paper sheets daily")],
     "데이터 메시(Data Mesh)는 도메인 팀에게 데이터 소유권을 부여하여 중앙 집중식 병목을 없애고 전사적 데이터 활용을 극대화합니다."),

    ("Amazon DataZone Federated Cataloging", "Amazon DataZone 데이터 거버넌스",
     "비즈니스 사용자와 기술팀이 도메인 간 데이터를 검색, 카탈로그화, 공유하고 데이터 메시 거버넌스를 구현할 수 있도록 지원하는 AWS 서비스는 무엇입니까?",
     "Which fully managed AWS service provides a business data portal to discover, catalog, subscribe to, and govern data products across domains?",
     "Amazon DataZone", "Amazon DataZone",
     [("Amazon Route 53 DNS 서버 관리자", "Amazon Route 53 DNS host manager"),
      ("AWS Snowmobile 초대형 데이터 트럭", "Ordering an AWS Snowmobile 45-foot container truck"),
      ("Amazon Simple Email Service 이메일 발송기", "Amazon SES transactional email dispatchers")],
     "Amazon DataZone은 데이터 생산자와 소비자를 비즈니스 용어 기반 카탈로그로 연결하여 안전한 데이터 공유와 거버넌스를 제공합니다."),

    ("AWS Lake Formation Granular Access", "AWS Lake Formation 세분화 권한",
     "데이터 레이크에 저장된 방대한 테이블에 대해 열(Column) 및 행(Row) 수준의 세분화된 보안 권한을 중앙에서 일괄 제어하는 AWS 서비스는 무엇입니까?",
     "Which AWS security service simplifies data lake creation while enforcing granular column- and row-level access permissions across analytical tools?",
     "AWS Lake Formation", "AWS Lake Formation",
     [("컴퓨터 바탕화면 화면보호기 설정", "Configuring operating system screensaver timeout delays"),
      ("서버실 입구의 열쇠 자물쇠 교체", "Replacing physical brass padlocks on server room doors"),
      ("마우스 패드의 인체공학적 교체", "Purchasing ergonomic silicone mouse pads for data entry clerks")],
     "AWS Lake Formation은 최소 권한 원칙(PoLP)에 따라 분석가와 AI 모델이 민감한 개인정보 열을 제외하고 허가된 데이터만 조회하도록 통제합니다."),

    ("Data Contracts between Producers & AI", "데이터 계약 (Data Contracts)",
     "업스트림 데이터 엔지니어링 팀이 사전 통보 없이 데이터베이스 스키마를 변경하여 다운스트림 AI 모델이 갑자기 중단되는 사고를 방지하는 거버넌스 협약은 무엇입니까?",
     "What explicit agreement between upstream data producers and downstream AI consumers establishes schema versioning and freshness guarantees?",
     "데이터 계약 (Data Contracts)", "Data Contracts",
     [("팀원들끼리 구두로 나눈 약속", "Informal verbal agreements over coffee breaks"),
      ("데이터가 깨져도 아무런 알림을 보내지 않겠다는 각서", "Pledges never to fire alerts when pipelines fail"),
      ("모든 데이터 파이프라인의 모니터링 경보를 무음 처리하기", "Muting all pipeline error alarms permanently")],
     "데이터 계약(Data Contracts)은 데이터 생산자와 AI 소비자 간의 공식적인 약속으로, 스키마 변경 사전 공지와 품질 기준을 의무화합니다."),

    ("Internal SLAs for Pipeline Stability", "파이프라인 내부 SLA",
     "AI 모델에 공급되는 데이터의 최신성(Freshness), 전송 지연 시간(Latency), 결측치 허용 임계값을 사전에 규정하는 내부 약정은 무엇입니까?",
     "What internal operational agreement defines acceptable data pipeline latency, data freshness, and maximum error thresholds for AI ingestion?",
     "내부 서비스 수준 협약 (Internal SLAs)", "Internal Service Level Agreements (SLAs)",
     [("사내 식당의 점심 배식 시간표", "Cafeteria lunch service timetable schedules"),
      ("사무실 에어컨 가동 희망 온도표", "Thermostat temperature preference charts in office halls"),
      ("직원들의 주간 휴가 신청 계획서", "Annual leave application balance sheets")],
     "내부 SLA는 데이터 파이프라인의 가용성과 품질 기준을 명확히 하여 다운스트림 AI 애플리케이션의 신뢰성을 보장합니다."),

    ("AI Center of Excellence (CoE) Mandate", "AI CoE의 사명과 역할",
     "전사 AI 전략 수립, 클라우드 아키텍처 표준화, 재사용 가능한 프롬프트/에셋 큐레이션, 거버넌스 표준을 총괄하는 중앙 전문 조직은 무엇입니까?",
     "Which central governance body formulates enterprise AI strategy, standardizes architectures, manages reusable assets, and guides compliance?",
     "AI 우수성 센터 (AI Center of Excellence / AI CoE)", "AI Center of Excellence (CoE)",
     [("사내 주차장 관리 위원회", "Corporate parking lot space allocation committee"),
      ("사무실 비품 구매 전담 태스크포스", "Office stationary procurement committee"),
      ("사내 탁구 동호회 집행부", "Intra-company table tennis tournament executive board")],
     "AI CoE는 전사 AI 혁신을 체계적으로 리드하고, 부서 간 중복 투자를 방지하며, 공통 거버넌스 표준을 수립하는 핵심 조직입니다."),

    ("Centralized vs Decentralized CoE Trade-offs", "중앙 집중형 vs 분산형 CoE 비교",
     "AI 조직 구조에서 중앙 집중형(일관성은 높으나 현업 대응 지연)과 분산형(현업 민첩성은 높으나 중복 투자 및 사일로 발생)의 한계를 극복한 모델은 무엇입니까?",
     "Which hybrid operating model balances the central governance of centralized teams with the business domain agility of decentralized teams?",
     "허브 앤 스포크 모델 (Hub-and-Spoke Model)", "Hub-and-Spoke Operating Model",
     [("AI 전담 팀을 완전히 해체하고 각자도생하기", "Abolishing all AI governance and permitting total shadow IT"),
      ("모든 소프트웨어 개발을 100% 외주사에 하청 주기", "Outsourcing 100% of internal technology to unvetted contractors"),
      ("단 1명의 개발자에게 회사의 모든 AI 업무를 떠넘기기", "Assigning all enterprise systems to a single junior software engineer")],
     "허브 앤 스포크(Hub-and-Spoke) 모델은 중앙의 거버넌스 통제력과 현업 부서의 도메인 문제 해결 민첩성을 동시에 달성하는 최적의 조직 구조입니다."),

    ("Hub-and-Spoke CoE Operating Model", "허브 앤 스포크 CoE 운영 모델",
     "중앙 CoE(Hub)가 인프라, 거버넌스 가이드라인, 공통 도구를 제공하고, 각 사업 부서의 실무자(Spoke)가 비즈니스 문제를 직접 해결하는 조직 모델의 명칭은 무엇입니까?",
     "In enterprise AI organization, what model pairs a central governing core (Hub) with embedded domain product teams (Spokes)?",
     "허브 앤 스포크 (Hub-and-Spoke) 조직 모델", "Hub-and-Spoke Organizational Model",
     [("모든 직원이 1개의 책상에 모여 앉는 단일 모델", "A monolithic model where 5,000 employees sit around one table"),
      ("부서 간 대화를 엄격히 법적으로 금지하는 분리 모델", "A segregated model legally banning cross-departmental dialogue"),
      ("조직도를 완전히 없애고 무정부 상태를 만드는 모델", "An anarchic model with zero management hierarchy")],
     "Hub-and-Spoke 모델은 중앙의 표준화(Hub)와 현장의 유연성(Spoke)을 결합하여 대규모 엔터프라이즈 AI 확장에 가장 적합합니다."),

    ("AI Champions Grassroots Network", "AI 챔피언 네트워크의 목적",
     "비기술 현업 부서(인사, 재무, 마케팅) 전반에서 일상적인 AI 도구 활용을 촉진하고 동료들을 코칭하기 위해 임명하는 풀뿌리 리더 네트워크는 무엇입니까?",
     "Which grassroots network embeds peer-coaches across non-technical business units to foster daily prompt literacy and surface local use cases?",
     "AI 챔피언 네트워크 (AI Champions Network)", "AI Champions Network",
     [("사내 비밀 감찰단", "Covert internal corporate surveillance spies"),
      ("주말 등산 동호회 임원진", "Weekend hiking club officers"),
      ("사내 매점 바코드 스캔 도우미", "Cafeteria barcode scanning volunteer staff")],
     "AI 챔피언은 현업 동료들에게 AI 활용법을 전수하고, 부서의 페인 포인트를 발굴하여 중앙 CoE에 연결하는 풀뿌리 혁신의 주역입니다."),

    ("Peer-Coaching & Use Case Discovery", "동료 코칭과 유스케이스 발굴",
     "AI 챔피언이 현업 부서 내에서 수행하는 가장 가치 있는 일상적 활동은 무엇입니까?",
     "What is the most impactful operational responsibility fulfilled by departmental AI Champions on a day-to-day basis?",
     "동료들에게 실무 프롬프트 팁을 코칭하고, 부서 내 파급력 높은 비즈니스 유스케이스를 발굴하여 CoE에 전달함", "Peer-coaching colleagues on effective prompt patterns and surfacing high-impact departmental use cases to the CoE",
     [("동료들의 컴퓨터 모니터를 몰래 훔쳐보는 감시 활동", "Spying on colleagues' desktop monitors to catch personal web browsing"),
      ("부서의 모든 문서를 파쇄기에 넣어 분쇄하기", "Shredding all paper documents in industrial waste disposal units"),
      ("AI 도입을 방해하기 위해 컴퓨터 바이러스를 유포하기", "Distributing malware to intentionally damage cloud workflows")],
     "AI 챔피언은 동료들의 거부감을 줄이고 일상 업무에 맞는 프롬프트 모범 사례를 전파하는 가교 역할을 수행합니다."),

    ("Augmentation over Replacement Philosophy", "'대체가 아닌 증강' 철학",
     "AI 어시스턴트 도입 과정에서 일자리 상실을 우려하여 소프트웨어 사용을 거부하는 직원들의 심리적 저항을 극복하기 위한 리더십 철학은 무엇입니까?",
     "When frontline workers resist AI tools out of fear of job loss, what change management leadership philosophy addresses this cultural anxiety?",
     "'대체(Replacement)가 아닌 증강(Augmentation)' 원칙을 천명하고, 반복 업무를 AI에 맡겨 인간은 고부가가치 창의 업무로 승격하도록 지원", "Championing an 'Augmentation over Replacement' philosophy, proving AI eliminates drudgery to elevate human creativity",
     [("AI에 우려를 표하는 모든 직원을 즉각 징계하고 해고하기", "Threatening immediate termination for any employee expressing fear"),
      ("직원들의 키보드 입력을 몰래 감시하는 프로그램을 설치하기", "Secretly deploying covert keyloggers to force AI compliance"),
      ("AI 도입을 전면 백지화하고 구시대 수작업으로 회귀하기", "Cancelling all modernization and returning to 19th-century manual ledgers")],
     "리더십은 AI가 인간을 대체하는 것이 아니라 능력을 배가시켜 주는 도구임을 명확히 하고, 직무 재교육(Upskilling)과 안정감을 제공해야 합니다."),

    ("Psychological Safety in AI Adoption", "심리적 안전감과 실험 문화",
     "직원들이 새로운 AI 기술을 두려움 없이 실험하고, AI 도구의 결함이나 오류를 솔직하게 피드백할 수 있도록 보장하는 조직 문화적 환경은 무엇입니까?",
     "What cultural attribute ensures employees feel safe experimenting with new generative AI tools and reporting flaws without fear of punishment?",
     "심리적 안전감 (Psychological Safety)", "Psychological Safety",
     [("엄격한 상명하복의 군대식 공포 분위기", "Strict authoritarian corporate fear cultures"),
      ("실수를 저지른 직원의 실명을 사내 로비에 공개 전시하기", "Publicly displaying names of employees who make mistakes on lobby billboards"),
      ("모든 실패에 대해 급여 삭감 페널티를 부과하기", "Deducting salaries for any experimental prototype defect")],
     "심리적 안전감(Psychological Safety)이 조성되어야만 직원들이 처벌에 대한 두려움 없이 과감히 AI를 실험하고 혁신을 이룰 수 있습니다."),

    ("Role-Based Upskilling Curricula", "직무별 맞춤형 재교육 커리큘럼",
     "전사 AI 리터러시를 높이기 위해 경영진, 비즈니스 기획자, 소프트웨어 개발자 등 각 직무의 페르소나에 맞춰 차별화된 교육을 제공하는 전략은 무엇입니까?",
     "To systematically elevate organizational literacy, which educational strategy crafts distinct training curricula tailored to specific professional personas?",
     "직무별 맞춤형 재교육 (Role-Based Upskilling / Persona-Based Training)", "Role-Based Upskilling and Persona-Based Training Curricula",
     [("모든 직원에게 C++ 언어로 하드웨어 반도체를 설계하도록 강요하기", "Forcing all HR staff to study low-level C++ semiconductor design"),
      ("교육을 일체 제공하지 않고 각자 알아서 공부하도록 방치하기", "Providing zero educational resources and penalizing lack of knowledge"),
      ("사내 도서관의 모든 책을 불태우기", "Burning all educational books in corporate training centers")],
     "직무별 맞춤형 재교육은 임원진(전략 및 거버넌스), 기획자(프롬프트 및 ROI), 개발자(API 및 MLOps) 등 각자에게 실질적으로 필요한 역량을 키워줍니다."),

    ("Culture of Experimentation & Fail Fast", "실험 문화와 빠른 학습",
     "새로운 생성형 AI 아이디어를 검증할 때, 완벽한 기획서를 쓰느라 1년을 낭비하는 대신 2주 만에 시제품을 만들어 빠르게 검증하는 애자일 문화를 무엇이라 합니까?",
     "Which agile cultural value encourages teams to validate AI hypotheses rapidly via 2-week prototypes rather than spending months writing speculative plans?",
     "실험 문화 및 빠른 실패 (Culture of Experimentation & Fail Fast)", "A Culture of Experimentation and Fast Learning (Fail Fast)",
     [("10년간 기획안만 작성하고 개발은 전혀 하지 않는 문화", "Spending ten years drafting planning binders without writing one line of code"),
      ("첫 시도에서 완벽하지 않으면 프로젝트 팀을 해체하는 문화", "Disbanding project teams if their very first alpha release has any flaws"),
      ("모든 소프트웨어 릴리스를 5년에 1번씩만 허용하는 문화", "Permitting software deployments only once every five fiscal years")],
     "실험 문화는 작은 가설을 빠르게 프로토타이핑하여 시장 반응을 살피고, 실패로부터 신속히 배워 성공 확률을 높이는 애자일 혁신의 정수입니다."),

    ("AWS PartyRock No-Code Prototyping", "AWS PartyRock 노코드 프로토타이핑",
     "비개발자 직원들이 코딩 없이 프롬프트만으로 단 몇 분 만에 직관적인 생성형 AI 미니 앱을 만들고 공유할 수 있는 AWS의 노코드 플레이그라운드는 무엇입니까?",
     "Which intuitive no-code web environment empowers non-technical business employees to build and share generative AI mini-apps using natural language prompts?",
     "AWS PartyRock", "AWS PartyRock",
     [("C 언어 저수준 컴파일러 도구", "Low-level C programming language compiler utilities"),
      ("리눅스 커널 소스코드 빌더", "Linux operating system kernel compilation terminals"),
      ("데이터베이스 서버실 네트워크 패치 케이블", "Physical Ethernet network patching cables in server closets")],
     "AWS PartyRock은 비개발자도 프롬프트만으로 손쉽게 AI 앱을 만들고 사내 해커톤에서 아이디어를 빠르게 실체화할 수 있도록 지원합니다."),

    ("Secure Prototyping Sandboxes", "안전한 사내 프로토타이핑 샌드박스",
     "현업 직원들이 사내 기밀 유출 걱정 없이 안전하게 최신 파운데이션 모델을 실험하고 프롬프트를 테스트할 수 있도록 제공해야 하는 격리 환경은 무엇입니까?",
     "Which controlled environment enables staff to experiment with foundation models without risk of leaking proprietary corporate IP to public consumer clouds?",
     "Amazon Bedrock Guardrails가 적용된 격리된 사내 프로토타이핑 샌드박스 (Secure Internal Sandbox)", "Secure Prototyping Sandbox governed by Amazon Bedrock Guardrails",
     [("직원 개인 스마트폰으로 검증되지 않은 무료 외부 챗봇을 쓰도록 지시", "Instructing employees to use unvetted consumer chatbots on personal phones"),
      ("AWS 계정의 루트(Root) 마스터 비밀번호를 모든 직원에게 공유", "Distributing root administrative AWS credentials to all temporary contractors"),
      ("AI 실험을 전면 금지하고 AI를 언급하면 처벌하기", "Banning all AI prototyping and penalizing staff who propose innovative tools")],
     "사내 보안 샌드박스는 Bedrock Guardrails를 통해 기밀 유출을 차단하면서 직원들이 자유롭게 프롬프트 엔지니어링을 실험하도록 보장합니다."),

    ("AWS 4-Stage Innovation: Envision", "4단계 혁신: Envision (구상)",
     "AWS AI 혁신 프레임워크의 첫 번째 단계로, 해결하고자 하는 비즈니스 문제를 정의하고 고임팩트 유스케이스를 발굴하여 우선순위를 매기는 단계는 무엇입니까?",
     "What is the foundational first phase in the AWS AI transformation lifecycle focused on business alignment, value definition, and use case prioritization?",
     "1단계: Envision (구상 및 가치 정의)", "Stage 1: Envision (Alignment and Value Definition)",
     [("소프트웨어 코딩부터 무작정 시작하는 단계", "Haphazardly writing raw software scripts without knowing the business problem"),
      ("서버 장비를 구매하기 위해 모든 예산을 탕진하는 단계", "Exhausting all financial reserves buying servers before scoping projects"),
      ("프로젝트를 완료하고 서비스를 종료하는 단계", "Project Termination and Decommissioning Phase")],
     "Envision 단계는 기술 도입에 앞서 '어떤 비즈니스 문제를 해결할 것인가'를 명확히 하고 고가치 유스케이스를 발굴하는 전략적 시작점입니다."),

    ("AWS 4-Stage Innovation: Experiment", "4단계 혁신: Experiment (실험)",
     "AWS AI 혁신 프레임워크의 두 번째 단계로, 소규모 PoC(개념 증명)를 통해 기술적 실현 가능성을 신속하게 검증하고 가치를 타진하는 단계는 무엇입니까?",
     "What second phase in the AWS transformation framework focuses on agile proof-of-concept validation, testing hypotheses, and failing fast?",
     "2단계: Experiment (실험 및 PoC 검증)", "Stage 2: Experiment (Rapid Prototyping and Hypothesis Validation)",
     [("전 세계 모든 고객에게 검증되지 않은 제품을 즉시 배포하기", "Deploying untested code globally to millions of live customers on day one"),
      ("실험을 일체 금지하고 기획서만 10년간 결재받기", "Banning all coding experiments in favor of decade-long paperwork reviews"),
      ("개발팀 전원에게 휴가를 보내고 개발을 중단하기", "Halting all engineering operations and sending staff home")],
     "Experiment 단계는 소규모 프로토타입으로 가설을 빠르게 검증하여 실제 비즈니스 가치가 있는지 확인하는 '빠른 학습' 단계입니다."),

    ("AWS 4-Stage Innovation: Launch", "4단계 혁신: Launch (출시)",
     "AWS AI 혁신 프레임워크의 세 번째 단계로, 파일럿 사용자 그룹을 대상으로 최소 기능 제품(MVP)을 배포하여 초기 피드백을 수렴하는 단계는 무엇입니까?",
     "Which third transformation phase releases a Minimum Viable Product (MVP) to a controlled pilot cohort to harvest feedback and establish baseline metrics?",
     "3단계: Launch (출시 및 파일럿 배포)", "Stage 3: Launch (Pilot Deployment and MVP Release)",
     [("제품 개발을 전면 백지화하고 프로젝트를 포기하는 단계", "Abandoning the project and deleting all repositories"),
      ("성과 측정을 거부하고 홍보 기사만 배포하는 단계", "Publishing press releases while keeping systems offline"),
      ("고객 피드백 수렴을 법적으로 금지하는 단계", "Legally prohibiting users from submitting feedback reports")],
     "Launch 단계는 제한된 파일럿 그룹에 MVP를 공개하여 실제 운영 환경에서의 피드백을 수렴하고 안정성을 검증하는 단계입니다."),

    ("AWS 4-Stage Innovation: Scale", "4단계 혁신: Scale (전사 확장)",
     "AWS AI 혁신 프레임워크의 마지막 단계로, 파일럿의 성공을 바탕으로 전사 조직에 배포를 확산하고, MLOps/LLMOps를 적용하며 지속적 ROI를 창출하는 단계는 무엇입니까?",
     "What concluding transformation phase scales validated solutions enterprise-wide, operationalizing MLOps pipelines and maximizing sustained ROI?",
     "4단계: Scale (전사적 확장 및 MLOps 운영)", "Stage 4: Scale (Enterprise-wide Scaling and MLOps Integration)",
     [("소프트웨어를 삭제하고 초기 PoC 단계로 다시 되돌아가는 단계", "Deleting production software and regressing to day-one brainstorming"),
      ("모든 AI 시스템을 끄고 운영을 영구 중단하는 단계", "Powering down all AI inference servers permanently"),
      ("사내 AI CoE를 해체하고 거버넌스를 폐지하는 단계", "Disbanding the CoE and ending all enterprise governance")],
     "Scale 단계는 자동화된 MLOps/LLMOps 파이프라인과 CoE 거버넌스를 결합하여 전사적인 비즈니스 가치를 대규모로 수확하는 단계입니다."),

    ("Business Process Re-engineering (BPR)", "비즈니스 프로세스 재설계",
     "구시대적인 복잡한 결재선과 수작업 업무 절차에 단순히 AI 챗봇을 덧붙이는 것이 아니라, AI의 역량에 맞춰 전체 워크플로우를 근본적으로 재설계하는 혁신은 무엇입니까?",
     "Rather than simply superimposing AI onto legacy manual bureaucracy, what discipline radically redesigns end-to-end workflows around AI capabilities?",
     "비즈니스 프로세스 재설계 (Business Process Re-engineering / BPR)", "Business Process Re-engineering (BPR)",
     [("낡은 종이 결재판의 페인트 색상만 새로 칠하기", "Repainting physical wooden office memo trays"),
      ("기존의 비효율적인 수작업 절차를 100% 그대로 유지하기", "Rigidly enforcing legacy manual bureaucracy without any modification"),
      ("모든 결재 단계를 10단계 더 늘려 프로세스를 더 느리게 만들기", "Adding ten additional redundant manual approval steps to slow down operations")],
     "BPR은 기존 프로세스에 단순히 AI를 끼워 넣는 것이 아니라, AI와 인간의 협업에 최적화되도록 전체 업무 흐름을 근본적으로 재구성하는 혁신입니다."),

    ("Technical Debt Mitigation in AI", "AI 기술 부채 완화",
     "버전 관리나 MLOps 파이프라인 없이 임시방편으로 배포된 모델, 관리되지 않는 프롬프트 템플릿으로 인해 장기적으로 발생하는 유지보수 위험을 방지하는 조치는 무엇입니까?",
     "What engineering governance mitigates long-term AI Technical Debt stemming from unversioned models, ad-hoc scripts, and unmanaged prompt templates?",
     "표준화된 MLOps/LLMOps 파이프라인 구축 및 프롬프트/데이터/모델 버전 관리", "Standardized MLOps/LLMOps CI/CD pipelines and rigorous version control",
     [("모든 소프트웨어 버전 관리를 중단하고 바탕화면에 메모하기", "Abolishing Git version control in favor of desktop sticky notes"),
      ("파이프라인 오류가 발생해도 로그를 남기지 않기", "Configuring systems to never log errors or track pipeline states"),
      ("코드를 작성하지 않고 모든 작업을 수동 클릭으로만 때우기", "Relying purely on manual console clicks without any infrastructure-as-code")],
     "AI 기술 부채를 방지하려면 조기에 MLOps/LLMOps 표준을 확립하여 프롬프트, 데이터, 모델의 버전을 체계적으로 관리해야 합니다."),

    ("Ethical AI Whistleblowing & Safety Reporting", "윤리적 AI 안전 제보 채널",
     "사내에서 개발되거나 운영 중인 AI 모델이 심각한 편향, 차별, 또는 불법적 기밀 유출을 일으킬 때, 직원들이 불이익 없이 안전하게 보고할 수 있는 거버넌스 채널은 무엇입니까?",
     "Which organizational governance channel provides a confidential, non-punitive avenue for staff to escalate ethical AI risks, bias, or safety flaws?",
     "윤리적 AI 내부 고발 및 안전 제보 채널 (Ethical AI Whistleblowing / Safety Reporting Channel)", "Ethical AI Safety Reporting and Whistleblower Protection Channels",
     [("윤리적 문제를 제기하는 직원을 즉시 징계하는 비밀 감찰반", "Internal disciplinary squads punishing any employee who raises safety concerns"),
      ("모든 보안 제보 이메일을 스팸함으로 자동 분류하여 삭제하기", "Configuring safety mailbox rules to permanently delete whistleblower reports"),
      ("안전성 문제를 외부에 공개적으로 자랑하기", "Bragging publicly about unresolved security defects on social media")],
     "윤리적 AI 제보 채널은 직원들이 잠재적 위험이나 편향을 발견했을 때 보복에 대한 두려움 없이 즉시 경영진과 거버넌스 협의체에 알릴 수 있도록 보장합니다.")
]

def main():
    print("=== Generating Full 1,200 Question Bank with 120 Distinct Categories ===")
    
    from build_deduplicated_question_bank import generate_domain_questions
    
    # 1. Domain 1 (30 categories x 10 = 300 questions)
    d1 = generate_domain_questions(1, "AI 기초 및 활용 능력 (AI Fundamentals and Literacy)", D1_TAXONOMY, 300)
    print(f"Domain 1: Generated {len(d1)} questions across {len(D1_TAXONOMY)} categories.")
    
    # 2. Domain 2 (30 categories x 10 = 300 questions)
    d2 = generate_domain_questions(2, "AI 전략 및 비즈니스 가치 창출 (AI Strategy & Business Value Creation)", D2_TAXONOMY, 300)
    print(f"Domain 2: Generated {len(d2)} questions across {len(D2_TAXONOMY)} categories.")
    
    # 3. Domain 3 (30 categories x 10 = 300 questions)
    d3 = generate_domain_questions(3, "AI 거버넌스 및 책임 있는 AI 리더십 (AI Governance & Responsible AI Leadership)", D3_TAXONOMY, 300)
    print(f"Domain 3: Generated {len(d3)} questions across {len(D3_TAXONOMY)} categories.")
    
    # 4. Domain 4 (30 categories x 10 = 300 questions)
    d4 = generate_domain_questions(4, "비즈니스 준비성, 리더십, AI 혁신 (Business Readiness, Leadership & Transformation)", D4_TAXONOMY, 300)
    print(f"Domain 4: Generated {len(d4)} questions across {len(D4_TAXONOMY)} categories.")
    
    # Save each domain json
    with open(os.path.join(QUESTIONS_DIR, 'questions_domain1.json'), 'w', encoding='utf-8') as f:
        json.dump(d1, f, ensure_ascii=False, indent=2)
    with open(os.path.join(QUESTIONS_DIR, 'questions_domain2.json'), 'w', encoding='utf-8') as f:
        json.dump(d2, f, ensure_ascii=False, indent=2)
    with open(os.path.join(QUESTIONS_DIR, 'questions_domain3.json'), 'w', encoding='utf-8') as f:
        json.dump(d3, f, ensure_ascii=False, indent=2)
    with open(os.path.join(QUESTIONS_DIR, 'questions_domain4.json'), 'w', encoding='utf-8') as f:
        json.dump(d4, f, ensure_ascii=False, indent=2)
    print("✓ All 4 domain JSON files written.")

    # Canonical Mock Exam 1: 60 questions from 60 distinct categories!
    # D1: 12 categories, D2: 19 categories, D3: 16 categories, D4: 13 categories (12 + 19 + 16 + 13 = 60)
    # Pick 1 question from each selected category
    mock_qs = []
    # D1: categories 0 to 11 (12 questions)
    for c_idx in range(12):
        mock_qs.append(d1[c_idx * 10]) # 1 question per category
    # D2: categories 0 to 18 (19 questions)
    for c_idx in range(19):
        mock_qs.append(d2[c_idx * 10])
    # D3: categories 0 to 15 (16 questions)
    for c_idx in range(16):
        mock_qs.append(d3[c_idx * 10])
    # D4: categories 0 to 12 (13 questions)
    for c_idx in range(13):
        mock_qs.append(d4[c_idx * 10])
        
    assert len(mock_qs) == 60, f"Expected 60 mock questions, got {len(mock_qs)}"
    
    with open(os.path.join(QUESTIONS_DIR, 'mock_exam_1.json'), 'w', encoding='utf-8') as f:
        json.dump(mock_qs, f, ensure_ascii=False, indent=2)
    print("✓ Canonical 60-question mock exam written (all 60 from 60 distinct categories).")

    # Combine all
    all_pool = d1 + d2 + d3 + d4
    exam_data = {
        "domain1": d1,
        "domain2": d2,
        "domain3": d3,
        "domain4": d4,
        "mock1": mock_qs,
        "all_pool": all_pool
    }
    
    js_content = (
        "// AWS Certified AI Business Strategist (AIB-C01) Complete Question Bank\n"
        f"// Total {len(all_pool)} Questions across 120 Distinct Topic Categories (30 per Domain)\n"
        f"const EXAM_DATA = {json.dumps(exam_data, ensure_ascii=False, indent=2)};\n\n"
        "if (typeof window !== 'undefined') {\n  window.EXAM_DATA = EXAM_DATA;\n}\n"
        "if (typeof module !== 'undefined' && module.exports) {\n  module.exports = EXAM_DATA;\n}\n"
    )
    
    with open(os.path.join(BASE_DIR, 'questions-data.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)
    with open(os.path.join(BASE_DIR, 'cbt-app', 'questions-data.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("✓ Synchronized questions-data.js and cbt-app/questions-data.js")
    print("\n🎉 ALL 1,200 QUESTIONS GENERATED & COMPILED WITH ZERO REDUNDANCY! 🎉")

if __name__ == '__main__':
    main()
