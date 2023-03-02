import pandas as pd
from modules.assumptions_and_constants import transfer_tax_allocation
from modules.projected_units import plan_area
from modules.assessment_tables_and_income_tax_per_unit import plan_area_assessment_tables


regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

transfer_taxes_per_region = {}
total_transfer_taxes_per_region = pd.DataFrame(columns=years)

def transfer_tax():
    for i in range(len(regions)):
        
        r = regions[i]

        r_assessment_table = plan_area_assessment_tables(assessed_cat[i])

        r_plan = plan_area()[0][r].astype(float)
        r_plan.index = ['SFD','SFA','Condo_Apts','Rentals','ADUS']
        r_plan[2038] = r_plan[2038]+r_plan[2023]
        r_plan[2039] = r_plan[2039]+r_plan[2024]
        r_plan[2040] = r_plan[2040]+r_plan[2025]
        units_used_in_calculation = r_plan.loc[['SFD','SFA','Condo_Apts','ADUS'],:]
        funds_not_part_of_general_plan = transfer_tax_allocation().loc['Agricultural Land Preservation'].squeeze() + transfer_tax_allocation().loc['Housing and Community Development'].squeeze()
        net_allocatable_to_general_fund = transfer_tax_allocation().loc['Total'].squeeze() - funds_not_part_of_general_plan
        transfer_taxes = units_used_in_calculation.mul(r_assessment_table['Market Value Per unit']*net_allocatable_to_general_fund, axis=0)
        # transfer_taxes.loc['Total'] = transfer_taxes[years].sum()
        transfer_taxes_per_region[r]=transfer_taxes.loc[['SFD','SFA','Condo_Apts','ADUS']]


        total_transfer_taxes_per_region.loc[r] = transfer_taxes[years].sum()
    
    

    return transfer_taxes_per_region, total_transfer_taxes_per_region