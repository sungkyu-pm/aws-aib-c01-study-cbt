#!/usr/bin/env python3
"""
AWS Certified AI Business Strategist (AIB-C01)
Practice Exam Question Injector for Domain 1-4 Deep Dive Guides
Injects concrete, authentic 4-choice practice questions into each of the 30 summary
topics across Domains 1, 2, 3, and 4 (120 topics total).
"""

import os
import re
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Mapping of section number (1 to 30) to question index or question ID
# For Domain 1 (30 sections)
D1_MAP = {
    1: "D1-Q001",   # AI vs ML vs GenAI Hierarchy
    2: "D1-Q011",   # Structured vs Unstructured Data Selection
    3: "D1-Q021",   # Rule-Based RPA vs Probabilistic AI
    4: "D1-Q031",   # Hybrid Automation (IDP)
    5: "D1-Q041",   # Temperature & Greedy Decoding
    6: "D1-Q051",   # Top-P Nucleus Sampling & Top-K
    7: "D1-Q061",   # Token Streaming & Perceived Latency
    8: "D1-Q071",   # Context Window Limits & Costs
    9: "D1-Q081",   # Lost in the Middle Mitigation
    10: "D1-Q091",  # Document Chunking & Overlap
    11: "D1-Q101",  # Vector Embeddings & Semantic Search
    12: "D1-Q111",  # Vector Databases & Similarity Metrics
    13: "D1-Q121",  # RAG Architecture Fundamentals
    14: "D1-Q131",  # Knowledge Bases for Amazon Bedrock
    15: "D1-Q141",  # Fine-Tuning Objectives & Use Cases
    16: "D1-Q151",  # Catastrophic Forgetting in Fine-Tuning
    17: "D1-Q161",  # Pre-training Constraints & Feasibility
    18: "D1-Q171",  # Zero-Shot vs Few-Shot Prompting
    19: "D1-Q172",  # Few-Shot In-Context Prompting Examples
    20: "D1-Q181",  # Chain-of-Thought (CoT) Prompting
    21: "D1-Q191",  # System Prompts & Persona Setting
    22: "D1-Q201",  # Prompt Injection & Jailbreak Defense
    23: "D1-Q211",  # Autonomous AI Agents Architecture
    24: "D1-Q221",  # Action Groups & External Tool Calling
    25: "D1-Q231",  # Multi-Agent Orchestration
    26: "D1-Q241",  # Model Quantization & Optimization
    27: "D1-Q251",  # LLM-as-a-Judge Automated Evaluation
    28: "D1-Q271",  # Data Drift & Concept Drift Monitoring
    29: "D1-Q281",  # Shadow AI Mitigation with Sanctioned Tools
    30: "D1-Q291"   # Multimodal Foundation Models & Grounding
}

# For Domain 2 (30 sections)
D2_MAP = {
    1: "D2-Q001",   # Build vs Buy vs Partner Trade-offs
    2: "D2-Q011",   # Core Differentiator vs Commodity Utility
    3: "D2-Q021",   # Data Sovereignty in Build vs Buy
    4: "D2-Q031",   # Comprehensive AI TCO Modeling
    5: "D2-Q041",   # Cost of Inaction (COI) Strategic Value
    6: "D2-Q051",   # Sunk Cost Fallacy in AI Governance
    7: "D2-Q061",   # Project Kill/Pause Decision Gates
    8: "D2-Q071",   # Baseline Metric Definition
    9: "D2-Q081",   # ROI Mathematical Calculation & Modeling
    10: "D2-Q091",  # Tangible vs Intangible Benefits
    11: "D2-Q101",  # Leading Indicators of AI Success
    12: "D2-Q111",  # Lagging Indicators of Long-term Value
    13: "D2-Q121",  # Prioritization 2x2 Matrix
    14: "D2-Q131",  # Quick Wins Execution Strategy
    15: "D2-Q141",  # Strategic Bets Long-term Investment
    16: "D2-Q151",  # PoC Purgatory Exit Strategies
    17: "D2-Q161",  # Time-to-Market (TTM) Optimization
    18: "D2-Q171",  # Data Flywheel Defensible Moat
    19: "D2-Q181",  # AI FinOps Operating Framework
    20: "D2-Q191",  # Cost Allocation Tags & Chargeback
    21: "D2-Q211",  # Model Routing & Cascading TCO Savings
    22: "D2-Q221",  # Provisioned Throughput vs On-Demand
    23: "D2-Q241",  # Unit Economics in Scaled Inference
    24: "D2-Q251",  # Customer Retention & NPS Valuation
    25: "D2-Q201",  # AWS Budgets & Cost Anomaly Alerts
    26: "D2-Q231",  # Multi-Model Strategy & Lock-in Mitigation
    27: "D2-Q261",  # Developer Productivity ROI
    28: "D2-Q271",  # AI Business Model Innovation
    29: "D2-Q281",  # A/B Testing & Causal Attribution
    30: "D2-Q291"   # Fail Fast & Agile Experimentation
}

