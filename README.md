# 📰 Fake News Detection Using Machine Learning

A machine learning web application that detects whether a news article is **real** or **fake** using Natural Language Processing (NLP) and a Logistic Regression model. Built as part of an internship project with a Flask-based interface for real-time testing.

---

## 🚀 Features

- Logistic Regression trained on real-world dataset
- TF-IDF vectorization of news content
- Flask web app for input and output
- Detects fake news based on title + content
- Simple and clean UI (HTML/CSS)

---

## 📁 Project Structure

```
fakeNews/
├── main.py              # Trains and saves the model & vectorizer
├── app.py               # Flask web application
├── model.pkl            # Trained Logistic Regression model
├── vectorizer.pkl       # Trained TF-IDF vectorizer
├── Fake.csv             # Fake news dataset (from Kaggle)
├── True.csv             # Real news dataset (from Kaggle)
└── templates/
    └── index.html       # Frontend web page
```

---

## 📊 Dataset

This project uses the **Fake and Real News Dataset** from Kaggle:  
🔗 https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset

- `Fake.csv`: ~23,000 fake articles  
- `True.csv`: ~21,000 real articles

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fake-news-detector.git
   cd fake-news-detector
   ```

2. Install dependencies:
   ```bash
   pip install pandas scikit-learn flask nltk
   ```

3. Download and place `Fake.csv` and `True.csv` into the project directory.

---

## 🧠 Model Training

To train and save the ML model and vectorizer:
```bash
python main.py
```

This will generate:
- `model.pkl`
- `vectorizer.pkl`

---

## 🌐 Run the Web App

To launch the Flask web app:
```bash
python app.py
```

Then go to `http://127.0.0.1:5000/` in your browser.

---

## 🛠 Future Enhancements

- Switch to LSTM or BERT for improved accuracy
- Add prediction confidence scores
- Allow URL/article scraping for input
- Host on Streamlit or Hugging Face Spaces

---

## 🙋‍♂️ Author

**Drishi Kachchhawaha**  
Built as an internship project for detecting misinformation in media using AI.

---

## 📜 License

This project is licensed under the MIT License.
