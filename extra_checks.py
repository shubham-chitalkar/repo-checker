import os
import re
from github import Github

token = os.getenv("GITHUB_TOKEN")
if not token:
    raise Exception("Please set your GITHUB_TOKEN environment variable")

g = Github(token)
repo = g.get_repo("shubham-chitalkar/repo-checker") 

files = [f.name for f in repo.get_contents("")]
if ".gitignore" in files:
    print("✅ .gitignore found")
else:
    print("❌ .gitignore missing")

if repo.description:
    print(f"✅ Repository description: {repo.description}")
else:
    print("❌ Repository description missing")

topics = repo.get_topics()
if topics:
    print(f"✅ Repository topics: {topics}")
else:
    print("❌ Repository has no topics/tags")
