import pandas as pd
from modules.assumptions_and_constants import tax_cat_factors
from modules.projected_units import people_generated
from modules.employment_data import job_type

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

tax_category = tax_cat_factors()

per_capita_table = tax_category.loc[tax_category['Methodology']=='Per Capita']
per_captia_category_values = {}
projected_per_capita_tax = pd.DataFrame(columns=years)
results_for_one_cat_all_regions = pd.DataFrame(columns=years)

def per_capita():
    r_people= people_generated()[1].loc['Columbia':'South East'].astype(float)

    for i in per_capita_table.index.to_list():
        result_for_one_cat = r_people.mul(per_capita_table.loc[i,'Factor'], axis=0)
        per_captia_category_values[i] = result_for_one_cat
        projected_per_capita_tax.loc[i]=result_for_one_cat.loc['Columbia':'South East', years].sum()
   
    return per_captia_category_values, projected_per_capita_tax

per_employee_table = tax_category.loc[tax_category['Methodology']=='Per Employee']
per_employee_category_values = {}
projected_per_employee_tax = pd.DataFrame(columns=years)
result_for_one_cat_e= pd.DataFrame(columns=years)
results_for_one_cat_all_regions_e = pd.DataFrame(columns=years)

def per_employee():

    for i in per_employee_table.index.to_list():
        factor = per_employee_table.loc[i,'Factor']
        result_for_one_cat_e= pd.DataFrame(columns=years)
        for m in range(len(regions)):
            r = regions[m]
            r_jobs= job_type()[0][r].astype(float)
            r_jobs_multiplied = r_jobs.mul(factor, axis=0)
            result_for_one_cat_e.loc[r] = r_jobs_multiplied.loc['Retail':'Ind./Manuf./Warehouse',years].sum()
        per_employee_category_values[i] = result_for_one_cat_e
        projected_per_employee_tax.loc[i] = result_for_one_cat_e.loc['Columbia':'South East',years].sum()
    
    return per_employee_category_values, projected_per_employee_tax


per_capita_employee_table = tax_category.loc[tax_category['Methodology']=='Per Capita and Employee']
per_capita_employee_category_values = {}
projected_per_capita_employee_tax = pd.DataFrame(columns=years)
result_for_one_cat_ce= pd.DataFrame(columns=years)
results_for_one_cat_all_regions_ce = pd.DataFrame(columns=years)
emp_res_count = {}
def per_capita_employee():
    
    for i in per_capita_employee_table.index.to_list():
        result_for_one_cat_ce= pd.DataFrame(columns=years)
        for r in regions:
            r_people = people_generated()[0][r].astype(float)
            r_employment = job_type()[1].loc[r].astype(float)
            r_people.loc['Employment'] = r_employment
            emp_res_count[r] = r_people
            result_for_one_cat_ce.loc[r] = r_people.loc['SFD':'Employment',years].sum().mul(per_capita_employee_table.loc[i,'Factor'],axis=0)
        per_capita_employee_category_values[i] = result_for_one_cat_ce
        projected_per_capita_employee_tax.loc[i]=result_for_one_cat_ce.loc['Columbia':'South East', years].sum()

    return per_capita_employee_category_values, projected_per_capita_employee_tax