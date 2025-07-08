# app.py

import streamlit as st
import pandas as pd
from analyzer import analyze_dataframe
from llm_suggester import get_cleaning_suggestions
from code_generator import generate_python_code_from_final_instructions
from executor import execute_cleaning_code
from history_manager import save_cleaning_session, get_history

st.set_page_config(layout="wide", page_title="🧼 AI Data Cleaning Agent")

st.title("🧼 AI Data Cleaning Agent")
st.markdown("Upload a dataset, get cleaning suggestions, customize instructions, and clean your data with AI!")

# --- Upload Dataset ---
uploaded_file = st.file_uploader("📁 Upload CSV or Excel File", type=["csv", "xls", "xlsx"])
if uploaded_file:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"Failed to load file: {e}")
        st.stop()

    st.success(f"✅ Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns")

    # --- Data Summary ---
    st.subheader("📊 Dataset Summary")
    summary = analyze_dataframe(df)
    st.text(summary)

    # --- Cleaning Suggestions ---
    st.subheader("🤖 AI Cleaning Suggestions")
    with st.spinner("Asking the AI for cleaning suggestions..."):
        suggestions = get_cleaning_suggestions(summary)
    st.text_area("LLM Suggestions", suggestions, height=180)

    # --- Human Feedback ---
    st.subheader("✏️ Add or Modify Instructions")
    user_input = st.text_area("Additional Instructions (Optional)", placeholder="e.g., Also lowercase all column names")

    # Combine all instructions
    final_instructions = suggestions
    if user_input.strip():
        final_instructions += f"\n\nAdditional User Instructions:\n{user_input.strip()}"

    # --- Generate Python Code ---
    st.subheader("🧾 Generated Cleaning Code")
    if st.button("Generate Cleaning Code"):
        with st.spinner("Generating code..."):
            code = generate_python_code_from_final_instructions(final_instructions)
            st.session_state['code'] = code
        st.code(code, language="python")

    # --- Execute Cleaning Code ---
    if "code" in st.session_state:
        if st.button("⚙️ Run Cleaning Code"):
            with st.spinner("Running cleaning script..."):
                cleaned_df = execute_cleaning_code(df, st.session_state['code'])
                st.session_state['cleaned_df'] = cleaned_df
            st.success("✅ Cleaning complete!")
            st.dataframe(cleaned_df.head())

    # --- Save Session & Download ---
    if "cleaned_df" in st.session_state and "code" in st.session_state:
        version_id = f"v{len(get_history()) + 1}"
        save_cleaning_session(
            version_id=version_id,
            df=st.session_state["cleaned_df"],
            code=st.session_state["code"],
            instructions=final_instructions
        )
        st.success(f"💾 Cleaning session saved as {version_id}")

        st.download_button("📥 Download Cleaned Dataset", data=st.session_state['cleaned_df'].to_csv(index=False),
                           file_name=f"{version_id}_cleaned.csv", mime="text/csv")

        st.download_button("💾 Download Cleaning Script", data=st.session_state['code'],
                           file_name=f"{version_id}_script.py", mime="text/x-python")

    # --- Session History View ---
    st.subheader("🕓 Cleaning History")
    history = get_history()
    if history:
        for record in history[::-1]:
            st.markdown(f"**{record['version_id']}** — {record['timestamp']}")
            st.code(record['instructions'], language="text")
            with open(record['csv_path'], 'rb') as csv_file:
                st.download_button("📥 Download CSV", data=csv_file, file_name=f"{record['version_id']}.csv")
            with open(record['code_path'], 'rb') as code_file:
                st.download_button("💾 Download Script", data=code_file, file_name=f"{record['version_id']}.py")
    else:
        st.info("No history yet. Clean a dataset to begin tracking versions.")

