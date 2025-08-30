import streamlit as st

def recommend_hair_dye(age, hair_condition):
    """
    사용자의 연령과 모발 상태에 따라 염색약을 추천합니다.
    이 함수는 예시이므로, 더 구체적인 추천 로직으로 확장할 수 있습니다.
    """
    recommendations = []

    # 1. 연령에 따른 추천
    if age < 20:
        recommendations.append("트렌디한 애쉬 계열 또는 파스텔톤 염색")
        if hair_condition == "건강함":
            recommendations.append("밝은 톤의 애쉬 브라운, 핑크 브라운")
        elif hair_condition == "손상됨":
            recommendations.append("비교적 톤 다운된 애쉬 그레이 또는 모카 브라운")
        elif hair_condition == "염색모":
            recommendations.append("기존 색상에 어울리는 톤업/톤다운 염색 또는 시크릿 투톤")

    elif 20 <= age < 40:
        recommendations.append("세련되고 개성을 살릴 수 있는 컬러")
        if hair_condition == "건강함":
            recommendations.append("초코 브라운, 카키 브라운, 레드 와인색")
        elif hair_condition == "손상됨":
            recommendations.append("내추럴한 다크 브라운, 톤다운된 애쉬 계열")
        elif hair_condition == "염색모":
            recommendations.append("브릿지 또는 톤온톤 염색으로 입체감 표현")
        elif hair_condition == "새치 커버":
            recommendations.append("새치 커버 겸용 자연 갈색 또는 다크 브라운")

    elif 40 <= age < 60:
        recommendations.append("고급스럽고 우아한 분위기를 연출하는 컬러")
        if hair_condition == "건강함":
            recommendations.append("깊이 있는 다크 브라운, 와인 브라운")
        elif hair_condition == "손상됨":
            recommendations.append("모발 손상을 최소화하는 자연스러운 다크 브라운")
        elif hair_condition == "염색모":
            recommendations.append("뿌리 염색 위주로 기존 색상 유지, 새치 커버 겸용 고려")
        elif hair_condition == "새치 커버":
            recommendations.append("자연 갈색, 흑갈색 등 자연스러운 새치 커버 염색약")

    else: # age >= 60
        recommendations.append("두피와 모발 건강을 최우선으로 하는 순한 성분 컬러")
        if hair_condition == "건강함" or hair_condition == "손상됨":
            recommendations.append("자연스러운 블랙 또는 내추럴 브라운")
        elif hair_condition == "염색모":
            recommendations.append("기존 염색모와 자연스럽게 연결되는 톤 유지")
        elif hair_condition == "새치 커버":
            recommendations.append("저자극 순한 성분의 새치 커버용 블랙 또는 다크 브라운")

    # 모발 상태에 따른 추가 고려사항 (전체 연령대 공통)
    if hair_condition == "손상됨":
        recommendations.append("모발 손상을 줄여주는 트리트먼트 성분 함유 염색약 사용")
        recommendations.append("잦은 염색보다는 텀을 두고 염색하기")
    elif hair_condition == "새치 커버":
        recommendations.append("커버력과 지속력이 좋은 새치 전용 염색약 추천")
    elif hair_condition == "염색모":
        recommendations.append("탈색/블리치 경험이 있다면 전문가와 상담 권장")

    if not recommendations:
        return "죄송해요, 입력하신 정보로는 적절한 염색약 추천을 찾기 어렵습니다."
    else:
        return "\n- ".join(recommendations)

# Streamlit 웹 앱의 제목 설정
st.title('🎨 당신의 헤어 컬러 컨설턴트')
st.markdown("나이와 모발 상태에 맞춰 당신에게 가장 어울리는 염색약을 추천해 드립니다.")

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
st.markdown("_이 추천은 참고용이며, 실제 염색 전에는 전문가와 상담하시는 것이 좋습니다._")

