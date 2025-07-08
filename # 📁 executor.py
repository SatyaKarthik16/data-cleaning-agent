# 📁 executor.py

import pandas as pd
import traceback


def execute_cleaning_code(df: pd.DataFrame, code: str) -> pd.DataFrame:
    local_vars = {'df': df.copy()}
    try:
        exec(code, {}, local_vars)
        cleaned_df = local_vars['df']
        return cleaned_df
    except Exception as e:
        print("❌ Error while executing cleaning code:")
        traceback.print_exc()
        return df  # fallback to original if failed
