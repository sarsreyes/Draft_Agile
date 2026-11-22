"""Headline counts and KPIs.

Counting rule for the whole project: report counts use the number of DISTINCT
REPORT_ID values, never the number of joined rows.

Story: US-03.
"""

import pandas as pd


def kpi_summary(reports: pd.DataFrame, drugs: pd.DataFrame, reactions: pd.DataFrame) -> dict:
    """Return headline numbers: distinct reports, distinct drug products,
    distinct reaction terms (PT) and the date range covered."""
    raise NotImplementedError("US-03: write failing tests first (Red), then implement.")


def report_type_counts(reports: pd.DataFrame) -> pd.DataFrame:
    """Return distinct report counts per REPORT_TYPE_ENG (for example Study vs Spontaneous)."""
    raise NotImplementedError("US-03: write failing tests first (Red), then implement.")
