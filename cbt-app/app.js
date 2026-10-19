// AWS Certified AI Business Strategist (AIB-C01) CBT App

class CBTSimulator {
  constructor() {
    this.questions = [];
    this.currentIndex = 0;
    this.userAnswers = {}; // { questionId: ['A'] or 'A' }
    this.flaggedQuestions = new Set();
    this.checkedQuestions = new Set(); // 학습 모드에서 정답 확인을 누른 문항
    this.mode = 'study'; // 'study' or 'exam'
    this.koreanVisible = false;
    this.timerInterval = null;
    this.secondsRemaining = 0;
    this.totalSeconds = 0;
    this.timeSpentSeconds = 0;

    this.initDOMElements();
    this.bindEvents();
  }

  initDOMElements() {
    // 화면들
    this.startScreen = document.getElementById('start-screen');
    this.examScreen = document.getElementById('exam-screen');
    this.resultScreen = document.getElementById('result-screen');

    // 헤더 컨트롤
    this.timerBox = document.getElementById('timer-box');
    this.timeDisplay = document.getElementById('time-display');
    this.modeToggleBtn = document.getElementById('mode-toggle-btn');
    this.modeLabel = document.getElementById('mode-label');
    this.modeIcon = document.getElementById('mode-icon');

    // 문제 컴포넌트
    this.qCounter = document.getElementById('q-counter');
    this.qDomain = document.getElementById('q-domain');
    this.toggleFlagBtn = document.getElementById('toggle-flag-btn');
    this.flagText = document.getElementById('flag-text');
    this.toggleTransBtn = document.getElementById('toggle-trans-btn');
    this.qTextEn = document.getElementById('q-text-en');
    this.qTextKr = document.getElementById('q-text-kr');
    this.optionsContainer = document.getElementById('options-container');

    // 피드백 (학습 모드)
    this.studyFeedback = document.getElementById('study-feedback');
    this.feedbackBadge = document.getElementById('feedback-badge');
    this.feedbackTitle = document.getElementById('feedback-title');
    this.feedbackConcept = document.getElementById('feedback-concept');
    this.feedbackExplanation = document.getElementById('feedback-explanation');
    this.checkAnswerBtn = document.getElementById('check-answer-btn');

    // 네비게이션
    this.prevBtn = document.getElementById('prev-btn');
    this.nextBtn = document.getElementById('next-btn');
    this.submitExamBtn = document.getElementById('submit-exam-btn');
    this.questionPalette = document.getElementById('question-palette');

    // 통계 요약
    this.summaryTotal = document.getElementById('summary-total');
    this.summaryAnswered = document.getElementById('summary-answered');
    this.summaryUnanswered = document.getElementById('summary-unanswered');
    this.summaryFlagged = document.getElementById('summary-flagged');

    // 결과 화면 컴포넌트
    this.passFailBadge = document.getElementById('pass-fail-badge');
    this.resultMeta = document.getElementById('result-meta');
    this.scaledScore = document.getElementById('scaled-score');
    this.accuracyPercent = document.getElementById('accuracy-percent');
    this.correctCountText = document.getElementById('correct-count-text');
    this.timeSpentText = document.getElementById('time-spent-text');
    this.domainBreakdownList = document.getElementById('domain-breakdown-list');

    this.reviewAllBtn = document.getElementById('review-all-btn');
    this.reviewWrongBtn = document.getElementById('review-wrong-btn');
    this.restartBtn = document.getElementById('restart-btn');
    this.startExamBtn = document.getElementById('start-exam-btn');
  }

  bindEvents() {
    this.startExamBtn.addEventListener('click', () => this.startExamFromSettings());
    this.prevBtn.addEventListener('click', () => this.navigateQuestion(-1));
    this.nextBtn.addEventListener('click', () => this.navigateQuestion(1));
    this.toggleTransBtn.addEventListener('click', () => this.toggleTranslation());
    this.toggleFlagBtn.addEventListener('click', () => this.toggleFlag());
    this.checkAnswerBtn.addEventListener('click', () => this.checkCurrentAnswer());
    this.submitExamBtn.addEventListener('click', () => this.confirmSubmitExam());

    this.reviewAllBtn.addEventListener('click', () => this.startReviewMode(false));
    this.reviewWrongBtn.addEventListener('click', () => this.startReviewMode(true));
    this.restartBtn.addEventListener('click', () => this.showStartScreen());

    this.modeToggleBtn.addEventListener('click', () => this.switchModeInExam());
  }

