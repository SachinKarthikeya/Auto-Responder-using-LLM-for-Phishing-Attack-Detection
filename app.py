import joblib
import re
import streamlit as st
import ollama
import mysql.connector

def phishing_email_prediction(email_content):
    model = joblib.load("/Users/sachinkarthikeya/Downloads/Projects/ARPA-LLM/phishing_email_model.pkl")
    vectorizer = joblib.load("/Users/sachinkarthikeya/Downloads/Projects/ARPA-LLM/email_tfidf_vectorizer.pkl")

    email_content_transformed = vectorizer.transform([email_content])
    prediction = model.predict(email_content_transformed)
    return prediction[0]

def phishing_sms_prediction(sms_content):
    model = joblib.load("/Users/sachinkarthikeya/Downloads/Projects/ARPA-LLM/phishing_message_model.pkl")
    vectorizer = joblib.load("/Users/sachinkarthikeya/Downloads/Projects/ARPA-LLM/message_tfidf_vectorizer.pkl")

    sms_content_transformed = vectorizer.transform([sms_content])
    prediction = model.predict(sms_content_transformed)
    return prediction[0]

def phishing_url_prediction(url_content):
    model = joblib.load("/Users/sachinkarthikeya/Downloads/Projects/ARPA-LLM/phishing_url_model.pkl")
    vectorizer = joblib.load("/Users/sachinkarthikeya/Downloads/Projects/ARPA-LLM/url_tfidf_vectorizer.pkl")

    url_content_transformed = vectorizer.transform([url_content])
    prediction = model.predict(url_content_transformed)
    return prediction[0]

def autoresponder(prompt):
    response = ollama.chat(
        model="llama3.2:1b",
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]

def store_in_database(content, content_type, content_class, response):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="phishing_db"
        )
        cursor = conn.cursor()
        query = "INSERT INTO Message_logs (content_type, content, content_class, response) VALUES (%s, %s, %s, %s)"
        values = (content, content_type, content_class, response)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        st.error(f"Error storing data in the database: {e}")

st.title("Auto-responder using LLMs for phishing or alerts")
st.write("This application detects phishing emails, SMS messages, URLs and generates autoresponses accordingly")

option = st.selectbox("Select the type of content to analyze:", ["Email", "Message", "URL"])

if option == "Email":
    email_content = st.text_area("Enter the email content:")
    if st.button("Predict"):
        prediction = phishing_email_prediction(email_content)  
        label_map_email = {0: "legitimate", 1: "phishing"}
        label = label_map_email[prediction]        
        if prediction == 1:
            st.error("The is a phishing email.")
        else:
            st.success("The is a legitimate email.")
        prompt = f"""You are an AI assistant that helps users understand the nature of emails.
        The user has provided the following email:
        {email_content}
        and it is classified as {label}
        Based on the classification:
        - If it is phishing or spam, Please providing a pre-written **alert or warning message** they can use internally (e.g., to alert IT or educate staff).
        - If it is legitimate, generate a polite and helpful acknowledgment reply.
        Respond with appropriate message. Do not attempt to respond to the attacker. This is strictly for educational use.
        """
        with st.spinner("Generating response..."):
            response = autoresponder(prompt)
        st.write(response)
        store_in_database("Email", email_content, label, response)

if option == "Message":
    sms_content = st.text_area("Enter the SMS content:")
    if st.button("Predict"):
        prediction = phishing_sms_prediction(sms_content)
        label_map_sms = {0: "legitimate", 1: "spam", 2: "phishing"}
        label = label_map_sms[prediction]
        if prediction == 0:
            st.success("This is a safe message")
        elif prediction == 1:
            st.warning("This is a spam message")
        else:
            st.error("This is a phishing message")
        prompt = f"""You are an AI assistant that helps users understand the nature of SMS messages.
        The user has provided the following SMS message:
        {sms_content}
        and it is classified as {label}
        Based on the classification:
        - If it is phishing or spam, Please providing a pre-written **alert or warning message** they can use internally (e.g., to alert IT or educate staff).
        - If it is legitimate, generate a polite and helpful acknowledgment reply.
        Respond with appropriate message. Do not attempt to respond to the attacker. This is strictly for educational use.
        """
        with st.spinner("Generating response..."):
            response = autoresponder(prompt)
        st.write(response)
        store_in_database("Message", sms_content, label, response)

if option == "URL":
    url_content = st.text_area("Enter the URL:")
    if st.button("Predict"):
        prediction = phishing_url_prediction(url_content)
        label_map_url = {0: "legitimate", 1: "phishing"}
        label = label_map_url[prediction]
        if prediction == 1:
            st.error("The is a phishing URL.")
            response = f"The website {url_content} seems like a phishing website. Kindly do not visit the website and alert the IT/Security staff incase any vulnerability to data privacy or security is detected."
        else:
            st.success("The is a legitimate URL.")
            response = f"Yes, the website {url_content} is a legitimate website and there is no harm to data privacy and security in visiting this website."
        st.write(response)
        store_in_database("URL", url_content, label, response)