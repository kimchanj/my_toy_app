'''
Streamlit UI
├─ 학생 정보 입력
│   ├─ 학년/현재 내신 등급
│   ├─ 목표 대학/전공
│   └─ MBTI 성향
├─ 데이터 처리
│   ├─ 대학별 전공 합격 등급/수능 커트라인
│   ├─ 과목별 내신 통계
│   └─ MBTI별 최적 공부법 매핑
├─ 결과 출력
│   ├─ 과목별 성적 향상 필요치/통계
│   ├─ 성적 올리는 방법 & 공부량 가이드
│   └─ MBTI 맞춤 공부법
'''

import streamlit as st
import pandas as pd

st.title("대학 목표 성적 가이드")

# 1️⃣ 학생 정보 입력
st.sidebar.header("학생 정보 입력")
current_grades = {
    "국어": st.sidebar.slider("국어 현재 등급", 1, 9, 5),
    "수학": st.sidebar.slider("수학 현재 등급", 1, 9, 5),
    "영어": st.sidebar.slider("영어 현재 등급", 1, 9, 5),
    "과학": st.sidebar.slider("과학 현재 등급", 1, 9, 5),
    "사회": st.sidebar.slider("사회 현재 등급", 1, 9, 5)
}

target_univ = st.sidebar.selectbox("목표 대학", ["중앙대", "경희대", "외대", "시립대"])
target_major = st.sidebar.selectbox("전공", ["AI", "바이오"])
mbti = st.sidebar.selectbox("MBTI", ["INTJ", "ESFP", "ENTP", "ISFJ"])

# 2️⃣ 대학/전공별 목표 등급 예시 데이터
# 실제 구현 시 과거 입시 통계 활용 가능
grade_cut = {
    "중앙대": {"AI": {"국어": 3, "수학": 2, "영어": 2, "과학": 3, "사회": 3},
              "바이오": {"국어": 2, "수학": 3, "영어": 2, "과학": 2, "사회": 3}},
    "경희대": {"AI": {"국어": 3, "수학": 2, "영어": 3, "과학": 3, "사회": 3},
              "바이오": {"국어": 2, "수학": 3, "영어": 3, "과학": 2, "사회": 3}},
    "외대": {"AI": {"국어": 3, "수학": 3, "영어": 2, "과학": 3, "사회": 3},
            "바이오": {"국어": 3, "수학": 3, "영어": 2, "과학": 3, "사회": 3}},
    "시립대": {"AI": {"국어": 4, "수학": 3, "영어": 3, "과학": 4, "사회": 3},
             "바이오": {"국어": 3, "수학": 4, "영어": 3, "과학": 3, "사회": 3}}
}

target_grades = grade_cut[target_univ][target_major]

# 3️⃣ 필요한 등급 상승 계산
needed_improvement = {subj: max(0, current_grades[subj] - target_grades[subj])
                      for subj in current_grades}

st.header(f"{target_univ} {target_major} 목표 분석")
st.subheader("과목별 현재 등급 vs 목표 등급")
df_compare = pd.DataFrame({
    "현재 등급": current_grades,
    "목표 등급": target_grades,
    "필요 상승": needed_improvement
})
st.table(df_compare)

# 4️⃣ MBTI 기반 공부법 추천
study_plan = {
    "INTJ": "혼자 집중 계획형 학습, 주간 목표 설정, 자기 점검 필수",
    "ESFP": "짧게 집중 + 그룹 스터디 활용, 활동 중심 학습",
    "ENTP": "문제 해결형 학습, 토론 및 다양한 자료 활용",
    "ISFJ": "정리형 학습, 반복 연습, 계획된 스케줄 따라가기"
}

st.subheader("MBTI 맞춤 공부법 추천")
st.write(study_plan[mbti])

# 5️⃣ 추가 확장 아이디어
st.info("다음 단계로, 과목별 공부 시간, 세부 주간 계획표, 인강/학원 추천 등을 연결할 수 있어요.")
