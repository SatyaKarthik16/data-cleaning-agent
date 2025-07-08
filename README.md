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

## 📂 Project Structure

data_cleaning_agent/
├── app.py # Streamlit app
├── agent_graph.py # LangGraph nodes and flow
├── analyzer.py # Data analysis engine
├── code_generator.py # Generates Python code via GPT
├── config.py # LLM and env loader
├── data_loader.py # Validates and loads datasets
├── executor.py # Executes Python script on df
├── graph_runner.py # LangGraph runner
├── history_manager.py # Version logging
├── llm_suggester.py # Suggests cleaning steps via GPT
├── main.py # CLI entrypoint
├── requirements.txt
├── .env # API keys (excluded from Git)
├── .gitignore
└── cleaned_versions/ # Folder for versioned outputs
