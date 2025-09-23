import csv
import matplotlib.pyplot as plt

contributors = []
commits = []

try:
    with open("contributors.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            contributors.append(row["Contributor"])
            commits.append(int(row["Commits"]))
    print("✅ CSV data loaded successfully")
except FileNotFoundError:
    print("❌ contributors.csv not found. Run Day 7 script first.")
    exit(1)
except Exception as e:
    print(f"❌ Error reading CSV: {e}")
    exit(1)

try:
    plt.figure(figsize=(10, 6))
    plt.bar(contributors, commits, color="skyblue")
    plt.xlabel("Contributors")
    plt.ylabel("Commits")
    plt.title("Repository Contributors vs Commits")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.savefig("contributors.png")
    print("✅ Contributors chart saved as contributors.png")
    
except Exception as e:
    print(f"❌ Error generating chart: {e}")

