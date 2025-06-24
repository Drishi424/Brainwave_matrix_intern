from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    news = request.form["news"]
    data = [news]
    vect = vectorizer.transform(data)
    prediction = model.predict(vect)

    result = "Real News 🟢" if prediction[0] == 1 else "Fake News 🔴"
    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
