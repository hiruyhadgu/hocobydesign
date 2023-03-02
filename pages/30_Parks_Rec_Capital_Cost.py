import streamlit as st
from modules.parks_and_rec_capital_cost import parks_recs_per_capita

st.header('Projected Parks and Recreation Capital Cost General Expenditure')

st.markdown('---')

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
year1=2023
years = [year1+x for x in range(18)]

expander = st.expander('Parks and Recreation')
with expander:
    st.markdown('##### Parks and Recreation Projected Capital Cost')
    st.dataframe(parks_recs_per_capita().style.format('$ {:,.2f}'))