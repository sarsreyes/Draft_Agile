"""Streamlit entry point. UI only: no business logic belongs here.

Run with:  streamlit run app.py
Each feature lives in its own file under pages/ so that team members do not
edit the same file. Streamlit builds the sidebar navigation from that folder.
"""

import streamlit as st

st.set_page_config(page_title="Canada Vigilance Analytics", layout="wide")

st.title("Canada Vigilance Adverse Reaction Analytics")
st.info(
    "These are reports of suspected adverse reactions (2024-2025). Counts show "
    "reporting patterns only. They do not show that a drug caused a reaction and "
    "are not incidence rates."
)
st.write("Pick a page from the sidebar. Pages are added as user stories are completed.")
# TODO (US-03, task 3.4): load the data once with st.cache_data and add the Overview page.
