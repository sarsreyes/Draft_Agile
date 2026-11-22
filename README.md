# Canada Vigilance Adverse Reaction Analytics Tool

An interactive Streamlit dashboard for exploring reporting patterns in Health Canada's Canada Vigilance adverse reaction data (reports initially received January 2024 to December 2025). Built as the final group project for CPSC 620 Agile Software Development using Scrum, test-driven development, and GitHub Projects.

> **Important:** The data contains reports of *suspected* adverse reactions. Counts show reporting patterns only. They do not show that a drug caused a reaction, and they are not incidence rates or probabilities of risk.

## Project links

| | |
|---|---|
| GitHub Project (backlog, Sprints, board) | [TODO: paste Project URL] |
| Technical report | [TODO: link or filename] |
| Video presentation | [TODO: link] |
| Instructor | @alamdari |

## Team

| Name | GitHub | Role |
|---|---|---|
| Nicholas Smith | [TODO: @handle] | Scrum Master |
| Leon Ramales | [TODO: @handle] | Developer |
| Sara Reyes | [TODO: @handle] | Developer |
| Maria Alejandra Boada Rodriguez | [TODO: @handle] | Developer |

## Quick start

These steps assume Python 3.10 or newer and Git are installed.

### 1. Clone the repository

```bash
git clone [TODO: repository URL]
cd [TODO: repository folder name]
```

### 2. Create and activate a virtual environment

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the datasets

The CSV files are **not** stored in this repository. Create a folder named `data` in the project root and place the three provided files in it:

```
data/
  reports.csv
  report_drugs.csv
  reactions.csv
```

The `data/` folder and all `*.csv` files are listed in `.gitignore`, so they will not be committed.

### 5. Run the dashboard

```bash
streamlit run app.py
```

Streamlit prints a local address (usually http://localhost:8501). Open it in a browser. The first load takes several seconds because about 148 MB of CSV data is read.

### 6. Run the tests

```bash
pytest
```

To see more detail, or to run a single file:

```bash
pytest -v
pytest tests/test_data_loader.py
```

## Dashboard features

| Page | What it shows | User story |
|---|---|---|
| Overview | Headline numbers (distinct reports, drugs, reaction terms, date range) and report types | US-03 |
| Top reactions | Most frequently reported reaction terms, counted by distinct report | US-04 |
| Reports over time | Monthly count of reports received | US-05 |
| Seriousness and outcomes | Breakdowns by seriousness and patient outcome | US-06 |
| [TODO: add Sprint 2 pages] | [TODO] | [TODO] |

[TODO: Keep this table in sync with what is actually built, and match the story count and points to the GitHub Project before submitting.]

## Project structure

```
.
├── app.py                 # Streamlit entry point (UI only, no business logic)
├── pages/                 # One Streamlit page per feature
├── src/
│   ├── data_loader.py     # Load, validate, and clean the three CSV files
│   ├── metrics.py         # Headline counts and KPIs
│   ├── analysis.py        # Top-N, trends, and breakdowns
│   └── charts.py          # Functions that return chart figures
├── tests/                 # pytest tests and shared fixtures (conftest.py)
├── data/                  # CSV files go here (not tracked by Git)
├── docs/                  # Team charter and supporting documents
├── requirements.txt
└── README.md
```

Every function in `src/` can be imported and used without Streamlit, for example:

```python
from src.data_loader import load_data, clean_reports
from src.analysis import top_reactions

reports, drugs, reactions = load_data("data")
reports = clean_reports(reports)
print(top_reactions(reactions, n=10))
```

## How the data is counted

The three files are linked by `REPORT_ID`. One report can have many drugs and many reactions, so joining the files multiplies rows. In this dataset a full three-way join produces roughly 77 times more rows than there are reports.

**Counting rule:** every count of reports uses the number of distinct `REPORT_ID` values, never the number of joined rows. Tests with small fixture data check this for each analysis function.

Other data-handling decisions:

- `REPORT_NO` is read as text so leading zeros are kept.
- Missing and placeholder values are shown as "Unknown", and reports are never dropped by cleaning.
- Ages outside the valid range are set to missing, and ages are grouped into documented bins.
- [TODO: add any other cleaning decisions the team agreed.]

## Data limitations

- Reports describe suspected reactions, not confirmed drug causation.
- Counts do not show how likely a reaction is. A drug with more reports may simply be used more widely.
- The dates show when a report was first received, not when the reaction happened.
- Many fields contain missing values, and reporting is subject to bias.
- The dataset mixes report types (for example Study and Spontaneous reports), which behave differently.

## How we worked (Agile process)

- **Methodology:** Scrum with two Sprints, planned and tracked in the GitHub Project.
- **Branching:** feature branches named `feature/<issue#>-short-name`, merged to `main` only through pull requests.
- **Reviews:** every pull request needs one formal approving review from a teammate other than the author.
- **Commits:** every commit message references an issue, for example `feat: add top reactions (#12)`.
- **TDD:** the Red, Green, Refactor steps are visible in the commit history of the TDD stories (see the report).
- **Definition of Done:** see [docs/team-charter.md](docs/team-charter.md).

## Contributing (team setup)

Run these once on your own computer after cloning:

```bash
git config user.name "First Last"
git config user.email "your-github-email@example.com"
git config core.hooksPath .githooks
```

The hook rejects commits that do not reference an issue. Never commit the dataset files.

## Dependencies

Main packages (see `requirements.txt` for the exact list and versions):

- pandas
- streamlit
- plotly
- pytest

## Before submitting: README checklist

- [ ] Search this file for `TODO`; none remain
- [ ] Project, repository, report, and video links all open correctly
- [ ] Story and point counts match the GitHub Project board
- [ ] The feature table matches the dashboard pages that actually exist
- [ ] A teammate followed the Quick start steps from a fresh clone and everything worked
- [ ] Delete this checklist section
