import streamlit as st
import plotly.express as px

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
    st.title('VeriGuard: Deep Learning for Image Classification')

    st.subheader("💡 Abstract:")
    inspiration = '''
    Deep learning, especially through Generative Adversarial Networks (GANs), has seen significant advancements in creating highly realistic synthetic content, including images, audio, news articles, and even fake social media accounts. While GANs have been instrumental in generating high-quality outputs that can be indistinguishable from real inputs, they also pose serious risks.

    These technologies can be misused to create deepfake images and audio, which can deceive individuals and even machine learning classifiers. For example, deepfake videos can be used to spread misinformation, manipulate public opinion, and damage the reputation of individuals or organizations. Furthermore, advanced editing software like Adobe Photoshop can be used to alter images in sophisticated ways, making it difficult to discern real from fake.

    YouTube and other platforms host tutorials and guides on creating deepfake content, contributing to the widespread dissemination of such fraudulent material on the internet. This raises concerns about defamation, impersonation, and the distortion of facts. The ease of sharing content on social media further amplifies these risks, making it crucial to develop robust detection and prevention mechanisms to combat the spread of deepfake content.
    '''
    st.write(inspiration)
    st.title("About the Fake Detection System")
    st.write("Welcome to the Fake Detection System!")
    st.write("This web application is designed to classify various types of fakes:")
    st.markdown("- Image Fake Detection: Upload an image to determine if it's fake or not. :camera:")
    st.markdown("- Account Fake Detection: Enter an Details of the account to  check if it's fake or not.")
    st.markdown("- Audio Fake Detection: Upload an audio file to predict if it's fake or not. :sound:")
    st.markdown("- Fake News Detection:  Input a text to predict if it's fake or not.")

    st.subheader("Instructions :scroll:")
    st.write("1. Select the task from the sidebar.")
    st.write("2. Follow the instructions for each task to upload images or input data.")
    st.write("3. Click on the 'Predict' or 'Check' button to get the results.")

    st.subheader("About the Models:")
    st.markdown("- **Image Fake Detection**: The image model has been trained on a dataset of fake and real images.")
    st.markdown("- **Account Fake Detection**: The account model checks various features of an account to determine its authenticity.")
    st.markdown("- **Audio Fake Detection**: The audio model analyzes audio features to detect fake or manipulated audio.")
    st.markdown("- **Fake News Detection**: This model analyzes texts to detect fake or manipulated news.")
    st.subheader("Disclaimer")
    st.write("This application provides predictions based on machine learning models.")
    st.write("Results may not always be accurate and should not be used for critical decisions.")
    st.subheader("👨🏻‍💻 What our Project Does?")
    what_it_does1 = '''
    At the forefront of combating misinformation in the digital age, we are proud to introduce our AI-Powered Media Authenticity Verification System. In an era where the authenticity of digital content is constantly under scrutiny, our platform emerges as a beacon of trust and reliability.'''
    what_it_does2='''Our mission is clear: to empower users with the tools and knowledge needed to navigate the digital landscape with confidence and integrity. We understand the detrimental effects of misinformation on society, and we are committed to providing a solution that promotes transparency, authenticity, and digital literacy.'''
    st.markdown(what_it_does1, unsafe_allow_html=True)
    st.markdown(what_it_does2, unsafe_allow_html=True)

    st.subheader("🧠 ML Process")
    st.markdown("<h5> 📊 Getting the Data and EDA Process </h5>", unsafe_allow_html=True)
    st.markdown("*The dataset was taken from Kaggle and you can find it [here](https://www.kaggle.com/hamzaboulahia/hardfakevsrealfaces).*")
    st.markdown('''The Dataset contains 1288 faces out of which
    <li> 589 are Real </li> 
    <li> 700 are Fake </li>
    ''', unsafe_allow_html=True) 

    fig = px.bar(x=['Real', 'Fake'], y=[589, 700], height=400)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('''The Dataset contains 10 Audio files out of which
    <li> 7 are Real </li> 
    <li> 3 are Fake </li>
    ''', unsafe_allow_html=True) 
    st.image('/content/Audio Chart.png', use_column_width=True)
    st.write('The "fake" faces collected in this dataset are generated using the StyleGAN2, which present a harder challenge to classify them correctly even for the human eye.')
    
    st.image('faces_1.png', use_column_width=True)
    st.image('faces_2.png', use_column_width=True)

    st.subheader("⚙️ Model Architecture for Image")
    st.image('model.png', use_column_width=True)
    st.subheader("⚙️ Model Architecture For Audio")
    st.image('/content/Audio Architecture.png', use_column_width=True)
    st.subheader("Detailed Model Information For Both Image And Audio")
    ml_process = f'''
- We designed a Sequential Model having 5 Convolutional Layers and 4 Dense Layers.
- The first layer started with 32 filters and kernel of 2x2.
- The number of filters are doubled at every next layer and kernel is incremented by 1.
- We introduced some Max Pooling Layers after Convolutional Layers to avoid over-fitting and reduce Computational Costs.
- The Output from Covolutional Layer is Flattened and passed over to Dense Layers.
- We started with 512 neurons in the first Dense layer and reduced them to half over the next two Dense layers.
- Some Dropout Layers were also introduced throughout the model to randomly ignore some of the neurons and reduce over-fitting.
- We used ReLU activation in all layers except the output layer to reduce computation cost and introduce non-linearity.
- Finally, the Output Layer was constructed containing 2 neurons (1 for each class) and softmax activation.
- Introduce Max Pooling Layers after Convolutional Layers to reduce the spatial dimensions and extract key features.
- Depending on the audio format and length, you can use a suitable input representation such as spectrograms or raw audio waveforms.
- Use a Dense Layer with softmax activation for multi-class classification (e.g., distinguishing between real and fake audio).
'''
    st.write(ml_process)

    results = f'''
    - The model with the least Validation Loss was saved during the training and reloaded before obtaining the final results.
    - The model was able to classify all of the samples correctly.
    '''
    st.subheader("📈 Results")
    st.markdown(results, unsafe_allow_html=True)

    st.write("Classification Report:")
    
    cfr = '''
 Report Title     precision    recall  f1-score   support

        Real       1.00      1.00      1.00        59
        Fake       1.00      1.00      1.00        70

    accuracy                           1.00       129
   macro avg       1.00      1.00      1.00       129
weighted avg       1.00      1.00      1.00       129
'''
    st.code(cfr)

    st.write(" ")
    st.write("*Try it out now by clicking on Classify Image/Audio/News/Account button on the Sidebar*")

if __name__ == "__main__":
    app()
