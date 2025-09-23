from github import Github
import os

token = os.getenv("GITHUB_TOKEN")
g = Github(token)

repo = g.get_repo("shubham-chitalkar/repo-checker")

commits = repo.get_commits()[:5]
print("Last 5 commits:")
for commit in commits:
    print(commit.commit.message)

