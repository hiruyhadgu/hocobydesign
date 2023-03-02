import pandas as pd
from modules.projected_units import people_generated
from modules.employment_data import job_type

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

opeb_trust_fund = 5.66
local_payment_to_sdat = 2.12
total = opeb_trust_fund + local_payment_to_sdat

per_capita_employee_category_values = {}
projected_per_capita_employee_tax = pd.DataFrame(columns=years)
result_for_one_cat_ce= pd.DataFrame(columns=years)
results_for_one_cat_all_regions_ce = pd.DataFrame(columns=years)


def non_departmental_per_capita_employee():
    
    result_for_one_cat_ce= pd.DataFrame(columns=years)
    for r in regions:
        r_people = people_generated()[0][r].astype(float)
        r_employment = job_type()[1].loc[r].astype(float)
        r_people.loc['Employment'] = r_employment
        per_capita_employee_category_values[r] = r_people.mul(total,axis=0)
        result_for_one_cat_ce.loc[r] = per_capita_employee_category_values[r].loc['SFD':'Employment',years].sum()


    return per_capita_employee_category_values, result_for_one_cat_ce