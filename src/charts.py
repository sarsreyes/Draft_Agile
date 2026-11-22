"""Functions that turn analysis DataFrames into Plotly figures.

Charts never call Streamlit; the pages display the returned figure.

Stories: US-04, US-05, US-06.
"""

import pandas as pd


def bar_chart(data: pd.DataFrame, x: str, y: str, title: str = "", horizontal: bool = True):
    """Return a bar chart figure (horizontal by default)."""
    raise NotImplementedError("US-04: implement and test.")


def line_chart(data: pd.DataFrame, x: str, y: str, title: str = ""):
    """Return a line chart figure with hover values."""
    raise NotImplementedError("US-05: implement and test.")
