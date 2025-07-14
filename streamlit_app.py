
import streamlit as st
import openai
import json
import random
import os
from datetime import datetime
import azure.cognitiveservices.speech as speechsdk
from openai import AzureOpenAI

# Load Azure config
with open("config.json") as f:
    config = json.load(f)

# Azure OpenAI setup
openai.api_type = "azure"
openai.api_key = config["openai_key"]
openai.api_base = config["openai_endpoint"]
openai.api_version = "2023-05-15"

# Azure Speech setup
speech_config = speechsdk.SpeechConfig(subscription=config["speech_key"], region=config["speech_region"])
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

# Question bank
question_bank = {
    "technical": [
        "What is polymorphism in OOP?",
        "Explain the difference between TCP and UDP.",
        "What are the four pillars of Object-Oriented Programming?",
        "How does a hash table work?",
        "What are RESTful APIs?"
    ],
    "aptitude": [
        "What is the next number in the series: 2, 6, 12, 20, 30?",
        "Solve: (3x + 5) / 2 = 11",
        "If a car covers 150 km in 2.5 hours, what is its average speed?",
        "What is the HCF of 24 and 36?",
        "Find the simple interest on ₹1000 at 5% for 2 years."
    ],
    "non_technical": [
        "What are your strengths and weaknesses?",
        "Where do you see yourself in 5 years?",
        "Why should we hire you?",
        "Describe a time you faced a challenge and how you handled it.",
        "How do you handle stress and pressure?"
    ]
}

# Get feedback from OpenAI
def get_feedback(transcript):
    prompt = f"""
You are an interview coach. Analyze the following interview answer:

"{transcript}"

Give a score out of 10 and provide 2–3 tips for improvement.
"""
    client = AzureOpenAI(
        api_key=config["openai_key"],
        api_version="2023-05-15",
        azure_endpoint=config["openai_endpoint"]
    )

    response = client.chat.completions.create(
        model=config["deployment_id"],
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300
    )
    return response.choices[0].message.content


# Record speech using Azure
def record_speech():
    result = speech_recognizer.recognize_once()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text
    else:
        return None

# Streamlit UI
st.set_page_config(page_title="Interview Coach", layout="centered")
st.title("💼 AI Interview Readiness Coach")

if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.category = None
    st.session_state.questions = []
    st.session_state.index = 0
    st.session_state.feedback = ""
    st.session_state.transcript = ""

if not st.session_state.started:
    st.write("Select a category to begin your mock interview:")
    cat = st.selectbox("Choose Category", ["Technical", "Aptitude", "Non-Technical"])
    if st.button("Start Interview"):
        st.session_state.started = True
        st.session_state.category = cat.lower().replace("-", "_")
        st.session_state.questions = ["Tell me about yourself"] + random.sample(question_bank[st.session_state.category], 3)
        st.session_state.index = 0

if st.session_state.started:
    question = st.session_state.questions[st.session_state.index]
    st.subheader(f"Question {st.session_state.index + 1}: {question}")

    mic_input = st.button("🎙️ Use Microphone to Answer")
    typed_answer = st.text_area("Or type your answer below:")

    if mic_input:
        st.info("Listening... Please speak clearly.")
        text = record_speech()
        if text:
            st.session_state.transcript = text
            st.success(f"Transcribed: {text}")
        else:
            st.warning("Could not recognize speech. Try typing your answer.")
    elif typed_answer:
        st.session_state.transcript = typed_answer

    if st.session_state.transcript:
        if st.button("Get Feedback"):
            feedback = get_feedback(st.session_state.transcript)
            st.session_state.feedback = feedback
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            os.makedirs("transcripts", exist_ok=True)
            with open(f"transcripts/feedback_{timestamp}.txt", "w") as f:
                f.write(f"Question: {question}\n\nTranscript: {st.session_state.transcript}\n\nFeedback:\n{feedback}")
            st.subheader("📊 AI Feedback")
            st.write(feedback)

    if st.session_state.feedback:
        col1, col2, col3 = st.columns(3)
        if col1.button("Continue"):
            st.session_state.index += 1
            st.session_state.transcript = ""
            st.session_state.feedback = ""
            if st.session_state.index >= len(st.session_state.questions):
                st.success("✅ Interview complete. Great job!")
                st.session_state.started = False
        if col2.button("Switch Category"):
            st.session_state.started = False
        if col3.button("Quit"):
            st.session_state.started = False
            st.success("👋 Session ended. Good luck with your interviews!")
