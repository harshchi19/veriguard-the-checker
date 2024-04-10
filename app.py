import streamlit as st
import dashboard
import classifyPage
import classifyAudio
import contact
import About
import text
import fakeAccount
st.set_page_config(
    page_title="VeriGuard",
    page_icon="🤖",
    layout="wide")
PAGES = {
    "About": dashboard,
    "Classify Image": classifyPage,
    "Classify Audio": classifyAudio,
    "Classify News": text,
    "Classify Account": fakeAccount,
    "Contact": contact,
    
}
st.sidebar.image('/content/Veriguard.png')

st.sidebar.title("VeriGuard")

st.sidebar.write("VeriGuard is a tool that utilizes the power of Deep Learning to distinguish Real images,audios and profiles from the Fake ones.")

st.sidebar.subheader('Navigation:')
selection = st.sidebar.radio("", list(PAGES.keys()))

page = PAGES[selection]

page.app()
