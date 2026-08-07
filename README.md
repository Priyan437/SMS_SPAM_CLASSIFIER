# 📩 SMS Spam Classifier

A Machine Learning web application that classifies SMS messages as **Spam** or **Ham (Not Spam)** using **Natural Language Processing (NLP)**. The application is built using **Python**, **Scikit-learn**, and **Streamlit**, allowing users to instantly detect whether an SMS message is spam.

---

## 🚀 Features

- 📌 Classifies SMS messages into **Spam** or **Ham**
- 📝 Text preprocessing using NLP techniques
- 🔍 TF-IDF Vectorization for feature extraction
- 🤖 Machine Learning model trained on labeled SMS data
- 🌐 Interactive web application built with Streamlit
- ⚡ Fast and lightweight prediction system

---

## 🛠️ Tech Stack

### Language
- Python

### Libraries & Frameworks
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- NLTK
- Pickle

### NLP Techniques
- Lowercase Conversion
- Tokenization
- Stopword Removal
- Stemming
- TF-IDF Vectorization

---

## 📂 Project Structure

```text
SMS_SPAM_CLASSIFIER/
│
├── app.py                 # Streamlit Application
├── model.pkl              # Trained Machine Learning Model
├── vectorizer.pkl         # TF-IDF Vectorizer
├── requirements.txt       # Project Dependencies
├── README.md
│
├── notebooks/
│   └── model_training.ipynb
│
├── dataset/
│   └── spam.csv
│
└── assets/
    └── screenshot.png
```

---

## 📊 Machine Learning Pipeline

```text
SMS Message
     │
     ▼
Text Preprocessing
     │
     ▼
Tokenization
     │
     ▼
Stopword Removal
     │
     ▼
Stemming
     │
     ▼
TF-IDF Vectorization
     │
     ▼
Trained Machine Learning Model
     │
     ▼
Spam / Ham Prediction
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Priyan437/SMS_SPAM_CLASSIFIER.git
```

### 2. Navigate to the Project Directory

```bash
cd SMS_SPAM_CLASSIFIER
```

### 3. Create a Virtual Environment (Recommended)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will automatically open in your default web browser.

---

## 💬 Example Predictions

### Example 1

**Input**

```text
Congratulations!

You have won a FREE vacation.

Click here to claim your prize.
```

**Prediction**

```text
Spam 🚨
```

---

### Example 2

**Input**

```text
Hey, are we meeting tomorrow at 5 PM?
```

**Prediction**

```text
Ham ✅
```

---

## 🧠 Machine Learning Workflow

The project follows a complete end-to-end Machine Learning pipeline:

- Data Collection
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Text Preprocessing
- Feature Extraction using TF-IDF
- Model Training
- Model Evaluation
- Model Serialization using Pickle
- Deployment with Streamlit

---

## 📈 Future Improvements

- 🔹 Deep Learning Models (LSTM/GRU)
- 🔹 BERT-based Spam Detection
- 🔹 Multilingual SMS Classification
- 🔹 Confidence Score for Predictions
- 🔹 Explainable AI (SHAP/LIME)
- 🔹 REST API using FastAPI
- 🔹 Docker Containerization
- 🔹 CI/CD with GitHub Actions

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📜 License

This project is created for **educational and learning purposes**.

---

## 👨‍💻 Author

**Priyanshu Kumar Thakur**

- GitHub: https://github.com/Priyan437

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
