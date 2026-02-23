import streamlit as st
import subprocess

st.set_page_config(page_title="Cold Email Engine", page_icon="🚀", layout="wide")

# ---------- CUSTOM DARK THEME CSS ----------
st.markdown("""
<style>
body {
    background-color: #0f0f0f;
    color: white;
}

.main {
    background-color: #0f0f0f;
}

.stTextInput>div>div>input, 
.stTextArea textarea {
    background-color: #1c1c1c;
    color: white;
    border-radius: 8px;
    border: 1px solid #333;
}

.stSelectbox div {
    background-color: #1c1c1c;
    color: white;
}

.stButton>button {
    background: linear-gradient(90deg, #6a11cb, #2575fc);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #2575fc, #6a11cb);
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<h1 style='text-align:center; color:white;'>
🚀 B2B Cold Email Outreach Engine
</h1>
<p style='text-align:center; color:gray; font-size:18px;'>
Generate high-converting personalized outreach sequences in seconds.
</p>
""", unsafe_allow_html=True)

st.divider()

# ---------- INPUT SECTION ----------
col1, col2 = st.columns(2)

with col1:
    prospect_name = st.text_input("👤 Prospect Name")
    company_name = st.text_input("🏢 Company Name")
    website = st.text_input("🌐 Company Website")

with col2:
    your_service = st.text_area("💼 Your Service / Offer")
    pain_point = st.text_area("⚡ Target Pain Point")
    tone = st.selectbox("🎯 Tone", ["Professional", "Confident", "Friendly", "Direct"])

st.divider()

# ---------- GENERATE BUTTON ----------
if st.button("🚀 Generate Outreach Sequence"):

    if prospect_name and company_name and your_service:

        prompt = f"""
        You are a B2B cold email expert.

        Prospect Name: {prospect_name}
        Company Name: {company_name}
        Website: {website}
        Service Offered: {your_service}
        Pain Point: {pain_point}
        Tone: {tone}

        Generate:

        1) 3 Subject Line options
        2) Primary Cold Email (short, personalized)
        3) Follow-up Email 1
        4) Follow-up Email 2
        5) Strong Call-to-Action

        Keep it concise and high converting.
        """

        with st.spinner("Generating sequence..."):
            result = subprocess.run(
                ["ollama", "run", "mistral", prompt],
                capture_output=True,
                text=True
            )

            st.success("✅ Sequence Generated")

            st.markdown("### 📩 Your Outreach Sequence")
            st.markdown(result.stdout)

    else:
        st.warning("⚠ Please fill required fields.")