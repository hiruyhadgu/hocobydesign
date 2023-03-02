import streamlit as st
from modules.road_expenditure import road_expenditure_per_capita_employee

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

st.header('Projected Road Capital Expenditure')

st.markdown('---')

expander = st.expander('Projected Road Capital Expenditure by Planning Area')
with expander:
    select_region3 = st.selectbox('Select Planning Area',regions)
    if select_region3:
        st.markdown('#### Road Expenditure Capital by Planning Area')
        st.dataframe(road_expenditure_per_capita_employee()[0][regions[regions.index(select_region3)]].style.format('$ {:,.2f}'))

st.markdown('---')

expander1 = st.expander('Total Road Capital Expenditure')
with expander1:
        
    st.markdown('#### Total Road Capital Expenditure')
    todisplay = road_expenditure_per_capita_employee()[1]
    todisplay.loc['Total'] = todisplay.loc['Columbia':'South East', years].sum()
    st.dataframe(todisplay.style.format('$ {:,.2f}'))

st.markdown('---')

expander2 = st.expander('Annual Debt Service for Road Capital Expenditure')
with expander2:
    todisplay1 = road_expenditure_per_capita_employee()[2]
    todisplay1.loc['Total'] = todisplay1.loc['Columbia':'South East', years].sum()
    st.dataframe(todisplay1.style.format('$ {:,.2f}'))