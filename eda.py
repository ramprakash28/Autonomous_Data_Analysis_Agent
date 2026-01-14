import pandas as pd

def run_eda(df:pd.DataFrame):
    observations = {}

    #Missing values summary
    missing = df.isna().mean().sort_values(ascending=False)
    observations['missing_values'] = missing[missing > 0].to_dict()

    # Numeric Distribution
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    observations['numeric_distribution'] = {}

    for col in numeric_cols:
        observations['numeric_distribution'][col] = {
            'mean': df[col].mean(),
            'median': df[col].median(),
            'std': df[col].std(),
            'min': df[col].min(),
            'max': df[col].max(),
        }

    #correlation matrix
    if len(numeric_cols) >=2:
        observations['correlations'] = (
            df[numeric_cols].corr().round(2).to_dict()
        )

    return observations 