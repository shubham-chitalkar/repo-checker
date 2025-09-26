import os
from github import Github

token = os.getenv("GITHUB_TOKEN")
from github import Github, Auth
g = Github(auth=Auth.Token(token))
repo = g.get_repo("shubham-chitalkar/repo-checker")

try:
    gitignore = repo.get_contents(".gitignore")
    print("✅ .gitignore found")
except:
    print("❌ .gitignore missing")

if repo.description:
    print(f"✅ Repo description: {repo.description}")
else:
    print("❌ Repo description not set")

topics = repo.get_topics()
if topics:
    print(f"✅ Topics: {topics}")
else:
    print("❌ No topics set")

with open("report.txt", "w") as f:
    f.write("Repo Health Check Report\n")
    f.write("----------------------\n")
    f.write(f"Repository: {repo.name}\n")
    f.write(f"Branches: {[b.name for b in repo.get_branches()]}\n")
    f.write(f"Commits: {repo.get_commits().totalCount}\n")

