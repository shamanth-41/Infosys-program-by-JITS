# Infosys-program-by-JITS
💼 AI-powered Interview Readiness Coach simulates mock interviews, analyzes responses using the STAR method and sentiment analysis, and provides instant feedback. Ideal for job seekers to practice and improve interview skills. Built in Python, ready to run on Google Colab.

project demo link : https://drive.google.com/file/d/1C-NjM4t2sopg6XzbeEATcZGVLpFSNzvx/view?usp=sharing


🎙️ AI Interview Readiness Coach
An interactive AI-powered mock interview platform built with Streamlit and Azure AI Services, designed to simulate real interview scenarios and provide real-time speech-to-text transcription and automated feedback.
![WhatsApp Image 2025-07-14 at 14 20 57_5248e26b](https://github.com/user-attachments/assets/869d0bad-026d-4174-814d-d91197d10476)
![WhatsApp Image 2025-07-14 at 14 20 58_2ebadc2c](https://github.com/user-attachments/assets/349d7713-f3e3-4b70-afee-2a25c19a0c8b)
![WhatsApp Image 2025-07-14 at 14 20 58_384d21b1](https://github.com/user-attachments/assets/c43b8914-4433-4819-a418-07805f4c42b4)
![WhatsApp Image 2025-07-14 at 14 20 56_d4c5b469](https://github.com/user-attachments/assets/73ed9e57-6fb3-448f-a4a9-c41d7979f1f9)

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
