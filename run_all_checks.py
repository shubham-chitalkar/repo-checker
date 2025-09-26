import os
import subprocess

# Ensure reports folder exists
os.makedirs("reports", exist_ok=True)

# List of scripts to run
scripts = [
    "basic_checks.py",
    "extra_checks.py",
    "contributor_analysis.py",
    "contributors_analysis_and_visualization.py",
    "safe_checks.py",
    "advanced_checks.py"
]

print("🚀 Running all repo-checker scripts...\n")

for script in scripts:
    print(f"🔹 Running {script}...")
    try:
        result = subprocess.run(
            ["python3", script],
            check=True,
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        print(result.stdout)
        print(f"✅ {script} completed successfully\n")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {script}: {e.stderr}\n")

print("🎉 All scripts executed. Check the reports/ folder for outputs.\n")

