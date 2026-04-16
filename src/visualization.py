import matplotlib.pyplot as plt
import seaborn as sns

def create_charts(df):
    # Bar chart
    plt.figure()
    sns.countplot(x="Preferred Tool", data=df)
    plt.savefig("outputs/bar_chart.png")

    # Pie chart
    df["Preferred Tool"].value_counts().plot.pie(autopct='%1.1f%%')
    plt.savefig("outputs/pie_chart.png")