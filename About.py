import streamlit as st


def app():
    '''st.set_page_config(
        page_title="Fake Detection System - About",
        page_icon="🤖"
    )'''
    st.markdown(
        """
        <style>
        img{
            border-radius:10px;
            width:150px !important
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
    st.title("About the Fake Detection System")
    st.write("Welcome to the Fake Detection System!")
    st.write("This web application is designed to classify various types of fakes:")
    st.markdown("- Image Fake Detection: Upload an image to determine if it's fake or not. :camera:")
    st.markdown("- Account Fake Detection: Enter an Details of the account to  check if it's fake or not.")
    st.markdown("- Audio Fake Detection: Upload an audio file to predict if it's fake or not. :sound:")

    st.subheader("Instructions :scroll:")
    st.write("1. Select the task from the sidebar.")
    st.write("2. Follow the instructions for each task to upload images or input data.")
    st.write("3. Click on the 'Predict' or 'Check' button to get the results.")

    st.subheader("About the Models:")
    st.markdown("- **Image Fake Detection**: The image model has been trained on a dataset of fake and real images.")
    st.markdown("- **Account Fake Detection**: The account model checks various features of an account to determine its authenticity.")
    st.markdown("- **Audio Fake Detection**: The audio model analyzes audio features to detect fake or manipulated audio.")

    st.subheader("Disclaimer")
    st.write("This application provides predictions based on machine learning models.")
    st.write("Results may not always be accurate and should not be used for critical decisions.")

if __name__ == "__main__":
    app()
