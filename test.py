import streamlit as st

# --- Custom CSS for background color and chat-like UI ---
# BlanchedAlmond: #FFEBCD (매우 연하고 따뜻한 살구빛 노란색 계열)
custom_css = """
<style>
/* 전체 바디와 앱 영역의 배경색을 설정합니다 */
body {
    background-color: #FFEBCD; /* 따뜻하고 연한 살구색 */
    color: #333333; /* 글자색을 진한 회색으로 설정하여 가독성을 높입니다 */
}
.stApp {
    background-color: #FFEBCD; /* Streamlit 앱 컨테이너의 배경색도 동일하게 설정 */
}
/* 헤더 글자색을 살짝 부드럽게 조정합니다 */
h1, h2, h3, h4, h5, h6 {
    color: #4A4A4A;
}

/* Chat-like UI styles */
.chat-container {
    max-width: 700px;
    margin: 0 auto;
    padding: 10px;
    background-color: #F8F8F8; /* 채팅 배경색을 살짝 다르게 */
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
}

.message {
    padding: 10px 15px;
    border-radius: 20px;
    margin-bottom: 10px;
    max-width: 70%;
    word-wrap: break-word;
    font-size: 15px;
}

.harulralla-message {
    background-color: #E2F0CB; /* 하룰랄라 메시지 배경색 (카톡 기본 녹색 계열) */
    align-self: flex-start;
    border-bottom-left-radius: 5px; /* 왼쪽 하단 모서리는 덜 둥글게 */
    display: flex;
    align-items: flex-start;
}
.harulralla-profile {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 10px;
    flex-shrink: 0;
}
.harulralla-profile img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
}
.harulralla-text-container {
    flex-grow: 1;
}

.user-message {
    background-color: #FFFACD; /* 사용자 메시지 배경색 (밝은 노란색 계열) */
    align-self: flex-end;
    border-bottom-right-radius: 5px; /* 오른쪽 하단 모서리는 덜 둥글게 */
}
.message-timestamp {
    font-size: 12px;
    color: #888888;
    margin-top: 5px;
    text-align: right; /* 사용자 메시지는 오른쪽, AI 메시지는 왼쪽 */
}
.harulralla-message .message-timestamp {
    text-align: left;
}
.stButton>button {
    background-color: #ADD8E6; /* Light Blue for send button */
    color: white;
    font-weight: bold;
    border-radius: 8px;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}
.stButton>button:hover {
    background-color: #87CEEB;
}
/* 정보 메시지 박스의 테두리를 부드럽게 만듭니다 */
.stAlert {
    border-radius: 8px;
}

/* Chat input area at bottom */
.chat-input-area {
    position: sticky;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #FFEBCD; /* 배경색과 동일하게 */
    padding: 10px 0;
    border-top: 1px solid #EDEDED;
    z-index: 100;
}

</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 페이지 설정
st.set_page_config(layout="centered")

# --- 하룰랄라 아이콘 (실제 이미지 경로를 지정하거나 base64로 인코딩) ---
# 예시: 여기서는 이모티콘으로 대체하거나, 실제 이미지 URL을 사용합니다.
HARULRALLA_ICON = "👩‍💻" # 실제 이미지가 있다면 "https://your-image-url/harulralla_icon.png"
USER_ICON = "😊"

# --- 상담 조언 함수 정의 (이전과 동일) ---
def get_counseling_message(category):
    # (이전과 동일한 조언 내용 함수)
    if category == '학업':
        return """
        사랑하는 당신, 학업이라는 큰 산 앞에서 고민하고 계시는군요. 때로는 너무나 버겁고, 나만 뒤처지는 것 같은 기분이 들 수도 있을 거예요. 하지만 기억해주세요, 당신은 지금 이 순간에도 충분히 잘 해내고 있고, 꾸준히 나아가고 있답니다.

        **점수나 결과에 너무 얽매이지 마세요.** 중요한 것은 어제보다 조금 더 성장한 오늘, 그리고 그 작은 노력들이 모여 만들어낼 내일이에요. 완벽해야 한다는 부담감에 지쳐있다면, 잠시 쉬어가며 마음의 여유를 찾는 것도 좋습니다.

        스스로에게 '이만하면 잘했어!'라고 따뜻하게 말해주세요. 당신의 노력과 인내는 분명 아름다운 결실을 맺을 거예요. 하룰랄라가 언제나 당신의 길을 진심으로 응원할게요.
        """
    elif category == '진로':
        return """
        소중한 당신, 진로에 대한 고민은 참으로 무겁고 막연하게 느껴질 수 있어요. 어떤 길을 선택해야 할지 몰라 불안하기도 하고, 주위의 기대 때문에 더 혼란스러울 수도 있겠죠. 하지만 이 고민의 시간은 결코 헛되지 않습니다. 이것은 당신이 진정으로 원하는 것이 무엇인지 찾아가는 소중한 과정이랍니다.

        **조급해하지 마세요.** 당장 정답을 찾지 못해도 괜찮아요. 다양한 경험을 통해 당신의 마음이 이끌리는 곳이 어디인지, 무엇을 할 때 가장 빛나는지 탐색해보세요. 인턴십, 동아리 활동, 관심 분야 스터디 등 작은 시도들이 큰 그림을 완성하는 조각이 될 수 있습니다.

        실패를 두려워하지 않는 용기, 그리고 나를 믿는 굳건한 마음만 있다면 분명 당신만의 특별한 길을 찾을 수 있을 거예요. 당신의 빛나는 미래를 하룰랄라가 진심으로 응원합니다.
        """
    elif category == '가족':
        return """
        다정한 당신, 가족과의 관계에서 힘든 마음을 가지고 계시는군요. 가장 가까운 존재이기에 오히려 더 어렵고 상처받을 때도 있다는 것을 알고 있어요. 서로에게 솔직한 마음을 표현하는 것이 쉽지 않을 때도 있고, 때로는 오해가 쌓여 마음의 벽이 생기기도 하죠.

        **가족은 우리 삶의 가장 소중한 울타리이자 근원적인 사랑의 공간이랍니다.** 잠시 시간을 내어 서로의 이야기를 들어주고, 진심으로 이해하려는 노력을 해보는 것은 어떨까요? 작은 진심이 담긴 따뜻한 말 한마디가 얼어붙었던 마음을 녹여줄 수도 있어요.

        당신도 충분히 노력하고 있으니 너무 자책하지 마세요. 당신의 소중한 가족에게 평화와 사랑이 가득하기를 하룰랄라가 마음 다해 기도합니다.
        """
    elif category == '연애':
        return """
        설레는 당신, 연애 때문에 고민하고 계시군요. 사랑은 우리를 행복하게도 하지만, 때로는 큰 아픔과 고민을 안겨주기도 해요. 상대방의 마음을 이해하기 어렵거나, 내 마음을 어떻게 표현해야 할지 몰라 답답할 수도 있겠네요.

        **가장 중요한 것은 바로 '당신 자신'입니다.** 스스로를 사랑하고 소중히 여길 때, 비로소 건강하고 아름다운 관계를 만들 수 있어요. 상대방에게 모든 것을 맞추기보다, 당신의 가치를 잊지 마세요.

        상대방과 솔직하고 열린 마음으로 대화하며 서로의 감정을 나누고, 작은 순간들을 소중히 여겨보세요. 관계는 두 사람이 함께 가꾸어 나가는 정원과 같으니까요. 지금 이 고민의 시간이 더 깊은 사랑으로 가는 밑거름이 될 거예요. 당신의 사랑이 늘 행복하기를 하룰랄라가 빌어줄게요.
        """
    elif category == '직장':
        return """
        성실한 당신, 직장 생활의 어려움 때문에 마음이 지쳐있으시군요. 쉼 없이 돌아가는 업무, 때로는 인간관계에서 오는 스트레스, 그리고 미래에 대한 불안감까지... 이 모든 것을 홀로 감당하기 버거울 때가 있을 거예요. 하지만 당신은 지금까지 정말 잘 버텨왔고, 당신의 노력은 분명 소중한 가치를 지니고 있답니다.

        **잠시 멈춰 서서 자신을 돌보는 시간을 가져보세요.** 스트레스를 해소할 나만의 방법은 무엇인지 찾아보고, 가능하다면 신뢰하는 동료나 선배와 터놓고 이야기해보는 것도 큰 힘이 될 수 있어요. 모든 것을 완벽하게 하려 하지 않아도 괜찮아요.

        당신의 건강과 행복이 가장 중요합니다. 하룰랄라는 당신이 직장에서 더욱 빛날 수 있도록 언제나 응원할게요. 당신의 노력이 헛되지 않을 거예요.
        """
    elif category == '인간관계':
        return """
        섬세한 당신, 인간관계로 인해 고민하고 계시군요. 사람은 사회적 존재이기에 관계는 우리의 삶에서 빼놓을 수 없는 중요한 부분이지만, 때로는 가장 큰 고민거리가 되기도 합니다. 오해와 갈등, 때로는 기대에 미치지 못하는 관계 때문에 마음이 아플 수도 있겠네요.

        **모든 사람과 완벽하게 잘 지낼 수는 없다는 것을 기억해주세요.** 당신의 소중한 에너지를 빼앗아가는 관계보다는, 당신을 진심으로 이해하고 지지해주는 관계에 더 집중하는 것이 중요해요. 스스로를 존중하고 건강한 경계를 설정하는 것이 행복한 관계의 시작이랍니다.

        당신의 마음을 편안하게 해주는 소중한 인연들이 가득하기를 하룰랄라가 진심으로 바랍니다. 괜찮아요, 좋은 관계는 분명히 존재합니다.
        """
    else: # 기타
        return """
        사랑하는 당신, 어떤 종류의 고민이든 홀로 감당하기 힘들 때는 언제든지 하룰랄라를 찾아와주세요. 당신의 마음속 깊은 이야기를 꺼내어 놓는 것만으로도 큰 위로가 될 수 있답니다. 모든 고민에는 해결책이 있거나, 아니면 최소한 그것을 견뎌낼 수 있는 당신의 강인함이 숨어 있어요.

        **당신은 혼자가 아닙니다.** 때로는 전문가의 도움을 받는 것도 아주 현명한 선택입니다. 당신을 아끼고 지지하는 많은 이들이 주변에 있다는 것을 잊지 마세요.

        이 힘든 시간이 당신을 더욱 단단하고 지혜롭게 만들 것이라고 믿어요. 하룰랄라는 언제나 당신의 옆에서 응원의 메시지를 보낼 거예요. 힘내세요, 당신의 내일은 오늘보다 더 밝을 거예요.
        """

# --- Initialize chat history in session_state ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "category" not in st.session_state:
    st.session_state.category = None
if "initialized" not in st.session_state:
    st.session_state.messages.append({"role": "harulralla", "content": "안녕하세요, 당신! 😊 하룰랄라 고민 상담소에 오신 것을 환영해요. 어떤 고민이 있으신가요?", "timestamp": "지금"})
    st.session_state.initialized = True

# --- 앱의 제목 및 설명 ---
st.title("💡 하룰랄라 고민 상담소")
st.markdown("편안하게 마음을 털어놓으세요.")
st.markdown("---") # 시각적인 구분선

# --- Main chat UI ---
st.container()
with st.container(): # Use a container to visually group chat history
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    # Display chat messages from history
    for message in st.session_state.messages:
        if message["role"] == "harulralla":
            st.markdown(f"""
            <div class="harulralla-message">
                <div class="harulralla-profile">{HARULRALLA_ICON}</div>
                <div class="harulralla-text-container">
                    <div style="font-weight: bold; margin-bottom: 3px;">하룰랄라</div>
                    <div>{message["content"]}</div>
                    <div class="message-timestamp">{message["timestamp"]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else: # user message
            st.markdown(f"""
            <div class="user-message">
                <div>{message["content"]}</div>
                <div class="message-timestamp">{message["timestamp"]}</div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Category Selection (at the top, before chat input for initial setup) ---
if st.session_state.category is None:
    st.markdown("---")
    st.header("1. 어떤 고민이신가요?")
    selected_category = st.selectbox(
        "아래 목록에서 당신의 마음에 가장 가까운 고민의 종류를 선택해주세요.",
        ['고민 종류를 선택해주세요', '학업', '진로', '가족', '연애', '직장', '인간관계', '기타'],
        key="category_select"
    )

    if selected_category != '고민 종류를 선택해주세요':
        st.session_state.category = selected_category
        st.session_state.messages.append({"role": "user", "content": f"제 고민은 '{st.session_state.category}'과 관련이 있어요.", "timestamp": "방금"})
        st.session_state.messages.append({"role": "harulralla", "content": f"네, **'{st.session_state.category}'** 관련 고민이시군요. 괜찮아요, 하룰랄라가 당신의 마음속 이야기를 들을 준비가 되어 있어요. 무엇이든 편안하게 이야기해주세요.📝", "timestamp": "지금"})
        # Rerun to update chat history after category selection
        st.experimental_rerun()
else:
    # --- Chat Input Area ---
    st.markdown('<div class="chat-input-area">', unsafe_allow_html=True)
    st.markdown("---")
    user_input = st.text_area(
        "당신의 고민을 여기에 편안하게 적어주세요. (최소 20자)",
        key="user_worry_input", # Unique key for the text area
        height=100,
        help="구체적으로 작성할수록 하룰랄라가 더 따뜻하고 적절한 조언을 해드릴 수 있어요."
    )

    if st.button("✉️ 보내기"):
        if user_input and len(user_input) >= 20:
            # Add user message to history
            st.session_state.messages.append({"role": "user", "content": user_input, "timestamp": "방금"})

            # Generate AI response based on selected category
            counseling_message = get_counseling_message(st.session_state.category)
            st.session_state.messages.append({"role": "harulralla", "content": counseling_message, "timestamp": "지금"})

            # Clear the input area after sending
            st.session_state.user_worry_input = "" # Clear the text_area

            # Rerun the app to display updated messages
            st.experimental_rerun()
        else:
            st.warning("⚠️ 당신의 소중한 고민 내용을 최소 20자 이상 작성해주셔야 하룰랄라가 더 깊이 있는 조언을 해드릴 수 있어요! 다시 한번 확인해주세요.")
    st.markdown('</div>', unsafe_allow_html=True)


# --- 앱 하단 푸터 (고정) ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'><sub>이 앱은 사용자에게 따뜻한 위로와 조언을 드리고자 제작되었습니다. 모든 조언은 일반적인 내용을 담고 있으며, 전문적인 상담을 대체할 수 없습니다.</sub></p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'><sub>Developed with ❤️ by 하룰랄라</sub></p>", unsafe_allow_html=True)
