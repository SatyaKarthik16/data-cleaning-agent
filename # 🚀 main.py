# 🚀 main.py – Entry Point

from config import OPENAI_API_KEY
from data_loader import load_dataset
from analyzer import analyze_dataframe
from llm_suggester import get_cleaning_suggestions
from code_generator import generate_python_code_from_final_instructions
from executor import execute_cleaning_code


def welcome():
    print("👋 Hello! I'm your Data Cleaning Agent.")
    print("📁 Please upload your dataset (CSV or Excel).")


def load_data():
    path = input("Enter path to your dataset: ").strip()
    df = load_dataset(path)
    return df, path


def get_user_consent_and_feedback(suggestions: str) -> str:
    print("\n👀 Please review the above cleaning suggestions.")
    print("💬 You can now add or modify instructions (or press Enter to accept as-is).")
    user_input = input("\n✏️ Additional instructions or clarifications: ").strip()

    if user_input == "":
        print("✅ Proceeding with original suggestions.")
        return suggestions
    else:
        print("🔄 Updating instructions with your input...")
        return suggestions + "\n\nAdditional User Instructions:\n" + user_input


if __name__ == "__main__":
    welcome()

    # Step 1: Load Dataset
    df, path = load_data()
    print(f"\n✅ Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")

    # Step 2: Analyze Dataset
    print("\n📋 Data Summary:\n")
    summary = analyze_dataframe(df)
    print(summary)

    # Step 3: Get Initial Cleaning Suggestions from LLM
    print("\n🧠 Asking AI for cleaning suggestions...\n")
    suggestions = get_cleaning_suggestions(summary)
    print("🤖 Cleaning Suggestions:\n")
    print(suggestions)

    # Step 4: Human Review & Add Instructions
    final_instructions = get_user_consent_and_feedback(suggestions)

    # Step 5: Generate Python Code from Final Instructions
    print("\n🧾 Generating final Python cleaning script based on full instruction set...\n")
    code = generate_python_code_from_final_instructions(final_instructions)
    print(code)

    # Optional: Save Python Script
    save_script = input("\n💾 Do you want to save this script to a file? (y/n): ").lower()
    if save_script == 'y':
        with open("cleaning_script.py", "w") as f:
            f.write(code)
        print("✅ Saved to cleaning_script.py")

    # Step 6: Execute Script on the Dataset
    print("\n⚙️ Running the generated script on the dataset...\n")
    cleaned_df = execute_cleaning_code(df, code)

    # Step 7: Show Preview of Cleaned Data
    print("\n🧼 Cleaned Data Preview (first 5 rows):\n")
    print(cleaned_df.head())

    # Step 8: Save Cleaned Dataset
    save_cleaned = input("\n📦 Do you want to save the cleaned dataset to a file? (y/n): ").lower()
    if save_cleaned == 'y':
        cleaned_df.to_csv("cleaned_dataset.csv", index=False)
        print("✅ Saved to cleaned_dataset.csv")
