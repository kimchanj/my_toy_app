import streamlit as st

st.set_page_config(page_title="나의 웹사이트", page_icon="🏠", layout="wide")

st.title("🏠 홈")
st.markdown("---")
st.write("""
이건 **Streamlit 멀티페이지 웹사이트** 예제입니다.  
왼쪽 사이드바에서 페이지를 선택해 이동할 수 있습니다.
""")


col1, col2 = st.columns(2)
with col1:
    st.subheader("소개 페이지")
    st.write("앱의 목적, 제작자, 철학 등을 소개하는 페이지입니다.")
with col2:
    st.subheader("분석 페이지")
    st.write("데이터 시각화, 통계 분석 결과를 보여주는 공간입니다.")

st.markdown("---")
st.info("💡 팁: 'pages' 폴더 안의 .py 파일이 자동으로 새로운 페이지로 인식됩니다.")
