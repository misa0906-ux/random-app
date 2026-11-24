import random
import streamlit as st

# 1. 화면 상단에 멋진 제목과 안내 문구 넣기
st.set_page_config(page_title="가위바위보 게임", page_icon="🎮")
st.title("🎮 AI와 함께하는 가위바위보 대결!")
st.markdown("아래 버튼 중 하나를 선택해 컴퓨터와 승부를 겨뤄보세요! 과연 승자는 누구일까요?")
st.divider()

# 선택지 설정
choices = ["✌️ 가위", "✊ 바위", "✋ 보"]
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
        st.warning("🤝 비겼습니다! 다시 한 번 도전해 보세요.")
    elif (
        (user_choice == "✌️ 가위" and computer_choice == "✋ 보") or
        (user_choice == "✊ 바위" and computer_choice == "✌️ 가위") or
        (user_choice == "✋ 보" and computer_choice == "✊ 바위")
    ):
        st.success("🎉 축하합니다! 당신이 이겼습니다!")
        st.balloons()  # 승리 시 풍선 효과
    else:
        st.error("😭 아쉽네요! 컴퓨터가 이겼습니다.")
