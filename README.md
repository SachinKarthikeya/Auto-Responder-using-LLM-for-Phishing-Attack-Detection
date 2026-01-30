# 🛡️ Auto-Responder using LLM for Phishing Attack Detection

An intelligent auto-responding system that detects and classifies digital communication content—such as Emails, SMS messages, and URLs—into **Legitimate**, **Spam**, or **Phishing** using Machine Learning. The system automatically generates appropriate responses based on the detected category, helping users identify potential security threats and minimizing human effort.

## 🚀 Features

- **Machine Learning Models**: Classify user-provided content 
- **LLM (Llama 3.2:1b)**: Generate automated security-aware responses
- **XAMPP (MySQL)**: Saves the classified content with the response 
- Supports input formats like **Email**, **SMS Text**, and **URLs**
- **Streamlit** for interactive web application

## 📄 Workflow
- User chooses the content type (Email, SMS, URL) via Streamlit and uploads the content
- Trained ML models classify the content category between **Legitimate**, **Spam** or **Phishing**
- Analyzing the content and classified category, the LLM generates an automated response relevant to the content
- Saves the original content, predicted content category and generated response in a MySQL database

## 🧰 Tech Stack

- **Frontend:** Streamlit
- **ML Models:** Random Forest Classifier, Support Vector Machine, Logistic Regression
- **Database:** XAMPP (MySQL)
- **LLM:** Llama3.2:1b 

## 📢 Future Improvements

- Add support for voice messages
- Automated classification of content type 
- Integrate with email clients for real-time scanning
- Improve response personalization with user context