  showStartScreen() {
    this.isReviewMode = false;
    clearInterval(this.timerInterval);
    this.userAnswers = {};
    this.flaggedQuestions = new Set();
    this.checkedQuestions = new Set();
    this.submitExamBtn.textContent = '시험 제출 (Submit) ✔';
    this.startScreen.classList.add('active');
    this.examScreen.classList.remove('active');
    this.resultScreen.classList.remove('active');
    this.timerBox.classList.add('hidden');
  }

  // Fisher-Yates 배열 셔플 유틸리티
  shuffleArray(array) {
    const arr = [...array];
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }

  // 문항 내 보기(A~D) 순서 셔플 및 정답 키 동적 재매핑
  randomizeQuestionOptions(question) {
    const q = JSON.parse(JSON.stringify(question));
    if (!Array.isArray(q.options) || q.options.length < 2) return q;

    const isMultiple = Array.isArray(q.correct_answer);
    const origCorrect = isMultiple ? new Set(q.correct_answer) : new Set([q.correct_answer]);

    // 각 옵션의 원래 정답 여부 태깅
    const tagged = q.options.map(opt => ({
      opt: { ...opt },
      isCorrect: origCorrect.has(opt.key)
    }));

    const shuffled = this.shuffleArray(tagged);
    const keyLetters = ['A', 'B', 'C', 'D', 'E', 'F'];
    const newCorrect = [];

    shuffled.forEach((item, idx) => {
      const letter = keyLetters[idx];
      item.opt.key = letter;
      if (item.isCorrect) {
        newCorrect.push(letter);
      }
    });

    q.options = shuffled.map(item => item.opt);
    q.correct_answer = isMultiple ? newCorrect.sort() : (newCorrect[0] || q.correct_answer);
    return q;
  }

  startExamFromSettings() {
    const setInput = document.querySelector('input[name="examSet"]:checked');
    const modeInput = document.querySelector('input[name="examMode"]:checked');
    const scopeInput = document.querySelector('input[name="examRandomScope"]:checked');
    const selectedSet = setInput ? setInput.value : 'mock1';
    const selectedMode = modeInput ? modeInput.value : 'study';
    const selectedScope = scopeInput ? scopeInput.value : 'sample';

    let rawQuestions = [];
    if (typeof EXAM_DATA !== 'undefined') {
      if (selectedScope === 'canonical') {
        // 기본 출제: 셔플 없이 공식 순서 그대로 출제
        if (selectedSet === 'mock1') {
          rawQuestions = JSON.parse(JSON.stringify(EXAM_DATA.mock1 || []));
        } else if (EXAM_DATA[selectedSet]) {
          rawQuestions = JSON.parse(JSON.stringify((EXAM_DATA[selectedSet] || []).slice(0, 15)));
        }
      } else if (selectedSet === 'mock1') {
        // AWS 공식 가이드 비중에 맞춘 60문항 랜덤 추출 (D1:12, D2:19, D3:16, D4:13)
        const d1 = this.shuffleArray(EXAM_DATA.domain1 || []).slice(0, 12);
        const d2 = this.shuffleArray(EXAM_DATA.domain2 || []).slice(0, 19);
        const d3 = this.shuffleArray(EXAM_DATA.domain3 || []).slice(0, 16);
        const d4 = this.shuffleArray(EXAM_DATA.domain4 || []).slice(0, 13);
        rawQuestions = this.shuffleArray([...d1, ...d2, ...d3, ...d4]);
      } else if (EXAM_DATA[selectedSet]) {
        const pool = EXAM_DATA[selectedSet] || [];
        if (selectedScope === 'full') {
          rawQuestions = this.shuffleArray(pool); // 30문항 전체 순서 셔플
        } else {
          rawQuestions = this.shuffleArray(pool).slice(0, 15); // 15문항 무작위 추출
        }
      }
    }

    if (!rawQuestions || rawQuestions.length === 0) {
      alert('문제 데이터를 로드할 수 없습니다. 페이지를 새로고침(F5) 해주세요.');
      return;
    }

    // 기본 출제(canonical) 모드인 경우 보기 셔플 없이 원본 그대로 출제, 그 외 모드는 보기(A~D) 셔플
    const processedQuestions = (selectedScope === 'canonical')
      ? rawQuestions
      : rawQuestions.map(q => this.randomizeQuestionOptions(q));
    this.startSession(processedQuestions, selectedMode);
  }

