# 🛡️ Auto-Responder using LLM for Phishing Attack Detection

An intelligent auto-responding system that detects and classifies digital communication content—such as Emails, SMS messages, and URLs—into **Legitimate**, **Spam**, or **Phishing** using Machine Learning. The system automatically generates appropriate responses based on the detected category, helping users identify potential security threats and minimizing human effort.

## 🚀 Features

- Classifies user-provided content into **Legitimate**, **Spam**, or **Phishing**
- Uses a fine-tuned **LLM (Llama 3.2:1b)** via Ollama for context-aware response generation
- Supports input formats like **Email**, **SMS Text**, and **URLs**
- Automatically generates security-aware responses
- Enhances protection against phishing attacks
- Reduces manual workload in responding to malicious content

## 🧰 Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python, Machine Learning (Random Forest Classifier, Support Vector Machine, Logistic Regression)
- **Database:** XAMPP (MySQL)
- **LLM Runtime:** Ollama

## 🖼️ System Architecture

User Input (Email/SMS/URL)
        ↓
Preprocessing → ML Classifier (Scikit-Learn)
        ↓
Class Detected: Legitimate / Spam / Phishing
        ↓
LLM (Llama 3.2:1b via Ollama)
        ↓
Generated Response → Shown on UI

📢 Future Improvements

- Add support for voice messages
- Integrate with email clients for real-time scanning
- Improve response personalization with user context
