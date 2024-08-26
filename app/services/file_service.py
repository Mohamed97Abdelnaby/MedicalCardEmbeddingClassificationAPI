import os
import numpy as np
import pandas as pd
from app.core.config import config


def load_excel_file():
    if os.path.exists(config.EXCEL_FILE_PATH):
        df = pd.read_csv(config.EXCEL_FILE_PATH)
        df['Embedding'] = df['Embedding'].apply(
            lambda x: np.array(eval(x)))  # Convert string representation of list back to numpy array
        return df
    else:
        # Create a DataFrame with the appropriate columns if the file does not exist
        return pd.DataFrame(columns=['Card Name', 'Sample Text', 'Embedding'])


def save_excel_file(df):
    df['Embedding'] = df['Embedding'].apply(lambda x: x.tolist())  # Convert numpy array to list for saving
    df.to_csv(config.EXCEL_FILE_PATH, index=False)
