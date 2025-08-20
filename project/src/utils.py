def get_summary_stats(df):
    print(df.describe())
    summary = df.groupby('category').mean(numeric_only=True).reset_index()
    print(summary)
    return