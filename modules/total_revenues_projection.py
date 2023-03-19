from modules.property_taxes import prop_tax_by_region
from modules.income_taxes import project_income_tax
from modules.transfer_taxes import transfer_tax
from modules.school_surcharge_fees import school_surcharge
from modules.road_excise_taxes import road_excise_tax
from modules.fire_tax import project_fire_tax
from modules.recordation_taxes import recordation
from modules.hotel_motel_taxes import hotel_motel
from modules.admissions_amusement_taxes import admission_amusement
from modules.other_revenues import per_capita, per_employee, per_capita_employee
import pandas as pd
import streamlit as st
from modules.funcs import inflation

year1=2023
years = [year1+x for x in range(18)]
operating_revenue_projections = pd.DataFrame(columns=years)
capital_revenue_projections = pd.DataFrame(columns=years)
other_local_taxes = pd.DataFrame(columns=years)

@st.cache_data
def compiled_revenue_projections():

    other_rev_per_capita = per_capita()[1]
    other_rev_per_employee = per_employee()[1]
    other_rev_per_capita_employee = per_capita_employee()[1]

    projected_other_revenue = pd.concat([other_rev_per_capita, other_rev_per_employee, other_rev_per_capita_employee])
    # projected_other_revenue.drop(index='Total', inplace=True)
    # projected_other_revenue.loc['Total']=projected_other_revenue.loc['Highway User Tax':'Parking Violations',years].sum()
    
    other_local_taxes.loc['Hotel/Motel Tax'] = hotel_motel().loc['Columbia':'South East',years].sum().mul(inflation().loc['rate'])
    other_local_taxes.loc['Admissions and Amusement Tax'] = admission_amusement()[1].loc['Columbia':'South East',years].sum().mul(inflation().loc['rate'])


    operating_revenue_projections.loc['Property Taxes'] = prop_tax_by_region()[4].loc['Real Property Tax':'Penalties/Interest Property Taxes',years].sum().mul(inflation().loc['rate'])
    operating_revenue_projections.loc['Fire Tax'] = project_fire_tax()[0].loc['Columbia':'South East',years].sum().mul(inflation().loc['rate'])
    operating_revenue_projections.loc['Income Taxes'] = project_income_tax()[0].loc['Columbia':'South East',years].sum().mul(inflation().loc['rate'])
    operating_revenue_projections.loc['Other Local Taxes']=other_local_taxes.loc['Hotel/Mote Tax':'Admissions and Amusement Tax',years].sum().mul(inflation().loc['rate'])
    operating_revenue_projections.loc['Other Revenues']=projected_other_revenue.loc['Highway User Tax':'Parking Violations',years].sum().mul(inflation().loc['rate'])

    capital_revenue_projections.loc['Transfer Taxes']=transfer_tax()[1].loc['Columbia':'South East',years].sum().mul(inflation().loc['rate'])
    capital_revenue_projections.loc['Road Excise Taxes'] = road_excise_tax().loc['Columbia':'Non Residential',years].sum().mul(inflation().loc['rate'])
    capital_revenue_projections.loc['School Surcharge Fees']=school_surcharge()[1].loc['Columbia':'South East',years].sum().mul(inflation().loc['rate'])
    
    return operating_revenue_projections, capital_revenue_projections

cumulative_revenue_projections = pd.DataFrame(columns=years)

@st.cache_data
def cumulative_projections():

    cumulative_operating_revenue_projections = compiled_revenue_projections()[0].cumsum(axis=1)
    cumulative_operating_revenue_projections.loc['Recordation Fees'] = recordation()[1].loc['Columbia':'South East',years].sum().mul(inflation().loc['rate'])
    cumulative_operating_revenue_projections.loc['Total Operating Revenues'] = cumulative_operating_revenue_projections.loc['Property Taxes':'Recordation Fees',years].sum()
    cumulative_capital_revenue_projections = compiled_revenue_projections()[1]
    cumulative_capital_revenue_projections.loc['Total Capital Revenues'] = cumulative_capital_revenue_projections.loc['Transfer Taxes':'School Surcharge Fees',years].sum()
    cumulative_projections = pd.concat([cumulative_operating_revenue_projections,cumulative_capital_revenue_projections])

    return cumulative_projections
