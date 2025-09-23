from github import Github
import requests

import os
token = os.getenv("GITHUB_TOKEN")
g = Github(token)

repo = g.get_repo("shubham-chitalkar/repo-checker") 

try:
    readme = repo.get_readme().decoded_content.decode()
    links = [line for line in readme.split() if line.startswith("http")]
    for link in links:
        try:
            response = requests.head(link, allow_redirects=True, timeout=5)
            if response.status_code == 200:
                print(f"✅ Link OK: {link}")
            else:
                print(f"⚠️ Broken link ({response.status_code}): {link}")
        except:
            print(f"⚠️ Broken link (error): {link}")
except:
    print("❌ README.md missing")

contents = repo.get_contents("")
def check_files(contents):
    for content_file in contents:
        if content_file.type == "dir":
            check_files(repo.get_contents(content_file.path))
        else:
            if content_file.size > 100*1024*1024:  
                print(f"⚠️ Large file: {content_file.path} ({content_file.size/1024/1024:.2f} MB)")
check_files(contents)

