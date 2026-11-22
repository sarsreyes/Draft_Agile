"""T1.4 (Red): tests for validate_data. Written before the implementation exists."""

import pandas as pd

from src.data_loader import validate_data


def test_row_counts_per_table(reports_df, drugs_df, reactions_df):
    result = validate_data(reports_df, drugs_df, reactions_df)
    assert result["row_counts"] == {"reports": 5, "drugs": 5, "reactions": 7}


def test_clean_fixtures_have_no_duplicates_or_orphans(reports_df, drugs_df, reactions_df):
    result = validate_data(reports_df, drugs_df, reactions_df)
    assert result["duplicate_report_ids"] == 0
    assert result["orphan_drug_report_ids"] == 0
    assert result["orphan_reaction_report_ids"] == 0


def test_duplicate_report_ids_are_counted(reports_df, drugs_df, reactions_df):
    duplicated = reports_df.loc[[0, 0, 1, 2, 3, 4]]  # report 1 appears twice
    result = validate_data(duplicated, drugs_df, reactions_df)
    assert result["duplicate_report_ids"] == 1


def test_orphan_ids_are_counted(reports_df, drugs_df_with_orphan, reactions_df_with_orphan):
    result = validate_data(reports_df, drugs_df_with_orphan, reactions_df_with_orphan)
    assert result["orphan_drug_report_ids"] == 1
    assert result["orphan_reaction_report_ids"] == 1


def test_reports_without_drugs_or_reactions(reports_df, drugs_df, reactions_df):
    reactions_without_report_5 = reactions_df[reactions_df["REPORT_ID"] != 5]
    result = validate_data(reports_df, drugs_df, reactions_without_report_5)
    assert result["reports_without_drugs"] == 2      # reports 3 and 5
    assert result["reports_without_reactions"] == 1  # report 5


def test_report_no_length_warning(reports_df, drugs_df, reactions_df):
    result = validate_data(reports_df, drugs_df, reactions_df)
    assert result["report_no_lengths"] == {9: 4, 12: 1}
    assert any("REPORT_NO" in warning for warning in result["warnings"])


def test_clean_input_gives_no_warnings(reports_df, drugs_df, reactions_df):
    reports = reports_df.assign(
        REPORT_NO=["000000001", "000000002", "000000003", "000000004", "000000005"]
    )
    # Give reports 3 and 5 a drug so no report is missing drugs.
    extra_drugs = drugs_df.iloc[[0, 0]].assign(REPORT_ID=[3, 5])
    drugs = pd.concat([drugs_df, extra_drugs], ignore_index=True)
    result = validate_data(reports, drugs, reactions_df)
    assert result["warnings"] == []


def test_validate_does_not_modify_its_inputs(reports_df, drugs_df, reactions_df):
    before = (reports_df.copy(), drugs_df.copy(), reactions_df.copy())
    validate_data(reports_df, drugs_df, reactions_df)
    assert reports_df.equals(before[0])
    assert drugs_df.equals(before[1])
    assert reactions_df.equals(before[2])