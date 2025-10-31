import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Gate 25 - Light of Love", layout="centered")
st.title("☀️ Gate 25 – Spirit of the Self")
st.markdown("**“모든 존재는 이미 신성하다.”**")

# 사용자 메시지 입력
message = st.text_input("사랑의 메시지를 입력하세요:", "모든 존재는 이미 신성하다.")

# 우주 별 세팅
n_stars = 500
stars_x = np.random.uniform(-1, 1, n_stars)
stars_y = np.random.uniform(-1, 1, n_stars)
stars_size = np.random.uniform(1, 3, n_stars)
stars_alpha = np.random.uniform(0.1, 0.5, n_stars)

# placeholder 생성
placeholder = st.empty()

# 프레임 반복
for alpha in np.linspace(0, 1, 30):
    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.axis("off")
    ax.set_facecolor("black")

    # 별 표시
    ax.scatter(stars_x, stars_y, s=stars_size, color='white', alpha=stars_alpha)

    # 중앙 태양
    sun_radius = 0.2
    sun = plt.Circle((0,0), sun_radius, color='white', alpha=0.8)
    ax.add_patch(sun)

    # 중앙 메시지
    ax.text(0, 0, message, color='white', fontsize=16,
            ha='center', va='center', alpha=alpha, fontweight='bold')

    # 화면 갱신
    placeholder.pyplot(fig)
    plt.close(fig)  # 메모리 누수 방지
    time.sleep(0.05)

st.caption("🌞 존재함으로써 우주를 밝히는 Gate 25의 빛.")
