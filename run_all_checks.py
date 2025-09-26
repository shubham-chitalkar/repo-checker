import os

os.makedirs("reports", exist_ok=True)

os.system("python3 basic_checks.py")
os.system("python3 extra_checks.py")
os.system("python3 contributor_analysis.py")
os.system("python3 contributors_analysis_and_visualization.py")
os.system("python3 safe_checks.py")

print("✅ All scripts executed. Check the reports/ folder for outputs.")

