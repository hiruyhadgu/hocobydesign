import pandas as pd
from modules.projected_units import people_generated
from modules.employment_data import job_type

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]


per_capita_employee_factor = 343.88
results_for_one_region = {}
result_for_all_regions= pd.DataFrame(columns=years)
results_for_one_cat_all_regions_ce = pd.DataFrame(columns=years)
emp_res_count = {}
def fire_stations_per_capita_employee():
    
    for r in regions:
        r_people = people_generated()[0][r].astype(float)
        r_employment = job_type()[1].loc[r].astype(float)
        r_people.loc['Employment'] = r_employment
        emp_res_count[r] = r_people
        results_for_one_region[r]= r_people.mul(per_capita_employee_factor,axis=0)
        result_for_all_regions.loc[r] = results_for_one_region[r].loc['SFD':'Employment',years].sum()
    result_for_all_regions.loc['Total']=result_for_all_regions.loc['Columbia':'South East', years].sum()

    return results_for_one_region, result_for_all_regions