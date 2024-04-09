import streamlit as st
import numpy as np
import librosa
import os
from tensorflow.keras.models import load_model

# Load the pre-trained Keras model
model = load_model('audio_classifier.h5')

# Define paths and parameters
SAMPLE_RATE = 16000  # Sample rate of your audio files
DURATION = 5  # Duration of audio clips in seconds
N_MELS = 128  # Number of Mel frequency bins

def extract_features(file_path):
    try:
        audio, _ = librosa.load(file_path, sr=SAMPLE_RATE, duration=DURATION)
        mel_spectrogram = librosa.feature.melspectrogram(y=audio, sr=SAMPLE_RATE, n_mels=N_MELS)
        mel_spectrogram = librosa.power_to_db(mel_spectrogram, ref=np.max)

        # Ensure all spectrograms have the same width (time steps)
        max_time_steps = 109  # Define the maximum time steps for your model
        if mel_spectrogram.shape[1] < max_time_steps:
            mel_spectrogram = np.pad(mel_spectrogram, ((0, 0), (0, max_time_steps - mel_spectrogram.shape[1])), mode='constant')
        else:
            mel_spectrogram = mel_spectrogram[:, :max_time_steps]

        mel_spectrogram = np.expand_dims(mel_spectrogram, axis=-1)  # Add channel dimension
        mel_spectrogram = np.expand_dims(mel_spectrogram, axis=0)   # Add batch dimension
        return mel_spectrogram
    except Exception as e:
        print("Error encountered while parsing file:", file_path)
        print(e)
        return None

def app():
    st.title('Classify Audio')

    # Add CSS styles
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
    st.subheader("Welcome to our Audio Classification Page!")
    welcome='''In today's digital landscape, audio content plays a significant role in communication, entertainment, and information sharing. However, the rise of audio manipulation and synthetic voice technologies has raised concerns about the authenticity of audio recordings. At [Your Website Name], our Audio Classification feature employs advanced machine learning algorithms to classify audio recordings, providing users with confidence in the integrity of the auditory content they encounter.'''
    st.markdown(welcome,unsafe_allow_html=True)
    st.write('Upload an audio file to see if it is real or fake.')

    file_uploaded = st.file_uploader("Choose an Audio File", type=["wav", "flac"])

    if file_uploaded is not None:
        st.audio(file_uploaded, format='audio/wav')
        st.write("File Uploaded Successfully!")

        # Save the uploaded file
        with open('temp_audio.wav', 'wb') as f:
            f.write(file_uploaded.read())

        # Extract features from audio
        example_features = extract_features('temp_audio.wav')

        if example_features is not None:
            # Make prediction
            prediction = model.predict(example_features)

            class_label = "Real" if prediction[0][0] >= 0.5 else "Fake"
            st.write(f"The audio is classified as {class_label}.")
        else:
            st.write("Error extracting features from the audio file.")

        # Remove the temporary audio file
        os.remove('temp_audio.wav')

if __name__ == "__main__":
    app()
