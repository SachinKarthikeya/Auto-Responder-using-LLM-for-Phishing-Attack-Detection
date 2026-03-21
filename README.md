# 🛡️ Auto-Responder using LLM for Phishing Attack Detection

An intelligent auto-responding system that detects and classifies digital communication content—such as Emails, SMS messages, and URLs—into **Legitimate**, **Spam**, or **Phishing** using Machine Learning. The system automatically generates appropriate responses based on the detected category, helping users identify potential security threats and minimizing human effort.

## 🚀 Features

- **Machine Learning Models**: Classify user-provided content 
- **Llama 3.2:1b / Llama 3.1:8b**: Generate automated security-aware responses
- **MongoDB**: Saves the classified content with the response 
- Supports input formats like **Email**, **SMS Text**, and **URLs**
- **Streamlit** for interactive web application

## 📄 Workflow
- User chooses the content type (Email, SMS, URL) via Streamlit and uploads the content
- Trained ML models classify the content category between **Legitimate**, **Spam** or **Phishing**
- Analyzing the content and classified category, the LLM generates an automated response relevant to the content
- Saves the original content, predicted content category and generated response in MongoDB database

## Versions

For this project, there are two versions which work separately:

**Version 1:**

- No MongoDB database integrated
- Changed the LLM from locally running Ollama model to API-based OpenAI model
- Containerized the project using Docker and hosted using Render

**Version 2:**

- MongoDB database integrated
- Original local Ollama model integrated
- Docker containerization and Render hosting not performed.

## 🧰 Tech Stack

- **Frontend:** Streamlit
- **ML Models:** Random Forest Classifier, Support Vector Machine, Logistic Regression
- **Database:** MongoDB
- **LLM:** Llama3.2:1b / Llama3.1:8b(production)
- **Deployment**: Docker & Render

## 📢 Future Improvements

- Automated pipelines of email/sms/url for real-time scanning
- Improve response personalization with user context
- 
