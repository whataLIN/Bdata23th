import streamlit as st

st.write("함수를 응용해서 페이지 만들어보기")

st.write("# 행운뽑기")

#1-5개까지 살 수 있음
#1-3등까지

#0-9까지 고름
#당첨 시 상금 - 직접 입력
#button - 당첨/낙첨

number=st.selectbox("번호를 골라주세요",list(range(10)))
st.write(f"내가 고른 번호 : {number}")

