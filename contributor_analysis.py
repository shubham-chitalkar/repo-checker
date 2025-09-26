import os
import csv
from github import Github, GithubException, Auth

token = os.getenv("GITHUB_TOKEN")
if not token:
    raise Exception("❌ No GITHUB_TOKEN found. Please export it first.")

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

try:
    contributors = repo.get_contributors()
    contributor_list = []
    for c in contributors:
        print(f"{c.login}: {c.contributions} commits")
        contributor_list.append({
            "login": c.login,
            "contributions": c.contributions
        })
except Exception as e:
    print(f"❌ Error fetching contributors: {e}")
    exit(1)

csv_file = "contributors.csv"
try:
    with open(csv_file, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["login", "contributions"])
        writer.writeheader()
        writer.writerows(contributor_list)
    print(f"📄 Contributors saved to {csv_file}")
except Exception as e:
    print(f"❌ Failed to save CSV: {e}")
    exit(1)