  startSession(questionList, mode = 'study', keepAnswers = false) {
    this.questions = questionList;
    this.currentIndex = 0;
    this.mode = mode;
    this.isReviewMode = keepAnswers;

    if (!keepAnswers) {
      this.userAnswers = {};
      this.flaggedQuestions = new Set();
      this.checkedQuestions = new Set();
      this.koreanVisible = false;
      this.totalSeconds = this.questions.length * 90;
      this.secondsRemaining = this.totalSeconds;
      this.timeSpentSeconds = 0;
      this.submitExamBtn.textContent = '시험 제출 (Submit) ✔';
    } else {
      this.koreanVisible = true;
      this.checkedQuestions = new Set(this.questions.map(q => q.id));
      this.checkAnswerBtn.classList.add('hidden');
      this.submitExamBtn.textContent = '📊 결과 리포트로 돌아가기';
    }

    // 모드 UI 설정
    this.updateModeUI();

    this.startScreen.classList.remove('active');
    this.resultScreen.classList.remove('active');
    this.examScreen.classList.add('active');

    if (!this.isReviewMode) {
      this.timerBox.classList.remove('hidden');
      this.startTimer();
    } else {
      this.timerBox.classList.add('hidden');
      clearInterval(this.timerInterval);
    }

    this.renderPalette();
    this.renderQuestion();
    this.updateSummary();
  }

  updateModeUI() {
    if (this.mode === 'study') {
      this.modeIcon.textContent = '💡';
      this.modeLabel.textContent = '학습 모드';
      this.checkAnswerBtn.classList.remove('hidden');
    } else {
      this.modeIcon.textContent = '⏱️';
      this.modeLabel.textContent = '실전 모드';
      this.checkAnswerBtn.classList.add('hidden');
      this.studyFeedback.classList.add('hidden');
    }
  }

  switchModeInExam() {
    this.mode = this.mode === 'study' ? 'exam' : 'study';
    this.updateModeUI();
    this.renderQuestion();
  }

  startTimer() {
    clearInterval(this.timerInterval);
    this.updateTimerDisplay();

    this.timerInterval = setInterval(() => {
      this.timeSpentSeconds++;
      if (this.mode === 'exam') {
        this.secondsRemaining--;
        if (this.secondsRemaining <= 0) {
          clearInterval(this.timerInterval);
          alert('시험 시간이 종료되었습니다! 시험이 자동 제출됩니다.');
          this.submitExam();
          return;
        }
      }
      this.updateTimerDisplay();
    }, 1000);
  }

  updateTimerDisplay() {
    let displaySec = this.mode === 'exam' ? this.secondsRemaining : this.timeSpentSeconds;
    const mins = Math.floor(displaySec / 60);
    const secs = displaySec % 60;
    this.timeDisplay.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

    if (this.mode === 'exam' && this.secondsRemaining <= 300) {
      this.timerBox.classList.add('warning');
    } else {
      this.timerBox.classList.remove('warning');
    }
  }

  renderPalette() {
    this.questionPalette.innerHTML = '';
    this.questions.forEach((q, idx) => {
      const btn = document.createElement('button');
      btn.className = 'palette-btn';
      btn.textContent = idx + 1;
      btn.id = `palette-btn-${idx}`;

      btn.addEventListener('click', () => {
        this.currentIndex = idx;
        this.renderQuestion();
      });

      this.questionPalette.appendChild(btn);
    });
    this.updatePaletteStatus();
  }

  updatePaletteStatus() {
    this.questions.forEach((q, idx) => {
      const btn = document.getElementById(`palette-btn-${idx}`);
      if (!btn) return;

      btn.classList.remove('current', 'answered', 'flagged');

      if (idx === this.currentIndex) {
        btn.classList.add('current');
      }

      if (this.isReviewMode) {
        const userAns = this.userAnswers[q.id];
        const isMultiple = Array.isArray(q.correct_answer);
        const isCorrect = isMultiple
          ? (Array.isArray(userAns) && userAns.length === q.correct_answer.length && userAns.every((val, i) => val === q.correct_answer[i]))
          : (userAns === q.correct_answer);
        btn.classList.add(isCorrect ? 'answered' : 'flagged');
      } else {
        const ans = this.userAnswers[q.id];
        if (ans && (Array.isArray(ans) ? ans.length > 0 : true)) {
          btn.classList.add('answered');
        }

        if (this.flaggedQuestions.has(q.id)) {
          btn.classList.add('flagged');
        }
      }
    });
  }

