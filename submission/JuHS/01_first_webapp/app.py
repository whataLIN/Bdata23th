# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    ![이미지에 대한 설명](https://cdn.imweb.me/thumbnail/20221116/b33db8955fb2f.png)
    #### **데이터 엔지니어링 트랙 23기 주현성**
    
    # 나에게 가장 도움이 될 것 같은 유튜브
    
    ![이미지에 대한 설명](https://i.ytimg.com/vi/1I3hMwQU6GU/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLADnpGfxOX13n9Sp78ug6cFst-XPw)
    ## [얄팍한 코딩사전](https://www.youtube.com/@yalco-coding)

    > 구독자 : 8.58만명


    > 이유 : 새로운 머신러닝/딥러닝 지식들이 많다
    ## 다른 학생들에게 가장 도움이 될 것 같은 유튜브
    ### 노마드코더
    > 이유 : 최신 IT 트렌드를 쉽고 재밌게 전달해준다
    # 참고 사이트
    * [icons8](https://icons8.com/)
    * [flaticon](https://www.flaticon.com/)
    * [pixabay](https://pixabay.com/ko/)
    """
)

# """ """ : 여러 줄을 묶어서 표시할 수 있는 문자열
# ''' ''' (동일기능)