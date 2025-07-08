# 📄 data_loader.py

import pandas as pd
import os

SUPPORTED_EXTENSIONS = ['.csv', '.xls', '.xlsx']

def is_supported(file_path: str) -> bool:
    return any(file_path.endswith(ext) for ext in SUPPORTED_EXTENSIONS)

def load_dataset(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if not is_supported(file_path):
        raise ValueError(f"Unsupported file type. Supported: {SUPPORTED_EXTENSIONS}")

    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)

    return df
