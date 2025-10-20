import streamlit as st

st.set_page_config(page_title="소개", page_icon="📘")

st.title("📘 소개 페이지")
st.markdown("---")
st.write("""
이 앱은 Streamlit을 이용한 **멀티페이지 웹사이트** 예시입니다.  
아래 내용은 개발자 정보나 서비스 소개를 담을 수 있습니다.
""")

st.subheader("👨‍💻 개발자 정보")
st.write("- 이름: 홍길동")
st.write("- 이메일: example@example.com")
st.write("- 기술스택: Python, Streamlit, Vue.js")

st.markdown("---")
st.caption("버전 1.0 | 작성일: 2025-10-17")
