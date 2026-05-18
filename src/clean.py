import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the UCI Heart Disease dataset.
        - Missing values in 'ca' and 'thal'
        - Type casting for float columns that should be integers
        - Binarizing the target column 'num' (0 = no disease, 1 = disease)
        - Renaming 'num' to 'target' for clarity
    """

    df = df.copy()

    # Drop rows where 'ca' or 'thal' are null
    # Only 6 rows total — dropping is safer than imputing for medical data
    before = len(df)
    df = df.dropna(subset=['ca', 'thal'])
    after = len(df)
    print(f"Rows dropped due to nulls in 'ca' or 'thal': {before - after}")

    # Cast 'ca' and 'thal' from float to int now that nulls are removed
    df['ca']   = df['ca'].astype(int)
    df['thal'] = df['thal'].astype(int)

    # Binarize target column
    # Original 'num' has values 0-4 representing severity
    # 0 = no heart disease, 1-4 = presence of heart disease
    # Standard practice is to convert to binary for classification
    df['num'] = (df['num'] > 0).astype(int)

    # Rename target column for clarity
    df = df.rename(columns={'num': 'target'})

    print(f"Clean shape: {df.shape}")
    print(f"Target distribution:\n{df['target'].value_counts()}")

    return df