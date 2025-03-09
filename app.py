import streamlit as st
import google.generativeai as genai

import re

# Configure Gemini API
genai.configure(api_key="AIzaSyDYyQZKFJnnzvyjQoptaT5Pc_0xWDsch80")
model = genai.GenerativeModel("gemini-1.5-flash")  # Updated to Gemini 2.0 Flash

# Function to analyze URL for phishing
def analyze_url(url):
    phishing_keywords = ["login", "verify", "update", "secure", "free", "bonus", "banking", "account", "password", "reset"]
    
    if any(keyword in url.lower() for keyword in phishing_keywords) or re.search(r"\d{6,}", url):
        return "🚨 Warning! This URL may be a phishing link. Avoid clicking on unknown links."
    return "✅ This URL looks safe, but always verify the source."

# Function to check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "❌ Weak: Password should be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return "⚠️ Moderate: Add at least one uppercase letter."
    if not re.search(r"[0-9]", password):
        return "⚠️ Moderate: Add at least one number."
    if not re.search(r"[!@#$%^&*()_+]", password):
        return "⚠️ Moderate: Add at least one special character (!@#$%^&*)."
    return "✅ Strong password! Keep it secure."

# Function to get AI-powered security tips using Gemini 2.0 Flash
def get_security_advice(query):
    try:
        response = model.generate_content(query)
        return response.text if response and response.text else "⚠️ Error: Unable to fetch security advice."
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="Cybersecurity Advisor AI", layout="wide")
st.title("🛡️ Cybersecurity Advisor AI (Powered by Gemini 2.0 Flash)")

# Tab layout
tab1, tab2, tab3 = st.tabs(["🔗 Phishing Detection", "🔑 Password Strength", "🛠️ Security Tips"])

# Phishing detection
with tab1:
    st.subheader("🔍 Phishing URL Detector")
    url = st.text_input("Enter a URL to check for phishing:", placeholder="E.g., https://secure-login.com")
    if st.button("Check URL"):
        if url:
            result = analyze_url(url)
            st.write(result)
        else:
            st.warning("Please enter a valid URL.")

# Password strength checker
with tab2:
    st.subheader("🔑 Password Strength Checker")
    password = st.text_input("Enter your password:", type="password")
    if st.button("Check Password Strength"):
        if password:
            strength = check_password_strength(password)
            st.write(strength)
        else:
            st.warning("Please enter a password.")

# AI-powered security tips using Gemini 2.0 Flash
with tab3:
    st.subheader("🛠️ Ask for Cybersecurity Tips")
    query = st.text_area("Ask me about online security:", placeholder="E.g., How to protect my email?")
    if st.button("Get Security Advice"):
        if query:
            advice = get_security_advice(query)
            st.write(advice)
        else:
            st.warning("Please enter a query.")

st.markdown("🚀 Developed with ❤️ using Streamlit & Gemini 2.0 Flash")
