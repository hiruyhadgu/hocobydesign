import streamlit as st
import pandas as pd
import sqlite3 as db
from modules.total_revenues_projection import cumulative_projections
from modules.total_expenditure_projections import compiled_operating_expenditure_projections, \
    compiled_capital_expenditure_projections
from PIL import Image
import numpy_financial as npf
from millify import millify
import plotly.express as px

image = Image.open('combined.jpeg')
# st.sidebar.image("combined.jpeg", use_column_width=True)
treasury_bond_rate = 0.04213	
year1=2023
years = [year1+x for x in range(18)]

conn5 = db.connect('hocobydesign.db')
c = conn5.cursor()

year1=2023
years = [year1+x for x in range(18)]

st.header('HoCoByDesign Fiscal Impact Summary')
# fiscal_impact_results = pd.DataFrame(columns=years)
st.markdown('---')

projected_revenues = cumulative_projections()
projected_revenues.loc['Total Revenues']=projected_revenues.loc['Total Operating Revenues'] + projected_revenues.loc['Total Capital Revenues']

operating_expenditure = compiled_operating_expenditure_projections()
capital_expenditure = compiled_capital_expenditure_projections()
#  ['County Funding Only', 'County and State Funding']
# ['HoCoByDesign Approach 50% PAYGO and 50% Debt', '100% PAYGO using county\'s per-student costs',\
#                                               '100% PAYGO using updated per-student costs']

fiscal_impact_results = pd.DataFrame(columns=years)
fiscal_impact_results.loc['County Funding Only'] = projected_revenues.loc['Total Revenues'] - operating_expenditure['County Funding Only'].loc['Total Operating Costs']\
      -capital_expenditure['HoCoByDesign Approach 50% PAYGO and 50% Debt'].loc['Total Capital Costs']
fiscal_impact_results.loc['County and State Funding'] = projected_revenues.loc['Total Revenues'] - operating_expenditure['County and State Funding'].loc['Total Operating Costs']\
      -capital_expenditure['HoCoByDesign Approach 50% PAYGO and 50% Debt'].loc['Total Capital Costs']
fiscal_impact_results.loc['100% PAYGO using county\'s per-student costs'] = projected_revenues.loc['Total Revenues'] - operating_expenditure['County Funding Only'].loc['Total Operating Costs']\
      -capital_expenditure['100% PAYGO using county\'s per-student costs'].loc['Total Capital Costs']
fiscal_impact_results.loc['100% PAYGO using updated per-student costs'] = projected_revenues.loc['Total Revenues'] - operating_expenditure['County Funding Only'].loc['Total Operating Costs']\
      -capital_expenditure['100% PAYGO using updated per-student costs'].loc['Total Capital Costs']
fiscal_impact_results.loc['Fiscally Conservative Approach'] = projected_revenues.loc['Total Revenues'] - operating_expenditure['County and State Funding'].loc['Total Operating Costs']\
      -capital_expenditure['100% PAYGO using updated per-student costs'].loc['Total Capital Costs']




# total_revenues = fiscal_impact_results.loc['Total Revenues'].to_numpy()

# total_costs = (fiscal_impact_results.loc['Total Operating Costs'] + fiscal_impact_results.loc['Total Capital Costs']).to_numpy()
# total_costs[0]=total_costs[0]*-1
# net = fiscal_impact_results.loc['Net'].to_numpy()
# net_npv = npf.npv(treasury_bond_rate, net)
st.markdown("""
 The FY2022 Annual Comprehensive Financial Report (ACFR) states that at the end of the [FY2022] fiscal year, 
 the County had total long-term debt outstanding of \\$2.1 billion of which \\$1.8 billion comprises debt backed 
 by the full faith and credit of the government. The remainder of the County’s debt represents bonds secured solely by specific 
 revenue sources (i.e., revenue bonds). The County’s total long-term debt increased by \\$158.5 million (8.2% during the current fiscal year).
""")
# st.write(f"${net_npv:,.2f}")
npv = {}
for index in fiscal_impact_results.index:
    results = fiscal_impact_results.loc[index].to_numpy()
    npv[index]=npf.npv(treasury_bond_rate,results)

st.markdown("""
<style>
div[data-testid="metric-container"] {
   background-color: rgba(28, 131, 225, 0.1);
   border: 1px solid rgba(28, 131, 225, 0.1);
   padding: 5% 5% 5% 10%;
   border-radius: 5px;
   color: rgb(30, 103, 119);
   overflow-wrap: break-word;
}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: red; font-size: 200% !important;
}
</style>
"""
, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("FY2022 Total Debt", millify(-2100000000, precision=2))

index = fiscal_impact_results.index.to_list()
with col2:
    selected = st.selectbox('Pick A Fiscal Approach', index)
    val = millify(npv[selected], precision=2)
    st.metric(selected, val)

with col3:
    net = millify(-2100000000 + npv[selected], precision=2)
    st.metric('New County Debt', net)

st.dataframe(fiscal_impact_results.style.format('$ {:,.2f}'))

st.markdown('---')

fig = px.line(fiscal_impact_results.T, width=700, height=500,\
               labels=dict(index="Year", value="Annual Net Impact ($)"))
fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01
))
st.plotly_chart(fig)


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