def analyze(df):
    vote_counts = df["Preferred Tool"].value_counts()
    percentage = (vote_counts / len(df)) * 100

    return vote_counts, percentage