# For Domain 3 (30 sections)
D3_MAP = {
    1: "D3-Q001",   # Responsible AI (RAI) Core Principles
    2: "D3-Q011",   # Fairness & Historical Bias Mitigation
    3: "D3-Q021",   # Demographic Parity & Disparate Impact
    4: "D3-Q012",   # Historical Bias in Training Data
    5: "D3-Q031",   # Explainability & Black-Box Transparency
    6: "D3-Q041",   # SHAP Values & Feature Attribution
    7: "D3-Q051",   # Amazon SageMaker Clarify Operations
    8: "D3-Q061",   # Personally Identifiable Information (PII) Protection
    9: "D3-Q071",   # Automated PII Masking & Redaction
    10: "D3-Q081",  # AWS Customer Data Protection Pledge
    11: "D3-Q091",  # Transparency & AI Disclosure Mandates
    12: "D3-Q101",  # Synthetic Media & Digital Watermarking
    13: "D3-Q121",  # Kill-Switch Mechanism & Circuit Breakers
    14: "D3-Q141",  # Amazon Bedrock Guardrails Architecture
    15: "D3-Q151",  # Denied Topics Enforcement
    16: "D3-Q161",  # Contextual Grounding Check for Hallucinations
    17: "D3-Q171",  # Human-in-the-Loop (HITL) High-Risk Escalation
    18: "D3-Q181",  # Amazon Augmented AI (Amazon A2I) Workflows
    19: "D3-Q211",  # High-Risk AI Mandatory Conformity
    20: "D3-Q191",  # EU AI Act Four-Tier Risk Classification
    21: "D3-Q201",  # Unacceptable Risk Banned AI
    22: "D3-Q241",  # NIST AI Risk Management Framework
    23: "D3-Q251",  # Cross-Functional AI Governance Committee
    24: "D3-Q231",  # ISO/IEC 42001 (AIMS) Global Standard
    25: "D3-Q281",  # Copyright Infringement & Cloud Indemnification
    26: "D3-Q221",  # Limited & Minimal Risk Regulatory Obligations
    27: "D3-Q261",  # Model Cards & System Cards Documentation
    28: "D3-Q131",  # Robustness against Adversarial Attacks / Prompt Injection
    29: "D3-Q271",  # Model Lineage & Audit Trail Tracking
    30: "D3-Q291"   # Operational Incident Response Protocol
}

# For Domain 4 (30 sections)
D4_MAP = {
    1: "D4-Q001",   # 4 Dimensions of AI Readiness
    2: "D4-Q011",   # AI Maturity Stage 1: Exploration
    3: "D4-Q051",   # AWS Cloud Adoption Framework (CAF) AI/ML Lens
    4: "D4-Q061",   # Data Silos Organizational Friction
    5: "D4-Q071",   # Data Mesh Decentralized Architecture
    6: "D4-Q101",   # Data Contracts between Producers & AI
    7: "D4-Q181",   # Psychological Safety in AI Adoption
    8: "D4-Q151",   # AI Champions Grassroots Network
    9: "D4-Q191",   # Role-Based Upskilling Curricula
    10: "D4-Q171",  # Augmentation over Replacement Philosophy
    11: "D4-Q121",  # AI Center of Excellence (CoE) Mandate
    12: "D4-Q131",  # Centralized vs Decentralized CoE Trade-offs
    13: "D4-Q221",  # Secure Prototyping Sandboxes
    14: "D4-Q231",  # AWS 4-Stage Innovation: Envision
    15: "D4-Q141",  # Hub-and-Spoke CoE Operating Model
    16: "D4-Q021",  # AI Maturity Stage 2: Opportunistic
    17: "D4-Q031",  # AI Maturity Stage 3: Systematic
    18: "D4-Q201",  # Culture of Experimentation & Fail Fast
    19: "D4-Q161",  # Peer-Coaching & Use Case Discovery
    20: "D4-Q081",  # Amazon DataZone Federated Cataloging
    21: "D4-Q271",  # Business Process Re-engineering (BPR)
    22: "D4-Q211",  # AWS PartyRock No-Code Prototyping
    23: "D4-Q091",  # AWS Lake Formation Granular Access
    24: "D4-Q111",  # Internal SLAs for Pipeline Stability
    25: "D4-Q261",  # AWS 4-Stage Innovation: Scale
    26: "D4-Q251",  # AWS 4-Stage Innovation: Launch
    27: "D4-Q041",  # AI Maturity Stage 4: Transformational
    28: "D4-Q241",  # AWS 4-Stage Innovation: Experiment
    29: "D4-Q281",  # Technical Debt Mitigation in AI
    30: "D4-Q291"   # Ethical AI Whistleblowing & Safety Reporting
}

