import os
import csv
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from github import Github, Auth, GithubException

os.makedirs("reports", exist_ok=True)

token = os.getenv("GITHUB_TOKEN")
if not token:
    raise Exception("❌ No GITHUB_TOKEN found. Export it first.")

try:
    g = Github(auth=Auth.Token(token))
    print("✅ GitHub client initialized successfully")
except Exception as e:
    print(f"❌ Failed to initialize GitHub client: {e}")
    exit(1)

repo_name = "shubham-chitalkar/repo-checker"
try:
    repo = g.get_repo(repo_name)
    print(f"✅ Accessed repository: {repo.full_name}")
except GithubException as e:
    print(f"❌ Error accessing repository {repo_name}: {e}")
    exit(1)
except Exception as e:
    print(f"❌ Unexpected error accessing repository: {e}")
    exit(1)

contributors_list = []
try:
    contributors = repo.get_contributors()
    for contributor in contributors:
        contributors_list.append([contributor.login, contributor.contributions])
        print(f"{contributor.login}: {contributor.contributions} commits")
except Exception as e:
    print(f"⚠️ Error fetching contributors: {e}")

csv_file = "reports/contributors.csv"
try:
    with open(csv_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Contributor", "Commits"])
        writer.writerows(contributors_list)
    print(f"📄 Contributors saved to {csv_file}")
except Exception as e:
    print(f"⚠️ Failed to write CSV: {e}")
    exit(1)

contributors = []
commits = []
try:
    with open(csv_file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            contributors.append(row["Contributor"])
            commits.append(int(row["Commits"]))
    print("✅ CSV data loaded successfully for visualization")
except Exception as e:
    print(f"❌ Error reading CSV: {e}")
    exit(1)

png_file = "reports/contributors.png"
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
    plt.savefig(png_file, dpi=300)
    plt.close()
    print(f"✅ Static chart saved as {png_file}")
except Exception as e:
    print(f"❌ Error generating static chart: {e}")

html_file = "reports/contributors_interactive.html"
interactive_png_file = "reports/contributors_interactive.png"
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

    fig.write_html(html_file)
    print(f"✅ Interactive chart saved as {html_file}")

    try:
        fig.write_image(interactive_png_file, scale=2)
        print(f"✅ Interactive PNG saved as {interactive_png_file}")
    except:
        print("⚠️ PNG export failed. Install 'kaleido' for static image export.")

except Exception as e:
    print(f"❌ Error generating interactive chart: {e}")

