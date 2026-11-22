# Personal practice workspace

This private repository is an independent snapshot of the application's main branch. It is not the team's working repository. Only this repository is modified during practice.

## What was copied

- All 21 files from the source main snapshot (tree 289fd7a0588444e18173721d4e5f9f30362afa96).
- 38 issue descriptions and baseline open/closed states, with no assignees.
- Issue references rewritten to this repository.
- Source commit history, reviews, notifications, and historical TDD evidence were not copied. Baseline states are not proof of work completed here.
- Existing team wording inside the baseline README is copied documentation, not an invitation or access grant.

## Board setup still required

A GitHub Project is separate from a code repository. No personal Project has been created or linked by this copy. The connector cannot copy Project 138, read its custom fields, or recreate parent/sub-issue relationships.

To reproduce the course layout in a personal, private Project:
1. Create or copy a Project owned by sarsreyes, named Draft Agile.
2. Keep it private and grant no collaborators access.
3. Link only sarsreyes/Draft_Agile and set it as the default repository.
4. Use the required views: Backlog Table, Current Sprint, Tasks by Story.
5. Set up Status (To Do, In Progress, Done), Sprint, Story Points, Item Type (User Story, Task, Refactor), and TDD.
6. Add the copied issues and recreate parent/sub-issue relationships using the mapping below.
7. Verify each field, filter, sprint date, and view against Project 138 before calling the board identical. Do not add original issues to the practice Project.

The above layout is based on the supplied assignment, not a live verified export of Project 138. Burn-up charts and activity history cannot be reproduced by copying current issue descriptions.

## Start the first practice

Original task 26 corresponds to draft issue 23; original US-04 issue 25 corresponds to draft issue 22.
Review the proposed tests before creating a feature commit. Preserve a genuine failing-test run before implementation. Do not use baseline history as new TDD evidence.

Run setup and tests using the repository README. The baseline contains unimplemented functions; failures are expected until the relevant tasks are implemented.

If you want the PR to be created directly by your GitHub session, open it yourself. A PR created through the connector can show the connector attribution even when commit author and committer are sarsreyes.

## Issue mapping

