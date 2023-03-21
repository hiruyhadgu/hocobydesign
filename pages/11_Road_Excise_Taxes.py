import streamlit as st
from modules.road_excise_taxes import res_road_excise_tax, road_excise_tax, non_res_road_excise_tax
import time

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
sub_assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

st.header(':vertical_traffic_light: Projected Road Excise Taxes')

st.markdown('---')

st.markdown("""
Road excise taxes have not changed much over the years. The County assumes a fee of \\$1.67 per square foot, which explains why the county
finances 100% of road projects with debt.
""")

expander = st.expander('Projected Road Excise Taxes by Planning Area')
with expander:
    select_region = st.selectbox('**Select Planning Areas**',regions)
    if select_region:
        st.markdown('#### Residential Road Excise Taxes by Planning Area')
        to_display = res_road_excise_tax()[regions[regions.index(select_region)]]
        to_display.loc['Total']=to_display.loc['SFD':'Rentals',years].sum()
        st.dataframe(to_display.style.format('$ {:,.2f}'))

        st.markdown('---')
        st.markdown('#### Non Residential Road Excise Taxes')
        to_display3 = non_res_road_excise_tax()[1][regions[regions.index(select_region)]]
        to_display3.loc['Total'] = to_display3.loc['Office':'Warehouse', years].sum()
        st.dataframe(to_display3.style.format('$ {:,.2f}'))

st.markdown('---')

expander1 = st.expander('Total Projected Road Excise Taxes')
with expander1:
    st.markdown('#### Total Road Excise Taxes')
    display_road_excise_tax = road_excise_tax()
    display_road_excise_tax.loc['Total'] = road_excise_tax().loc['Columbia':'Non Residential', years].sum()
    st.dataframe(road_excise_tax().style.format('$ {:,.2f}'))

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