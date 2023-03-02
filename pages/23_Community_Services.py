import pandas as pd
import streamlit as st
from modules.get_tables import community_services_expense
from modules.community_services import community_services_per_capita

st.header('Community Services Expenditure')

st.markdown('---')

community_services = community_services_expense()

per_capita_table = community_services.loc[community_services['Methodology']=='Per Capita']

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]


expander = st.expander('Community Services Expenditure Projected Using Per-Captia Factors')
with expander:
    select_category = st.selectbox('Select Expense Category',per_capita_table.index.to_list())
    if select_category:
        st.markdown('### Public Facilities Expenses Projected Using Per-Captia Factors')
        per_captia_to_display = community_services_per_capita()[0][select_category]
        per_captia_to_display.loc['Total'] = per_captia_to_display[years].sum()
        st.dataframe(per_captia_to_display.style.format('$ {:,.2f}'))

st.markdown('---')

expander1 = st.expander('Total Community Services Expenditure Projected Using Per-Captia Factors')
with expander1:
    st.markdown('### Total Community Services Expenditure Projected Using Per-Captia Factors')
    per_captia_to_display1 = community_services_per_capita()[1]
    per_captia_to_display1.loc['Total'] = per_captia_to_display1.loc['Depart. of Rec. and Parks - General Fund':'Community Service Partnerships', years].sum()
    st.dataframe(per_captia_to_display1.style.format('$ {:,.2f}'))