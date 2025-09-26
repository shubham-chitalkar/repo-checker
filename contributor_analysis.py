import os
import csv
from github import Github, Auth, GithubException

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

contributors_list = []
try:
    contributors = repo.get_contributors()
    for contributor in contributors:
        contributors_list.append([contributor.login, contributor.contributions])
        print(f"{contributor.login}: {contributor.contributions} commits")
except Exception as e:
    print(f"⚠️ Error fetching contributors: {e}")

try:
    with open("contributors.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Contributor", "Commits"])  
        writer.writerows(contributors_list)
    print("📄 Contributors saved to contributors.csv")
except Exception as e:
    print(f"⚠️ Failed to write CSV: {e}")

