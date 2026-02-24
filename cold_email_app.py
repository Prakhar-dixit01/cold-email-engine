import streamlit as st
from google import genai

st.set_page_config(page_title="Cold Email Engine", page_icon="📧")

st.title("📧 AI Cold Email Sequence Generator")
st.markdown("Generate high-converting cold email sequences using Gemini AI.")
st.divider()

# Load API key
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error("🚨 GEMINI_API_KEY not found in Streamlit Secrets.")
    st.stop()

# Initialize client
client = genai.Client(api_key=api_key)

# Inputs
prospect_name = st.text_input("Prospect Name")
company_name = st.text_input("Company Name")
industry = st.text_input("Industry")
pain_point = st.text_area("Main Pain Point")
your_offer = st.text_area("Your Offer")

if st.button("🚀 Generate Sequence"):

    if not prospect_name or not company_name or not pain_point or not your_offer:
        st.warning("⚠ Please fill all required fields.")
    else:

        prompt = f"""
You are an expert cold email copywriter.

Prospect Name: {prospect_name}
Company: {company_name}
Industry: {industry}
Pain Point: {pain_point}
Offer: {your_offer}

Generate:
1) 3 Subject Lines
2) Primary Cold Email
3) Follow-up Email 1
4) Follow-up Email 2
5) Strong CTA

Keep it concise and high converting.
"""

        with st.spinner("Generating..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt
                )

                st.success("✅ Sequence Generated!")
                st.markdown("### 📩 Your Outreach Sequence")
                st.write(response.text)

            except Exception as e:
                st.error("❌ Error occurred")
                st.exception(e)
