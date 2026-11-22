"""US-04 T4.1: Red tests for top_reactions, before implementation.

Return contract: PT_NAME_ENG and report_count columns; count descending,
then reaction name ascending. Tests use synthetic fixtures, never real CSVs.
"""

import pandas as pd
from pandas.testing import assert_frame_equal

from src.analysis import top_reactions


def test_counts_distinct_reports_per_reaction(reactions_df):
    result = top_reactions(reactions_df)
    assert dict(zip(result["PT_NAME_ENG"], result["report_count"])) == {
        "Headache": 2, "Nausea": 2, "Death": 1, "Rash": 1
    }


def test_repeated_reaction_within_one_report_counts_once(reactions_df):
    one_report = reactions_df.loc[reactions_df["REPORT_ID"] == 1]
    result = top_reactions(one_report)
    assert dict(zip(result["PT_NAME_ENG"], result["report_count"])) == {
        "Headache": 1, "Nausea": 1
    }


def test_sorts_by_count_descending_then_name_ascending(reactions_df):
    shuffled = reactions_df.sample(frac=1, random_state=42)
    result = top_reactions(shuffled)
    assert result["PT_NAME_ENG"].tolist() == ["Headache", "Nausea", "Death", "Rash"]
    assert result["report_count"].tolist() == [2, 2, 1, 1]


def test_n_limits_results_after_ranking(reactions_df):
    result = top_reactions(reactions_df, n=2)
    assert result["PT_NAME_ENG"].tolist() == ["Headache", "Nausea"]
    assert result["report_count"].tolist() == [2, 2]


def test_n_larger_than_available_terms_returns_all_terms(reactions_df):
    result = top_reactions(reactions_df, n=25)
    assert len(result) == 4


def test_default_n_returns_ten_results():
    reactions = pd.DataFrame({
        "REPORT_ID": list(range(12)),
        "PT_NAME_ENG": [f"Reaction {i:02d}" for i in range(12)],
    })
    result = top_reactions(reactions)
    assert result["PT_NAME_ENG"].tolist() == [f"Reaction {i:02d}" for i in range(10)]


def test_empty_input_returns_empty_dataframe_with_result_columns(reactions_df):
    result = top_reactions(reactions_df.iloc[:0].copy())
    assert isinstance(result, pd.DataFrame)
    assert result.empty
    assert list(result.columns) == ["PT_NAME_ENG", "report_count"]


def test_does_not_modify_input(reactions_df):
    before = reactions_df.copy(deep=True)
    top_reactions(reactions_df)
    assert_frame_equal(reactions_df, before)
