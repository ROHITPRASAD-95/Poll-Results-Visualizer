from src.data_creation import create_data
from src.data_cleaning import clean_data
from src.analysis import analyze
from src.visualization import create_charts
from src.insights import generate_insights

# Step 1: Create data
df = create_data()

# Step 2: Clean
df = clean_data(df)

# Step 3: Analyze
votes, percent = analyze(df)

# Step 4: Visualize
create_charts(df)

# Step 5: Insights
insight = generate_insights(votes)

print("\n📊 RESULTS")
print(percent)
print(insight)