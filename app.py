import random
import streamlit as st

# 1. 화면 상단에 멋진 제목과 안내 문구 넣기
st.set_page_config(page_title="가위바위보 벌칙 게임", page_icon="🎮")
st.title("🎮 AI와 함께하는 가위바위보 대결!")
st.markdown("아래 버튼 중 하나를 선택해 컴퓨터와 승부를 겨뤄보세요! **지면 유머스러운 벌칙이 기다립니다!**")
st.divider()

# 선택지 및 유머 벌칙 리스트 설정
choices = ["✌️ 가위", "✊ 바위", "✋ 보"]
penalties = [
    "엉덩이로 자기 이름 쓰기 ✍️",
    "지금 바로 옆 사람(또는 허공)에게 진지하게 '사랑해'라고 말하기 ❤️",
    "10초 동안 세상에서 제일 귀여운 표정 짓기 🐱",
    "물 한 컵 원샷하고 '캬~ 시원하다!' 외치기 🥤",
    "코끼리 코 5바퀴 돌고 제자리에 3초 서 있기 🐘",
    "가장 자신 있는 동물 성대모사 1가지 하기 🐶",
    "기지개 쭉 펴면서 '나는 우주 최강이다!' 외치기 🚀",
    "눈 깜빡이지 않고 15초 동안 화면 노려보기 👀"
]

user_choice = None

# 2. [✌️ 가위], [✊ 바위], [✋ 보] 버튼 3개를 나란히 배치하기
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✌️ 가위", use_container_width=True):
        user_choice =
