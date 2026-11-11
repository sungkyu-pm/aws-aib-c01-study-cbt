#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part 3 of the Master Glossary & Exam Expressions Builder for AWS AIB-C01.
Generates:
- Part 4: 산업 도메인별(바이오·제조·R&D·소매·유통·금융·헬스케어) 실전 빈출 영문 표현 & KPI 사전
- Combines Part 1, Part 2, Part 3, and existing Domain 1~4 Master Glossary tables into docs/01_GLOSSARY_KR_EN.md.
"""

from pathlib import Path
from build_master_glossary_part1 import PART1_MD
from build_master_glossary_part2 import PART2_MD

PART3_MD = """
---

## 🏭 Part 4. 산업 도메인별(바이오·제조·R&D·소매·유통·금융) 실전 빈출 영문 표현 & KPI 사전

실제 `AIB-C01` 시험은 단순 IT 기업이 아니라 **바이오/제약, 스마트 제조, 기업 R&D 연구소, 옴니채널 소매, 콜드체인 물류·유통, 금융/보험** 등 다양한 산업 현장의 고유 제약조건과 KPI를 지문에 등장시킵니다.

| 산업 도메인 (Industry Domain) | 시험 지문 빈출 핵심 영문 표현 (Domain-Specific Exam Terminology) | 핵심 비즈니스 가치 KPI & 아키텍처 정답 패턴 |
| :--- | :--- | :--- |
| **🧬 바이오 / 제약 / 임상**<br>(Bio / Pharma / Clinical Trials) | • **Target Identification & Lead Optimization** (신약 타겟 발굴 및 선도물질 최적화)<br>• **De Novo Molecular / Protein Design** (신규 분자·단백질 구조 생성)<br>• **Clinical Trial Patient Stratification** (임상시험 환자군 정밀 층화/선별)<br>• **GxP Compliance & FDA 21 CFR Part 11 Audit Trail** (의약품 제조·품질관리 기준 및 전자기록 무결성 감사 추적)<br>• **Pharmacovigilance / Adverse Event Detection** (약물감시 및 이상반응 탐지) | • **KPI**: `Phase-Transition Success Rate` (임상 단계 진입 성공률), `Time-to-IND Filing` (임상시험계획 승인 신청 단축 기간)<br>• **아키텍처 정답**: 환자 유전체/임상 데이터는 `HIPAA/GxP` 준수 환경에서 **Differential Privacy(차등 프라이버시) 합성 데이터** 활용, 모든 모델 버전·데이터 혈통을 `SageMaker Model Lineage`로 불변 기록, 임상 의사결정은 반드시 **전문의 HITL(Human-in-the-Loop)** 필수. |
| **⚙️ 스마트 제조 / 반도체 / 설비**<br>(Smart Manufacturing & Fab) | • **Predictive Maintenance (PdM) & Remaining Useful Life (RUL)** (예지보전 및 잔여 수명 예측)<br>• **Overall Equipment Effectiveness (OEE)** (설비종합효율 = 가동률 × 성능 × 양품률)<br>• **Sub-10ms Edge Computer Vision Defect Inspection** (10ms 미만 초저지연 엣지 비전 불량 검출)<br>• **OT (Operational Technology) Air-Gapped Network** (공장 폐쇄망 환경)<br>• **Digital Twin & PLC/SCADA Telemetry** (디지털 트윈 및 제어기 센서 텔레메트리) | • **KPI**: `Unplanned Downtime Reduction (%)` (비계획 설비 정지 감소율), `First-Pass Yield (FPY)` (초도 양품률), `Scrap Rate Reduction` (폐기율 감소), `False-Positive Line Stop Rate` (오탐지로 인한 라인 정지율)<br>• **아키텍처 정답**: 고속 생산라인(초당 수십 개 부품 이동)이나 네트워크 단절 위험이 있는 공장은 클라우드 왕복 지연(Latency)을 피하기 위해 **클라우드에서 학습·양자화(`SageMaker Edge / IoT Greengrass`)한 경량 비전 모델을 현장 Edge IPC에 배포**하고, 이상 샘플만 클라우드로 비동기 업로드하여 재학습(`Edge-Cloud Hybrid Loop`). |
| **🔬 기업 R&D (배터리·소재·화학)**<br>(Corporate R&D & Materials) | • **Electronic Lab Notebooks (ELN) & LIMS** (전자연구노트 및 실험실 정보관리 시스템)<br>• **Trade Secret & Proprietary Formulation Leakage** (핵심 영업비밀 및 독점 배합비 유출)<br>• **High-Throughput Virtual Screening** (고속 가상 물질 스크리닝)<br>• **Inverse Materials Design & Surrogate Simulation** (역설계 및 물리 시뮬레이션 대리 모델)<br>• **Prior Art Patent Search & Multi-Hop GraphRAG** (선행특허 조사 및 다단계 지식그래프 검색) | • **KPI**: `Experiment Cycle Time Reduction` (실험 주기 단축률), `Failed Wet-Lab Experiment Avoidance` (실패할 물리 실험 사전 회피 비용 절감), `R&D Engineer Retrieval Productivity`<br>• **아키텍처 정답**: 수십 년간 축적된 비정형 실험노트·특허·분자구조식은 외부 공개 모델 학습에 절대 유출되면 안 되므로 **`AWS PrivateLink` + Zero-Training Policy + 문서 등급별 ACL이 적용된 Hybrid GraphRAG** 로 구축. |
| **🛍️ 옴니채널 소매 / 이커머스**<br>(Omnichannel Retail & E-Commerce) | • **Hyper-Personalized Cross-Sell / Up-Sell** (초개인화 교차판매·상향판매)<br>• **Shopping Cart Abandonment & Churn Propensity** (장바구니 이탈 및 고객 이탈 성향)<br>• **Store Planogram Optimization & Markdown Pricing** (매대 진열 최적화 및 재고 소진 할인율 최적화)<br>• **Stockout Rate vs. Inventory Carrying Cost** (품절률 vs. 재고 유지비 트레이드오프)<br>• **Visual Search & Virtual Try-On** (시각 검색 및 가상 피팅) | • **KPI**: `Conversion Rate Uplift` (구매 전환율 상승), `Average Order Value (AOV) / Basket Size` (객단가), `Gross Margin Return on Inventory (GMROI)`, `Return Rate Reduction` (반품률 감소)<br>• **아키텍처 정답**: 실시간 개인화 추천은 `Amazon Personalize` 같은 관리형 서비스(Buy)로 빠르게 구축하여 `Time-to-Market`을 단축하고, 인과적 매출 증분은 반드시 **Holdout 대조군 기반 A/B 테스트(`Incremental Revenue Uplift`)** 로 증명. |
| **🚚 콜드체인 유통 / 글로벌 물류**<br>(Cold-Chain & Supply Chain Logistics) | • **SKU-Location Demand Forecasting** (품목·거점별 정밀 수요 예측)<br>• **Cold-Chain Spoilage & Temperature Excursion** (신선식품/백신 콜드체인 부패 및 온도 이탈)<br>• **Dynamic Last-Mile Route Optimization** (실시간 라스트마일 배송 경로 최적화)<br>• **Warehouse Management System (WMS) Slotting** (물류센터 적치 위치 최적화)<br>• **Bullwhip Effect Mitigation** (공급망 채찍 효과 완화) | • **KPI**: `MAPE (Mean Absolute Percentage Error)` 또는 `WAPE` (수요예측 오차율 감소), `Spoilage / Waste Rate (%)` (폐기율 감소), `On-Time In-Full (OTIF)` (정시·전량 납품률), `Fuel Cost per Delivery`<br>• **아키텍처 정답**: 기상 악화·항만 파업 등 외부 변수로 인해 과거 통계 패턴이 깨질 때는(`Concept Drift`), 외부 거시/기상 피처를 결합한 **앙상블 시계열 모델 + 이상 징후 감지 시 공급망 플래너 HITL 개입 구조**를 설계. |
| **🏦 금융 / 핀테크 / 보험**<br>(FinTech, Banking & Insurance) | • **Equal Credit Opportunity Act (ECOA) & Adverse Action Notice** (신용평등법 및 대출 거절 사유 통지 의무)<br>• **Real-Time Fraud Detection (Sub-50ms SLA)** (50ms 이내 실시간 이상거래 탐지)<br>• **False Positive Customer Friction vs. False Negative Fraud Loss** (오탐지로 인한 정상 카드 결제 차단 불편 vs. 미탐지로 인한 사기 손실)<br>• **Straight-Through Processing (STP) in Claims** (보험금 청구 무인 자동 심사 처리율) | • **KPI**: `Fraud Loss Reduction ($)`, `False Decline Rate` (정상 고객 오차단율), `Claims Processing Turnaround Time`, `Regulatory Audit Pass Rate`<br>• **아키텍처 정답**: 대출/보험 심사 모델은 규제 당국과 소비자에게 개별 거절 사유를 투명하게 제시해야 하므로 불투명한 거대 블랙박스 단독 사용을 피하고 **`XGBoost` 등 해석 가능한 모델 + `SageMaker Clarify (Local SHAP Values)`** 를 결합. |

---
"""


def main():
    glossary_path = Path("/Users/sungkyu/Study/AI BS_AWS/docs/01_GLOSSARY_KR_EN.md")
    existing_text = glossary_path.read_text(encoding="utf-8")

    # Find where the original Domain 1 table begins so we preserve all original domain tables as Part 5
    marker = "## 1. 도메인 1: AI/ML 및 생성형 AI의 비즈니스 전략적 기초"
    if marker in existing_text:
        domain_tables_part = existing_text[existing_text.index(marker):]
        # Rename section headers to fit cleanly under Part 5
        domain_tables_part = (
            "## 📚 Part 5. 도메인 1~4 전 범위 핵심 마스터 용어 사전 (Domain-by-Domain Reference)\n\n"
            + domain_tables_part
        )
    else:
        domain_tables_part = existing_text

    full_markdown = PART1_MD.strip() + "\n\n" + PART2_MD.strip() + "\n\n" + PART3_MD.strip() + "\n\n" + domain_tables_part.strip() + "\n"
    glossary_path.write_text(full_markdown, encoding="utf-8")
    print(f"[SUCCESS] Updated {glossary_path} ({len(full_markdown):,} chars, {len(full_markdown.splitlines()):,} lines)")


if __name__ == "__main__":
    main()
