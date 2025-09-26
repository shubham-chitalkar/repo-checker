A small Python toolset to check GitHub repository health, analyze contributors, and generate visual reports.

- Check for README, LICENSE, .gitignore
- Count commits and list branches
- Detect large files and missing tests
- Contributor analysis → `contributors.csv`
- Static & interactive visualizations → `contributors.png`, `contributors_interactive.html`
- Safe token usage via environment variable (`GITHUB_TOKEN`)

- Python 3.8+
- Git
- A GitHub personal access token (with `repo` or `public_repo` permissions depending on repo visibility)

```bash
git clone https://github.com/shubham-chitalkar/repo-checker.git
cd repo-checker
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

