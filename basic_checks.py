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
    readme = repo.get_readme()
    print("✅ README.md found")
except GithubException:
    print("❌ README.md missing")
except Exception as e:
    print(f"⚠️ Error checking README.md: {e}")

try:
    commits = repo.get_commits()
    if commits.totalCount > 0:
        print(f"✅ Repository has {commits.totalCount} commits")
    else:
        print("❌ Repository has no commits")
except Exception as e:
    print(f"⚠️ Error fetching commits: {e}")

try:
    license_file = repo.get_license()
    print(f"✅ License found: {license_file.license.name}")
except GithubException:
    print("❌ LICENSE file missing")
except Exception as e:
    print(f"⚠️ Error checking LICENSE: {e}")

