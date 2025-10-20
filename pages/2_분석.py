import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="분석", page_icon="📊")

st.title("📊 데이터 분석 페이지")
st.markdown("---")

# 더미 데이터
data = pd.DataFrame({
    "x": np.linspace(0, 10, 100),
    "y": np.sin(np.linspace(0, 10, 100))
})

# 차트 그리기
fig, ax = plt.subplots()
ax.plot(data["x"], data["y"])
ax.set_title("Sine Curve 예시")
st.pyplot(fig)

st.markdown("---")
st.write("데이터 분석 결과나 그래프를 여기에 표시할 수 있습니다.")
