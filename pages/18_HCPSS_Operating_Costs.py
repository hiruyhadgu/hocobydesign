import streamlit as st
from modules.hcpss_operating_costs import school_operating_budget, school_projected_operating_budget, hcpss_opeb_trust_fund

st.header('Projected HCPSS General Fund Expenditure')

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
year1=2023
years = [year1+x for x in range(18)]

hcpss_selected = st.checkbox('Use Total Funding Method')
if hcpss_selected==False:
    method = 'hocobydesign'
else:
    method = 'totalfundingmethod'

st.markdown('---')

expander = st.expander('Historical Operating Budget and Total Student Enrollment')
with expander:
    st.dataframe(school_operating_budget().style.format('$ {:,.2f}'))

st.markdown('---')

expander5 = st.expander('Projected Total Operating Cost')
with expander5:
    st.dataframe(school_projected_operating_budget(method).style.format('$ {:,.2f}'))

st.markdown('---')

expander6 = st.expander('Projected Total HCPSS OPEB Trustfund')
with expander6:
    st.markdown('##### Projected Total HCPSS OPEB Trustfund')
    st.dataframe(hcpss_opeb_trust_fund().style.format('$ {:,.2f}'))
    # if selected == 'Total School Funding':
    #     st.dataframe(school_projected_operating_budget(selected))
