import pandas as pd
import streamlit as st
from modules.fire_and_rescue import fire_rescue_factors, per_capita_trip_fire_rescue, project_fire_rescue


regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]


st.header(':fire_engine: :ambulance: Projected Fire and Rescue General Fund Expenditure')

st.markdown('---')

expander = st.expander('Projected Non Residential Trips')
with expander:
    select_region = st.selectbox('Select Planning Area',regions, key=1)
    if select_region:
        st.markdown('##### Projected Non Residential Trips by Planning Area')
        st.dataframe(per_capita_trip_fire_rescue()[0][regions[regions.index(select_region)]].style.format('$ {:,.2f}'))
    
    st.markdown('---')

    st.markdown('##### Projected Non Residential Trips Total')
    st.dataframe(per_capita_trip_fire_rescue()[1].style.format('$ {:,.2f}'))

st.markdown('---')

expander1 = st.expander('Projected Fire and Rescue Expenditure')
with expander1:
    select_demand_unit = st.selectbox('Select Demand Unit',['Population', 'Non Residential Trips'], key=3)
    if select_demand_unit:
        st.markdown(f'##### Projected {select_demand_unit} Demand Total')
        st.dataframe(project_fire_rescue()[0][select_demand_unit].style.format('$ {:,.2f}'))

st.markdown('---')

expander1 = st.expander('Projected Total Fire and Rescue Expenditure')
with expander1:
    st.dataframe(project_fire_rescue()[1].style.format('$ {:,.2f}'))