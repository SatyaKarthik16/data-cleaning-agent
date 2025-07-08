# code_generator.py

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from config import OPENAI_API_KEY, MODEL_NAME


def generate_python_code_from_final_instructions(instructions: str) -> str:
    system_prompt = (
        "You are a helpful data cleaning assistant. "
        "You were previously asked to suggest cleaning steps based on a dataset summary. "
        "Now, based on your earlier suggestions AND the user’s additional instructions, "
        "generate a complete Python cleaning script using Pandas for a DataFrame named 'df'.\n\n"
        "✅ Include comments to explain each step\n"
        "✅ Do not include markdown formatting or quotes\n"
        "✅ Only output raw Python code"
    )

    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=MODEL_NAME)

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Please generate a complete Python script for the following cleaning plan:\n\n{instructions}")
    ]

    response = llm(messages)
    return response.content.strip()
