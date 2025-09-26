import os
from github import Github, Auth

token = os.getenv("GITHUB_TOKEN")
if not token:
    raise Exception("❌ No GITHUB_TOKEN found. Export it first.")

g = Github(auth=Auth.Token(token))
repo_name = "shubham-chitalkar/repo-checker" 
repo = g.get_repo(repo_name)

report_lines = []

print("\n🔍 Checking for large files (>10 MB)...")
large_files = []
contents = repo.get_contents("")
while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        if file_content.size > 10 * 1024 * 1024:
            large_files.append((file_content.path, file_content.size))

if large_files:
    for f, s in large_files:
        print(f"❌ Large file: {f} ({s/1024/1024:.2f} MB)")
        report_lines.append(f"Large file: {f} ({s/1024/1024:.2f} MB)")
else:
    print("✅ No large files found")
    report_lines.append("No large files found")

print("\n🔍 Checking for tests/ folder...")
try:
    repo.get_contents("tests")
    print("✅ tests/ folder exists")
    report_lines.append("tests/ folder exists")
except:
    print("❌ No tests/ folder")
    report_lines.append("No tests/ folder")

print("\n🔍 Checking if main branch is protected...")
try:
    branch = repo.get_branch("main")
    if branch.protected:
        print("✅ main branch is protected")
        report_lines.append("main branch is protected")
    else:
        print("❌ main branch is not protected")
        report_lines.append("main branch is not protected")
except:
    print("⚠️ Could not check branch protection (need admin rights)")
    report_lines.append("Could not check branch protection")

with open("report.txt", "a") as f:
    f.write("\nAdvanced Checks:\n")
    f.write("----------------\n")
    for line in report_lines:
        f.write(line + "\n")
print("\n📄 Results appended to report.txt")

