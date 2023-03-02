import pandas as pd
from modules.projected_units import plan_area
from modules.assessment_tables_and_income_tax_per_unit import assessment_tables, plan_area_assessment_tables

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]


recordation_taxes_per_region = {}
total_recordation_taxes_per_region = pd.DataFrame(columns=years)

def recordation():
    for i in range(len(regions)):
        
        r = regions[i]
        r_assessment_table = plan_area_assessment_tables(assessed_cat[i])

        r_plan = plan_area()[0][r].astype(float)
        r_plan.index = ['SFD','SFA','Condo_Apts','Rentals','ADUS']
        r_plan[2038] = r_plan[2038]+r_plan[2023]
        r_plan[2039] = r_plan[2039]+r_plan[2024]
        r_plan[2040] = r_plan[2040]+r_plan[2025]

        recordation_taxes = r_plan.mul(r_assessment_table['Assessed Value Per unit']*2.5/500, axis=0)
        recordation_taxes.loc['Total'] = recordation_taxes[years].sum()
        recordation_taxes_per_region[r]=recordation_taxes



        total_recordation_taxes_per_region.loc[r] = recordation_taxes.loc['Total']
    # total_recordation_taxes_per_region.loc['Total'] = total_recordation_taxes_per_region[total_recordation_taxes_per_region.columns.to_list()].sum()
   
    

    return recordation_taxes_per_region, total_recordation_taxes_per_region