  renderQuestion() {
    const q = this.questions[this.currentIndex];
    if (!q) return;

    this.qCounter.textContent = `Question ${this.currentIndex + 1} of ${this.questions.length}`;
    this.qDomain.textContent = q.domain || 'General';

    // 플래그 버튼 상태
    if (this.flaggedQuestions.has(q.id)) {
      this.toggleFlagBtn.classList.add('btn-warning');
      this.toggleFlagBtn.classList.remove('btn-outline');
      this.flagText.textContent = '검토 해제 (Unflag)';
    } else {
      this.toggleFlagBtn.classList.remove('btn-warning');
      this.toggleFlagBtn.classList.add('btn-outline');
      this.flagText.textContent = '나중에 검토 (Flag)';
    }

    // 문제 지문
    this.qTextEn.textContent = q.question_en;
    this.qTextKr.textContent = q.question_kr;
    if (this.koreanVisible) {
      this.qTextKr.classList.remove('hidden');
    } else {
      this.qTextKr.classList.add('hidden');
    }

    // 선지 렌더링
    const isMultiple = Array.isArray(q.correct_answer);
    this.optionsContainer.innerHTML = '';

    const currentSelected = this.userAnswers[q.id] || (isMultiple ? [] : null);

    q.options.forEach(opt => {
      const isSelected = isMultiple
        ? currentSelected.includes(opt.key)
        : currentSelected === opt.key;

      const optDiv = document.createElement('div');
      optDiv.className = `option-item ${isSelected ? 'selected' : ''}`;
      optDiv.dataset.key = opt.key;

      // 해설이 표시된 상태일 때 정오답 스타일링
      if ((this.checkedQuestions.has(q.id) && this.mode === 'study') || this.isReviewMode) {
        const isCorrect = isMultiple
          ? q.correct_answer.includes(opt.key)
          : q.correct_answer === opt.key;
        if (isCorrect) optDiv.classList.add('correct');
        else if (isSelected && !isCorrect) optDiv.classList.add('incorrect');
      }

      optDiv.innerHTML = `
        <div class="option-control">
          <input type="${isMultiple ? 'checkbox' : 'radio'}" name="q_opt" value="${opt.key}" ${isSelected ? 'checked' : ''} ${this.isReviewMode ? 'disabled' : ''}>
        </div>
        <div class="option-content">
          <div class="option-en"><span class="option-key">(${opt.key})</span> ${opt.text_en}</div>
          <div class="option-kr ${this.koreanVisible ? '' : 'hidden'}">${opt.text_kr}</div>
        </div>
      `;

      optDiv.addEventListener('click', (e) => {
        this.selectOption(q, opt.key, isMultiple);
      });

      this.optionsContainer.appendChild(optDiv);
    });

    // 이전/다음 버튼 제어
    this.prevBtn.disabled = this.currentIndex === 0;
    this.nextBtn.disabled = this.currentIndex === this.questions.length - 1;

    // 학습 모드 또는 리뷰 모드 피드백 표시
    if ((this.mode === 'study' && this.checkedQuestions.has(q.id)) || this.isReviewMode) {
      this.displayFeedback(q);
    } else {
      this.studyFeedback.classList.add('hidden');
    }

    this.updatePaletteStatus();
    this.updateSummary();
  }

  selectOption(q, key, isMultiple) {
    if (this.isReviewMode) return; // 리뷰 모드에서는 제출된 정답 유지

    if (isMultiple) {
      let current = this.userAnswers[q.id] || [];
      if (!Array.isArray(current)) current = [current];

      if (current.includes(key)) {
        current = current.filter(k => k !== key);
      } else {
        current.push(key);
      }
      this.userAnswers[q.id] = current.sort();
    } else {
      this.userAnswers[q.id] = key;
    }

    // 만약 학습 모드에서 이미 정답 확인을 본 상태에서 답을 바꾼다면 피드백 갱신
    if (this.mode === 'study' && this.checkedQuestions.has(q.id)) {
      this.displayFeedback(q);
    }

    this.renderQuestion();
  }

