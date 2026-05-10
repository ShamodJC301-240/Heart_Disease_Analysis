from src.UCI_link import load_heart_disease


def main():
    """
    Main pipeline execution for Heart Disease analysis.
    """

    # Load dataset
    df = load_heart_disease()

    # Safety check (important in real pipelines)
    if df is None:
        print("Dataset failed to load. Exiting pipeline.")
        return

    # Basic overview
    print("\n--- Dataset Preview ---")
    print(df.head())

    print("\n--- Dataset Shape ---")
    print(df.shape)

    print("\n--- Columns ---")
    print(df.columns)

    print("\nPipeline executed successfully.")


if __name__ == "__main__":
    main()