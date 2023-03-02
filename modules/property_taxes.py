import pandas as pd
from modules.income_taxes import reg_dev_type_income_tax
from modules.assessment_tables_and_income_tax_per_unit import plan_area_assessment_tables
from modules.projected_units import plan_area
from modules.employment_data import job_type


## use a for loop to build projected property taxes by plan area
regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]


real_property_tax_by_region = {}
total_real_property_region = pd.DataFrame(columns=years)
total_property_taxes = pd.DataFrame(columns=years)
r_personal_merchants_pro_tax = pd.DataFrame(columns=years)
r_penalties = pd.DataFrame(columns=years)
used_regional_table = {}
used_emloyment_table={}
per_unit = {}

def prop_tax_by_region():
    for i in range(len(regions)):
        
        r = regions[i]
        r_assessment_table = plan_area_assessment_tables(assessed_cat[i])

        r_plan = plan_area()[0][r].astype(float)
        r_plan.index = ['SFD','SFA','Condo_Apts','Rentals','ADUS']
        used_regional_table[r]=r_plan
        r_employment = job_type()[0][r].astype(float)
        used_emloyment_table[r] = r_employment

        r_income_taxes = reg_dev_type_income_tax()[r].astype(float)
        r_income_taxes.index=['SFD','SFA','Condo_Apts','Rentals','ADUS']
        

        per_unit[r] = r_assessment_table['Assessed Value Per unit']*(1.014+0.08)/100+325
        r_prop_tax = r_plan.mul(per_unit[r],axis=0)
        real_property_tax_by_region[r] = r_prop_tax

        r_personal_merchants_pro_tax.loc[r] = r_employment[years].sum() * 204.64
        
        r_penalties.loc[r]= r_prop_tax[years].sum() * 0.12/100

        total_real_property_region.loc[r] = r_prop_tax[years].sum()


    total_property_taxes.loc['Real Property Tax'] = total_real_property_region.loc['Columbia':'South East', years].sum()
    total_property_taxes.loc['Personal/Merchants Property Tax'] = r_personal_merchants_pro_tax.loc['Columbia':'South East', years].sum()
    total_property_taxes.loc['Penalties/Interest Property Taxes'] = r_penalties.loc['Columbia':'South East', years].sum()


    return real_property_tax_by_region, r_personal_merchants_pro_tax, r_penalties, total_real_property_region, total_property_taxes