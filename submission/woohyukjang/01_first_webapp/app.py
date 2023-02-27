# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # 인생 첫 웹페이지 제작

    

    >>이유:

    ## 부족하지만 많이 사랑해주세요!

    # 다른 학생들에게 가장 도움이 될 것 같은 유튜브

    ##

    >>이유:

    * 1$ = 1,300원
    * ^_^dqjkwfhgkeljarfhalkejrfhalkef


    # 참고 사이트
    * [icons8](https://icons8.com)
    * [flation](https://flaticon.com)
    * [pixabay](https://pixabay.com/ko/)


    """
)

# https://pixabay.com/ko
st.image(
    "https://cdn.pixabay.com/photo/2014/11/30/14/11/cat-551554_960_720.jpg"
)
