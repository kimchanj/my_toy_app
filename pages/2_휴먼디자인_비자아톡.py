import os
import json
import random
import streamlit as st


# 1. JSON 데이터 로드
def load_center_data(file_path=None):
    if file_path is None:
        base_dir = os.path.dirname(os.path.dirname(__file__))  # app/ → human_design_app/
        file_path = os.path.join(base_dir, 'data', 'centers.json')

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


# 2. 랜덤 문장 선택
def get_random_sentence(center_name, data):
    if center_name in data:
        return random.choice(data[center_name])
    else:
        return "해당 센터 데이터가 없습니다."


# --- Streamlit UI ---
st.title("휴먼디자인 비자아 톡 💫")

centers = load_center_data()

# 센터 선택
center_choice = st.selectbox("센터를 선택하세요:", list(centers.keys()))

if st.button("랜덤 문장 보기"):
    sentence = get_random_sentence(center_choice, centers)
    st.success(sentence)