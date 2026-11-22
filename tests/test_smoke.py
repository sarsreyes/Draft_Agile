"""Checks that the project skeleton is wired correctly. Safe to keep for the whole project."""


def test_modules_import():
    import src.analysis  # noqa: F401
    import src.charts  # noqa: F401
    import src.data_loader  # noqa: F401
    import src.metrics  # noqa: F401


def test_fixtures_have_expected_shape(reports_df, drugs_df, reactions_df):
    # Report 1 has several drugs and reactions, so a naive join inflates counts.
    assert reports_df["REPORT_ID"].nunique() == 5
    assert (drugs_df["REPORT_ID"] == 1).sum() == 3
    assert (reactions_df["REPORT_ID"] == 1).sum() == 3
    joined = reports_df.merge(drugs_df, on="REPORT_ID").merge(reactions_df, on="REPORT_ID")
    assert len(joined) > reports_df["REPORT_ID"].nunique()
