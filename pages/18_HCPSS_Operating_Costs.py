import streamlit as st
from modules.hcpss_operating_costs import school_operating_budget, school_projected_operating_budget_hocobydesign_method,\
    school_projected_operating_budget_total_funding_method, hcpss_opeb_trust_fund

st.header(':school: Projected HCPSS General Fund Expenditure')

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
year1=2023
years = [year1+x for x in range(18)]

st.markdown('---')

expander = st.expander('Historical Operating Budget and Total Student Enrollment')
with expander:
    st.dataframe(school_operating_budget().style.format('$ {:,.2f}'))

st.markdown('---')

expander1 = st.expander('Projected Total Operating Cost HoCoByDesign Method')
with expander1:
    st.dataframe(school_projected_operating_budget_hocobydesign_method().style.format('$ {:,.2f}'))


st.markdown('---')

expander2 = st.expander('Projected Total Operating Cost Total Funding Method')
with expander2:
    st.dataframe(school_projected_operating_budget_total_funding_method().style.format('$ {:,.2f}'))

st.markdown('---')

expander3 = st.expander('Projected Total HCPSS OPEB Trustfund')
with expander3:
    st.markdown('##### Projected Total HCPSS OPEB Trustfund')
    st.dataframe(hcpss_opeb_trust_fund().style.format('$ {:,.2f}'))
    # if selected == 'Total School Funding':
    #     st.dataframe(school_projected_operating_budget(selected))
