from modules.hcpss_operating_costs import school_projected_operating_budget_hocobydesign_method,\
    school_projected_operating_budget_total_funding_method, hcpss_opeb_trust_fund
from modules.community_college_and_libraries_operating_costs import hcc_expenditure, hcc_opeb_trust_fund, hcl_expenditure, hcl_opeb_trust_fund
from modules.public_safety import project_public_safety
from modules.fire_and_rescue import project_fire_rescue
from modules.public_facilities import public_facilities_expenditure
from modules.community_services import community_services_per_capita
from modules.other_general_government import other_general_govt_total
from modules.hcpss_captial_costs import hcpss_captial_total_expenditure
from modules.community_college_and_libraries_capital_costs import hcl_captial_costs, hcc_captial_costs
from modules.road_expenditure import road_expenditure_per_capita_employee
from modules.fire_stations import fire_stations_per_capita_employee
from modules.parks_and_rec_capital_cost import parks_recs_per_capita
from modules.other_county_capital_expenditure import other_general_county_expenditure
from modules.non_departmental_services import non_departmental_per_capita_employee
import pandas as pd
import streamlit as st
from modules.funcs import inflation

year1=2023
years = [year1+x for x in range(18)]
operating_revenue_projections = pd.DataFrame(columns=years)
capital_revenue_projections = pd.DataFrame(columns=years)
other_local_taxes = pd.DataFrame(columns=years)

operating_expenditure_projections = pd.DataFrame(columns=years)

operating_expenditure_case = [school_projected_operating_budget_hocobydesign_method(), school_projected_operating_budget_total_funding_method()]
operating_case_set = {}
case = ['County Funding Only', 'County and State Funding']
@st.cache_data
def compiled_operating_expenditure_projections():

    for i in range(len(operating_expenditure_case)):
        operating_expenditure_projections = pd.DataFrame(columns=years)
        operating_expenditure_projections.loc['HCPSS - Operating Costs'] = operating_expenditure_case[i].loc['Columbia':'South East',years].sum().mul(inflation().loc['rate']).cumsum() + hcpss_opeb_trust_fund().loc['Columbia':'South East',years].sum().mul(inflation().loc['rate']).cumsum()
        operating_expenditure_projections.loc['Community College and Libraries - Operating Costs'] = hcc_expenditure().loc['Columbia':'South East',years].sum().mul(inflation().loc['rate']).cumsum()+hcc_opeb_trust_fund().loc['Columbia':'South East',years].sum().mul(inflation().loc['rate']).cumsum()+\
            hcl_expenditure().loc['Columbia':'South East',years].sum().mul(inflation().loc['rate'])+hcl_opeb_trust_fund().loc['Columbia':'South East',years].sum().mul(inflation().loc['rate']).cumsum()
        operating_expenditure_projections.loc['Public Safety'] = project_public_safety()[1].loc['Total Public Safety'].mul(inflation().loc['rate']).cumsum()
        operating_expenditure_projections.loc['Fire and Rescue'] = project_fire_rescue()[1].loc['Total Fire and Rescue'].mul(inflation().loc['rate']).cumsum()
        operating_expenditure_projections.loc['Public Facilities'] = public_facilities_expenditure().loc['Facilities - Adminstration':'Soil Conservation District',years].sum().mul(inflation().loc['rate']).cumsum()
        operating_expenditure_projections.loc['Community Services'] = community_services_per_capita()[1].loc['Depart. of Rec. and Parks - General Fund':'Community Service Partnerships', years].sum().mul(inflation().loc['rate']).cumsum()
        operating_expenditure_projections.loc['Other General Government'] = other_general_govt_total().loc['Circuit Court':'Economic Development Authority',years].sum().mul(inflation().loc['rate']).cumsum()
        operating_expenditure_projections.loc['Total Operating Costs'] = operating_expenditure_projections.loc['HCPSS - Operating Costs':'Other General Government',years].sum()
        operating_case_set[case[i]] = operating_expenditure_projections
    return operating_case_set

capital_expenditure_projections = pd.DataFrame(columns=years)

capital_case_set = {}
case1 = ['HoCoByDesign Approach 50% PAYGO and 50% Debt', '100% PAYGO using county\'s per-student costs',\
                                              '100% PAYGO using updated per-student costs']
@st.cache_data
def compiled_capital_expenditure_projections():

    for i in range(len(hcpss_captial_total_expenditure())):
        capital_expenditure_projections = pd.DataFrame(columns=years)
        capital_expenditure_projections.loc['HCPSS - Captial Costs'] =hcpss_captial_total_expenditure()[i].loc['Columbia':'South East',years].sum().mul(inflation().loc['rate'])
        capital_expenditure_projections.loc['Non Departmental Services'] = non_departmental_per_capita_employee()[1].loc['Columbia':'South East',years].sum().mul(inflation().loc['rate']).cumsum()
        capital_expenditure_projections.loc['Community College and Libraries - Captial Costs'] = hcc_captial_costs().loc['Columbia':'South East',years].sum().mul(inflation().loc['rate']).cumsum()\
            + hcl_captial_costs().loc['Columbia':'South East',years].sum().mul(inflation().loc['rate']).cumsum()
        capital_expenditure_projections.loc['Roads'] = road_expenditure_per_capita_employee()[2].loc['Columbia':'South East',years].sum().mul(inflation().loc['rate']).cumsum()
        capital_expenditure_projections.loc['Fire Stations'] = fire_stations_per_capita_employee()[1].loc['Columbia':'South East',years].sum().mul(inflation().loc['rate']) 
        capital_expenditure_projections.loc['Parks and Recreation'] = parks_recs_per_capita().loc['Columbia':'South East',years].sum().mul(inflation().loc['rate']).cumsum() 
        capital_expenditure_projections.loc['Other County'] = other_general_county_expenditure().loc['Community Renewal':'Bond Anticipation Notes', years].mul(inflation().loc['rate']).cumsum(axis=1).sum()
        capital_expenditure_projections.loc['Total Capital Costs'] = capital_expenditure_projections.loc['HCPSS - Captial Costs':'Other County', years].sum().mul(inflation().loc['rate'])
        capital_case_set[case1[i]] = capital_expenditure_projections
    return capital_case_set