import pandas as pd
import numpy as np

def create_data():
    np.random.seed(42)
    n = 300

    df = pd.DataFrame({
        "Age Group": np.random.choice(["18-24", "25-34", "35-44", "45+"], n),
        "Gender": np.random.choice(["Male", "Female"], n),
        "Preferred Tool": np.random.choice(["Python", "Excel", "R", "Power BI"], n),
        "Satisfaction": np.random.randint(1, 6, n),
        "Feedback": np.random.choice(["Great tool","Needs improvement","Excellent"], n)
    })

    df.to_csv("data/poll_data.csv", index=False)
    return df