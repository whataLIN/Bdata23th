# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # 나에게 가장 도움이 될 것 같은 유튜브
    ## 빵형의 개발도상국
    [링크](http://naver.com)
![이미지에 대한 설명](https://ouch-cdn2.icons8.com/I1jo3kiWiqFTrx9iGCXvMvgOraN1a1ToBW03QbC7mbw/rs:fit:256:256/czM6Ly9pY29uczgu/b3VjaC1wcm9kLmFz/c2V0cy9wbmcvMzAx/L2I5ZjYyY2ZkLTU2/YzQtNDc5Zi1hMzBk/LWQxYjljZjJjNjUz/NS5wbmc.png)
    !(https://w7.pngwing.com/pngs/914/758/png-transparent-github-social-media-computer-icons-logo-android-github-logo-computer-wallpaper-banner-thumbnail.png)
    > 이유 : 새로운 머신러닝/딥러닝 지식들이 많다
    # 다른 학생들에게 가장 도움이 될 것 같은 유튜브
    ## 노마드코더
    > 이유 : 최신 IT 트렌드를 쉽고 재밌게 전달해준다
    # 참고 사이트
    * [icons8](https://icons8.com/)
    * [flaticon](https://www.flaticon.com/)
    * [pixabay](https://pixabay.com/ko/)
    """
)

# """ """ : 여러 줄을 묶어서 표시할 수 있는 문자열
# ''' ''' (동일기능)