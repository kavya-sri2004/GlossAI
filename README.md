# GlossAI 🔗

### AI-Powered Business Glossary Mapper

GlossAI is an AI-powered application designed to map dataset columns to standardized business glossary terms using semantic matching and Large Language Models (LLMs).

## Features

- AI-powered business glossary mapping
- CSV dataset profiling
- Semantic similarity-based retrieval
- LLM-powered mapping suggestions
- Human-in-the-loop review
- Exportable mapping results

## Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- Groq API
- Ollama (optional local LLM)

## Project Status

🚧 Under active development.

Currently, the initial Streamlit application and development environment have been set up.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/kavya-sri2004/GlossAI.git
cd GlossAI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

## Roadmap

- [x] Initial project setup
- [x] Streamlit interface
- [ ] CSV data profiling
- [ ] Business glossary management
- [ ] Semantic retrieval
- [ ] Groq LLM integration
- [ ] Ollama integration
- [ ] Human-in-the-loop mapping
- [ ] CSV export
- [ ] Docker deployment

## License

MIT License