  toggleTranslation() {
    this.koreanVisible = !this.koreanVisible;
    this.toggleTransBtn.querySelector('span').textContent = this.koreanVisible
      ? '🌐 영어 원문만 보기'
      : '🌐 한국어 번역 보기';
    this.renderQuestion();
  }

  toggleFlag() {
    const q = this.questions[this.currentIndex];
    if (this.flaggedQuestions.has(q.id)) {
      this.flaggedQuestions.delete(q.id);
    } else {
      this.flaggedQuestions.add(q.id);
    }
    this.renderQuestion();
  }

  navigateQuestion(delta) {
    const newIdx = this.currentIndex + delta;
    if (newIdx >= 0 && newIdx < this.questions.length) {
      this.currentIndex = newIdx;
      this.renderQuestion();
    }
  }

  checkCurrentAnswer() {
    const q = this.questions[this.currentIndex];
    this.checkedQuestions.add(q.id);
    this.displayFeedback(q);
    this.renderQuestion();
  }

  displayFeedback(q) {
    const userAns = this.userAnswers[q.id];
    const isMultiple = Array.isArray(q.correct_answer);

    let isCorrect = false;
    if (isMultiple) {
      isCorrect = Array.isArray(userAns) &&
        userAns.length === q.correct_answer.length &&
        userAns.every((val, idx) => val === q.correct_answer[idx]);
    } else {
      isCorrect = userAns === q.correct_answer;
    }

    const myChoiceText = userAns ? (Array.isArray(userAns) ? userAns.join(', ') : userAns) : '미선택';
    const correctChoiceText = Array.isArray(q.correct_answer) ? q.correct_answer.join(', ') : q.correct_answer;

    this.studyFeedback.classList.remove('hidden', 'correct-feedback', 'wrong-feedback');
    if (isCorrect) {
      this.studyFeedback.classList.add('correct-feedback');
      this.feedbackBadge.className = 'badge badge-primary';
      this.feedbackBadge.style.backgroundColor = 'var(--success, #10b981)';
      this.feedbackBadge.style.color = 'white';
      this.feedbackBadge.textContent = '정답입니다! 🎉';
      this.feedbackTitle.textContent = `내가 선택한 정답: (${myChoiceText})`;
    } else {
      this.studyFeedback.classList.add('wrong-feedback');
      this.feedbackBadge.className = 'badge';
      this.feedbackBadge.style.backgroundColor = 'var(--danger, #ef4444)';
      this.feedbackBadge.style.color = 'white';
      this.feedbackBadge.textContent = '오답입니다 ⚠️';
      this.feedbackTitle.textContent = `내가 선택한 답: (${myChoiceText}) | 정답: (${correctChoiceText})`;
    }

    this.feedbackConcept.textContent = q.key_concept || 'AWS AI Strategy';
    this.feedbackExplanation.textContent = q.explanation_kr;
  }

  updateSummary() {
    const total = this.questions.length;
    let answered = 0;
    this.questions.forEach(q => {
      const a = this.userAnswers[q.id];
      if (a && (Array.isArray(a) ? a.length > 0 : true)) answered++;
    });

    this.summaryTotal.textContent = total;
    this.summaryAnswered.textContent = answered;
    this.summaryUnanswered.textContent = total - answered;
    this.summaryFlagged.textContent = this.flaggedQuestions.size;
  }

  confirmSubmitExam() {
    if (this.isReviewMode) {
      this.examScreen.classList.remove('active');
      this.resultScreen.classList.add('active');
      return;
    }
    const total = this.questions.length;
    let answered = 0;
    this.questions.forEach(q => {
      const a = this.userAnswers[q.id];
      if (a && (Array.isArray(a) ? a.length > 0 : true)) answered++;
    });

    const unanswered = total - answered;
    let msg = `총 ${total}문제 중 ${answered}문제를 작성했습니다.`;
    if (unanswered > 0) {
      msg += `\n아직 ${unanswered}문제가 미응답 상태입니다. 그래도 제출하시겠습니까?`;
    } else {
      msg += '\n모든 문제를 풀었습니다. 시험을 제출하시겠습니까?';
    }

    if (confirm(msg)) {
      this.submitExam();
    }
  }

