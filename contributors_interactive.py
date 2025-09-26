import csv
import plotly.express as px

names = []
commits = []

try:
    with open('contributors.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            names.append(row['login'])            
            commits.append(int(row['contributions']))
    print("✅ CSV data loaded successfully")
except FileNotFoundError:
    print("❌ contributors.csv not found. Run contributor_analysis.py first.")
    exit(1)
except Exception as e:
    print(f"❌ Error reading CSV: {e}")
    exit(1)

data = sorted(zip(names, commits), key=lambda x: x[1], reverse=True)
names, commits = zip(*data)

colors = ['gold' if i == 0 else 'skyblue' for i in range(len(names))]

fig = px.bar(
    x=names,
    y=commits,
    labels={'x':'Contributor', 'y':'Commits'},
    title='GitHub Repo Contributors',
    color=colors
)

fig.write_html('contributors_interactive.html')
print("✅ Interactive chart saved as contributors_interactive.html")

