# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # 나에게 가장 도움이 될 것 같은 유튜브
    ## 빵형의 개발 도상국
    > 이유 : 강사님 추천^^..

    # 남이 보면 좋을 것 같은 유튜브
    ## 노마드 코더
    > 이유 : 썸네일이 간단명료하고 이쁨, it 트렌디함

    # 참고 사이트
    * [icons8](https://icons8.com/)
    * [flaticon](https://flaticon.com/)
    * [pixabay](https://pixabay.com/ko/)

    """
)

# https://pixabay.com/ko
# st.image(
#     "https://cdn.pixabay.com/photo/2014/11/30/14/11/cat-551554_960_720.jpg"
# )