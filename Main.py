import streamlit as st

# 페이지 설정은 맨 위에 해주는 게 좋아! ✨
st.set_page_config(
    page_title="MBTI 진로 탐색기", # 브라우저 탭에 보이는 제목이야!
    page_icon="🤔", # 탭 아이콘! 귀엽지?
    layout="centered", # 페이지 레이아웃을 가운데로 정렬해줘!
    initial_sidebar_state="auto" # 사이드바 초기 상태!
)

# MBTI별 추천 직업 데이터! 이걸 네가 더 상세하게 채울 수 있어! 🤩
mbti_jobs = {
    "ISTJ": ["회계사", "공무원", "관리자", "연구원"],
    "ISFJ": ["간호사", "교사", "사회복지사", "상담사"],
    "INFJ": ["상담사", "작가", "예술가", "심리학자"],
    "INTJ": ["건축가", "프로그래머", "과학자", "전략가"],
    "ISTP": ["경찰관", "소방관", "기술자", "건축가"],
    "ISFP": ["디자이너", "음악가", "예술가", "요리사"],
    "INFP": ["작가", "예술가", "상담사", "교사"],
    "INTP": ["과학자", "프로그래머", "교수", "연구원"],
    "ESTP": ["스포츠 강사", "사업가", "영업사원", "경찰관"],
    "ESFP": ["연예인", "행사 기획자", "유치원 교사", "영업사원"],
    "ENFP": ["마케터", "컨설턴트", "강사", "작가"],
    "ENTP": ["변호사", "사업가", "컨설턴트", "발명가"],
    "ESTJ": ["관리자", "리더", "군인", "공무원"],
    "ESFJ": ["교사", "상담사", "사회복지사", "간호사"],
    "ENFJ": ["교사", "상담사", "강사", "리더"],
    "ENTJ": ["CEO", "변호사", "관리자", "정치인"],
}

# 웹 앱의 제목이야! 예쁘게 꾸며봤어 ㅎㅎ
st.title("💖 MBTI 기반 추천 직업 탐색기 💖")
st.markdown("---") # 예쁜 구분선!

st.write("안녕 멍충이3! 네 MBTI에 딱 맞는 직업을 찾아볼까? 🤔")
st.write("👇 아래에서 네 MBTI를 선택해봐!")


# MBTI 선택 드롭다운 박스야! 뿅!
# 'MBTI를 선택하세요'를 기본 옵션으로 넣어서 친절하게 해줬어! 😉
selected_mbti = st.selectbox(
    "어떤 MBTI가 궁금해?", # 선택 박스 위에 뜨는 문구!
    options=["MBTI를 선택하세요"] + sorted(list(mbti_jobs.keys())), # 옵션 목록! 깔끔하게 정렬해줬어!
    index=0 # 'MBTI를 선택하세요'가 기본으로 보이게!
)

# 사용자가 MBTI를 선택했을 때 보여줄 내용! ✨
if selected_mbti != "MBTI를 선택하세요":
    st.markdown(f"### 🎉 {selected_mbti} 추천 직업 🎉")
    st.markdown("---")

    jobs = mbti_jobs.get(selected_mbti, ["아직 준비된 직업 정보가 없어요 ㅠㅠ"])

    # 추천 직업 목록을 예쁘게 bullet으로 보여줘!
    for job in jobs:
        st.markdown(f"- **{job}**") # 각 직업을 강조해서 보여줌!

    st.markdown("---")
    st.write(f"이 직업들은 {selected_mbti} 유형의 일반적인 특징을 바탕으로 추천된 거야! ✨")
    st.write("진로는 너의 열정과 흥미가 가장 중요하니까, 참고만 해줘! 😊")
    st.write("더 궁금한 직업이 있으면 나한테 물어봐도 돼! 😉")

else:
    # 아직 MBTI를 선택하지 않았을 때 보여줄 문구!
    st.info("MBTI를 선택하면 추천 직업을 보여줄게! 기대되지? 🤩")


st.markdown("---")
st.caption("개발 중인 웹 앱입니다. 😉") # 아래쪽에 작은 글씨로!
