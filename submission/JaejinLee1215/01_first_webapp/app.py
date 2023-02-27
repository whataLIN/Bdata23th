# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # 나에게 가장 도움이 될 것 같은 유튜브
    ## 빵형의 개발도상국
    > 이유 : 블라블라

    # 다른 학생들에게 가장 도움이 될 것 같은 유튜브
    ## 노마드코더
    > 이유 : 최신 it 트렌드를 쉽고 재밌게 전달해준다

    * 1$ = 1,300원
    * ^_^
    
    # 참고 사이트
    * [icons8](https://icons8.com/)
    * [flaticon](https://www.flaticon.com/)
    * [pixabay](https://pixabay.com/ko/)
    """
)