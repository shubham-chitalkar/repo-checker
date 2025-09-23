import csv
import matplotlib.pyplot as plt
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
    print("❌ contributors.csv not found. Run Day 7 first.")
    exit(1)
except Exception as e:
    print(f"❌ Error reading CSV: {e}")
    exit(1)

try:
    plt.figure(figsize=(max(6, len(contributors)*0.7), 6))
    bars = plt.bar(contributors, commits, color="skyblue", edgecolor="black")

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + max(commits)*0.01,
            str(height),
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold"
        )

    plt.xlabel("Contributors", fontsize=12, fontweight="bold")
    plt.ylabel("Commits", fontsize=12, fontweight="bold")
    plt.title("Repository Contributors vs Commits", fontsize=14, fontweight="bold")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.xticks(rotation=45 if len(contributors) > 1 else 0,
               ha="right" if len(contributors) > 1 else "center")

    plt.tight_layout()
    plt.savefig("contributors.png", dpi=300)
    print("✅ Static chart saved as contributors.png")

except Exception as e:
    print(f"❌ Error generating static chart: {e}")

try:
    data = sorted(zip(contributors, commits), key=lambda x: x[1], reverse=True)
    contributors_sorted, commits_sorted = zip(*data)

    top_color = 'gold'
    other_color = '#1f77b4'
    colors = [top_color] + [other_color]*(len(contributors_sorted)-1)

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=contributors_sorted,
        y=commits_sorted,
        text=commits_sorted,
        textposition='auto',
        marker_color=colors,
        hovertemplate='<b>%{x}</b><br>Commits: %{y}<extra></extra>'
    ))

    fig.update_layout(
        title='Repository Contributors vs Commits',
        xaxis_title='Contributors',
        yaxis_title='Commits',
        xaxis_tickangle=-45 if len(contributors_sorted) > 1 else 0,
        template='plotly_white',
        width=max(600, len(contributors_sorted)*60),
        height=500
    )

    fig.write_html("contributors_interactive.html")
    print("✅ Interactive chart saved as contributors_interactive.html")

    try:
        fig.write_image("contributors_interactive.png", scale=2)
        print("✅ Interactive PNG saved as contributors_interactive.png")
    except:
        print("⚠ PNG export failed. Install 'kaleido' for static image export.")

    fig.show()

except Exception as e:
    print(f"❌ Error generating interactive chart: {e}")

