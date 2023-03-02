import streamlit as st
from modules.admissions_amusement_taxes import admission_amusement

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
sub_assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

st.header('Projected Admissions and Amusement Revenues')

st.write("""
The fiscal impact methdology and analysis calculates per unit income tax revenue and these values are
multiplied by the number of projected units to calculate the annual income taxs.
""")

st.markdown('---')

expander = st.expander('Admissions and Amusement Taxes by Planning Area')
with expander:
    select_region = st.selectbox('Select Planning Area',regions)
    st.markdown('#### Admission and Amusement Taxes by Planning Area')
    if select_region:
        st.dataframe(admission_amusement()[0][regions[regions.index(select_region)]].style.format('$ {:,.2f}'))

st.markdown('---')

expander1 = st.expander('Total Admissions and Amusement Taxes')
with expander1:
    st.markdown('#### Total Admission and Amusement Taxes')
    display_admission_amusement = admission_amusement()[1]
    display_admission_amusement.loc['Total'] = display_admission_amusement.loc['Columbia':'South East', years].sum()
    st.dataframe(display_admission_amusement.style.format('$ {:,.2f}'))

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