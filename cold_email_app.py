import streamlit as st
import os
from google import genai

# ----------------------------
# Configure Gemini API
# ----------------------------
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="Cold Email Engine", page_icon="📧")

st.title("📧 AI Cold Email Sequence Generator")
st.markdown("Generate high-converting cold email sequences using Gemini AI.")
st.divider()

# ----------------------------
# Input Fields
# ----------------------------
prospect_name = st.text_input("Prospect Name")
company_name = st.text_input("Company Name")
industry = st.text_input("Industry")
pain_point = st.text_area("Main Pain Point")
your_offer = st.text_area("Your Offer")

# ----------------------------
# Generate Button
# ----------------------------
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
1) 3 Subject Line options
2) Primary Cold Email
3) Follow-up Email 1
4) Follow-up Email 2
5) Strong Call-to-Action

Keep it concise and high converting.
"""

        with st.spinner("Generating sequence..."):

            try:
                response = client.models.generate_content(
                    model="gemini-1.5-flash_latest",
                    contents=prompt
                )

                st.success("✅ Sequence Generated!")
                st.markdown("### 📩 Your Outreach Sequence")
                st.write(response.text)

            except Exception as e:
                st.error("❌ Error occurred")
                st.exception(e)

