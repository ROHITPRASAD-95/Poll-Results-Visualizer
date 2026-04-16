def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()

    df["Preferred Tool"] = df["Preferred Tool"].str.strip().str.title()

    return df