import streamlit as st
from modules.community_college_and_libraries_operating_costs import hcc_expenditure, hcc_opeb_trust_fund,\
     hcl_expenditure, hcl_opeb_trust_fund

st.header('Projected Howard Community College and Library Systems General Fund Expenditure')

st.markdown('---')

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
year1=2023
years = [year1+x for x in range(18)]

expander = st.expander('Howard Community College')
with expander:
    st.markdown('##### Projected Total HCC Operating Cost')
    st.dataframe(hcc_expenditure().style.format('$ {:,.2f}'))
    st.markdown('---')
    st.markdown('##### Projected Total HCC OPEB Trustfund')
    st.dataframe(hcc_opeb_trust_fund().style.format('$ {:,.2f}'))

st.markdown('---')

expander2 = st.expander('Howard County Library Project')
with expander2:
    st.markdown('##### Projected Total HCL Operating Cost')
    st.dataframe(hcl_expenditure().style.format('$ {:,.2f}'))
    st.markdown('---')
    st.markdown('##### Projected Total HCL OPEB Trustfund')
    st.dataframe(hcl_opeb_trust_fund().style.format('$ {:,.2f}'))