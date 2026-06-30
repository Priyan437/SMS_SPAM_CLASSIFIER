import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string
import sklearn
ps = PorterStemmer()



def trans_text(text):
  text = text.lower()
  text = nltk.word_tokenize(text)

  y = []
  for i in text:
    if i.isalnum():
      y.append(i)

  text = y[:]
  y.clear()

  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)

  text = y[:]
  y.clear()

  for i in text:
    y.append(ps.stem(i))

  return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("SMS SPAM ClASSIFIER")
input_sms = st.text_area("Enter the Message")

if st.button('Predict'):
   # 1. Preprocess of the Input Text.
   transformed_msg = trans_text(input_sms)
   # 2. Vectorization of the Processed text
   vectorized_text = tfidf.transform([transformed_msg])
   # 3. Prediction
   prediction = model.predict(vectorized_text)[0]
   # 4. Displaying of the result.

   if prediction == 1:
     st.header("Spam")
   else:
     st.header("Not Spam")

