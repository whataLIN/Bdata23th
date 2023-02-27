# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
# 가장 간단한 웹 사이트를 만드는 방법

st.write(
    """
    st.image("https://www.flaticon.com/free-icon/quality_654117?term=recommend&page=1&position=3&origin=search&related_id=654117")
    ## 코딩 유튜브 추천 채널 목록
    #### 나에게 가장 도움이 될 것 같은 유튜브
    ##### 빵형의 개발 도상국
    > 이유 : 강사님 추천^^..

    #### 남이 보면 좋을 것 같은 유튜브
    ##### 노마드 코더
    > 이유 : 썸네일이 간단명료하고 예쁨, IT 트렌드 흐름을 알기 쉽고 빠르게 설명해 줍니다!
    video_file = open('https://youtu.be/Cnbmrh99c1o', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)

    st.image("https://user-images.githubusercontent.com/71927533/221631776-7815c4a2-6500-4c1b-ba7a-208b451972ee.jpg")

    # 참고 사이트
    * [icons8](https://icons8.com/)

    """
)

# """ """ 여러 줄을 묶어서 표시할 수 있는 문자열
# ''' ''' (동일 기능)


# https://pixabay.com/ko
# st.image(
#     "https://cdn.pixabay.com/photo/2014/11/30/14/11/cat-551554_960_720.jpg"
# )