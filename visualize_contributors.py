import csv
import plotly.graph_objects as go

contributors = []
commits = []

try:
    with open("contributors.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            contributors.append(row["Contributor"])
            commits.append(int(row["Commits"]))
    print("✅ CSV data loaded successfully")
except FileNotFoundError:
    print("❌ contributors.csv not found. Run Day 7 script first.")
    exit(1)
except Exception as e:
    print(f"❌ Error reading CSV: {e}")
    exit(1)

data = sorted(zip(contributors, commits), key=lambda x: x[1], reverse=True)
contributors, commits = zip(*data)  

top_color = 'gold'  
other_color = '#1f77b4'  
colors = [top_color] + [other_color]*(len(contributors)-1)

try:
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=contributors,
        y=commits,
        text=commits,
        textposition='auto',
        marker_color=colors,
        hovertemplate='<b>%{x}</b><br>Commits: %{y}<extra></extra>'
    ))

    fig.update_layout(
        title='Repository Contributors vs Commits',
        xaxis_title='Contributors',
        yaxis_title='Commits',
        xaxis_tickangle=-45 if len(contributors) > 1 else 0,
        template='plotly_white',
        width=max(600, len(contributors)*60),
        height=500
    )

    fig.write_html("contributors_interactive.html")
    print("✅ Interactive chart saved as contributors_interactive.html")

    fig.show()

except Exception as e:
    print(f"❌ Error generating interactive chart: {e}")
