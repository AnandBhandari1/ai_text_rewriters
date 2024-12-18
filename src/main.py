import streamlit as st
from dotenv import load_dotenv
import time

from config.providers import PROVIDERS
from config.prompts import PROMPTS
from config.tones import TONES
from services.clipboard import get_clipboard, copy_to_clipboard
from services.text_rewriter import rewrite_text
from utils.session import init_session_state
from utils.tts import init_tts, speak_text
from ui.styles import CUSTOM_CSS

# Load environment variables
load_dotenv()

def main():
    st.set_page_config(
        page_title="AI Text Rewriter",
        page_icon="✍️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    init_session_state()
    init_tts()

    # Apply custom CSS
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    
    # Custom CSS for better spacing and alignment
    st.markdown("""
        <style>
        .stButton > button {
            width: 100%;
        }
        .main-header {
            text-align: center;
            padding: 1rem 0;
            margin-bottom: 2rem;
        }
        .alert-box {
            padding: 1rem;
            border-radius: 0.5rem;
            margin: 1rem 0;
        }
        .output-section {
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #f8f9fa;
            margin-top: 1rem;
        }
        .voice-controls {
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 0.5rem;
            margin: 1rem 0;
        }
        .audio-player {
            margin-top: 1rem;
            padding: 1rem;
            background-color: #e9ecef;
            border-radius: 0.5rem;
        }
        .audio-status {
            margin-top: 0.5rem;
            padding: 0.5rem;
            border-radius: 0.25rem;
            background-color: #212529;
            color: #fff;
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar controls
    with st.sidebar:
        st.markdown("<h1 style='text-align: center;'>✍️ Controls</h1>", unsafe_allow_html=True)
        
        with st.expander("📝 Input Text", expanded=True):
            # Text area for input
            input_text = st.text_area(
                "Enter or paste your text here:",
                value=st.session_state.input_text,
                height=200,
                key="text_input",
                help="Type or paste the text you want to rewrite"
            )
            st.session_state.input_text = input_text
            
            # Clipboard controls
            col1, col2 = st.columns(2)
            with col1:
                if st.button("📋 Get Clipboard", use_container_width=True):
                    get_clipboard()
            with col2:
                if st.button("📋 Copy Output", use_container_width=True):
                    copy_to_clipboard()
        
        with st.expander("⚙️ AI Settings", expanded=True):
            provider = st.selectbox(
                "AI Provider",
                options=list(PROVIDERS.keys()),
                key="provider",
                help="Select the AI provider for text rewriting"
            )
            
            model = st.selectbox(
                "Model",
                options=PROVIDERS[provider],
                key="model",
                help="Select the AI model to use"
            )
            
            prompt_type = st.selectbox(
                "Writing Task",
                options=list(PROMPTS.keys()),
                key="prompt_type",
                help="Select the type of rewriting task"
            )
            
            tone = st.selectbox(
                "Writing Tone",
                options=list(TONES.keys()),
                key="tone",
                help="Select the tone for the rewritten text"
            )

        # Rewrite button
        if st.button("🔄 Rewrite Text", use_container_width=True, type="primary"):
            if not input_text.strip():
                st.sidebar.error("⚠️ Please enter some text to rewrite.")
            else:
                with st.spinner("✨ Rewriting your text..."):
                    rewritten_text = rewrite_text(
                        input_text,
                        provider,
                        model,
                        prompt_type,
                        tone,
                        PROMPTS,
                        TONES
                    )
                    if rewritten_text:
                        st.session_state.output_text = rewritten_text
                        st.sidebar.success("✅ Text rewritten successfully!")

    # Main content area
    st.markdown("<h1 class='main-header'>🎯 Generated Output</h1>", unsafe_allow_html=True)
    
    # Display the rewritten text
    if st.session_state.output_text:
        # st.markdown("<div class='output-section'>", unsafe_allow_html=True)
        st.markdown("### Generated Text:")
        st.write(st.session_state.output_text)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # TTS controls - moved below the generated text
        if st.session_state.available_voices:
            with st.container():
                # st.markdown("<div class='voice-controls'>", unsafe_allow_html=True)
                st.markdown("### 🎤 Text to Speech", unsafe_allow_html=True)
                
                # Language and voice selection
                col1, col2 = st.columns(2)
                with col1:
                    # Group voices by locale for better organization
                    voices_by_locale = {}
                    for voice in st.session_state.available_voices:
                        locale = voice['locale']
                        if locale not in voices_by_locale:
                            voices_by_locale[locale] = []
                        voices_by_locale[locale].append(voice)
                    
                    # Create voice selection
                    locale = st.selectbox(
                        "🌍 Select Language",
                        options=sorted(voices_by_locale.keys()),
                        index=sorted(voices_by_locale.keys()).index('en-US') if 'en-US' in voices_by_locale else 0,
                        key="voice_locale",
                        help="Select the language for text-to-speech"
                    )
                
                with col2:
                    voice_options = voices_by_locale[locale]
                    selected_voice = st.selectbox(
                        "🎤 Select Voice",
                        options=voice_options,
                        format_func=lambda x: f"{x['name']} ({x['gender']})",
                        key="voice_selector",
                        help="Select the voice for text-to-speech"
                    )
                
                # Play button and audio player in a new row
                if st.button("🔊 Play Audio", use_container_width=True, type="primary"):
                    with st.spinner("🎵 Generating audio..."):
                        speak_text(st.session_state.output_text, selected_voice['name'])
                
                st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.warning("🔧 No text-to-speech voices found. Make sure edge-tts is installed: pip install edge-tts")
    else:
        st.info("👈 Enter text in the sidebar and click 'Rewrite' to see the results here.")

if __name__ == "__main__":
    main()
