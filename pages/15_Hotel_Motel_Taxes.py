import streamlit as st
from modules.hotel_motel_taxes import hotel_motel

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
sub_assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

st.header(':hotel: Projected Hotels and Motels Taxes')

st.write("""
The fiscal impact methodology and analysis calculates per unit income tax revenue and these values are
multiplied by the number of projected units to calculate the annual income taxes.
""")

st.markdown('---')

expander1 = st.expander('Total Hotels and Motels Tax Projection')
with expander1:
    display_hotel_motel_tax = hotel_motel()
    st.markdown('#### Hotel/Motel Taxes by Planning Area')
    display_hotel_motel_tax.loc['Total'] = display_hotel_motel_tax.loc['Columbia':'South East', years].sum()
    st.dataframe(display_hotel_motel_tax.style.format('$ {:,.2f}'))


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