import streamlit as st
import edge_tts
import asyncio
import tempfile
import os
from typing import List, Dict
import sys
import pkg_resources

def check_edge_tts_installation():
    """Check if edge-tts is properly installed"""
    try:
        version = pkg_resources.get_distribution('edge-tts').version
        # st.info(f"edge-tts version {version} is installed")
        return True
    except pkg_resources.DistributionNotFound:
        st.error("edge-tts is not installed. Please run: pip install edge-tts")
        return False

async def get_voices() -> List[Dict[str, str]]:
    """Get available voices from Edge TTS"""
    if not check_edge_tts_installation():
        return []
        
    try:
        # Get voices
        voices = await edge_tts.list_voices()
        # st.info(f"Found {len(voices)} voices")
        
        # Convert to simpler format
        voice_list = [
            {
                "name": voice["ShortName"],
                "gender": voice["Gender"],
                "locale": voice["Locale"]
            }
            for voice in voices
        ]
        
        if not voice_list:
            # st.error("No voices found in the response")
            return []
            
        # Log some sample voices for debugging
        # if voice_list:
            # st.info(f"Sample voice: {voice_list[0]}")
            
        return voice_list
    except Exception as e:
        st.error(f"Error getting voices: {str(e)}")
        import traceback
        st.error(f"Traceback: {traceback.format_exc()}")
        return []

def init_tts():
    """Initialize TTS and get available voices"""
    try:
        # Always refresh voices on initialization
        voices = asyncio.run(get_voices())
        if voices:
            st.session_state.available_voices = voices
            return True
        return False
    except Exception as e:
        st.error(f"Error initializing TTS: {str(e)}")
        import traceback
        st.error(f"Traceback: {traceback.format_exc()}")
        return False

async def _speak_text_async(text: str, voice_name: str) -> str:
    """Internal async function to generate speech"""
    try:
        st.info(f"Generating speech with voice: {voice_name}")
        
        # Create communicate instance
        tts = edge_tts.Communicate(text, voice_name)
        
        # Create a temporary file to save the audio
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            temp_file = fp.name
            
        # Generate audio file
        await tts.save(temp_file)
        st.info(f"Audio file generated: {temp_file}")
        
        return temp_file
    except Exception as e:
        st.error(f"Error generating speech: {str(e)}")
        import traceback
        st.error(f"Traceback: {traceback.format_exc()}")
        return None

def speak_text(text: str, voice_name: str):
    """Generate speech from text using Edge TTS"""
    try:
        # Generate audio file
        audio_file = asyncio.run(_speak_text_async(text, voice_name))
        
        if audio_file and os.path.exists(audio_file):
            # Play the audio using streamlit's audio player
            with open(audio_file, 'rb') as f:
                audio_bytes = f.read()
            st.audio(audio_bytes, format='audio/mp3')
            st.success("Audio generated successfully!")
            
            # Clean up the temporary file
            try:
                os.unlink(audio_file)
            except Exception as e:
                st.warning(f"Could not delete temporary file: {str(e)}")
        else:
            st.error("Failed to generate audio file")
    except Exception as e:
        st.error(f"Error playing speech: {str(e)}")
        import traceback
        st.error(f"Traceback: {traceback.format_exc()}")