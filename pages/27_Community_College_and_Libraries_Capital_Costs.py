import streamlit as st
from modules.community_college_and_libraries_capital_costs import hcc_captial_costs, hcl_captial_costs

st.header('Projected Howard Community College and Library Capital Costs General Fund Expenditure')

st.markdown('---')

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
year1=2023
years = [year1+x for x in range(18)]

expander = st.expander('Howard Community College')
with expander:
    st.markdown('##### Projected Total Capital Cost')
    st.dataframe(hcc_captial_costs().style.format('$ {:,.2f}'))

st.markdown('---')

expander2 = st.expander('Howard County Library Project')
with expander2:
    st.markdown('##### Projected Total HCL Capital Cost')
    st.dataframe(hcl_captial_costs().style.format('$ {:,.2f}'))