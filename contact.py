import streamlit as st

def app():
    st.title("Contact Us")
    
    
    st.write("Developers behind this project:")
    
    row1_col1, row1_col2 = st.columns(2)
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
    with row1_col1:
        st.markdown("""
            <div style="border: 2px solid #4f8bf9; padding: 20px; height: 220px; width: 300px; display: flex; flex-direction: column; justify-content: center; align-items: center; background-color: rgba(235, 245, 255, 0.5);">
                <div style="text-align: center;">
                    <h3 style="margin: 0;">Arya Vaidya</h3>
                    <p style="font-size: 18px;">👨‍💻 Software Engineer</p>
                </div>
                <div style="margin-top: 20px;">
                    <p style="font-size: 16px;">Email: aryavaidya59@gmail.com</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("""
            <div style="border: 2px solid #4f8bf9; padding: 20px; height: 220px; width: 300px; display: flex; flex-direction: column; justify-content: center; align-items: center; background-color: rgba(235, 245, 255, 0.5);">
                <div style="text-align: center;">
                    <h3 style="margin: 0;">Harsh Chitaliya</h3>
                    <p style="font-size: 18px;">👩‍💻 Data Scientist</p>
                </div>
                <div style="margin-top: 20px;">
                    <p style="font-size: 16px;">Email: harshchitaliya010@gmail.com</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with row1_col2:
        st.markdown("""
            <div style="border: 2px solid #4f8bf9; padding: 20px; height: 220px; width: 300px; display: flex; flex-direction: column; justify-content: center; align-items: center; background-color: rgba(235, 245, 255, 0.5);">
                <div style="text-align: center;">
                    <h3 style="margin: 0;">Gaurav Khati</h3>
                    <p style="font-size: 18px;">👨‍💻 Machine Learning Engineer</p>
                </div>
                <div style="margin-top: 20px;">
                    <p style="font-size: 16px;">Email: khatigaurav8@gmail.com</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("""
            <div style="border: 2px solid #4f8bf9; padding: 20px; height: 220px; width: 300px; display: flex; flex-direction: column; justify-content: center; align-items: center; background-color: rgba(235, 245, 255, 0.5);">
                <div style="text-align: center;">
                    <h3 style="margin: 0;">Morvi Panchal</h3>
                    <p style="font-size: 18px;">👩‍💻 Frontend Developer</p>
                </div>
                <div style="margin-top: 20px;">
                    <p style="font-size: 16px;">Email: morvieee5@gmail.com</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
  app()
