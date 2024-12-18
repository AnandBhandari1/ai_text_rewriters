# Configuration for AI providers and their models
from services.text_rewriter import get_gemini_models

PROVIDERS = {
    'Gemini': get_gemini_models(),
    'Ollama': ['gnokit/improve-grammar','mistral', 'llama2', 'codellama', 'neural-chat'],
    'Groq': [
        'llama3-groq-70b-8192-tool-use-preview',
        'llama3-groq-8b-8192-tool-use-preview',
        'llama-3.3-70b-specdec',
        'llama-3.1-70b-specdec',
        'llama-3.2-1b-preview',
        'llama-3.2-3b-preview',
        'llama-3.2-11b-vision-preview',
        'llama-3.2-90b-vision-preview'
    ],
    'OpenRouter': [
        'google/gemini-2.0-flash-exp:free',
        'google/gemini-exp-1206:free',
        'google/gemini-exp-1121:free:free',
        'google/learnlm-1.5-pro-experimental:free',
        'google/gemini-exp-1114:free',
        'meta-llama/llama-3.2-3b-instruct',
        'meta-llama/llama-3.2-1b-instruct',
        'meta-llama/llama-3.2-90b-vision-instruct',
        'meta-llama/llama-3.2-11b-vision-instruct',
        'meta-llama/llama-3.1-405b-instruct',
        'meta-llama/llama-3.1-8b-instruct',
        'meta-llama/llama-3.1-70b-instruct',
        'qwen/qwen-2-7b-instruct',
        'google/gemma-2-9b-it',
        'mistralai/mistral-7b-instruct',
        'microsoft/phi-3-mini-128k-instruct',
        'microsoft/phi-3-medium-128k-instruct',
        'meta-llama/llama-3-8b-instruct',
        'openchat/openchat-7b',
        'undi95/toppy-m-7b',
        'huggingfaceh4/zephyr-7b-beta',
        'gryphe/mythomax-l2-13b'
    ]
}
