import streamlit as st
import dashboard
import classifyPage
import classifyAudio
st.set_page_config(
    page_title="VeriGuard",
    page_icon="🤖",
    layout="wide")
PAGES = {
    "Dashboard": dashboard,
    "Classify Image": classifyPage,
    "Classify Audio": classifyAudio
}
st.sidebar.image('VeriGuard.png')

st.sidebar.title("VeriGuard")

st.sidebar.write("VeriGuard is a tool that utilizes the power of Deep Learning to distinguish Real images,audios and profiles from the Fake ones.")

st.sidebar.subheader('Navigation:')
selection = st.sidebar.radio("", list(PAGES.keys()))

page = PAGES[selection]

page.app()
