import streamlit as st
from modules.assessment_tables_and_income_tax_per_unit import assessment_tables, income_tax_per_unit

assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city',\
         'table_rural_west','table_south_east','table_non_res','rental_apts','adus']

all_regions = ['Columbia','Elkridge','Ellicott City',\
      'Rural West','South East','Non Residential','Rental Apts','Accessory Dwelling Unit']

st.header('Assessment Tables and Income Tax Per Unit')

st.write("""
This page shows the market and assessed values of unit types in each planning area. Specifically,
Single Family Detached (SFD), Single Family Detached (SFD), and Condos are shown separately, while Rental Apartment,
and ADUS have their own individual tables. Non Residential properties are also shown separately.
""")

st.markdown('---')

expander = st.expander('Market and Assessed Values by Planning Area')
with expander:
    selected_region=st.selectbox('Select Planning Area',all_regions)
    if selected_region:
        to_display = assessment_tables()[assessed_cat[all_regions.index(selected_region)]]
        to_display.set_index('Category', inplace=True)
        st.dataframe(to_display.style.format(precision=2))

st.markdown('---')

col1, col2 = st.columns(2)

with col1:
    expander1 = st.expander('Income Tax Per Unit (SFD, SFA, Condos)')
    with expander1:
        st.dataframe(income_tax_per_unit()[0].style.format('$ {:,.2f}'))

with col2:
    expander2 = st.expander('Income Tax Per Unit (Rentals and ADUS')
    with expander2:
        st.dataframe(income_tax_per_unit()[1].style.format('$ {:,.2f}'))



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