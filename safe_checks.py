import os
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

try:
    with open("safe_report.txt", "w") as f:
        f.write("Safe Repo Health Check Report\n")
        f.write("----------------------------\n")
        f.write(f"Repository: {repo.full_name}\n")
        f.write(f"Commits: {commits.totalCount}\n")
        try:
            f.write(f"License: {license_file.license.name}\n")
        except:
            f.write("License: Not found\n")
        try:
            readme_check = "✅ README.md found" if readme else "❌ README.md missing"
        except:
            readme_check = "❌ README.md missing"
        f.write(f"{readme_check}\n")
    print("📄 Results saved to safe_report.txt")
except Exception as e:
    print(f"⚠️ Failed to write report: {e}")

