import streamlit as st
from modules.non_departmental_services import non_departmental_per_capita_employee

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

st.header('Non-Departmental Services Expenditure')

st.markdown('---')

expander = st.expander('Projected Non-Departmental Services Expenditure by Planning Area')
with expander:
    select_region3 = st.selectbox('**Select Planning Area**',regions)
    if select_region3:
        st.markdown('#### Road Expenditure by Planning Area')
        st.dataframe(non_departmental_per_capita_employee()[0][regions[regions.index(select_region3)]].style.format('$ {:,.2f}'))

st.markdown('---')

expander1 = st.expander('Total Non-Departmental Services Expenditure')
with expander1:
        
    st.markdown('#### Total Non Departmental Services Expenditure')
    todisplay = non_departmental_per_capita_employee()[1]
    todisplay.loc['Total'] = todisplay.loc['Columbia':'South East', years].sum()
    st.dataframe(todisplay.style.format('$ {:,.2f}'))