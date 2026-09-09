import streamlit as st
import joblib

st.set_page_config(page_title="Phishing Detector", page_icon="🛡️")
st.title("🛡️ Phishing Text Detector")
st.write("Paste any text below to check if it's phishing.")

vectorizer = joblib.load("vectorizer.joblib")
model = joblib.load("phishing_model.joblib")

text = st.text_area("Text to analyze:", height=150, placeholder="Paste the message here...")

if st.button("Analyze"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        vec = vectorizer.transform([text])
        proba = model.predict_proba(vec)[0]
        is_phishing = proba[1] > 0.5
        confidence = max(proba) * 100

        if is_phishing:
            st.error(f"🚨 **PHISHING DETECTED** — Confidence: {confidence:.1f}%")
        else:
            st.success(f"✅ **Legitimate** — Confidence: {confidence:.1f}%")

