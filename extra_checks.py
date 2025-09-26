import os
from github import Github, Auth, GithubException

token = os.getenv("GITHUB_TOKEN")
if not token:
    raise Exception("❌ No GITHUB_TOKEN found. Export it first.")

g = Github(auth=Auth.Token(token))
repo_name = "shubham-chitalkar/repo-checker" 
try:
    repo = g.get_repo(repo_name)
    print(f"✅ Accessed repository: {repo.full_name}")
except GithubException as e:
    print(f"❌ Error accessing repository {repo_name}: {e}")
    exit(1)

try:
    gitignore = repo.get_contents(".gitignore")
    print("✅ .gitignore found")
except GithubException:
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

try:
    with open("report.txt", "w") as f:
        f.write("Repo Health Check Report\n")
        f.write("----------------------\n")
        f.write(f"Repository: {repo.name}\n")
        f.write(f"Branches: {[b.name for b in repo.get_branches()]}\n")
        f.write(f"Commits: {repo.get_commits().totalCount}\n")
    print("📄 Report saved to report.txt")
except Exception as e:
    print(f"⚠️ Failed to write report: {e}")

