import streamlit as st
from modules.student_generation_rate import student_generation_rate

st.header('Projected Student Generation Rate')

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
year1=2023
years = [year1+x for x in range(18)]

st.markdown('---')

expander1 = st.expander('Projected Elementary School Student Generation Rate by Planning Area')
with expander1:
    select_region = st.selectbox('Select Planning Area',regions, key=1)
    if select_region:
        st.markdown('##### Elementary School Student Generation Rate')
        st.dataframe(student_generation_rate()[0][regions[regions.index(select_region)]].style.format(precision=2))
   
st.markdown('---')

expander2 = st.expander('Projected Middle School Student Generation Rate by Planning Area')
with expander2:
    select_region1 = st.selectbox('Select Planning Area',regions, key=2)
    if select_region:
        st.markdown('##### Middle School Generation Rate')
        st.dataframe(student_generation_rate()[1][regions[regions.index(select_region1)]].style.format(precision=2))


st.markdown('---')

expander3 = st.expander('Projected High School Student Generation Rate by Planning Area')
with expander3:
    select_region2 = st.selectbox('Select Planning Area',regions, key=3)
    if select_region:
        st.markdown('##### High School Generation Rate')
        st.dataframe(student_generation_rate()[2][regions[regions.index(select_region2)]].style.format(precision=2))

   
st.markdown('---')

expander4 = st.expander('Projected Total Student Generation Rate by Planning Area')
with expander4:
    st.markdown('##### Total School Generation Rate')
    st.dataframe(student_generation_rate()[3])
