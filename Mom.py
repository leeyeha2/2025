import streamlit as st

# 웹 앱의 기본 설정 (페이지 타이틀 등)
st.set_page_config(
    page_title="하룰랄라의 퍼스널 컬러 화장품 추천",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- 웹 앱 제목 및 설명 ---
st.title("💖 퍼스널 컬러 맞춤 화장품 추천 ✨")
st.markdown("""
안녕하세요! 당신의 퍼스널 컬러에 꼭 맞는 화장품을 찾아드릴게요.
아래에서 당신의 퍼스널 컬러를 선택하고, 인생템을 만나보세요!
""")

# --- 1. 퍼스널 컬러 선택 섹션 ---
st.header("1. 당신의 퍼스널 컬러는 무엇인가요?")

# 사용자로부터 퍼스널 컬러를 입력받는 드롭다운 메뉴
personal_color = st.selectbox(
    "아래에서 당신의 퍼스널 컬러를 선택해주세요.",
    ("선택해주세요", "봄 웜톤", "여름 쿨톤", "가을 웜톤", "겨울 쿨톤")
)

# --- 2. 화장품 추천 섹션 (조건부 표시) ---
if personal_color != "선택해주세요":
    st.header(f"2. {personal_color}을 위한 화장품 추천! 💄")
    st.write(f"**{personal_color}**에게 어울리는 화장품과 브랜드를 추천해드릴게요.")

    # 여기에 실제 화장품 추천 로직과 데이터를 연동하는 부분이 들어갈 거예요.
    # 지금은 예시 데이터를 사용합니다.

    # 🚨 중요: 실제 데이터는 데이터베이스나 CSV 파일 등에서 불러와서 처리해야 합니다.
    # 예시 데이터를 딕셔너리로 저장합니다. (실제로는 더 복잡한 데이터 구조가 필요)
    recommendations = {
        "봄 웜톤": {
            "립": ["코랄 핑크 립스틱 (브랜드 A)", "오렌지 레드 틴트 (브랜드 B)"],
            "블러셔": ["피치 블러셔 (브랜드 C)", "살구색 크림 블러셔 (브랜드 D)"],
            "아이섀도우": ["골드 브라운 팔레트 (브랜드 E)", "피치 코랄 팔레트 (브랜드 F)"],
            "추천 브랜드": ["로맨틱 코랄", "프레쉬 피치"]
        },
        "여름 쿨톤": {
            "립": ["모브 핑크 립스틱 (브랜드 G)", "체리 레드 틴트 (브랜드 H)"],
            "블러셔": ["라벤더 핑크 블러셔 (브랜드 I)", "딸기우유색 파우더 (브랜드 J)"],
            "아이섀도우": ["쿨 그레이 팔레트 (브랜드 K)", "뮤트 로즈 팔레트 (브랜드 L)"],
            "추천 브랜드": ["퓨어 블루", "쿨 로즈"]
        },
        "가을 웜톤": {
            "립": ["칠리 레드 립스틱 (브랜드 M)", "브릭 오렌지 틴트 (브랜드 N)"],
            "블러셔": ["말린 장미 블러셔 (브랜드 O)", "베이지 브라운 파우더 (브랜드 P)"],
            "아이섀도우": ["카키 브라운 팔레트 (브랜드 Q)", "골드 카키 팔레트 (브랜드 R)"],
            "추천 브랜드": ["딥 어텀", "골든 브라운"]
        },
        "겨울 쿨톤": {
            "립": ["버건디 립스틱 (브랜드 S)", "플럼 핑크 틴트 (브랜드 T)"],
            "블러셔": ["자주색 블러셔 (브랜드 U)", "베리 컬러 파우더 (브랜드 V)"],
            "아이섀도우": ["모노톤 그레이 팔레트 (브랜드 W)", "블루 블랙 팔레트 (브랜드 X)"],
            "추천 브랜드": ["모던 블랙", "클리어 윈터"]
        }
    }

    # 선택된 퍼스널 컬러에 맞는 추천 결과를 표시
    if personal_color in recommendations:
        st.subheader("추천 화장품")
        for item_type, items in recommendations[personal_color].items():
            if item_type == "추천 브랜드":
                continue # 브랜드는 따로 표시

            st.markdown(f"**- {item_type}:**")
            for item in items:
                st.write(f"  - {item}")

        st.subheader("추천 브랜드")
        if "추천 브랜드" in recommendations[personal_color]:
            for brand in recommendations[personal_color]["추천 브랜드"]:
                st.write(f"- {brand}")
    else:
        st.write("죄송합니다. 해당 퍼스널 컬러에 대한 추천 정보가 아직 없습니다. (데이터 부족)")

else:
    st.info("당신의 퍼스널 컬러를 선택하시면 맞춤 화장품을 추천해 드려요!")

st.markdown("---")
st.caption("궁금한 점이 있다면 언제든지 하룰랄라에게 물어보세요!")
    elif 40 <= age < 60:
        recommendations.append("고급스럽고 우아한 분위기를 연출하는 컬러")
        if hair_condition == "건강함":
            recommendations.append("깊이 있는 다크 브라운, 와인 브라운")
            product_suggestions.append("로레알 파리 엑셀랑스 앙증 크림 염색 또는 려(Ryo) 백려염 새치 전용")
        elif hair_condition == "손상됨":
            recommendations.append("모발 손상을 최소화하는 자연스러운 다크 브라운")
            product_suggestions.append("모발 손상을 줄여주는 제품: 티타드 물염색약 (PPD 무첨가), 로레알 파리 엑셀랑스 (모발 케어 포함)")
        elif hair_condition == "염색모":
            recommendations.append("뿌리 염색 위주로 기존 색상 유지, 새치 커버 겸용 고려")
            product_suggestions.append("로레알 파리 엑셀랑스 앙증 크림 염색 (강력 새치 커버)")
        elif hair_condition == "새치 커버":
            recommendations.append("자연 갈색, 흑갈색 등 자연스러운 새치 커버 염색약")
            product_suggestions.append("새치 커버 전문 제품: 로레알 파리 엑셀랑스 앙증 크림 염색 또는 려(Ryo) 백려염 새치 전용")

    else: # age >= 60
        recommendations.append("두피와 모발 건강을 최우선으로 하는 순한 성분 컬러")
        if hair_condition == "건강함" or hair_condition == "손상됨":
            recommendations.append("자연스러운 블랙 또는 내추럴 브라운")
            product_suggestions.append("두피 자극이 적은 제품: 티타드 물염색약, 려(Ryo) 백려염 새치 전용")
        elif hair_condition == "염색모":
            recommendations.append("기존 염색모와 자연스럽게 연결되는 톤 유지")
            product_suggestions.append("로레알 파리 엑셀랑스 앙증 크림 염색 (깔끔한 새치 커버 및 색상 유지)")
        elif hair_condition == "새치 커버":
            recommendations.append("저자극 순한 성분의 새치 커버용 블랙 또는 다크 브라운")
            product_suggestions.append("새치 커버 전문 및 순한 제품: 티타드 물염색약, 려(Ryo) 백려염 새치 전용")

    # 모발 상태에 따른 추가 고려사항 (전체 연령대 공통)
    if hair_condition == "손상됨":
        recommendations.append("모발 손상을 줄여주는 트리트먼트 성분 함유 염색약 사용")
        recommendations.append("잦은 염색보다는 텀을 두고 염색하기")
    elif hair_condition == "새치 커버":
        recommendations.append("커버력과 지속력이 좋은 새치 전용 염색약 추천")
    elif hair_condition == "염색모":
        recommendations.append("탈색/블리치 경험이 있다면 전문가와 상담 권장")

    final_recommendation = "\n- ".join(recommendations)
    if product_suggestions:
        final_recommendation += "\n\n**✅ 추천 제품:**\n- " + "\n- ".join(list(set(product_suggestions))) # 중복 제거

    if not recommendations and not product_suggestions:
        return "죄송해요, 입력하신 정보로는 적절한 염색약 추천을 찾기 어렵습니다."
    else:
        return final_recommendation

# Streamlit 웹 앱의 제목 설정
st.title('🎨 당신의 헤어 컬러 컨설턴트')
st.markdown("나이와 모발 상태에 맞춰 당신에게 가장 어울리는 염색약과 제품을 추천해 드립니다.")

# 사용자 입력 받기
age = st.number_input('당신의 나이를 입력해주세요 (만 나이 기준):', min_value=1, max_value=120, value=18)

hair_condition_options = [
    '선택해주세요',
    '건강함 (윤기 있고 탄력 있음)',
    '손상됨 (푸석하고 건조하며 끊어짐)',
    '염색모 (이미 염색된 상태)',
    '새치 커버 (새치가 많아 염색 필요)'
]
hair_condition_display_to_value = {
    '건강함 (윤기 있고 탄력 있음)': '건강함',
    '손상됨 (푸석하고 건조하며 끊어짐)': '손상됨',
    '염색모 (이미 염색된 상태)': '염색모',
    '새치 커버 (새치가 많아 염색 필요)': '새치 커버'
}
selected_condition_display = st.selectbox(
    '당신의 모발 상태는 어떤가요?',
    hair_condition_options
)
hair_condition = hair_condition_display_to_value.get(selected_condition_display, None)


# 추천 버튼
if st.button('염색약 추천받기'):
    if hair_condition == "선택해주세요" or hair_condition is None:
        st.warning("모발 상태를 선택해주세요.")
    else:
        st.markdown(f"### 당신을 위한 염색약 추천 결과:")
        st.markdown(f"**나이**: {age}세")
        st.markdown(f"**모발 상태**: {selected_condition_display.split(' (')[0]}") # 괄호 안 설명 제거
        
        recommendation_text = recommend_hair_dye(age, hair_condition)
        
        st.success(f"- {recommendation_text}")

st.markdown("---")
st.markdown("_이 추천은 참고용이며, 실제 염색 전에는 전문가와 상담하시는 것이 좋습니다. 제품 구매 전 성분 및 사용법을 꼭 확인하세요._")
