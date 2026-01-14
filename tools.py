import pandas as pd

def inspect_csv(file_path: str) -> pd.DataFrame:
    """Reads a CSV file and returns its contents as a DataFrame."""
    return pd.read_csv(file_path)
    report = {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'missing_values': df.isnull().sum().to_dict()
    }

    return report