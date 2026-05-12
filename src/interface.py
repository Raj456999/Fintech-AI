import streamlit as st
from rag_pipeline import get_answer
import base64
import os

# =========================================================
# LOAD BACKGROUND IMAGE
# =========================================================

# FUNCTION TO LOAD IMAGE
def get_base64_image(image_name):

    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, image_name)

    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(
            img_file.read()
        ).decode()

    return encoded

# LOAD IMAGE
bg_image = get_base64_image("fintech.jpg")

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="FinTech AI Assistant",
    page_icon="💳",
    layout="centered"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(f"""
<style>

/* ======================================================
MAIN BACKGROUND
====================================================== */

.stApp {{
    background-image: linear-gradient(
        rgba(0,0,0,0.75),
        rgba(0,0,0,0.80)
    ),
    url("data:image/jpg;base64,{bg_image}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    color: white;
}}

/* ======================================================
SIDEBAR
====================================================== */

[data-testid="stSidebar"] {{
    background-color: #0f172a;
}}

/* ======================================================
TITLE
====================================================== */

.main-title {{
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: #ffffff;
    margin-bottom: 10px;
}}

.sub-title {{
    text-align: center;
    font-size: 18px;
    color: #cbd5e1;
    margin-bottom: 30px;
}}

/* ======================================================
CHAT INPUT
====================================================== */

.stChatInput input {{
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 15px !important;
    border: 2px solid #06b6d4 !important;
}}

/* ======================================================
USER MESSAGE
====================================================== */

.user-message {{
    background: linear-gradient(
        90deg,
        #2563eb,
        #06b6d4
    );

    padding: 15px;
    border-radius: 15px;
    margin: 10px 0;
    color: white;
    font-size: 16px;
}}

/* ======================================================
ASSISTANT MESSAGE
====================================================== */

.assistant-message {{
    background-color: #111827;

    padding: 15px;
    border-radius: 15px;
    margin: 10px 0;
    color: white;
    font-size: 16px;
    border: 1px solid #1e40af;
}}

/* ======================================================
BUTTONS
====================================================== */

.stButton > button {{
    background: linear-gradient(
        90deg,
        #2563eb,
        #06b6d4
    );

    color: white;
    border-radius: 12px;
    border: none;
    height: 45px;
    width: 100%;
    font-size: 18px;
    transition: 0.3s;
}}

.stButton > button:hover {{
    transform: scale(1.02);
    background: linear-gradient(
        90deg,
        #1d4ed8,
        #0891b2
    );
}}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("💳 FinTech AI")

st.sidebar.markdown("---")

st.sidebar.write(
    "AI-powered FinTech assistant using RAG architecture."
)

st.sidebar.write("### 📌 Features")

st.sidebar.write("• RBI Regulations")
st.sidebar.write("• UPI & NPCI")
st.sidebar.write("• Digital Banking")
st.sidebar.write("• BNPL & Lending")
st.sidebar.write("• Financial Policies")
st.sidebar.write("• FinTech Knowledge Base")

st.sidebar.write("### ⚙ Built With")

st.sidebar.write("• LangChain")
st.sidebar.write("• FAISS / Pinecone")
st.sidebar.write("• Groq LLM")
st.sidebar.write("• Streamlit")

# =========================================================
# TITLE
# =========================================================

st.markdown(
    """
    <div class='main-title'>
        💳 FinTech AI Assistant
    </div>

    <div class='sub-title'>
        RBI • UPI • NPCI • Digital Banking • FinTech Regulations
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(
            f"""
            <div class="user-message">
            👤 {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="assistant-message">
            🤖 {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# CHAT INPUT
# =========================================================

query = st.chat_input(
    "Ask about RBI, UPI, fintech, banking, regulations..."
)

# =========================================================
# HANDLE USER QUERY
# =========================================================

if query:

    # STORE USER MESSAGE
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    # DISPLAY USER MESSAGE
    st.markdown(
        f"""
        <div class="user-message">
        👤 {query}
        </div>
        """,
        unsafe_allow_html=True
    )

    # GENERATE RESPONSE
    with st.spinner(
        "Analyzing fintech knowledge base..."
    ):

        response = get_answer(query)

    # STORE ASSISTANT RESPONSE
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    # DISPLAY RESPONSE
    st.markdown(
        f"""
        <div class="assistant-message">
        🤖 {response}
        </div>
        """,
        unsafe_allow_html=True
    )
