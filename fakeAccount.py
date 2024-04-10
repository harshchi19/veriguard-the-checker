import streamlit as st
import pandas as pd
import pickle
from sklearn.impute import SimpleImputer
import os
import joblib
import sklearn

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

    # Load the trained model for Twitter Fake News Detection
    model_path = "LogisticTwiiterss.pkl"
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    # Get feature names used during training
    feature_names = [
        'UserID',
        'No Of Abuse Report',
        'No Of Rejected Friend Requests',
        'No Of Freind Requests Thar Are Not Accepted',
        'No Of Friends',
        'No Of Followers',
        'No Of Likes To Unknown Account',
        'No Of Comments Per Day'
    ]

    st.header('Twitter Fake Account')
    st.write("Enter the following information from a Twitter user's profile to predict if it's fake or not:")

    # User inputs for Twitter Fake News Detection
    user_data = {
        'UserID': st.text_input("User ID"),
        'No Of Abuse Report': st.number_input("No Of Abuse Report", min_value=0, step=1),
        'No Of Rejected Friend Requests': st.number_input("No Of Rejected Friend Requests", min_value=0, step=1),
        'No Of Freind Requests Thar Are Not Accepted': st.number_input("No Of Freind Requests Thar Are Not Accepted", min_value=0, step=1),
        'No Of Friends': st.number_input("No Of Friends", min_value=0, step=1),
        'No Of Followers': st.number_input("No Of Followers", min_value=0, step=1),
        'No Of Likes To Unknown Account': st.number_input("No Of Likes To Unknown Account", min_value=0, step=1),
        'No Of Comments Per Day': st.number_input("No Of Comments Per Day", min_value=0, step=1)
    }

    # Convert user input to DataFrame
    user_df = pd.DataFrame(user_data, index=[0])

    # Ensure all required columns are present
    for feature in feature_names:
        if feature not in user_df.columns:
            user_df[feature] = 0

    # Ensure only relevant features are used for prediction
    user_df = user_df[feature_names]

    if st.button("Predict"):
        # Make prediction
        prediction = model.predict(user_df)[0]

        # Get the predicted class label
        if prediction == 0:
            st.success("Prediction: Not Fake")
        else:
            st.success("Prediction: Fake")

# Assuming this is the main entry point of your Streamlit app
if __name__ == '__main__':
    app()
