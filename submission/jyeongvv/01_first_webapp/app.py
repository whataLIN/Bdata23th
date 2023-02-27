# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # 나에게 추천하는 유튜브
    ## 부족하지만 많이 사랑해주세요!
    > 이유 : 

     # 나에게 추천하는 유튜브
    ## 부족하지만 많이 사랑해주세요!
    > 이유 :


    # 참고 사이트
    *[ ](URL)
    *[flaticon](URL)
    *[pixalbay](URL)

    """
    # """ """ : 여러 줄을 묶어서 표시할 수 있는 문자열
    # ''' ''' : (통일기능)
)

# https://pixabay.com/ko
st.image(
    "https://cdn.pixabay.com/photo/2014/11/30/14/11/cat-551554_960_720.jpg"
)