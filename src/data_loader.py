"""Load, validate and clean the three Canada Vigilance CSV files.

Files (linked by REPORT_ID): reports.csv, report_drugs.csv, reactions.csv.
Nothing here may import Streamlit.

Stories: US-01 (load, validate) and US-02 (clean).
"""

from pathlib import Path

import pandas as pd

REPORTS_FILE = "reports.csv"
DRUGS_FILE = "report_drugs.csv"
REACTIONS_FILE = "reactions.csv"


def load_data(data_dir: str | Path = "data") -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Read the three CSV files and return (reports, drugs, reactions).

    Requirements (US-01):
    - REPORT_NO is read as text so leading zeros are preserved.
    - A missing file or missing required column raises a clear, specific error.
    """
    raise NotImplementedError("US-01: write failing tests first (Red), then implement.")


def validate_data(reports: pd.DataFrame, drugs: pd.DataFrame, reactions: pd.DataFrame) -> dict:
    """Check the relationships between the three tables and return a summary dict.

    Should report (US-01): row counts per table, duplicate REPORT_ID in reports,
    orphan REPORT_IDs in drugs and reactions, reports with no drugs or no reactions,
    and the REPORT_NO length distribution (warning, not an error).
    """
    raise NotImplementedError("US-01: write failing tests first (Red), then implement.")


def clean_reports(reports: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy of the reports table with the same number of rows.

    Requirements (US-02): parse dates and add a year-month column, set invalid ages
    to missing, add an age-group column, map placeholder values to "Unknown",
    translate seriousness flags (1 = Yes, 2 = No, missing = Unknown), flag reports
    where DATRECEIVED is earlier than DATINTRECEIVED. Must be idempotent and must
    never drop reports.
    """
    raise NotImplementedError("US-02: write failing tests first (Red), then implement.")
