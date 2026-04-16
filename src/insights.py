def generate_insights(vote_counts):
    top = vote_counts.idxmax()
    return f"Most preferred tool is {top}"