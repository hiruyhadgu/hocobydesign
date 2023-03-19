import streamlit as st
from modules.fire_tax import project_fire_tax

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
sub_assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

st.header(':fire_engine: Projected Fire Taxes')

st.markdown('---')

expander = st.expander('Projected Fire Taxes by Planning Area')
with expander:
    select_region3 = st.selectbox('Select Planning Area',regions)
    if select_region3:
        st.markdown('#### Residential Fire Tax Assessment')
        st.dataframe(project_fire_tax()[1][regions[regions.index(select_region3)]].style.format('$ {:,.2f}'))

        st.markdown('---')
        
        st.markdown('#### Non Residential Fire Tax Assessment')
        st.dataframe(project_fire_tax()[2][regions[regions.index(select_region3)]].style.format('$ {:,.2f}'))

st.markdown('---')

expander1= st.expander('Total Projected Fire Taxes')
with expander1:
    st.markdown('#### Total Fire Tax Assessment')
    display_projected_fire_tax = project_fire_tax()[0]
    display_projected_fire_tax.loc['Total'] = display_projected_fire_tax.loc['Columbia':'South East', years].sum()
    st.dataframe(display_projected_fire_tax.style.format('$ {:,.2f}'))

    
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