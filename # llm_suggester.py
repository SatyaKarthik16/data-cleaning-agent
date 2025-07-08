# llm_suggester.py

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from config import OPENAI_API_KEY, MODEL_NAME

def get_cleaning_suggestions(summary: str) -> str:
    system_prompt = (
        "You are a helpful data cleaning assistant. "
        "Given the summary of a dataset, analyze and suggest the most important cleaning steps. "
        "Be concise and clear. Mention the specific column names and actions needed. "
        "Use a numbered list. Keep it understandable for non-technical users."
    )

    # Initialize OpenAI chat model
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=MODEL_NAME)

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Here is the dataset summary:\n\n{summary}")
    ]

    response = llm(messages)
    return response.content
