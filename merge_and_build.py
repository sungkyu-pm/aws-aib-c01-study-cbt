#!/usr/bin/env python3
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_DIR = os.path.join(BASE_DIR, 'questions')

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    print("=== Merging Question Pools ===")
    domains = {}
    for i in range(1, 5):
        base_file = os.path.join(QUESTIONS_DIR, f'questions_domain{i}.json')
        extra_file = os.path.join(QUESTIONS_DIR, f'questions_domain{i}_extra.json')
        
        base_qs = load_json(base_file)
        # Deduplicate or check if extra already added
        existing_ids = {q['id'] for q in base_qs}
        
        if os.path.exists(extra_file):
            extra_qs = load_json(extra_file)
            for eq in extra_qs:
                if eq['id'] not in existing_ids:
                    base_qs.append(eq)
                    existing_ids.add(eq['id'])
        
        domains[f'domain{i}'] = base_qs
        save_json(base_file, base_qs)
        print(f"Domain {i}: Total {len(base_qs)} questions (Saved to {base_file})")

    # Build 60-question reference mock exam (D1:12, D2:19, D3:16, D4:13 = 60)
    mock1_qs = []
    mock1_qs.extend(domains['domain1'][:12])
    mock1_qs.extend(domains['domain2'][:19])
    mock1_qs.extend(domains['domain3'][:16])
    mock1_qs.extend(domains['domain4'][:13])
    
    mock1_file = os.path.join(QUESTIONS_DIR, 'mock_exam_1.json')
    save_json(mock1_file, mock1_qs)
    print(f"Mock Exam 1: Total {len(mock1_qs)} questions (Saved to {mock1_file})")

    # Combine all questions
    all_qs = []
    for i in range(1, 5):
        all_qs.extend(domains[f'domain{i}'])
    print(f"Total Combined Pool: {len(all_qs)} questions across 4 domains.")

    # Build questions-data.js & cbt-app/questions-data.js
    exam_data = {
        "domain1": domains['domain1'],
        "domain2": domains['domain2'],
        "domain3": domains['domain3'],
        "domain4": domains['domain4'],
        "mock1": mock1_qs,
        "all_pool": all_qs
    }

    js_content = f"// AWS Certified AI Business Strategist (AIB-C01) Full Question Bank\n// Auto-generated total {len(all_qs)} questions (30 per domain)\nconst EXAM_DATA = {json.dumps(exam_data, ensure_ascii=False, indent=2)};\n\nif (typeof window !== 'undefined') {{\n  window.EXAM_DATA = EXAM_DATA;\n}}\nif (typeof module !== 'undefined' && module.exports) {{\n  module.exports = EXAM_DATA;\n}}\n"

    with open(os.path.join(BASE_DIR, 'questions-data.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"Updated questions-data.js ({len(js_content)} bytes)")

    with open(os.path.join(BASE_DIR, 'cbt-app', 'questions-data.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"Updated cbt-app/questions-data.js ({len(js_content)} bytes)")

if __name__ == '__main__':
    main()
