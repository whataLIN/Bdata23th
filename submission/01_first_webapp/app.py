# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동 """ 안에 마크다운 기반 입력 """
st.write(
    """
    # 나에게 가장 도움이 될것 같은 유튜브와 그 이유
    ## 오늘코드
    > 이유 : 데이터 관련한 예제가 많아보임

    # 남에게 가장 도움이 될 것 같은 유튜브와 그 이유
    ## 나도코딩
    > 이유 : 1분 파이썬 재생목록이 짧아서 쉬어보임

    #참고사이트
    *[icons8](https://icons8.com/illustrations/t/cat)
    *[flaticon](https://www.flaticon.com/)

    """
)