def format_practice_question(q):
    lines = [
        f"> ### 📝 기출 기반 실전 문제 예시 (Exam Practice Question - {q['id']})",
        ">",
        f"> **Q. [{q['topic_category']}]**  ",
        f"> **🇺🇸 English**: {q['question_en']}  ",
        f"> **🇰🇷 한국어**: {q['question_kr']}",
        ">"
    ]
    correct_key = q.get('correct_answer', '').strip().upper()
    for opt in q.get('options', []):
        key = opt['key'].strip().upper()
        text_en = opt['text_en'].strip()
        text_kr = opt['text_kr'].strip()
        if key == correct_key:
            lines.append(f"> * **({key})** **[정답]** {text_en} ({text_kr})")
        else:
            lines.append(f"> * **({key})** {text_en} ({text_kr})")
    lines.append(">")
    lines.append("> 💡 **정답 및 비즈니스 해설 (Answer & Explanation)**:  ")
    exp_kr = q.get('explanation_kr', '').strip()
    for exp_line in exp_kr.split('\n'):
        if exp_line.strip():
            lines.append(f"> {exp_line}")
        else:
            lines.append(">")
    return "\n".join(lines)

def inject_questions_for_domain(domain_num, section_map):
    file_path = os.path.join(BASE_DIR, f"generate_domain{domain_num}_deepdive.py")
    q_file = os.path.join(BASE_DIR, "questions", f"questions_domain{domain_num}.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    with open(q_file, "r", encoding="utf-8") as f:
        q_list = json.load(f)
        
    q_dict = {q["id"]: q for q in q_list}
    
    # Split content by sections
    parts = re.split(rf"(?=\n### {domain_num}\.\d+ )", content)
    header = parts[0]
    raw_sections = parts[1:]
    
    if len(raw_sections) != 30:
        raise ValueError(f"Expected 30 sections in Domain {domain_num}, found {len(raw_sections)}")
        
    updated_sections = []
    for idx, sec_text in enumerate(raw_sections, 1):
        target_qid = section_map.get(idx)
        if not target_qid or target_qid not in q_dict:
            raise KeyError(f"Question {target_qid} not found in questions_domain{domain_num}.json for sec {idx}")
            
        q = q_dict[target_qid]
        q_block = format_practice_question(q)
        
        # Find </div>\s*</div>
        m = re.search(r"(</div>\s*</div>)", sec_text)
        if not m:
            raise ValueError(f"Could not find </div></div> in Domain {domain_num} section {idx}")
            
        div_end = m.end()
        before_div = sec_text[:div_end]
        after_div = sec_text[div_end:]
        
        # Check and replace existing placeholder if present
        placeholder_pattern = r"\n*\s*> \*\*🎯 출제 예상 문제[^\n]*\n(?:> [^\n]*\n*)*"
        if re.search(placeholder_pattern, after_div):
            after_div = re.sub(placeholder_pattern, "\n\n" + q_block + "\n", after_div, count=1)
            new_sec = before_div + after_div
        else:
            new_sec = before_div + "\n\n" + q_block + after_div
            
        updated_sections.append(new_sec)
        
    new_content = header + "".join(updated_sections)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"✓ Domain {domain_num}: Injected 30 practice questions successfully.")

def main():
    print("=== Injecting 120 Exam Practice Questions across Domains 1-4 ===")
    inject_questions_for_domain(1, D1_MAP)
    inject_questions_for_domain(2, D2_MAP)
    inject_questions_for_domain(3, D3_MAP)
    inject_questions_for_domain(4, D4_MAP)
    print("\n🎉 ALL 120 PRACTICE EXAM QUESTIONS SUCCESSFULLY INJECTED! 🎉")

if __name__ == "__main__":
    main()
