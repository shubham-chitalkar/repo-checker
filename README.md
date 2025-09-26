
Repo Checker is a Python-based tool to analyze GitHub repositories. It performs health checks, analyzes contributors, and generates visualizations. The project helps developers and teams maintain clean, well-documented, and safe repositories.


1. **Basic Checks** – Verify README, commits, and LICENSE.
2. **Advanced Checks** – Detect large files, missing `tests/` folder, and check branch protection.
3. **Safe Checks** – Handles errors gracefully and saves results to `safe_report.txt`.
4. **Contributor Analysis** – Counts commits per contributor and saves data to `contributors.csv`.
5. **Visualization** – Generates static (`contributors.png`) and interactive (`contributors_interactive.html`) charts for contributors.



```bash
git clone https://github.com/your-username/repo-checker.git
cd repo-checker

