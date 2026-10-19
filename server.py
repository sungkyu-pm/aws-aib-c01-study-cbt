#!/usr/bin/env python3
"""
AWS Certified AI Business Strategist (AIB-C01) Local Backend Server
- Built using only Python 3 standard libraries (No external pip packages required).
- Serves static assets (HTML/CSS/JS/Docs).
- Provides REST APIs for Questions, Dynamic Docs, Exam History, and Submissions.
"""

import os
import sys
import json
import time
from datetime import datetime
from urllib.parse import urlparse, parse_qs
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

PORT = 8000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
HISTORY_FILE = os.path.join(DATA_DIR, 'history.json')
QUESTIONS_DIR = os.path.join(BASE_DIR, 'questions')
DOCS_DIR = os.path.join(BASE_DIR, 'docs')

os.makedirs(DATA_DIR, exist_ok=True)
if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump([], f, ensure_ascii=False, indent=2)


class AIBExamServerHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        # API 라우팅
        if path == '/api/status':
            self.handle_api_status()
        elif path == '/api/docs':
            self.handle_api_docs(query)
        elif path == '/api/questions':
            self.handle_api_questions(query)
        elif path == '/api/history':
            self.handle_api_history()
        else:
            # 정적 파일 서빙 (루트 접근 시 index.html)
            if path == '/':
                self.path = '/index.html'
            super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == '/api/submit':
            self.handle_api_submit()
        elif path == '/api/questions/add':
            self.handle_api_add_question()
        else:
            self.send_error(404, "Endpoint not found")

    # ==========================
    # API 핸들러들
    # ==========================

    def send_json_response(self, data, status_code=200):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body)

    def handle_api_status(self):
        """서버 상태 및 데이터베이스 요약 정보 반환"""
        total_questions = 0
        if os.path.exists(os.path.join(QUESTIONS_DIR, 'mock_exam_1.json')):
            with open(os.path.join(QUESTIONS_DIR, 'mock_exam_1.json'), 'r', encoding='utf-8') as f:
                total_questions = len(json.load(f))

        exam_count = 0
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                exam_count = len(json.load(f))

        self.send_json_response({
            "status": "online",
            "server": "AIB-C01 Local Backend",
            "total_questions": total_questions,
            "total_exams_taken": exam_count,
            "time": datetime.now().isoformat()
        })

    def handle_api_docs(self, query):
        """docs 디렉토리의 마크다운 내용 실시간 반환"""
        doc_key = query.get('key', [None])[0]
        file_map = {
            'overview': '00_AIB-C01_EXAM_GUIDE.md',
            'glossary': '01_GLOSSARY_KR_EN.md',
            'domain1': '02_DOMAIN_1_AI_FUNDAMENTALS.md',
            'domain2': '03_DOMAIN_2_AI_STRATEGY_VALUE.md',
            'domain3': '04_DOMAIN_3_GOVERNANCE_RESPONSIBLE_AI.md',
            'domain4': '05_DOMAIN_4_TRANSFORMATION_READINESS.md',
            'aws_services': '06_AWS_SERVICES_CHEAT_SHEET.md'
        }

        if doc_key:
            filename = file_map.get(doc_key)
            if filename:
                filepath = os.path.join(DOCS_DIR, filename)
                if os.path.exists(filepath):
                    with open(filepath, 'r', encoding='utf-8') as f:
                        return self.send_json_response({"key": doc_key, "content": f.read()})
            return self.send_json_response({"error": "Document not found"}, status_code=404)

        # 전체 목록 반환
        all_docs = {}
        for k, filename in file_map.items():
            filepath = os.path.join(DOCS_DIR, filename)
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    all_docs[k] = f.read()
        self.send_json_response(all_docs)

    def handle_api_questions(self, query):
        """문제 세트 조회 (mock1, domain1, domain2, domain3, domain4)"""
        set_name = query.get('set', ['mock1'])[0]
        file_map = {
            'mock1': 'mock_exam_1.json',
            'domain1': 'questions_domain1.json',
            'domain2': 'questions_domain2.json',
            'domain3': 'questions_domain3.json',
            'domain4': 'questions_domain4.json'
        }

        filename = file_map.get(set_name, 'mock_exam_1.json')
        filepath = os.path.join(QUESTIONS_DIR, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                questions = json.load(f)
            self.send_json_response({"set": set_name, "total": len(questions), "questions": questions})
        else:
            self.send_json_response({"error": f"Set {set_name} not found"}, status_code=404)

    def handle_api_history(self):
        """시험 응시 기록 조회"""
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                history = json.load(f)
            self.send_json_response({"history": history})
        else:
            self.send_json_response({"history": []})

    def handle_api_submit(self):
        """시험 제출 처리: 서버 측 정답 채점, 점수 계산, history.json 저장"""
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body_bytes = self.rfile.read(content_length)
            payload = json.loads(body_bytes.decode('utf-8'))

            set_name = payload.get('set', 'mock1')
            time_spent_seconds = payload.get('time_spent_seconds', 0)
            mode = payload.get('mode', 'exam')

            # 클라이언트 측 동적 평가 결과가 전달된 경우 우선 사용
            if 'client_evaluated' in payload and isinstance(payload['client_evaluated'], dict):
                ce = payload['client_evaluated']
                record = {
                    "id": f"EXAM-{int(time.time())}",
                    "timestamp": ce.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                    "set": set_name,
                    "mode": mode,
                    "total": ce.get("total", 0),
                    "correct_count": ce.get("correct_count", 0),
                    "accuracy": ce.get("accuracy", 0),
                    "scaled_score": ce.get("scaled_score", 0),
                    "passed": ce.get("passed", False),
                    "time_spent_seconds": time_spent_seconds,
                    "domain_stats": ce.get("domain_stats", {}),
                    "wrong_question_ids": ce.get("wrong_question_ids", [])
                }
            else:
                user_answers = payload.get('user_answers', {})
                # 해당 세트의 정답 데이터 로드
                file_map = {
                    'mock1': 'mock_exam_1.json',
                    'domain1': 'questions_domain1.json',
                    'domain2': 'questions_domain2.json',
                    'domain3': 'questions_domain3.json',
                    'domain4': 'questions_domain4.json'
                }
                filepath = os.path.join(QUESTIONS_DIR, file_map.get(set_name, 'mock_exam_1.json'))
                with open(filepath, 'r', encoding='utf-8') as f:
                    questions = json.load(f)

                correct_count = 0
                domain_stats = {}
                wrong_question_ids = []

                for q in questions:
                    dom = q.get('domain', 'Other')
                    if dom not in domain_stats:
                        domain_stats[dom] = {'total': 0, 'correct': 0, 'name': q.get('domain_name', dom)}
                    domain_stats[dom]['total'] += 1

                    ans = user_answers.get(q['id'])
                    corr = q['correct_answer']
                    is_correct = False

                    if isinstance(corr, list):
                        if isinstance(ans, list) and len(ans) == len(corr) and sorted(ans) == sorted(corr):
                            is_correct = True
                    else:
                        if ans == corr:
                            is_correct = True

                    if is_correct:
                        correct_count += 1
                        domain_stats[dom]['correct'] += 1
                    else:
                        wrong_question_ids.append(q['id'])

                total = len(questions)
                accuracy = round((correct_count / total * 100), 1) if total > 0 else 0
                scaled_score = round(100 + (accuracy / 100) * 900)
                passed = scaled_score >= 700

                record = {
                    "id": f"EXAM-{int(time.time())}",
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "set": set_name,
                    "mode": mode,
                    "total": total,
                    "correct_count": correct_count,
                    "accuracy": accuracy,
                    "scaled_score": scaled_score,
                    "passed": passed,
                    "time_spent_seconds": time_spent_seconds,
                    "domain_stats": domain_stats,
                    "wrong_question_ids": wrong_question_ids
                }

            # 기록 파일에 영구 추가
            history = []
            if os.path.exists(HISTORY_FILE):
                try:
                    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                        history = json.load(f)
                except Exception:
                    history = []

            history.insert(0, record)  # 최신순
            with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
                json.dump(history, f, ensure_ascii=False, indent=2)

            self.send_json_response({"result": record})

        except Exception as e:
            self.send_json_response({"error": str(e)}, status_code=500)

    def handle_api_add_question(self):
        """신규 문제 추가 API"""
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body_bytes = self.rfile.read(content_length)
            new_q = json.loads(body_bytes.decode('utf-8'))

            # 도메인 타깃 파일 결정
            dom_key = new_q.get('domain', 'Domain 1')
            file_target = 'questions_domain1.json'
            if '2' in dom_key:
                file_target = 'questions_domain2.json'
            elif '3' in dom_key:
                file_target = 'questions_domain3.json'
            elif '4' in dom_key:
                file_target = 'questions_domain4.json'

            target_path = os.path.join(QUESTIONS_DIR, file_target)
            data = []
            if os.path.exists(target_path):
                with open(target_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)

            data.append(new_q)
            with open(target_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            self.send_json_response({"status": "success", "added_to": file_target})
        except Exception as e:
            self.send_json_response({"error": str(e)}, status_code=500)


def run_server():
    server_address = ('', PORT)
    httpd = ThreadingHTTPServer(server_address, AIBExamServerHandler)
    print("=" * 65)
    print(f"🚀 AWS Certified AI Business Strategist (AIB-C01) Server Online!")
    print(f"🌐 Access URL : http://localhost:{PORT}")
    print(f"📁 Root Dir   : {BASE_DIR}")
    print(f"💾 Data Dir   : {DATA_DIR}")
    print("=" * 65)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down server gracefully...")
        httpd.server_close()
        sys.exit(0)


if __name__ == '__main__':
    run_server()
