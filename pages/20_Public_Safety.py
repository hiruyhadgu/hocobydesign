import pandas as pd
import streamlit as st
from modules.public_safety import per_capita_trip, project_public_safety


regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

st.header(':police_car: Projected Public Safety General Fund Expenditure')

st.markdown('---')

expander = st.expander('Projected Non Residential Trips')
with expander:
    select_region = st.selectbox('Select Planning Area',regions, key=1)
    if select_region:
        st.markdown('##### Projected Non Residential Trips by Planning Area')
        st.dataframe(per_capita_trip()[0][regions[regions.index(select_region)]].style.format('$ {:,.2f}'))
    
    st.markdown('---')

    st.markdown('##### Projected Non Residential Trips Total')
    st.dataframe(per_capita_trip()[1].style.format('$ {:,.2f}'))

st.markdown('---')

expander1 = st.expander('Projected Public Safety Expenditure')
with expander1:
    select_method = st.selectbox('Select Methodology',['Per Capita', 'Per Capita and Trips'], key=2)
    if select_method == 'Per Capita':
        st.markdown(f'##### Projected {select_method} Expenses')
        st.dataframe(project_public_safety()[0][select_method].style.format('$ {:,.2f}'))
    elif select_method == 'Per Capita and Trips':
        select_demand_unit = st.selectbox('Select Demand Unit',['Population', 'Non Residential Trips'], key=3)
        if select_demand_unit:
            st.markdown(f'##### Projected {select_demand_unit} Demand Total')
            st.dataframe(project_public_safety()[0][select_method][select_demand_unit].style.format('$ {:,.2f}'))

st.markdown('---')

expander2 = st.expander('Projected Total Public Safety Expenditure')
with expander2:
    st.dataframe(project_public_safety()[1].style.format('$ {:,.2f}'))
