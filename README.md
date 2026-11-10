
# GlossAI 🔗

### AI-Powered Business Glossary Mapper

GlossAI is an AI-powered application designed to map dataset columns to standardized business glossary terms. It combines traditional semantic similarity techniques with Large Language Models (LLMs) to generate meaningful business metadata mapping suggestions.

The goal is to help data analysts and engineers understand dataset columns, improve metadata consistency, and reduce manual business glossary mapping effort.

## Features

- CSV dataset upload and profiling
- Business glossary-based column mapping
- TF-IDF vectorization
- Cosine similarity-based matching
- Suggested business glossary terms with similarity scores
- Exportable mapping results
- Planned LLM-powered semantic mapping
- Planned human-in-the-loop mapping review

## Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- Groq API — planned
- Ollama — optional local LLM, planned

## Current Implementation

The initial version of GlossAI includes:

- A Streamlit interface for uploading CSV datasets
- Dataset overview, including row count, column count, and missing values
- Dataset preview and column profiling
- Statistical summary
- TF-IDF-based text vectorization
- Cosine similarity-based glossary matching
- Suggested glossary terms and similarity scores
- CSV export of mapping results

The current mapping engine uses TF-IDF and cosine similarity as a baseline. LLM-based semantic mapping is planned for a future version.

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
python -m streamlit run app.py
```

## Project Structure

```text
GlossAI/
├── app.py
├── mapping_engine.py
├── glossary.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## Roadmap

- [x] Initial project setup
- [x] Streamlit interface
- [x] CSV dataset profiling
- [x] Business glossary loading
- [x] TF-IDF vectorization
- [x] Cosine similarity-based mapping
- [x] Mapping results display
- [x] CSV export
- [ ] Groq LLM integration
- [ ] LLM-based semantic mapping
- [ ] Mapping explanations and confidence indicators
- [ ] Human-in-the-loop mapping review
- [ ] Optional Ollama integration
- [ ] Mapping evaluation and comparison
- [ ] Docker deployment

## License

MIT License
