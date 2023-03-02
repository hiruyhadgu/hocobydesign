import streamlit as st
import pandas as pd
from modules.other_revenues import per_capita, per_employee, per_capita_employee
from modules.assumptions_and_constants import tax_cat_factors

st.header('Projected Other Revenues')

st.markdown('---')

tax_category = tax_cat_factors()
per_capita_table = tax_category.loc[tax_category['Methodology']=='Per Capita']
per_employee_table = tax_category.loc[tax_category['Methodology']=='Per Employee']
per_capita_employee_table = tax_category.loc[tax_category['Methodology']=='Per Capita and Employee']

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]


expander = st.expander('Taxes Projected Using Per-Captia Factors')
with expander:
    select_category = st.selectbox('Select Tax Category',per_capita_table.index.to_list())
    if select_category:
        st.markdown('### Tax Categories Projected Using Per-Capita Factors')
        per_captia_to_display = per_capita()[0][select_category]
        per_captia_to_display.loc['Total'] = per_captia_to_display[years].sum()
        st.dataframe(per_captia_to_display.style.format('$ {:,.2f}'))

st.markdown('---')

expander1 = st.expander('Total Taxes Projected Using Per-Captia Factors')
with expander1:
    st.markdown('### Total Taxes Projected Using Per-Capita Factors')
    per_captia_to_display1 = per_capita()[1]
    per_captia_to_display1.loc['Total'] = per_captia_to_display1.loc['Highway User Tax':'Other Fines and Forfeitures', years].sum()
    st.dataframe(per_captia_to_display1.style.format('$ {:,.2f}'))

st.markdown('---')

expander2 = st.expander('Taxes Projected Using Per-Employee Factors')
with expander2:
    select_category1 = st.selectbox('Select Tax Category',per_employee_table.index.to_list())
    if select_category1:
        st.markdown('### Tax Categories Projected Using Per-Employee Factors')
        per_employee_to_display = per_employee()[0][select_category1]
        per_employee_to_display.loc['Total'] = per_employee_to_display.loc['Columbia':'South East',years].sum()
        st.dataframe(per_employee_to_display.style.format('$ {:,.2f}'))

st.markdown('---')

expander3 = st.expander('Taxes Projected Using Per-Employee Factors')
with expander3:
    st.markdown('### Total Taxes Projected Using Per-Capita Factors')
    per_employee_to_display1 = per_employee()[1]
    per_employee_to_display1.loc['Total'] = per_employee_to_display1.loc['Traders License':'Sign Permits',years].sum()
    st.dataframe(per_employee_to_display1.style.format('$ {:,.2f}'))

st.markdown('---')

expander4 = st.expander('Taxes Projected Using Per-Captia and Employee Factors')
with expander4:
    select_category2 = st.selectbox('Other Revenues Per-Capita and Employee Factor',per_capita_employee_table.index.to_list())
    if select_category2:
        st.markdown('### Tax Categories Projected Using Per Capita & Employee Factors')
        per_captia_employee_to_display = per_capita_employee()[0][select_category2]
        per_captia_employee_to_display.loc['Total'] = per_captia_employee_to_display[years].sum()
        st.dataframe(per_captia_employee_to_display.style.format('$ {:,.2f}'))

st.markdown('---')

expander5 = st.expander('Total Taxes Projected Using Per-Captia and Employee Factors')
with expander5:
    st.markdown('### Total Taxes Projected Using Per Capita & Employee Factors')
    per_captia_employee_to_display1 = per_capita_employee()[1]
    per_captia_employee_to_display1.loc['Total'] = per_captia_employee_to_display1[years].sum()
    st.dataframe(per_captia_employee_to_display1.style.format('$ {:,.2f}'))

other_rev_per_capita = per_capita()[1]
other_rev_per_employee = per_employee()[1]
other_rev_per_capita_employee = per_capita_employee()[1]


projected_other_revenue = pd.concat([other_rev_per_capita, other_rev_per_employee, other_rev_per_capita_employee])
projected_other_revenue.drop(index='Total', inplace=True)
projected_other_revenue.loc['Total']=projected_other_revenue.loc['Highway User Tax':'Parking Violations',years].sum()

st.markdown('---')

expander6 = st.expander('Total Other Revenues Projection')
with expander6:
    st.markdown('### Total Revenues in "Other Revenues" Category')
    st.dataframe(projected_other_revenue.style.format('$ {:,.2f}'))

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