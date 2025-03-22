import numpy as np
import pandas as pd
import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer

# Load the pre-trained model
model = pickle.load(open("model.pkl", 'rb'))

# Load the CountVectorizer used for training
with open("bow.pkl", 'rb') as f:
    bow = pickle.load(f)

# st.image(r"E:\innomatics\logo.png",width=200)

# Input review text
rev = st.text_input("enter the review here:")


# Transform the input review text to feature array
data = bow.transform([rev]).toarray()

# Predict if the email is spam or ham
reviews = model.predict(data)[0]


    # Display the prediction when the button is pressed
if st.button('Submit'):
    st.write(reviews)
    
    
    # st.write("The email is:", "Spam" if spam_ham == 'spam' else "Ham")
    # if spam_ham == 'spam':
    #     st.image(r"E:\innomatics\ml\NLP\email_spam_ham\OIP.jpeg",width=200)
    # else :
    #     st.image(r"E:\innomatics\ml\NLP\email_spam_ham\ham.jpeg",width=200)