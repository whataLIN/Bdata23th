# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
# 가장 간단한 웹 사이트를 만드는 방법


# """ """ 여러 줄을 묶어서 표시할 수 있는 문자열
# ''' ''' (동일 기능)


st.balloons()


st.write(
    """
    ## 코딩 유튜브 채널 추천❗
    #### 나에게 가장 도움이 될 것 같은 유튜브
    """
)


st.info('빵형의 개발 도상국', icon="ℹ️")
st.image(
     "https://user-images.githubusercontent.com/71927533/221631776-7815c4a2-6500-4c1b-ba7a-208b451972ee.jpg"
)


st.write(
    """
    > 추천 이유 : 신기하고 재밌는 인공지능을 쉽게, 짧게 설명해주는 유튜브 입니다!
    """
)

video_file = open('https://www.youtube.com/embed/EkmFkW03ftE', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)


st.write(
    """
    #### 남이 보면 좋을 것 같은 유튜브
    """
)

st.info('노마드 코더', icon="ℹ️")
st.image(
     "https://user-images.githubusercontent.com/71927533/221631810-b72fa62f-2c41-4a86-a105-2f4a0c1e1b2c.jpg"
)


st.write(
    """
    > 추천 이유 : IT 트렌드 흐름을 알기 쉽고 빠르게 설명해주고, 간단 명료합니다!
    """
)

video_file = open('https://youtu.be/Cnbmrh99c1o', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)



if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col = st.columns(2)

with col:
    text_input = st.text_input(
        "여러분이 추천하고 싶은 채널을 입력해 주세요! 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )

    if text_input:
        st.write("회원님의 추천 채널은 ", text_input, "입니다!")