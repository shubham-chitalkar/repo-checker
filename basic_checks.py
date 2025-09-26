import os
from github import Github

token = os.getenv("GITHUB_TOKEN")
from github import Github, Auth
g = Github(auth=Auth.Token(token))
repo = g.get_repo("shubham-chitalkar/repo-checker")

try:
    readme = repo.get_readme()
    print("✅ README.md found")
except:
    print("❌ README.md missing")

commits = repo.get_commits()
if commits.totalCount > 0:
    print(f"✅ Repository has {commits.totalCount} commits")
else:
    print("❌ Repository has no commits")

try:
    license_file = repo.get_license()
    print(f"✅ License found: {license_file.license.name}")
except:
    print("❌ LICENSE file missing")

