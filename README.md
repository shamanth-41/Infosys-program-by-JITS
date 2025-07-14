# Infosys-program-by-JITS
💼 AI-powered Interview Readiness Coach simulates mock interviews, analyzes responses using the STAR method and sentiment analysis, and provides instant feedback. Ideal for job seekers to practice and improve interview skills. Built in Python, ready to run on Google Colab.

project demo link : https://drive.google.com/file/d/1C-NjM4t2sopg6XzbeEATcZGVLpFSNzvx/view?usp=sharing

<img width="865" height="345" alt="Screenshot 2025-07-14 133955" src="https://github.com/user-attachments/assets/94bc223a-773d-4dbb-8f2f-25d1d92eed2f" />
<img width="926" height="286" alt="Screenshot 2025-07-14 134923" src="https://github.com/user-attachments/assets/e13d62f4-beff-4293-ab0a-c008853e02e4" />
<img width="1552" height="641" alt="Screenshot 2025-07-14 133135" src="https://github.com/user-attachments/assets/8b4736d8-4c03-477f-822b-01222c70df18" />
🎙️ AI Interview Readiness Coach
An interactive AI-powered mock interview platform built with Streamlit and Azure AI Services, designed to simulate real interview scenarios and provide real-time speech-to-text transcription and automated feedback.

🚀 Features
✅ Category Selection: Choose from Technical, Aptitude, or Non-Technical interview rounds

✅ Speech Input (Mic): Answer questions using your voice via Azure Speech Service

✅ Text Input Fallback: Type your answer if the mic isn't available or working

✅ AI Feedback: Get score (out of 10) and improvement tips from Azure OpenAI (GPT)

✅ Animated Avatars: Visually engaging layout with interviewer and interviewee profiles

✅ Transcripts Saved: Automatically stores your answers and feedback in .txt format

✅ Continue / Switch / Quit Options: Easily navigate through the mock session

🛠 Tech Stack
Frontend: Streamlit (Python)

Speech Recognition: Azure Speech Service

AI Feedback: Azure OpenAI (ChatGPT/GPT-4 deployment)

Transcription Storage: Local file system

Animated Interface: Avatar-based visual layout using GIFs/images

📦 Requirements
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Create a .env or config.json file with your Azure credentials:

json
Copy
Edit
{
  "speech_key": "YOUR_SPEECH_KEY",
  "speech_region": "YOUR_REGION",
  "openai_key": "YOUR_OPENAI_KEY",
  "openai_endpoint": "https://your-resource.openai.azure.com/",
  "deployment_id": "gpt-4"
}
🧪 To Run
bash
Copy
Edit
streamlit run streamlit_app_v2.py
📁 Output Example
transcripts/feedback_20250714_1340.txt

Contains:

Question

Transcribed Answer

AI Feedback (Score + Tips)

📸 Demo Preview
<img src="https://cdn-icons-png.flaticon.com/512/3177/3177440.png" width="100"/> Interviewer    
<img src="https://cdn-icons-png.flaticon.com/512/4140/4140037.png" width="100"/> Interviewee

✨ Future Enhancements
Streamlit Cloud or mobile support

Leaderboard or scoring history

PDF export or resume-builder integration
