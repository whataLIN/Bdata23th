# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # 나에게 가장 도움이 될 것 같은 유튜브
    ## 노마드코더
    > 이유 : 

    # 다른 학생들에게 가장 도움이 될 것 같은 유튜브
    ## 나도 코딩
    > 이유 :

    #참고사이트
    [icons8](http://icons88.com)
    [flaticon](http://flaticon.com)
    [pixabay](http://pixabay.com)
    
    """
)

# """ """ : 여러 줄을 묶어서 표시할 수 있는 문자열
# ''' ''' (동일 기능)