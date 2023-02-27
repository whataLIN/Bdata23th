# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    #남에게 도움이 될 것 같은 채널 : 메타코드M
    ##가끔 지나가다 본 적이 있는데 지식적인 면에서 도움이 되었던 것 같다.
    #나에게 도움이 될 것 같은 채널 : 조코딩
    ##전반적인 컴퓨터 분야의 흐름에 대해서 알수있을 것 같아서 도움이 될 것 같다.
    """
)

# https://pixabay.com/ko
st.image(
    "https://cdn.pixabay.com/photo/2014/11/30/14/11/cat-551554_960_720.jpg"
)