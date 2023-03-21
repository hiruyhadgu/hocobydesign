import pandas as pd
import streamlit as st
from modules.fire_stations import fire_stations_per_capita_employee


st.header('Projected Fire Stations Capital Expenditure')

st.markdown('---')

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]
fire_station_cost_for_each_region = fire_stations_per_capita_employee()[0]
total_fire_station_cost = fire_stations_per_capita_employee()[1]

expander = st.expander('Projected Fire Stations Cost')
with expander:
    select_region = st.selectbox('**Select Planning Area**',regions, key=1)
    if select_region:
        st.markdown('##### Projected Fire Stations Cost by Planning Area')
        st.dataframe(fire_station_cost_for_each_region[regions[regions.index(select_region)]].style.format('$ {:,.2f}'))
    
    st.markdown('---')
    
    st.markdown('##### Projected Total Fire Stations Cost')
    st.dataframe(total_fire_station_cost.style.format('$ {:,.2f}'))