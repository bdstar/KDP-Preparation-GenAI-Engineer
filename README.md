# Generative AI Engineer - Code Companion

This repository contains **114 runnable Python scripts** extracted directly from the book *"Preparation as a Generative AI Engineer — Complete Book"*.

These scripts serve as a practical, hands-on companion to the concepts taught in the book, covering everything from Python foundations to advanced Generative AI engineering.

## 📖 Contents

The extracted scripts (`script_001.py` through `script_114.py`) cover a wide range of topics essential for Generative AI engineers, including:

*   **Python Foundations & Toolkit:** Dataclasses, types, data manipulation.
*   **Deep Learning & NLP Core:** Neural network fundamentals using PyTorch.
*   **Transformers & LLMs:** Working with HuggingFace `transformers`, tokenization, and model inference.
*   **Prompting & Fine-Tuning:** Parameter-Efficient Fine-Tuning (PEFT), LoRA.
*   **RAG (Retrieval-Augmented Generation) & Vector Databases:** LangChain, vector embeddings, chunking, and similarity search.
*   **Agents & Orchestration:** Building multi-step AI agents and calling tools.
*   **APIs & Backends:** Serving models and interacting with cloud LLM providers.

## 🚀 Getting Started

### Prerequisites

To run these scripts, you will need a Python environment configured for Machine Learning and Generative AI. It is highly recommended to use a virtual environment (`venv` or `conda`).

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

2. **Install core dependencies:**
   While specific scripts may require specific libraries, the foundational stack includes:
   ```bash
   pip install torch transformers datasets evaluate
   pip install openai langchain langchain-community
   pip install chromadb pydantic fastapi uvicorn
   ```

### Running the Scripts

The scripts are standalone and meant to be executed individually. For example:
```bash
python script_020.py
```

> **⚠️ Important Notes:**
> *   **API Keys:** Many scripts interact with external APIs (like OpenAI). You will need to export your API keys as environment variables before running them (e.g., `export OPENAI_API_KEY="your-key-here"` or `set OPENAI_API_KEY="your-key-here"` on Windows).
> *   **Local Models:** Scripts that load local models via Hugging Face might require significant RAM/VRAM and will download model weights on the first run.
> *   **Context:** Because these scripts are extracted as code blocks from a textbook, some may represent specific functions or classes meant to be studied in the context of the book's explanations.

## 🛠️ Code Validation

All scripts in this repository have been automatically validated through Python's `ast` (Abstract Syntax Tree) module to ensure they are syntactically correct and structurally meaningful.

---
*Generated automatically from the source text.*
