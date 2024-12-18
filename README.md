# AI Text Rewriter 🤖✍️

A powerful AI-powered text rewriting application built with Streamlit that supports multiple AI providers and includes text-to-speech capabilities.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.0%2B-orange)

## 🌟 Features

- **Multiple AI Providers Support**
  - Groq
  - OpenRouter
  - Ollama
  - Gemini
  - Easy to extend for more providers

- **Advanced Text Rewriting**
  - Multiple writing tasks
  - Various writing tones
  - Different AI models for each provider
  - Real-time text generation

- **Text-to-Speech Integration**
  - Microsoft Edge TTS integration
  - Multiple languages support
  - Gender-specific voices
  - High-quality speech synthesis
  - Real-time audio generation

- **User-Friendly Interface**
  - Clean and modern UI
  - Clipboard integration
  - Expandable sections
  - Helpful tooltips
  - Progress indicators

## 🚀 Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/AnandBhandari1/ai-text-rewriters.git
cd ai-text-rewriters
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
Add your keys to your OS environment variables:
```env
GROQ_API_KEY=your_groq_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
GOOGLE_API_KEY=your_google_api_key
```

4. **Run the application**
```bash
streamlit run src/main.py
```

## 🛠️ Requirements

- Python 3.8 or higher
- Streamlit
- edge-tts
- python-dotenv
- Other dependencies listed in `requirements.txt`

## 📖 Usage

1. **Input Text**
   - Enter or paste your text in the sidebar
   - Use clipboard buttons for quick copy/paste

2. **Configure AI Settings**
   - Select AI provider
   - Choose AI model
   - Select writing task
   - Choose writing tone

3. **Generate Text**
   - Click "Rewrite Text" button
   - Wait for AI to process
   - View generated text in main area

4. **Text-to-Speech**
   - Select language and voice
   - Click "Play Audio" to hear the text
   - Audio controls appear automatically

## 🎯 Available Features

### AI Providers
- **Groq**: Fast and efficient AI models
- **OpenRouter**: Access to various AI models
- **Ollama**: Local AI processing
- **Gemini**: Google's advanced AI models

### Writing Tasks
- Grammar Improvement
- Content Rewriting
- Style Adaptation
- And more...

### Writing Tones
- Professional
- Casual
- Academic
- And others...

### TTS Features
- Multiple languages
- Various voice options
- Gender selection
- High-quality audio output

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Edge-TTS](https://github.com/rany2/edge-tts) for the text-to-speech functionality
- All the AI providers for their APIs

## 📞 Support

If you have any questions or run into issues, please open an issue in the GitHub repository.

## 🔮 Future Plans

- Add more AI providers
- Implement batch processing
- Add more writing tasks and tones
- Enhance TTS capabilities
- Add more language support

## 📚 References

- [Streamlit](https://streamlit.io/)
- [Edge-TTS](https://github.com/rany2/edge-tts)
- [Groq](https://groq.com/)
- [OpenRouter](https://openrouter.ai/)
- [Ollama](https://ollama.ai/)
- [Gemini](https://gemini.google.com/)

## Note

All this work is intended to be used for personal use only. I don't own any of the AI models or services used in this project. Everything here is for educational purposes only. You should not use this for any commercial purposes. My code is MIT licensed but other AI models and services are not. Please check their licenses for more information.

## Disclaimer

This project is not affiliated with any of the AI providers mentioned above. This project is not intended to be used for any commercial purposes. This project is intended to be used for educational purposes only.
