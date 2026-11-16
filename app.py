
import random
import streamlit as st

# 웹앱 제목
st.title("🍱 오늘의 점심 메뉴 추천")
st.write("오늘 점심은 무엇을 먹을까요?")
st.write("버튼을 누르면 랜덤으로 점심 메뉴를 추천해 드립니다!")

# 점심 메뉴 목록
menu_list = [
    "🍚 김치찌개",
    "🍜 짜장면",
    "🍗 치킨",
    "🍔 햄버거",
    "🍣 초밥",
    "🍝 파스타",
    "🥘 부대찌개",
    "🍛 카레",
    "🥩 제육볶음",
    "🍲 순두부찌개",
    "🌮 떡볶이",
    "🥗 샐러드"
]

# 메뉴 추천 버튼
if st.button("🎲 오늘의 점심 메뉴 뽑기"):

    # 랜덤으로 메뉴 선택
    lunch = random.choice(menu_list)

    # 추천 결과 출력
    st.success("오늘의 추천 메뉴는?")
    st.header(lunch)
    st.balloons()

