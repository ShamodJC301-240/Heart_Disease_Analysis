from src.load_data import load_heart_disease


def main():
    """
    Main pipeline execution for Heart Disease analysis.
    """

    df = load_heart_disease()

    if df is None:
        print("\nDataset failed to load. Exiting pipeline.")
        return

    # Preview
    print("\nThese are our first five rows in our dataset:")
    print(df.head())

    # Shape
    rows, cols = df.shape
    print(f"\nDataset shape -> Rows: {rows}, Columns: {cols}")

    # Columns
    print("\nHere are our columns:")
    for col in df.columns:
        print(f"- {col}")

    print("\nPipeline executed successfully.")


if __name__ == '__main__':
    main()