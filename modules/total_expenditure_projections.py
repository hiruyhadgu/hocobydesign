from modules.hcpss_operating_costs import school_projected_operating_budget, hcpss_opeb_trust_fund
from modules.community_college_and_libraries_operating_costs import hcc_expenditure, hcc_opeb_trust_fund, hcl_expenditure, hcl_opeb_trust_fund
from modules.public_safety import project_public_safety
from modules.fire_and_rescue import project_fire_rescue
from modules.public_facilities import public_facilities_expenditure
from modules.community_services import community_services_per_capita
from modules.other_general_government import other_general_govt_total
from modules.hcpss_captial_costs import projected_school_construction, cip, land_acquisition
from modules.community_college_and_libraries_capital_costs import hcl_captial_costs, hcc_captial_costs
from modules.road_expenditure import road_expenditure_per_capita_employee
from modules.fire_stations import fire_stations_per_capita_employee
from modules.parks_and_rec_capital_cost import parks_recs_per_capita
from modules.other_county_capital_expenditure import other_general_county_expenditure
from modules.non_departmental_services import non_departmental_per_capita_employee
import pandas as pd


year1=2023
years = [year1+x for x in range(18)]
operating_revenue_projections = pd.DataFrame(columns=years)
capital_revenue_projections = pd.DataFrame(columns=years)
other_local_taxes = pd.DataFrame(columns=years)

operating_expenditure_projections = pd.DataFrame(columns=years)


def compiled_operating_expenditure_projections(method):
   
    operating_expenditure_projections.loc['HCPSS - Operating Costs'] = school_projected_operating_budget(method).loc['Columbia':'South East',years].sum().cumsum() + hcpss_opeb_trust_fund().loc['Columbia':'South East',years].sum().cumsum()
    operating_expenditure_projections.loc['Community College and Libraries - Operating Costs'] = hcc_expenditure(method).loc['Columbia':'South East',years].sum().cumsum()+hcc_opeb_trust_fund().loc['Columbia':'South East',years].sum().cumsum()+\
        hcl_expenditure(method).loc['Columbia':'South East',years].sum()+hcl_opeb_trust_fund().loc['Columbia':'South East',years].sum().cumsum()
    operating_expenditure_projections.loc['Public Safety'] = project_public_safety()[1].loc['Total Public Safety'].cumsum()
    operating_expenditure_projections.loc['Fire and Rescue'] = project_fire_rescue()[1].loc['Total Fire and Rescue'].cumsum()
    operating_expenditure_projections.loc['Public Facilities'] = public_facilities_expenditure().loc['Facilities - Adminstration':'Soil Conservation District',years].sum().cumsum()
    operating_expenditure_projections.loc['Community Services'] = community_services_per_capita()[1].loc['Depart. of Rec. and Parks - General Fund':'Community Service Partnerships', years].sum().cumsum()
    operating_expenditure_projections.loc['Other General Government'] = other_general_govt_total().loc['Circuit Court':'Economic Development Authority',years].sum().cumsum()
    operating_expenditure_projections.loc['Total Operating Costs'] = operating_expenditure_projections.loc['HCPSS - Operating Costs':'Other General Government',years].sum()

    return operating_expenditure_projections

capital_expenditure_projections = pd.DataFrame(columns=years)

def compiled_capital_expenditure_projections(method):

    capital_expenditure_projections.loc['HCPSS - Captial Costs'] =projected_school_construction(method)[4].loc['Columbia':'South East',years].sum()+\
         projected_school_construction(method)[5].loc['Columbia':'South East',years].sum()+cip(method).loc['Columbia':'South East',years].cumsum(axis=1).sum()+\
            land_acquisition(method)[3].loc['Columbia':'South East',years].sum()
    capital_expenditure_projections.loc['Non Departmental Services'] = non_departmental_per_capita_employee()[1].loc['Columbia':'South East',years].sum().cumsum()
    capital_expenditure_projections.loc['Community College and Libraries - Captial Costs'] = hcc_captial_costs().loc['Columbia':'South East',years].sum().cumsum()\
         + hcl_captial_costs().loc['Columbia':'South East',years].sum().cumsum()
    capital_expenditure_projections.loc['Roads'] = road_expenditure_per_capita_employee()[2].loc['Columbia':'South East',years].sum().cumsum()
    capital_expenditure_projections.loc['Fire Stations'] = fire_stations_per_capita_employee()[1].loc['Columbia':'South East',years].sum() 
    capital_expenditure_projections.loc['Parks and Recreation'] = parks_recs_per_capita().loc['Columbia':'South East',years].sum().cumsum() 
    capital_expenditure_projections.loc['Other County'] = other_general_county_expenditure().loc['Community Renewal':'Bond Anticipation Notes', years].cumsum(axis=1).sum()
    capital_expenditure_projections.loc['Total Capital Costs'] = capital_expenditure_projections.loc['HCPSS - Captial Costs':'Other County', years].sum()
    return capital_expenditure_projections



