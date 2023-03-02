import pandas as pd
from modules.assessment_tables_and_income_tax_per_unit import plan_area_assessment_tables
from modules.projected_units import plan_area
from modules.projected_ronresidential_build import non_res_builds


regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

fire_tax_by_region = {}
total_fire_tax_by_region = pd.DataFrame(columns=years)
non_res_portion_by_region ={}

def project_fire_tax():
    for i in range(len(regions)):
        r = regions[i]

        r_assessment_table = plan_area_assessment_tables(assessed_cat[i])
        r_plan = plan_area()[0][r].astype(float)
        r_plan.index = ['SFD','SFA','Condo_Apts','Rentals','ADUS']

        non_r = non_res_builds()[1][r].astype(float)
        
        res_portion_assessment = r_assessment_table['Assessed Value Per unit']*0.236/100  
        
        r_fire_tax = r_plan.mul(res_portion_assessment,axis=0)
        non_res_portion_assessment = non_r * 0.236/100

        r_fire_tax.loc['Non Residential'] =  non_res_portion_assessment.loc['Total']
        r_fire_tax.loc['Total'] = r_fire_tax[years].sum()


        fire_tax_by_region[r]=r_fire_tax
        non_res_portion_by_region[r] = non_res_portion_assessment



        total_fire_tax_by_region.loc[r]= r_fire_tax.loc['Total']

    return total_fire_tax_by_region, fire_tax_by_region, non_res_portion_by_region