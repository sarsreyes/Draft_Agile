"""Small shared fixtures. Real CSVs are never used in tests.

Fixture design (5 reports):
  1  Multi-drug, multi-reaction report. 3 drugs (2 suspect, 1 concomitant) and
     3 reaction rows, where "Nausea" appears twice. Any count that returns
     more than 1 for this report is double counting.
  2  One suspect drug, one reaction.
  3  No drugs at all.
  4  12-character REPORT_NO, unknown gender, missing age.
  5  Impossible age (125), and DATRECEIVED earlier than DATINTRECEIVED.
"""

import pandas as pd
import pytest


@pytest.fixture
def reports_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "REPORT_ID": [1, 2, 3, 4, 5],
            "REPORT_NO": ["000000001", "000000002", "000000003", "ABC000000004", "000000005"],
            "VERSION_NO": [0, 0, 1, 0, 0],
            "DATRECEIVED": ["2024-02-10", "2024-03-01", "2025-01-20", "2025-06-15", "2025-11-01"],
            "DATINTRECEIVED": ["2024-02-01", "2024-03-01", "2025-01-15", "2025-06-15", "2025-12-01"],
            "REPORT_TYPE_ENG": ["Spontaneous", "Study", "Study", "Spontaneous", "Published"],
            "GENDER_ENG": ["Female", "Male", "Female", None, "Male"],
            "AGE_Y": [34.0, 67.0, 5.0, None, 125.0],
            "OUTCOME_ENG": ["Recovered/resolved", "Fatal", "Unknown", None, "Recovering/resolving"],
            "SERIOUSNESS_ENG": ["Serious", "Serious", "Not Serious", None, "Serious"],
            "DEATH": [2.0, 1.0, 2.0, None, 2.0],
            "HOSP_REQUIRED": [1.0, 1.0, 2.0, None, 2.0],
        }
    )


@pytest.fixture
def drugs_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "REPORT_DRUG_ID": [10, 11, 12, 13, 14],
            "REPORT_ID": [1, 1, 1, 2, 4],
            "DRUG_PRODUCT_ID": [100.0, 101.0, 102.0, 100.0, 103.0],
            "DRUGNAME": ["DRUG A", "Drug B", "DRUG C", "drug a ", "DRUG D"],
            "DRUGINVOLV_ENG": ["Suspect", "Suspect", "Concomitant", "Suspect", "Suspect"],
        }
    )


@pytest.fixture
def reactions_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "REACTION_ID": [20, 21, 22, 23, 24, 25, 26],
            "REPORT_ID": [1, 1, 1, 2, 3, 4, 5],
            "PT_NAME_ENG": ["Nausea", "Nausea", "Headache", "Nausea", "Death", "Rash", "Headache"],
            "SOC_NAME_ENG": [
                "Gastrointestinal disorders",
                "Gastrointestinal disorders",
                "Nervous system disorders",
                "Gastrointestinal disorders",
                "General disorders and administration site conditions",
                "Skin and subcutaneous tissue disorders",
                "Nervous system disorders",
            ],
            "MEDDRA_VERSION": ["v.29.1"] * 7,
        }
    )


@pytest.fixture
def drugs_df_with_orphan(drugs_df) -> pd.DataFrame:
    """drugs_df plus a row whose REPORT_ID (999) does not exist in reports."""
    orphan = pd.DataFrame(
        {
            "REPORT_DRUG_ID": [99],
            "REPORT_ID": [999],
            "DRUG_PRODUCT_ID": [199.0],
            "DRUGNAME": ["ORPHAN DRUG"],
            "DRUGINVOLV_ENG": ["Suspect"],
        }
    )
    return pd.concat([drugs_df, orphan], ignore_index=True)


@pytest.fixture
def reactions_df_with_orphan(reactions_df) -> pd.DataFrame:
    """reactions_df plus a row whose REPORT_ID (999) does not exist in reports."""
    orphan = pd.DataFrame(
        {
            "REACTION_ID": [99],
            "REPORT_ID": [999],
            "PT_NAME_ENG": ["Orphan reaction"],
            "SOC_NAME_ENG": ["Unknown"],
            "MEDDRA_VERSION": ["v.29.1"],
        }
    )
    return pd.concat([reactions_df, orphan], ignore_index=True)
