import streamlit as st

def init_session_state():
    """Initialize session state variables"""
    if 'input_text' not in st.session_state:
        st.session_state.input_text = ""
    if 'output_text' not in st.session_state:
        st.session_state.output_text = ""
    if 'selected_voice' not in st.session_state:
        st.session_state.selected_voice = None
    if 'available_voices' not in st.session_state:
        st.session_state.available_voices = []
