import streamlit as st

st.write("""## 어떤 유튜브 채널을 알아볼까?""")
whichChannel=[None,"나에게 가장 도움이 될 것 같은 유튜브", "다른 학생들에게 가장 도움이 될 것 같은 유튜브"]
my_choice = st.selectbox('선택하세요', whichChannel)

if my_choice==whichChannel[1]:
    st.write(

    """

    ## 나에게 가장 도움이 될 것 같은 유튜브
    #### 빵형의 개발도상국
    ![유튜브 이미지](https://yt3.googleusercontent.com/ytc/AL5GRJWEjUOIX_yyyHbeg73QKMQarL5Nu2qBrk3BXwyE=s88-c-k-c0x00ffffff-no-rj)
    [link](https://www.youtube.com/@bbanghyong)

    > 이유: 새로운 머신러닝/딥러닝 지식들이 많다

    """
    )


if my_choice==whichChannel[2]:
    st.write(

    """
    ## 다른 학생들에게 가장 도움이 될 것 같은 유튜브
    #### 노마드코더
    ![유튜브 이미지](https://yt3.googleusercontent.com/ytc/AL5GRJWCKbcOn_YX6jhiTrNoYBV3pg0eWu41jb2zpkXHjA=s88-c-k-c0x00ffffff-no-rj)
    [link](https://www.youtube.com/@nomadcoders)

    > 이유 : 최신 IT 트렌드를 쉽고 재밌게 전달해준다.
    """
    )
