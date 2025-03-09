AI Cybersecurity Advisor

🔒 Overview

The AI Cybersecurity Advisor is a powerful web application designed to assist users in enhancing their online security. Built using Streamlit and powered by Google Gemini 2.0 Flash, this AI-driven tool provides phishing detection, password strength analysis, and AI-generated cybersecurity tips.

🚀 Features

🔗 Phishing URL Detection: Analyze URLs for potential phishing threats.

🔑 Password Strength Checker: Evaluate password security and get suggestions to improve it.

🛠 AI-Powered Security Advice: Get expert cybersecurity tips using Google's Gemini AI model.

🏗️ Tech Stack

Frontend: Streamlit

Backend: Google Gemini AI (Generative Model)

Language: Python

APIs: Google AI API

📦 Installation

1️⃣ Clone the Repository

git clone https://github.com/yourusername/aicybersecurity-advisor.git
cd aicybersecurity-advisor

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Set Up API Key

Get your Google AI API key from Google MakerSuite and add it to your environment variables:

export GEMINI_API_KEY='your_api_key_here'

Or update the script:

genai.configure(api_key="your_api_key_here")

4️⃣ Run the Application

streamlit run app.py

🎯 How It Works

Phishing Detection: Enter a URL, and the AI will analyze it for phishing threats.

Password Strength: Input a password, and the system will provide a security rating.

Cybersecurity Tips: Ask any security-related question, and Gemini AI will generate advice.

🛠 Future Improvements

🔍 Real-time Threat Intelligence Integration

🛡️ Two-Factor Authentication Guide

📊 Cybersecurity Dashboard with Analytics

🤝 Contribution

Feel free to fork this repository, raise issues, or submit PRs to improve the AI Cybersecurity Advisor!

