import streamlit as st
import pandas as pd
import sqlite3 as db
from modules.total_expenditure_projections import compiled_operating_expenditure_projections, compiled_capital_expenditure_projections
from PIL import Image
import plotly.express as px


st.header('HoCoByDesign Total Expenditure Projections')
st.markdown('---')

st.markdown("""
The following table summarizes the County's projected operating expenditure. The operating expenditure scenarios compares two scenarios.
""")

case = ['County Funding Only', 'County and State Funding']
select_case = st.selectbox('**Select a projection approach to read the description of each approach:**',case, key=1)

fiscal_approach_description = [f"""
**{select_case}:** This case reproduces the County's results, by separating total school operating and capital expenditure into, State, County,
and Other. **Only** the expenditure assumed to be financed by County funds is included in the operating and capital costs. It also assumes that
50% of the school capital expenditure and 100% of the road capital expenditure are financed by debt.
""",
f"""
**{select_case}:** This case differs from the **County Funding** approach by adding the expenses associated with State funding of
the school operating budget. It is more realistic as the obligation to fund the schools falls on the County and not the State. Roads are also
financed by debt.
"""
]

if select_case:
    display = compiled_operating_expenditure_projections()[case[case.index(select_case)]]
    st.markdown(fiscal_approach_description[case.index(select_case)])
    st.dataframe(display.style.format('$ {:,.2f}'))

    fig = px.line(display.T, width=700, height=500,\
            labels=dict(index="Year", value="Annual Operating Expenditure ($)"))
    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ))

    st.plotly_chart(fig)

st.markdown("---")

st.markdown("""
The following table summarizes the County's projected capital expenditure. The capital expenditure scenarios compare three scenarios.
""")
            
case1 = ['HoCoByDesign Approach 50% PAYGO and 50% Debt', '100% PAYGO using county\'s per-student costs & roads',\
                                              '100% PAYGO using updated per-student costs & roads']

select_case1 = st.selectbox('**Select a projection approach to read the description of each approach:**',case1, key=2)

fiscal_approach_description1 = [
f"""
**{select_case1}:** This case differs from the **County Funding** approach by assuming 100% of the capital expenditure for schools 
and roads is funded by PAYGO. The per-student costs for school construction are the County's numbers. 

**Note** that this approach uses the County's funding approach for school operating costs.
""",
f"""
**{select_case1}:** This assumes that 100% of the capital expenditure for schools and roads is funded by PAYGO. However, the per-student school
construction cost used in this approach is much higher as the County's approach underestimates this cost significantly. The school operating
cost remains unchanged from the **County Funding** approach.

""",
f"""
**{select_case1}:** The fiscally conservative approach is the most responsible approach. First, it takes into account the County **and** State funding
needed to operate the school system. Second, it uses 100% PAYGO to fund road and school construction. Third, the per-student school construction cost
is much more accurate than used by the county.

"""
]
if select_case1:
    display1 = compiled_capital_expenditure_projections()[case1[case1.index(select_case1)]]
    st.markdown(fiscal_approach_description1[case1.index(select_case1)])
    st.dataframe(display1.style.format('$ {:,.2f}'))

    fig1 = px.line(display1.T, width=700, height=500,\
               labels=dict(index="Year", value="Annual Capital Expenditure ($)"))
    fig1.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ))
    st.plotly_chart(fig1)



# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)