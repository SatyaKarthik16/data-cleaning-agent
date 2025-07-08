# 🧠 agent_graph.py

from langgraph.graph import StateGraph, END
from langgraph.graph.message import MessageGraph
from typing import TypedDict, Optional
from data_loader import load_dataset
from analyzer import analyze_dataframe
from llm_suggester import get_cleaning_suggestions
from code_generator import generate_python_code_from_final_instructions
from executor import execute_cleaning_code
import pandas as pd


# Define the memory/state structure
class AgentState(TypedDict):
    df: Optional[pd.DataFrame]
    summary: Optional[str]
    suggestions: Optional[str]
    final_instructions: Optional[str]
    code: Optional[str]
    cleaned_df: Optional[pd.DataFrame]


### Node definitions:

def welcome_node(state: AgentState) -> AgentState:
    print("👋 Welcome to the AI Data Cleaning Agent (LangGraph version).")
    return state

def load_dataset_node(state: AgentState) -> AgentState:
    path = input("Enter path to your dataset: ").strip()
    df = load_dataset(path)
    state['df'] = df
    return state

def analyze_node(state: AgentState) -> AgentState:
    summary = analyze_dataframe(state['df'])
    print("\n📋 Data Summary:\n")
    print(summary)
    state['summary'] = summary
    return state

def suggest_node(state: AgentState) -> AgentState:
    print("\n🧠 Asking LLM for suggestions...\n")
    suggestions = get_cleaning_suggestions(state['summary'])
    print("🤖 Cleaning Suggestions:\n")
    print(suggestions)
    state['suggestions'] = suggestions
    return state

def human_feedback_node(state: AgentState) -> AgentState:
    print("\n💬 You can add or modify the cleaning instructions (or press Enter to accept as-is):")
    feedback = input("✏️ Additional input: ").strip()
    if feedback:
        combined = state['suggestions'] + "\n\nAdditional User Instructions:\n" + feedback
    else:
        combined = state['suggestions']
    state['final_instructions'] = combined
    return state

def generate_code_node(state: AgentState) -> AgentState:
    print("\n🧾 Generating final Python code...")
    code = generate_python_code_from_final_instructions(state['final_instructions'])
    print("\n🧾 Final Code:\n")
    print(code)
    state['code'] = code
    return state

def execute_code_node(state: AgentState) -> AgentState:
    print("\n⚙️ Executing the generated code...")
    cleaned_df = execute_cleaning_code(state['df'], state['code'])
    print("\n🧼 Cleaned data preview:\n")
    print(cleaned_df.head())
    state['cleaned_df'] = cleaned_df
    return state

def save_output_node(state: AgentState) -> AgentState:
    cleaned_df = state['cleaned_df']
    save = input("📦 Save cleaned dataset? (y/n): ").strip().lower()
    if save == 'y':
        cleaned_df.to_csv("cleaned_dataset.csv", index=False)
        print("✅ Saved to cleaned_dataset.csv")
    return state
