import pandas as pd
import string
import re
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the datasets
fake = pd.read_csv("Fake.csv")
real = pd.read_csv("True.csv")

# Add labels
fake['label'] = 0  # 0 = fake
real['label'] = 1  # 1 = real

# Combine datasets
data = pd.concat([fake, real], axis=0).reset_index(drop=True)

# Preprocessing
def clean_text(text):
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = text.lower()                  # Lowercase
    text = re.sub(r'\d+', '', text)      # Remove digits
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    return text

data['text'] = data['title'] + " " + data['text']
data['text'] = data['text'].apply(clean_text)

# Split
X_train, X_test, y_train, y_test = train_test_split(data['text'], data['label'], test_size=0.25, random_state=42)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Test Accuracy
y_pred = model.predict(X_test_tfidf)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model & vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
