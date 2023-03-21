import streamlit as st
from modules.property_taxes import prop_tax_by_region


regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
year1=2023
years = [year1+x for x in range(18)]

st.header('💵 Projected Property Tax Revenues')

st.write("""
The fiscal impact methodology and analysis computes property taxes from real property taxes, personal/merchant taxes,
and penalties as a fraction of real property taxes. Real property taxes are calculated as assessed value times
(\\$1.014 + \\$0.08)/100 + \\$325.
""")

st.markdown('---')

expander = st.expander('Annual Marginal Projected Property Taxes For All Plan Areas')
with expander:
    st.markdown('#### Real Property Taxes')
    display_total_property_taxes_by_region = prop_tax_by_region()[3]
    display_total_property_taxes_by_region.loc['Total'] = display_total_property_taxes_by_region.loc['Columbia':'South East'].sum()
    st.dataframe(display_total_property_taxes_by_region.style.format('$ {:,.2f}'))

st.markdown('---')

expander1 = st.expander('Annual Personal/Merchant Taxes For All Plan Areas')
with expander1:
    st.markdown('#### Personal/Merchant Taxes')
    display_personal_merchant_tax=prop_tax_by_region()[1]
    display_personal_merchant_tax.loc['Total'] = display_personal_merchant_tax.loc['Columbia':'South East'].sum()
    st.dataframe(display_personal_merchant_tax.style.format('$ {:,.2f}'))

st.markdown('---')

expander2 = st.expander('Annual Penalties For All Plan Areas')
with expander2:
    st.markdown('#### Penalties')
    display_penalties=prop_tax_by_region()[2]
    display_penalties.loc['Total'] = display_penalties.loc['Columbia':'South East'].sum()
    st.dataframe(display_penalties.style.format('$ {:,.2f}'))

st.markdown('---')

expander3 = st.expander('Total Property Taxes')
with expander3:
    st.markdown('#### Total Property Taxes')
    display_total_property_tax = prop_tax_by_region()[4]
    display_total_property_tax.loc['Total'] = display_total_property_tax.loc['Real Property Tax':'Penalties/Interest Property Taxes', years].sum()
    st.dataframe(display_total_property_tax.style.format('$ {:,.2f}'))


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