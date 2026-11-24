import random
import streamlit as st

# 1. 화면 상단에 멋진 제목과 안내 문구 넣기
st.set_page_config(page_title="가위바위보 벌칙 게임", page_icon="🎮")
st.title("🎮 AI와 함께하는 가위바위보 대결!")
st.markdown("아래 버튼 중 하나를 선택해 컴퓨터와 승부를 겨뤄보세요! **지면 유머스러운 벌칙이 기다립니다!**")
st.divider()

# 선택지 설정
choices = ["✌️ 가위", "✊ 바위", "✋ 보"]

# [추가] 새로고침되어도 추가한 벌칙이 유지되도록 session_state에 벌칙 목록 저장
if "penalties" not in st.session_state:
    st.session_state.penalties = [
        "엉덩이로 자기 이름 쓰기 ✍️",
        "지금 바로 옆 사람(또는 허공)에게 진지하게 '사랑해'라고 말하기 ❤️",
        "10초 동안 세상에서 제일 귀여운 표정 짓기 🐱",
        "물 한 컵 원샷하고 '캬~ 시원하다!' 외치기 🥤",
        "코끼리 코 5바퀴 돌고 제자리에 3초 서 있기 🐘",
        "가장 자신 있는 동물 성대모사 1가지 하기 🐶",
        "기지개 쭉 펴면서 '나는 우주 최강이다!' 외치기 🚀",
        "눈 깜빡이지 않고 15초 동안 화면 노려보기 👀"
    ]

# [추가] 사이드바에 나만의 벌칙 추가 기능 만들기
with st.sidebar:
    st.header("📝 벌칙 관리소")
    new_penalty = st.text_input("새로운 벌칙을 입력하세요:", placeholder="예: 팔굽혀펴기 5개 하기")
    if st.button("벌칙 추가하기"):
        if new_penalty.strip():  # 빈칸이 아닐 때만 추가
            st.session_state.penalties.append(new_penalty)
            st.success("새 벌칙이 추가되었습니다!")
        else:
            st.warning("벌칙 내용을 입력해 주세요.")
            
    with st.expander("현재 등록된 벌칙 목록 보기"):
        for idx, p in enumerate(st.session_state.penalties, 1):
            st.write(f"{idx}. {p}")

user_choice = None

# 2. [✌️ 가위], [✊ 바위], [✋ 보] 버튼 3개를 나란히 배치하기
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✌️ 가위", use_container_width=True):
        user_choice = "✌️ 가위"

with col2:
    if st.button("✊ 바위", use_container_width=True):
        user_choice = "✊ 바위"

with col3:
    if st.button("✋ 보", use_container_width=True):
        user_choice = "✋ 보"

# 3. 사용자가 버튼을 누르면 컴퓨터도 선택하고 대결 결과 보여주기
if user_choice:
    computer_choice = random.choice(choices)
    
    st.subheader("결과 발표!")
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.info(f"**🙋 나의 선택:** {user_choice}")
    with res_col2:
        st.info(f"**🤖 컴퓨터의 선택:** {computer_choice}")
    
    # 4. 승/패/무승부 판정 및 효과 적용
    if user_choice == computer_choice:
        st.warning("🤝 비겼습니다! 휴~ 벌칙은 피했네요. 다시 한 번 도전해 보세요.")
    elif (
        (user_choice == "✌️ 가위" and computer_choice == "✋ 보") or
        (user_choice == "✊ 바위" and computer_choice == "✌️ 가위") or
        (user_choice == "✋ 보" and computer_choice == "✊ 바위")
    ):
        st.success("🎉 축하합니다! 당신이 이겼습니다! 벌칙 면제!")
        st.balloons()  # 승리 시 풍선 효과
    else:
        st.error("😭 아쉽네요! 컴퓨터가 이겼습니다.")
        # [수정] session_state에 저장된 벌칙 목록에서 랜덤 추첨
        chosen_penalty = random.choice(st.session_state.penalties)
        st.markdown("### 🚨 오늘의 벌칙 당첨!")
        st.warning(f"👉 **{chosen_penalty}**")
