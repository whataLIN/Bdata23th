# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # 나에게 가장 도움이 될 것 같은 유튜브

    ---
    ## [메타코드M](https://www.youtube.com/@mcodeM)
    > 이유 : 기술 면접이나 새로운 트렌드 기술을 잘 알려주고 논문 등 개념에 대한 리딩법의 가독성이 좋다.

    # 다른 학생들에게 가장 도움이 될 것 같은 유튜브

    ---
    ## [드림코딩](https://www.youtube.com/@dream-coding)
    > 이유 : 개발에 아예 처음이시거나 개발자의 현실 등을 잘 보여주고 어렵지 않게 트렌드를 설명해준다.

    ```
    # 참고 사이트
    * [icons8](https://icons8.com/)
    * [flaticon](https://www.flaticon.com/)
    * [pixabay](https://pixabay.com/ko/)
    ```

    """
)

# """ """ : 여러 줄을 묶어서 표시할 수 있는 문자열
# ''' '''(동일기능)