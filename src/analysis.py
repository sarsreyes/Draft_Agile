"""Analytical summaries that return DataFrames (no Streamlit, no plotting).

All report counts are distinct REPORT_ID counts.

Stories: US-04 (top reactions), US-05 (reports over time), US-06 (seriousness and outcome).
"""

import pandas as pd


def top_reactions(reactions: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """Return the n most frequently reported reaction terms (PT_NAME_ENG).

    Columns: reaction term and number of distinct reports. A term repeated within
    one report counts once. Ties are sorted by count (descending) then name.
    """
    raise NotImplementedError("US-04: write failing tests first (Red), then implement.")


def monthly_report_counts(reports: pd.DataFrame) -> pd.DataFrame:
    """Return distinct reports per month (DATINTRECEIVED), all 24 months of
    2024-2025 included, with zero for months that have no reports."""
    raise NotImplementedError("US-05: implement and test.")


def seriousness_breakdown(reports: pd.DataFrame) -> pd.DataFrame:
    """Return distinct report counts and percentages by SERIOUSNESS_ENG,
    with missing values shown as "Unknown"."""
    raise NotImplementedError("US-06: implement and test.")


def outcome_breakdown(reports: pd.DataFrame) -> pd.DataFrame:
    """Return distinct report counts and percentages by OUTCOME_ENG,
    with missing values shown as "Unknown"."""
    raise NotImplementedError("US-06: implement and test.")
