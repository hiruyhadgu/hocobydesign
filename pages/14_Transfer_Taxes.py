import streamlit as st
from modules.transfer_taxes import transfer_tax

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
sub_assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

st.header('💵 Projected Transfer Taxes')

st.markdown('---')

st.markdown("""
The County uses a 1.25% Transfer Tax on all property transfers. Transfer tax categories are dividied into five, see the Assumptions section
for a breakdown of how the revenue is allocated. For example, the portion generated for School Land Acquisition and Construction (0.3125%) 
is used to pay for the debt service associated with school capital costs.
""")

expander = st.expander('Projected Transfer Taxes By Planning Area')
with expander:
    select_region = st.selectbox('**Select Planning Area**',regions)
    if select_region:
        st.markdown('#### Transfer Taxes by Planning Area')
        display_transfer_tax = transfer_tax()[0][regions[regions.index(select_region)]]
        display_transfer_tax.loc['Total']=display_transfer_tax.loc['SFD':'ADUS',years].sum()
        st.dataframe(display_transfer_tax.style.format('$ {:,.2f}'))

st.markdown('---')

expander1 = st.expander('Total Projected Transfer Taxes')
with expander1:
    st.markdown('#### Total Transfer Taxes')
    total_transfer_taxes=transfer_tax()[1]
    total_transfer_taxes.loc['Total'] = total_transfer_taxes.loc['Columbia':'South East',years].sum()
    st.dataframe(total_transfer_taxes.style.format('$ {:,.2f}'))

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