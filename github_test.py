from github import Github
import os

token = os.getenv("GITHUB_TOKEN")
g = Github(token)

repo = g.get_repo("shubham-chitalkar/repo-checker")

print(f"Repository Name: {repo.name}")
print(f"Default Branch: {repo.default_branch}")
print("Branches:")
for branch in repo.get_branches():
    print(f"- {branch.name}")

print(f"Total Commits: {repo.get_commits().totalCount}")

