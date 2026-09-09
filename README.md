# 🛡️ Phishing Text Detector

A lightweight machine learning web application built with [Streamlit](https://streamlit.io/) and [scikit-learn](https://scikit-learn.org/) to detect whether a given message or email is a phishing attempt or legitimate.

## 🚀 Features

- **Text Analysis**: Paste any message or email body to evaluate phishing probability.
- **Confidence Scoring**: Displays confidence percentage for the prediction.
- **Trained Model**: Powered by a TF-IDF Vectorizer and Logistic Regression classifier (`joblib`).

## 📁 Project Structure

```text
phishing-web/
├── web.py                 # Streamlit web application
├── vectorizer.joblib      # Pre-trained TF-IDF vectorizer
├── phishing_model.joblib  # Trained classification model
├── requirements.txt       # Project dependencies
├── .gitignore             # Git ignore configuration
└── README.md              # Project documentation
```

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run web.py
   ```
   or:
   ```bash
   python -m streamlit run web.py
   ```

4. Open your browser at `http://localhost:8501`.

