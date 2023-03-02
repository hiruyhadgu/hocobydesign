import pandas as pd
import streamlit as st
from modules.get_tables import other_govt_expenses
from modules.other_general_government import other_govt_expenses_per_capita, other_govt_expenses_per_capita_employee, other_general_govt_total

st.header('Other General Government Expenditure')

st.markdown('---')

other_govt_expenses1 = other_govt_expenses()

per_capita_table = other_govt_expenses1.loc[other_govt_expenses1['Methodology']=='Per Capita']
per_capita_employee_table = other_govt_expenses1.loc[other_govt_expenses1['Methodology']=='Per Capita & Emp']

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]


expander = st.expander('Other General Government Expenditure Projected Using Per-Captia Factors')
with expander:
    select_category = st.selectbox('Select Expense Category',per_capita_table.index.to_list())
    if select_category:
        st.markdown('### Other General Government Expenditure Projected Using Per-Captia Factors')
        per_captia_to_display = other_govt_expenses_per_capita()[0][select_category]
        per_captia_to_display.loc['Total'] = per_captia_to_display[years].sum()
        st.dataframe(per_captia_to_display.style.format('$ {:,.2f}'))

st.markdown('---')

expander1 = st.expander('Total General Government Expenditure Projected Using Per-Captia Factors')
with expander1:
    st.markdown('### Total General Government Expenditure Projected Using Per-Captia Factors')
    per_captia_to_display1 = other_govt_expenses_per_capita()[1]
    per_captia_to_display1.loc['Total'] = per_captia_to_display1.loc['Circuit Court':'Cable Administration', years].sum()
    st.dataframe(per_captia_to_display1.style.format('$ {:,.2f}'))

st.markdown('---')

expander4 = st.expander('Other General Government Expenditure Projected Using Per-Captia and Employee Factors')
with expander4:
    select_category2 = st.selectbox('Select Expense Category',per_capita_employee_table.index.to_list())
    if select_category2:
        st.markdown('### Other General Government Expenditure Projected Using Per Capita & Employee Factors')
        per_captia_employee_to_display = other_govt_expenses_per_capita_employee()[0][select_category2]
        per_captia_employee_to_display.loc['Total'] = per_captia_employee_to_display[years].sum()
        st.dataframe(per_captia_employee_to_display.style.format('$ {:,.2f}'))

st.markdown('---')

expander5 = st.expander('Total Other General Government Expenditure Projected Using Per Capita & Employee Factors')
with expander5:
    st.markdown('### Total Other General Government Expenditure Projected Using Per Capita & Employee Factors')
    per_captia_employee_to_display1 = other_govt_expenses_per_capita_employee()[1]
    per_captia_employee_to_display1.loc['Total'] = per_captia_employee_to_display1.loc['County Council':'Economic Development Authority',years].sum()
    st.dataframe(per_captia_employee_to_display1.style.format('$ {:,.2f}'))

st.markdown('---')

expander6 = st.expander('Total Other General Government Expenditure')
with expander6:
    st.markdown('### Total Other General Government Expenditure')
    to_display = other_general_govt_total()
    # print(to_display)
    # to_display = to_display.drop(index='Total')
    to_display.loc['Total'] = to_display.loc['Circuit Court':'Economic Development Authority', years].sum()
    st.dataframe(to_display.style.format('$ {:,.2f}'))

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