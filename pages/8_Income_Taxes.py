import streamlit as st
from modules.income_taxes import project_income_tax

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
sub_assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

st.header('💵 Projected Income Tax Revenue')

st.write("""
The fiscal impact methodology and analysis calculates per unit income tax revenue and these values are multiplied by the 
number of projected units to calculate the annual income taxes.
""")
         
st.markdown('---')

expander = st.expander('Income Tax Projection by Planning Area')
with expander:
    selected_region1=st.selectbox('**Select Planning Area**',regions)
    if selected_region1:
        st.markdown('#### Income Taxes By Planning Area')
        to_display1 = project_income_tax()[1][regions[regions.index(selected_region1)]]
        to_display1.loc['Total']=to_display1[years].sum()
        st.dataframe(to_display1.style.format('$ {:,.2f}'))

st.markdown('---')

expander1 = st.expander('Total Income Tax Projection')
with expander1:
    st.markdown('#### Total Income Taxes')
    display_total_income_tax_by_region = project_income_tax()[0]
    display_total_income_tax_by_region.loc['Total'] = display_total_income_tax_by_region.loc['Columbia':'South East', years].sum()
    st.dataframe(display_total_income_tax_by_region.style.format('$ {:,.2f}'))


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