| Original issue number | Draft issue | Title | Baseline state |
|---|---|---|---|
| 1 | [#1](https://github.com/sarsreyes/Draft_Agile/issues/1) | Document the shared user story workflow and verification prompt | closed |
| 5 | [#2](https://github.com/sarsreyes/Draft_Agile/issues/2) | US-01: Load and validate the three datasets | open |
| 6 | [#3](https://github.com/sarsreyes/Draft_Agile/issues/3) | US-01 T1.1: Create shared test fixtures in conftest.py | closed |
| 7 | [#4](https://github.com/sarsreyes/Draft_Agile/issues/4) | US-01 T1.2 [Red]: Failing tests for load_data | open |
| 8 | [#5](https://github.com/sarsreyes/Draft_Agile/issues/5) | US-01 T1.3 [Green]: Implement load_data | open |
| 9 | [#6](https://github.com/sarsreyes/Draft_Agile/issues/6) | US-01 T1.4 [Red]: Failing tests for validate_data | closed |
| 10 | [#7](https://github.com/sarsreyes/Draft_Agile/issues/7) | US-01 T1.5 [Green + Refactor]: Implement validate_data and tidy loader | open |
| 11 | [#8](https://github.com/sarsreyes/Draft_Agile/issues/8) | US-01 T1.6: Write README setup and test instructions | open |
| 12 | [#9](https://github.com/sarsreyes/Draft_Agile/issues/9) | US-02: Clean and standardize data | open |
| 13 | [#10](https://github.com/sarsreyes/Draft_Agile/issues/10) | US-02 T2.1 [Red]: Failing tests for date parsing and DATRECEIVED flag | open |
| 14 | [#11](https://github.com/sarsreyes/Draft_Agile/issues/11) | US-02 T2.2 [Green]: Implement date cleaning and flag | open |
| 15 | [#12](https://github.com/sarsreyes/Draft_Agile/issues/12) | US-02 T2.3 [Red + Green]: Age valid range, age groups, and Unknown group | open |
| 16 | [#13](https://github.com/sarsreyes/Draft_Agile/issues/13) | US-02 T2.4 [Red + Green]: Placeholders to Unknown and seriousness flags | open |
| 17 | [#14](https://github.com/sarsreyes/Draft_Agile/issues/14) | US-02 T2.5 [Red]: Tests that cleaning keeps all reports and is idempotent | open |
| 18 | [#15](https://github.com/sarsreyes/Draft_Agile/issues/15) | US-02 T2.6 [Refactor]: Combine into clean_reports pipeline and document rules | open |
| 19 | [#16](https://github.com/sarsreyes/Draft_Agile/issues/16) | US-03: Headline KPIs and overview page | open |
| 20 | [#17](https://github.com/sarsreyes/Draft_Agile/issues/17) | US-03 T3.1 [Red]: Failing tests for kpi_summary and report_type_counts | open |
| 21 | [#18](https://github.com/sarsreyes/Draft_Agile/issues/18) | US-03 T3.2 [Green]: Implement kpi_summary and report_type_counts | open |
| 22 | [#19](https://github.com/sarsreyes/Draft_Agile/issues/19) | US-03 T3.3 [Refactor]: Extract shared distinct-report count helper | open |
| 23 | [#20](https://github.com/sarsreyes/Draft_Agile/issues/20) | US-03 T3.4: Build Streamlit skeleton and Overview page | open |
| 24 | [#21](https://github.com/sarsreyes/Draft_Agile/issues/21) | US-03 T3.5: Clean-clone run test and Sprint Review demo script | open |
| 25 | [#22](https://github.com/sarsreyes/Draft_Agile/issues/22) | US-04: Top reported reactions | open |
| 26 | [#23](https://github.com/sarsreyes/Draft_Agile/issues/23) | US-04 T4.1 [Red]: Failing tests for top_reactions | open |
| 27 | [#24](https://github.com/sarsreyes/Draft_Agile/issues/24) | US-04 T4.2 [Green]: Implement top_reactions | open |
| 28 | [#25](https://github.com/sarsreyes/Draft_Agile/issues/25) | US-04 T4.3 [Refactor]: Use shared helper and add docstring | open |
| 29 | [#26](https://github.com/sarsreyes/Draft_Agile/issues/26) | US-04 T4.4: Bar chart function in charts.py | open |
| 30 | [#27](https://github.com/sarsreyes/Draft_Agile/issues/27) | US-04 T4.5: Streamlit page with N selector | open |
| 31 | [#28](https://github.com/sarsreyes/Draft_Agile/issues/28) | US-05: Reports over time | open |
| 32 | [#29](https://github.com/sarsreyes/Draft_Agile/issues/29) | US-05 T5.1: Implement monthly_report_counts | open |
| 33 | [#30](https://github.com/sarsreyes/Draft_Agile/issues/30) | US-05 T5.2: Write tests for monthly_report_counts | open |
| 34 | [#31](https://github.com/sarsreyes/Draft_Agile/issues/31) | US-05 T5.3: Line chart function in charts.py | open |
| 35 | [#32](https://github.com/sarsreyes/Draft_Agile/issues/32) | US-05 T5.4: Streamlit Reports over time page with caption | open |
| 36 | [#33](https://github.com/sarsreyes/Draft_Agile/issues/33) | US-06: Seriousness and outcome breakdown | open |
| 37 | [#34](https://github.com/sarsreyes/Draft_Agile/issues/34) | US-06 T6.1: Implement seriousness_breakdown and outcome_breakdown | open |
| 38 | [#35](https://github.com/sarsreyes/Draft_Agile/issues/35) | US-06 T6.2: Seriousness criteria counts and multiple-criteria note | open |
| 39 | [#36](https://github.com/sarsreyes/Draft_Agile/issues/36) | US-06 T6.3: Write tests for seriousness and outcome functions | open |
| 40 | [#37](https://github.com/sarsreyes/Draft_Agile/issues/37) | US-06 T6.4: Bar chart functions for both views | open |
| 41 | [#38](https://github.com/sarsreyes/Draft_Agile/issues/38) | US-06 T6.5: Streamlit page with seriousness and outcome toggle | open |
