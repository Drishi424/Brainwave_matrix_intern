# Brainwave_matrix_intern
# 📰 Fake News Detection Using Machine Learning

## 📌 Overview
This project aims to build a machine learning model that can detect fake news articles based on their content. It leverages natural language processing (NLP) techniques and classification algorithms to distinguish between real and fake news.

## 📂 Dataset
- **Source**: [Fake and Real News Dataset on Kaggle](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)
- **Features**: News text and labels (real or fake)

## 🧹 Data Preprocessing
- Text cleaning (punctuation, stopwords, special characters)
- Tokenization
- Lemmatization
- Vectorization using TF-IDF

## 🧠 Model Training
Implemented and compared the following models:
- Logistic Regression
- Multinomial Naive Bayes
- Support Vector Machine (SVM)
- Random Forest
- XGBoost

## 📊 Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

## ✅ Results
- Best model: **Multinomial Naive Bayes**
- Accuracy: ~92%
- F1 Score: ~91%

## 🚀 Deployment (Optional)
Can be deployed using Flask for real-time predictions via a web interface.

## ⚠️ Challenges
- Ambiguity in language
- Bias in training data
- Evolving nature of fake news

## 📌 Conclusion
Machine learning provides a scalable solution to combat misinformation. With continuous updates and hybrid approaches, fake news detection can become more reliable and impactful.

## 📁 How to Run
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run the notebook or script: `python fake_news_detector.py`

---

Feel free to fork, star, or contribute!
