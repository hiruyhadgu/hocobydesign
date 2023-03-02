import pandas as pd
from modules.get_tables import public_facilities_expense
from modules.projected_units import people_generated
from modules.employment_data import job_type

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

public_facilities = public_facilities_expense()

per_capita_table = public_facilities.loc[public_facilities['Methodology']=='Per Capita']
per_captia_category_values = {}
projected_per_capita_tax = pd.DataFrame(columns=years)
results_for_one_cat_all_regions = pd.DataFrame(columns=years)

def public_facilities_per_capita():
    r_people= people_generated()[1].loc['Columbia':'South East'].astype(float)

    for i in per_capita_table.index.to_list():
        result_for_one_cat = r_people.mul(per_capita_table.loc[i,'Factor'], axis=0)
        per_captia_category_values[i] = result_for_one_cat
        projected_per_capita_tax.loc[i]=result_for_one_cat.loc['Columbia':'South East', years].sum()
   
    return per_captia_category_values, projected_per_capita_tax


per_capita_employee_table = public_facilities.loc[public_facilities['Methodology']=='Per Capita & Emp']
per_capita_employee_category_values = {}
projected_per_capita_employee_tax = pd.DataFrame(columns=years)
result_for_one_cat_ce= pd.DataFrame(columns=years)
results_for_one_cat_all_regions_ce = pd.DataFrame(columns=years)
emp_res_count = {}
def public_facilities_per_capita_employee():
    
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

def public_facilities_expenditure():
    
    public_facilities_combined = pd.concat([public_facilities_per_capita()[1],  public_facilities_per_capita_employee()[1]])

    return public_facilities_combined