import streamlit as st
from modules.school_surcharge_fees import school_surcharge

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
sub_assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

st.header('💵 Projected School Surcharge Fees')

st.markdown('---')

expander = st.expander('Projected School Surcharge Fees by Planning Area')
with expander:
    select_region = st.selectbox('Select Planning Areas',regions)
    st.markdown('#### School Surcharge Fees by Planning Area')
    if select_region:
        st.dataframe(school_surcharge()[0][regions[regions.index(select_region)]].style.format('$ {:,.2f}'))

st.markdown('---')

expander1 = st.expander('Total Projected School Surcharge Fees')
with expander1:
    st.markdown('#### Total School Surcharge Fees')
    total_school_surcharge=school_surcharge()[1]
    total_school_surcharge.loc['Total'] = total_school_surcharge.loc['Columbia':'South East', years].sum()
    st.dataframe(total_school_surcharge.style.format('$ {:,.2f}'))

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