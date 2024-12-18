import pyperclip
import streamlit as st

def get_clipboard():
    """Get text from clipboard"""
    try:
        text = pyperclip.paste()
        st.session_state.input_text = text
        return True
    except Exception as e:
        st.error(f"Error accessing clipboard: {str(e)}")
        return False

def copy_to_clipboard():
    """Copy text to clipboard"""
    try:
        pyperclip.copy(st.session_state.output_text)
        st.success("Text copied to clipboard!")
    except Exception as e:
        st.error(f"Error copying to clipboard: {str(e)}")