  submitExam() {
    clearInterval(this.timerInterval);

    // 채점 계산
    let correctCount = 0;
    const domainStats = {}; // { 'Domain 1': { total: 0, correct: 0, name: '' } }

    this.questions.forEach(q => {
      const domKey = q.domain || 'Domain Other';
      if (!domainStats[domKey]) {
        domainStats[domKey] = {
          total: 0,
          correct: 0,
          name: q.domain_name || domKey
        };
      }
      domainStats[domKey].total++;

      const userAns = this.userAnswers[q.id];
      const isMultiple = Array.isArray(q.correct_answer);

      let isCorrect = false;
      if (isMultiple) {
        isCorrect = Array.isArray(userAns) &&
          userAns.length === q.correct_answer.length &&
          userAns.every((val, idx) => val === q.correct_answer[idx]);
      } else {
        isCorrect = userAns === q.correct_answer;
      }

      if (isCorrect) {
        correctCount++;
        domainStats[domKey].correct++;
      }
    });

    const total = this.questions.length;
    const accuracy = total > 0 ? (correctCount / total) * 100 : 0;
    // AWS 환산 점수: 기본 100 ~ 1000점 스케일 (700점 합격선)
    const scaled = Math.round(100 + (accuracy / 100) * 900);
    const passed = scaled >= 700;

    // 결과 화면 업데이트
    this.passFailBadge.className = `score-badge ${passed ? 'pass' : 'fail'}`;
    this.passFailBadge.textContent = passed ? 'PASSED (합격)' : 'FAILED (불합격)';

    this.scaledScore.textContent = `${scaled} / 1000`;
    this.accuracyPercent.textContent = `${Math.round(accuracy)}%`;
    this.correctCountText.textContent = `${correctCount} / ${total} 정답`;

    const mins = Math.floor(this.timeSpentSeconds / 60);
    const secs = this.timeSpentSeconds % 60;
    this.timeSpentText.textContent = `${mins}분 ${secs}초`;

    const avgSec = total > 0 ? Math.round(this.timeSpentSeconds / total) : 0;
    this.resultMeta.textContent = `총 문항: ${total}문항 | 합격 기준: 700점 | 평균 응시 속도: 문항당 ${avgSec}초`;

    // 도메인별 성취도 렌더링
    this.domainBreakdownList.innerHTML = '';
    Object.keys(domainStats).sort().forEach(dom => {
      const stat = domainStats[dom];
      const domPct = Math.round((stat.correct / stat.total) * 100);

      let fillClass = 'high';
      if (domPct < 60) fillClass = 'low';
      else if (domPct < 75) fillClass = 'medium';

      const domItem = document.createElement('div');
      domItem.className = 'domain-item';
      domItem.innerHTML = `
        <div class="domain-item-header">
          <span><strong>${dom}</strong>: ${stat.name}</span>
          <span>${stat.correct} / ${stat.total} (${domPct}%)</span>
        </div>
        <div class="progress-bar-bg">
          <div class="progress-bar-fill ${fillClass}" style="width: ${domPct}%"></div>
        </div>
      `;
      this.domainBreakdownList.appendChild(domItem);
    });

    // 화면 전환
    this.examScreen.classList.remove('active');
    this.resultScreen.classList.add('active');
    this.timerBox.classList.add('hidden');
  }

  startReviewMode(wrongOnly = false) {
    let reviewList = this.questions;
    if (wrongOnly) {
      reviewList = this.questions.filter(q => {
        const userAns = this.userAnswers[q.id];
        const isMultiple = Array.isArray(q.correct_answer);
        if (isMultiple) {
          return !(Array.isArray(userAns) &&
            userAns.length === q.correct_answer.length &&
            userAns.every((val, idx) => val === q.correct_answer[idx]));
        } else {
          return userAns !== q.correct_answer;
        }
      });

      if (reviewList.length === 0) {
        alert('틀린 문제가 없습니다! 모든 문제를 맞추셨습니다 👏');
        return;
      }
    }

    // 복습 모드는 답안을 보존(keepAnswers = true)하며 학습 모드로 진입
    this.startSession(reviewList, 'study', true);
    this.toggleTransBtn.querySelector('span').textContent = '🌐 영어 원문만 보기';
  }
}

// 앱 실행 (안전한 즉시/이벤트 초기화)
function initCbtApp() {
  if (!window.cbtApp) {
    try {
      window.cbtApp = new CBTSimulator();
      console.log('✅ CBTSimulator initialized successfully!');
    } catch (err) {
      console.error('❌ Failed to initialize CBTSimulator:', err);
    }
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initCbtApp);
} else {
  initCbtApp();
}
