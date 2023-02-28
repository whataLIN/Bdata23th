# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    ---
    # 나에게 가장 도움이 될 것 같은 유튜브

    ## 노마드코더

    [![이미지 설명](https://i.ytimg.com/vi/Cnbmrh99c1o/hqdefault.jpg)](https://www.youtube.com/@nomadcoders)

    >>이유: 영어로 IT지식을 배울수 있어서

    ---

    # 다른 학생들에게 가장 도움이 될 것 같은 유튜브

    ## 드림코딩

    [![이미지 설명](https://i.ytimg.com/vi/TTLHd3IyErM/hqdefault.jpg)](https://www.youtube.com/@dream-coding)

    >>이유: 웹개발 프론트엔드의 기초부터 심화까지 배울 수 있음

    ---

  #참고사이트
  [icons8](https://icons8.com)
  [flaticon](https://flaticon.com)
  [pixabay](https://pixabay.com)
  
    
    ![이미지 설명] https://icons8.com/illustrations/illustration/demure-man-programs-on-laptop-while-sitting-in-an-armchair-1
    ![남자] https://icons8.com/illustrations/illustration/demure-man-programs-on-laptop-while-sitting-in-an-armchair-1
    
    """
)
