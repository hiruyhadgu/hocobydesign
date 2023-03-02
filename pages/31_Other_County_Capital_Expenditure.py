import pandas as pd
import streamlit as st
from modules.get_tables import general_county_bonds
from modules.other_county_capital_expenditure import other_general_county_bonds_per_capita,\
      other_general_county_bonds_per_capita_employee, other_general_county_expenditure

st.header('General County Bonds')

st.markdown('---')

other_general_county_bonds = general_county_bonds()

per_capita_table = other_general_county_bonds.loc[other_general_county_bonds['Methodology']=='Per Capita']
per_capita_employee_table = other_general_county_bonds.loc[other_general_county_bonds['Methodology']=='Per Capita & Emp.']

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]


expander = st.expander('General County Bonds Projected Using Per-Captia Factors')
with expander:
    select_category = st.selectbox('Select Expense Category',per_capita_table.index.to_list())
    if select_category:
        st.markdown('### General County Bonds Projected Using Per-Captia Factors')
        per_captia_to_display = other_general_county_bonds_per_capita()[0][select_category]
        per_captia_to_display.loc['Total'] = per_captia_to_display[years].sum()
        st.dataframe(per_captia_to_display.style.format('$ {:,.2f}'))

st.markdown('---')

expander1 = st.expander('Total General County Bonds Projected Using Per-Captia Factors')
with expander1:
    st.markdown('### Total General County Bonds Projected Using Per-Captia Factors')
    per_captia_to_display1 = other_general_county_bonds_per_capita()[1]
    per_captia_to_display1.loc['Total'] = per_captia_to_display1.loc['Community Renewal':'Recreation and Parks', years].sum()
    st.dataframe(per_captia_to_display1.style.format('$ {:,.2f}'))

st.markdown('---')

expander4 = st.expander('General County Bonds Projected Using Per-Captia and Employee Factors')
with expander4:
    select_category2 = st.selectbox('Select Expense Category',per_capita_employee_table.index.to_list())
    if select_category2:
        st.markdown('### General County Bonds Projected Using Per Capita & Employee Factors')
        per_captia_employee_to_display = other_general_county_bonds_per_capita_employee()[0][select_category2]
        per_captia_employee_to_display.loc['Total'] = per_captia_employee_to_display[years].sum()
        st.dataframe(per_captia_employee_to_display.style.format('$ {:,.2f}'))

st.markdown('---')

expander5 = st.expander('Total General County Bonds Projected Using Per Capita & Employee Factors')
with expander5:
    st.markdown('### Total Public Facilities Expenses Projected Using Per Capita & Employee Factors')
    per_captia_employee_to_display1 = other_general_county_bonds_per_capita_employee()[1]
    per_captia_employee_to_display1.loc['Total'] = per_captia_employee_to_display1.loc['General County':'Bond Anticipation Notes',years].sum()
    st.dataframe(per_captia_employee_to_display1.style.format('$ {:,.2f}'))



st.markdown('---')

expander6 = st.expander('Total General County Bonds')
with expander6:
    st.markdown('### Total General County Bonds')
    total_to_display = other_general_county_expenditure()
    total_to_display = total_to_display.drop(index='Total')
    total_to_display.loc['Total'] = total_to_display.loc['Community Renewal':'Bond Anticipation Notes', years].sum()
    st.dataframe(total_to_display.style.format('$ {:,.2f}'))

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)