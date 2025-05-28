import os
import openai
import requests
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

def get_gemini_models():
    """Get list of available Gemini models"""
    load_dotenv()
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        st.error("Error: GOOGLE_API_KEY not set in environment variables")
        return []

    models = []
    try:
        genai.configure(api_key=api_key)
        for m in genai.list_models():
            if "generateContent" in m.supported_generation_methods:
                models.append(m.name)
        return models
    except Exception as e:
        st.error(f"Error getting Gemini models: {str(e)}")
        return []

def rewrite_text(text, provider, model, prompt_type, tone, prompts, tones):
    """Rewrite text using selected AI provider"""
    try:
        selected_tone = tones[tone]
        selected_prompt = prompts[prompt_type]['content']
        prompt = f'{selected_prompt} Use the following tone: {selected_tone}. Here is the text: {text}'
        
        st.write(f"Debug - Using provider: {provider}")  # Debug info
        
        if provider == 'Ollama':
            return _rewrite_with_ollama(prompt, model)
        elif provider == 'Groq':
            return _rewrite_with_groq(prompt, model)
        elif provider == 'OpenRouter':
            return _rewrite_with_openrouter(prompt, model)
        elif provider == 'Gemini':
            return _rewrite_with_gemini(prompt, model)
            
    except Exception as e:
        st.error(f"Error during text rewriting: {str(e)}")
        return None

def _rewrite_with_ollama(prompt, model):
    """Handle text rewriting with Ollama"""
    try:
        st.write("Debug - Sending request to Ollama")  # Debug info
        
        data = {
            'model': model,
            'prompt': prompt,
            'stream': False
        }
        response = requests.post('http://localhost:11434/api/generate', json=data, timeout=30)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        if response.status_code == 200:
            result = response.json()
            st.write(f"Debug - Ollama response: {result}")  # Debug info
            return result['response'].strip()
        else:
            st.error(f"Error from Ollama API: Status {response.status_code}")
            return None
            
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to Ollama. Make sure Ollama is running locally on port 11434.")
        return None
    except Exception as e:
        st.error(f"Error in Ollama request: {str(e)}")
        return None

def _rewrite_with_groq(prompt, model):
    """Handle text rewriting with Groq"""
    try:
        api_key = os.environ.get("GROQ_API_KEY")
        if not api_key:
            st.error("Error: GROQ_API_KEY not set in environment variables")
            return None
            
        st.write("Debug - Sending request to Groq")  # Debug info
        
        client = openai.OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=api_key
        )
        
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=2000
        )
        
        st.write(f"Debug - Groq response received")  # Debug info
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        st.error(f"Error in Groq request: {str(e)}")
        return None

def _rewrite_with_openrouter(prompt, model):
    """Handle text rewriting with OpenRouter"""
    try:
        api_key = os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            st.error("Error: OPENROUTER_API_KEY not set in environment variables")
            return None
            
        st.write("Debug - Sending request to OpenRouter")  # Debug info
        
        client = openai.OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key
        )
        
        response = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "http://localhost:8501",  # Local Streamlit app URL
                "X-Title": "Text Rewriter",
            },
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=2000
        )
        
        st.write(f"Debug - OpenRouter response received")  # Debug info
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        st.error(f"Error in OpenRouter request: {str(e)}")
        return None

def _rewrite_with_gemini(prompt, model):
    """Handle text rewriting with Gemini"""
    try:
        api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            st.error("Error: GOOGLE_API_KEY not set in environment variables")
            return None
            
        st.write("Debug - Sending request to Gemini")  # Debug info
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model)
        response = model.generate_content(prompt)
        
        if response.text:
            st.write(f"Debug - Gemini response received")  # Debug info
            return response.text.strip()
        else:
            st.error("Empty response from Gemini")
            return None
        
    except Exception as e:
        st.error(f"Error in Gemini request: {str(e)}")
        return None
