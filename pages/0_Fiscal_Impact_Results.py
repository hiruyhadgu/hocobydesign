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
fiscal_impact_results.loc['100% PAYGO using county\'s per-student costs & roads'] = projected_revenues.loc['Total Revenues'] - operating_expenditure['County Funding Only'].loc['Total Operating Costs']\
      -capital_expenditure['100% PAYGO using county\'s per-student costs & roads'].loc['Total Capital Costs']
fiscal_impact_results.loc['100% PAYGO using updated per-student costs & roads'] = projected_revenues.loc['Total Revenues'] - operating_expenditure['County Funding Only'].loc['Total Operating Costs']\
      -capital_expenditure['100% PAYGO using updated per-student costs & roads'].loc['Total Capital Costs']
fiscal_impact_results.loc['Fiscally Conservative Approach'] = projected_revenues.loc['Total Revenues'] - operating_expenditure['County and State Funding'].loc['Total Operating Costs']\
      -capital_expenditure['100% PAYGO using updated per-student costs & roads'].loc['Total Capital Costs']




# total_revenues = fiscal_impact_results.loc['Total Revenues'].to_numpy()

# total_costs = (fiscal_impact_results.loc['Total Operating Costs'] + fiscal_impact_results.loc['Total Capital Costs']).to_numpy()
# total_costs[0]=total_costs[0]*-1
# net = fiscal_impact_results.loc['Net'].to_numpy()
# net_npv = npf.npv(treasury_bond_rate, net)
st.markdown("""
 The FY2022 Annual Comprehensive Financial Report (ACFR) states that at the end of the [FY2022] fiscal year, 
 the County had total long-term debt outstanding of \\$2.1 billion of which \\$1.8 billion comprises debt backed 
 by the full faith and credit of the government. The remainder of the County’s debt represents bonds secured solely by specific 
 revenue sources (i.e., revenue bonds). The County’s total long-term debt increased by \\$158.5 million (8.2% during that year).

 Even though the County issues new debt to finance projects related to new development every year and the debt has increased every year,
 the fiscal impact results suggest that residential development generates net revenue. This is clearly not the case since even the county assumes 
 revenue from new residential development is used to pay off debt due to previous years' new residential development.
""")
            
st.markdown('---')

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
st.markdown("""
The following graphic and table summarize a comparison of various projection approaches on the over FY2022 County Debt. There are three broad
categories to compare. The first category is the assumption made by the County about excluding State funding of the school budget for both
operation and capital expenditure.

**Note** that in all the cases, the amount of debt the county continues to service using the General Fund is not included.

""")
            
index = fiscal_impact_results.index.to_list()
selected = st.selectbox('Select a projection approach to read the description of each approach:', index)
            
fiscal_approach_description = [f"""
**{selected}:** This case reproduces the County's results, by separating total school operating and capital expenditure into, State, County,
and Other. **Only** the expenditure assumed to be financed by County funds is included in the operating and capital costs. It also assumes that
50% of the school capital expenditure and 100% of the road capital expenditure are financed by debt.
""",
f"""
**{selected}:** This case differs from the **County Funding** approach by adding the expenses associated with State funding of
the school operating budget. It is more realistic as the obligation to fund the schools falls on the County and not the State. Roads are also
financed by debt.
""",
f"""
**{selected}:** This case differs from the **County Funding** approach by assuming 100% of the capital expenditure for schools 
and roads is funded by PAYGO. The per-student costs for school construction are the County's numbers. 

**Note** that this approach uses the County's funding approach for school operating costs.
""",
f"""
**{selected}:** This assumes that 100% of the capital expenditure for schools and roads is funded by PAYGO. However, the per-student school
construction cost used in this approach is much higher as the County's approach underestimates this cost significantly. The school operating
cost remains unchanged from the **County Funding** approach.

""",
f"""
**{selected}:** The fiscally conservative approach is the most responsible approach. First, it takes into account the County **and** State funding
needed to operate the school system. Second, it uses 100% PAYGO to fund road and school construction. Third, the per-student school construction cost
is much more accurate than used by the county.

"""

]

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("FY2022 Total Debt", millify(-2100000000, precision=2))

with col2:
    val = millify(npv[selected], precision=2)
    st.metric(selected, val)

with col3:
    net = millify(-2100000000 + npv[selected], precision=2)
    st.metric('New County Debt', net)

st.markdown('---')

st.markdown(fiscal_approach_description[index.index(selected)])


st.markdown('---')

st.dataframe(fiscal_impact_results.style.format('$ {:,.2f}'))

st.markdown('---')

fig = px.line(fiscal_impact_results.T, width=700, height=500,\
               labels=dict(index="Year", value="Annual Net Impact ($)"))
fig.update_layout(legend=dict(
    yanchor="bottom",
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