import json
import openai
import os
import random
import azure.cognitiveservices.speech as speechsdk
from datetime import datetime

# Load API config
with open('config.json') as f:
    config = json.load(f)
# Azure speech setup
speech_config = speechsdk.SpeechConfig(subscription=config['speech_key'], region=config['speech_region'])
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

# Azure OpenAI setup
openai.api_key = config["openai_key"]
openai.api_base = config["openai_endpoint"]
openai.api_type = "azure"
openai.api_version = "2023-05-15"

# Questions
question_bank = {
    "technical": [
        "What is polymorphism in OOP?",
        "Explain the difference between TCP and UDP.",
        "What are the four pillars of Object-Oriented Programming?",
        "What is normalization in databases?",
        "How does a hash table work?",
        "What is the difference between a process and a thread?",
        "Explain the concept of recursion with an example.",
        "What is the purpose of an index in SQL?",
        "Describe how a binary search algorithm works.",
        "What are RESTful APIs?"
    ],
    "aptitude": [
        "What is the next number in the series: 2, 6, 12, 20, 30?",
        "If a train travels 60 km in 45 minutes, what is its speed in km/h?",
        "Solve: (3x + 5) / 2 = 11",
        "What is the probability of getting a head when tossing a fair coin?",
        "What is the area of a triangle with base 10 cm and height 6 cm?"
    ],
    "non_technical": [
        "What are your strengths and weaknesses?",
        "Where do you see yourself in 5 years?",
        "Why should we hire you?",
        "Describe a time you faced a challenge and how you handled it.",
        "How do you handle stress and pressure?"
    ]
}

def ask_question(question):
    print(f"\n🎤 Interview Question: {question}")
    input("📣 Press Enter to start recording your answer...")

    print("🎙️ Listening... Speak now.")
    result = speech_recognizer.recognize_once()

    if result.reason != speechsdk.ResultReason.RecognizedSpeech:
        print("❌ No speech recognized. Skipping question.")
        return

    transcript = result.text
    print(f"\n📝 Transcription:\n{transcript}")

    prompt = f"""
You are an interview coach. Analyze the following interview answer:

"{transcript}"

Give a score out of 10 and provide 2–3 tips for improvement.
"""

    response = openai.ChatCompletion.create(
        engine=config["deployment_id"],
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300
    )

    feedback = response['choices'][0]['message']['content']
    print("\n📊 AI Feedback:\n" + feedback)

    os.makedirs("transcripts", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"transcripts/feedback_{timestamp}.txt", "w") as f:
        f.write(f"Question: {question}\n\nTranscript: {transcript}\n\nFeedback:\n{feedback}")

def menu():
    print("\nSelect a category:")
    print("1. Technical")
    print("2. Aptitude")
    print("3. Non-Technical")
    choice = input("Enter choice (1/2/3): ")
    if choice == "1":
        return "technical"
    elif choice == "2":
        return "aptitude"
    elif choice == "3":
        return "non_technical"
    else:
        print("Invalid choice, defaulting to Technical.")
        return "technical"

if __name__ == "__main__":
    print("💼 Welcome to AI Interview Readiness Coach!")

    # Always start with this question
    ask_question("Tell me about yourself")

    while True:
        category = menu()
        questions = question_bank[category]
        random.shuffle(questions)

        for question in questions:
            ask_question(question)
            print("\nDo you want to:")
            print("1. Continue in same category")
            print("2. Switch category")
            print("3. Quit")
            next_step = input("Enter choice (1/2/3): ")
            if next_step == "1":
                continue
            elif next_step == "2":
                break
            elif next_step == "3":
                print("✅ Exiting. Good luck with your interviews!")
                exit()
        print("✅ Finished all questions in this category.")
        print("🔄 Returning to main menu..")