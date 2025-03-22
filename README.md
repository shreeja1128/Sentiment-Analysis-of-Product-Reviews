# 🧠 Sentiment Classifier for Customer Reviews

A web-based machine learning app to classify the **sentiment of product reviews** as **Positive**, **Negative**, or **Neutral** using Natural Language Processing (NLP) techniques and a Naive Bayes classifier.

---

## 🚀 Project Features

- Built using `Scikit-learn`, `NLTK`, and `Streamlit`
- Text pre-processing using tokenization and stopword removal
- Trained on 10,000 customer product reviews
- Uses Bag-of-Words vectorization (`CountVectorizer`)
- Provides real-time sentiment prediction in browser

---

## 🧰 Tech Stack

- Python 3.x  
- Pandas, Numpy  
- NLTK  
- Scikit-learn  
- Streamlit  
- Pickle (for model serialization)

---

## 📁 Project Structure


---

## 🧪 How It Works

1. **Data Preparation**:  
   - 10,000 review samples were selected from a larger dataset.
   - Labels: `positive`, `negative`, `neutral`.

2. **Text Preprocessing**:
   - Tokenization
   - Stopword removal
   - Lowercasing
   - Vectorization using `CountVectorizer`

3. **Model Training**:
   - Algorithm: `Multinomial Naive Bayes`
   - Accuracy: **~73.5%**

4. **Model Deployment**:
   - Exported model and vectorizer using `pickle`
   - Frontend developed with `Streamlit` for user input & prediction

---

## 🌐 How to Run the App

1. **Install Dependencies**:
```bash
pip install -r requirements.txt

## Run Streamlit App:
streamlit run sentiment_app.py


Example
🔤 Input:
"The camera quality is terrible and the battery drains quickly."

✅ Output:
negative


Future Improvements
Add deep learning model (LSTM, BERT)
Improve model accuracy with more labeled data
Add emoji sentiment mapping
Visualization of word clouds per sentiment


👩‍💻 Author
Shreeja Konda
📧 kondashreeja21@gmail.com
🔗 LinkedIn | GitHub
