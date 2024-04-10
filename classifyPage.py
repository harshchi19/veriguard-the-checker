import streamlit as st
import util

def app():
    st.title('Classify Image')
    # Custom CSS styles
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
    st.subheader("Welcome to our Image Classification Page!")
    welcome='''We understand the importance of ensuring the authenticity of images in an era where visual content dominates digital communication. Our Image Verification feature utilizes advanced image forensics and deep learning algorithms to detect manipulated or doctored images, providing users with confidence in the integrity of the visual content they encounter.'''
    st.markdown(welcome,unsafe_allow_html=True)
    st.write("Upload a Picture to see if it is a fake or real face.")
    st.markdown("*Need a face to test? Visit this [link](https://github.com/harshchi19/Fake-Images-Detection-/tree/main/Model%20Training/dataset)*")
    file_uploaded = st.file_uploader("Choose the Image File", type=["jpg", "png", "jpeg"])
    if file_uploaded is not None:
        res = util.classify_image(file_uploaded)
        c1, buff, c2 = st.columns([2, 0.5, 2])
        c1.image(file_uploaded, use_column_width=True)
        c2.subheader("Classification Result")
        c2.write("The image is classified as **{}**.".format(res['label'].title()))

if __name__ == "__main__":
    app()
