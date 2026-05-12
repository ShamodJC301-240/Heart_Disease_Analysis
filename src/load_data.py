from ucimlrepo import fetch_ucirepo
import pandas as pd


def load_heart_disease():
    """
    Load the UCI Heart Disease dataset.

    Returns:
        pd.DataFrame:
            Combined dataframe containing both
            feature columns and target columns.

        None:
            Returned if dataset loading fails.
    """

    try:
        # Fetch dataset from UCI repository
        heart_disease = fetch_ucirepo(id=45)

        # Extract feature variables
        X = heart_disease.data.features

        # Extract target variable(s)
        y = heart_disease.data.targets

        # Combine features + target into one dataframe
        df = pd.concat([X, y], axis=1)

        # Success message
        print("Heart Disease dataset loaded successfully.")

        return df

    except Exception as e:
        # Handle loading errors gracefully
        print(f"Error loading dataset: {e}")

        return None