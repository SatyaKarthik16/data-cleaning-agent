# 🧼 AI Data Cleaning Agent

An intelligent, LLM-powered data cleaning tool built with **LangChain**, **LangGraph**, and **Streamlit**. Upload a dataset, receive auto-generated cleaning suggestions, customize them with human input, generate and run Python cleaning scripts — and version everything with rollback support.

> Built by Satya Karthik 👨‍💻

---

## 🎯 Features

- 📁 Upload CSV or Excel datasets
- 📊 Auto-analyze shape, nulls, types, duplicates, stats, sample data
- 🤖 GPT-powered cleaning suggestions
- ✍️ Human-in-the-loop customization
- 🧾 Python code generation using GPT (Pandas)
- ⚙️ Code execution on uploaded data
- 💾 Versioned history of cleaned outputs and scripts
- 🖥️ LangGraph orchestration and Streamlit UI

---

## 🧰 Tech Stack

| Tool        | Purpose                     |
|-------------|-----------------------------|
| LangChain   | LLM orchestration            |
| LangGraph   | Agent workflow/state engine  |
| OpenAI GPT  | LLM for analysis + code gen  |
| Streamlit   | Web UI frontend              |
| Pandas      | Data handling                |
| Python-dotenv | API key management         |
| JSON        | Version history tracking     |

---

📂 Final Project Structure

data_cleaning_agent/
│
├── 📄 app.py                     # Streamlit app (main UI entry point)
├── 📄 main.py                    # CLI entry point (optional for terminal users)
├── 📄 graph_runner.py            # LangGraph agent execution
├── 🧠 agent_graph.py             # LangGraph node definitions and agent state machine
│
├── 📁 cleaned_versions/          # Versioned cleaned datasets and scripts
│   ├── v1_cleaned.csv
│   ├── v1_script.py
│   ├── v2_cleaned.csv
│   └── ...
│
├── 📄 analyzer.py                # Generates dataset summaries and statistics
├── 📄 code_generator.py          # GPT-based cleaning code generation
├── 📄 config.py                  # Environment and LLM model configuration
├── 📄 data_loader.py             # Loads and validates user-uploaded datasets
├── 📄 executor.py                # Executes the cleaning script securely on DataFrame
├── 📄 history_manager.py         # Versioning and session storage (CSV + script + metadata)
├── 📄 llm_suggester.py           # Uses GPT to generate cleaning suggestions
│
├── 📄 requirements.txt           # Python dependencies
├── 📄 .env                       # API keys and model config (excluded from Git)
├── 📄 .gitignore                 # Prevents committing sensitive and generated files
└── 📄 README.md                  # Project documentation
