import streamlit as st
import pandas as pd
import pickle
from sklearn.impute import SimpleImputer
import os
import joblib
import sklearn


def predict_label(text):
    # Load the saved model and vectorizer for text classification
    text_model = joblib.load('logistic_regression_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')

    # Vectorize the text
    text_vectorized = vectorizer.transform([text])

    # Make prediction and return results
    prediction = text_model.predict(text_vectorized)[0]
    probabilities = text_model.predict_proba(text_vectorized)[0]
    return prediction, probabilities
def app():
    st.markdown(
        """
        <style>
        img{
            border-radius:10px;
            width:150px 
        }
        [data-testid="stHeader"]{
          background-color:#201658;
          color:white;
        }
        [data-testid="stAppViewContainer"]{
          background-color:#d2daf7;
          font-family:'Times New Roman';
        }
        [data-testid="stSidebar"]{
          background-color:#adb0f7;
        }
        [data-testid="StyledLinkIconContainer"]{
            font-family:'Times New Roman';
        }
        [data-testid="stMarkdownContainer"]{
            font-family:'Times New Roman';
        }
        [class="st-emotion-cache-1629p8f e1nzilvr2"]{
            font-family:'Times New Roman';
        }
        [data-testid="baseButton-secondary"]{
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border:1px solid #150038;
        }
        [data-testid="stFileUploaderDropzone"]{
            background-color:#FFEEBB;
            border:2px solid #150038;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.header('Text Classification')
    # Get user input
    text = st.text_area('Enter text to classify', '', height=200)

    # Make prediction and display results
    if st.button('Classify') and text:
        prediction, probabilities = predict_label(text)

        # Display prediction
        st.subheader('Prediction:')
        if prediction == 1:
            st.write('Relevant')
        else:
            st.write('Not Relevant')

        # Display probabilities
        st.subheader('Probabilities:')
        relevant_prob = probabilities[1]
        not_relevant_prob = probabilities[0]
        st.write(f'Relevant: {relevant_prob:.2f}')
        st.write(f'Not Relevant: {not_relevant_prob:.2f}')

# Assuming this is the main entry point of your Streamlit app
if __name__ == '__main__':
    app()
