import pandas as pd
import streamlit as st
from modules.get_tables import public_facilities_expense
from modules.public_facilities import public_facilities_per_capita, public_facilities_per_capita_employee, public_facilities_expenditure

st.header('Public Facilities Expenditure')

st.markdown('---')

public_facilities_expense = public_facilities_expense()

per_capita_table = public_facilities_expense.loc[public_facilities_expense['Methodology']=='Per Capita']
per_capita_employee_table = public_facilities_expense.loc[public_facilities_expense['Methodology']=='Per Capita & Emp']

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]


expander = st.expander('Public Facilities Expenses Projected Using Per-Captia Factors')
with expander:
    select_category = st.selectbox('Select Expense Category',per_capita_table.index.to_list())
    if select_category:
        st.markdown('### Public Facilities Expenses Projected Using Per-Captia Factors')
        per_captia_to_display = public_facilities_per_capita()[0][select_category]
        per_captia_to_display.loc['Total'] = per_captia_to_display[years].sum()
        st.dataframe(per_captia_to_display.style.format('$ {:,.2f}'))

st.markdown('---')

expander1 = st.expander('Total Public Facilities Expenses Projected Using Per-Captia Factors')
with expander1:
    st.markdown('### Total Public Facilities Expenses Projected Using Per-Captia Factors')
    per_captia_to_display1 = public_facilities_per_capita()[1]
    per_captia_to_display1.loc['Total'] = per_captia_to_display1.loc['Facilities - Adminstration':'Facilities - Maintenance', years].sum()
    st.dataframe(per_captia_to_display1.style.format('$ {:,.2f}'))

st.markdown('---')

expander4 = st.expander('Total Public Facilities Expenses Projected Using Per-Captia and Employee Factors')
with expander4:
    select_category2 = st.selectbox('Select Expense Category',per_capita_employee_table.index.to_list())
    if select_category2:
        st.markdown('### Total Public Facilities Expenses Projected Using Per Capita & Employee Factors')
        per_captia_employee_to_display = public_facilities_per_capita_employee()[0][select_category2]
        per_captia_employee_to_display.loc['Total'] = per_captia_employee_to_display[years].sum()
        st.dataframe(per_captia_employee_to_display.style.format('$ {:,.2f}'))

st.markdown('---')

expander5 = st.expander('Total Public Facilities Expenses Projected Using Per Capita & Employee Factors')
with expander5:
    st.markdown('### Total Public Facilities Expenses Projected Using Per Capita & Employee Factors')
    per_captia_employee_to_display1 = public_facilities_per_capita_employee()[1]
    per_captia_employee_to_display1.loc['Total'] = per_captia_employee_to_display1.loc["Director's Office":'Soil Conservation District',years].sum()
    st.dataframe(per_captia_employee_to_display1.style.format('$ {:,.2f}'))

st.markdown('---')

expander6 = st.expander('Total Public Facilities Expenses')
with expander6:
    st.markdown('### Total Public Facilities Expenses')
    todisplay = public_facilities_expenditure()
    todisplay = todisplay.drop(index='Total')
    todisplay.loc['Total'] = todisplay.loc['Facilities - Adminstration':'Soil Conservation District',years].sum()
    st.dataframe(todisplay.style.format('$ {:,.2f}'))

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