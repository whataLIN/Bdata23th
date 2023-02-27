# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # 나에게 가장
    ## 도움이 될 것 같은 유튜브
    ![](https://ouch-cdn2.icons8.com/8FMlpaAfpOBUuTXT0v_3h0-C-UslBKs-XAf_Ql0y6us/rs:fit:256:309/czM6Ly9pY29uczgu/b3VjaC1wcm9kLmFz/c2V0cy9wbmcvNTI4/L2ZhYTU5MzcyLTA5/YjctNGU0OC1hM2Jh/LTg1YzIwNzg2ZWI5/NC5wbmc.png)
    ---
    ### 노마드코더
    ---
    > 이유 : 주로 개발시장에 현황에 대해 소신 발언이 많은 편이며
    자칫 어려운 코딩 내용들을 쉬운 말로 풀어내서 이야기하기 때문에 
    나같은 입문자들에게 개발시장의 현황에 대해서 알 수 있었다.

    # 다른 학생들에게 가장 
    ## 도움이 될 것 같은 유튜브
    ![](https://ouch-cdn2.icons8.com/SaA2mPHCnnMuPfAaLtPt7s-AFaV8S9zJzIfT3DJPpA4/rs:fit:256:290/czM6Ly9pY29uczgu/b3VjaC1wcm9kLmFz/c2V0cy9wbmcvOTE3/L2NiOTE0NTFkLTI4/NjMtNGVhMy04MDNj/LWE2ZTJmNDJlMDJk/OS5wbmc.png)
    ---
    ### 나도 코딩
    ---
    > 이유 : 주로 고퀄리티 무료 강좌들을 업로드하지만
    가끔씩 개발자로써의 조언과 재밌는 심심풀이 영상을 올리기 때문에
    다양한 재미를 느낄 수 있는 채널이다.

    """
)

# """ """ : 여러 줄을 묶어서 표시할 수 있는 문자열
# ''' ''' (동일 기능)