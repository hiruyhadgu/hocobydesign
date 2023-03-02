import pandas as pd
from modules.assumptions_and_constants import hoco_population
from modules.get_tables import road_expenditure, bea_employment_rate
from modules.projected_units import people_generated
from modules.employment_data import job_type

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

employment_rate = bea_employment_rate()[1]
employment_rate = employment_rate.drop(columns='index')
road_expenditure = road_expenditure()
population = hoco_population()

population_change = population.loc['2022'] - population.loc['2010']
hocobydesign_2022_employment = 230745
job_change = hocobydesign_2022_employment - float(employment_rate.loc[1, '2010'])
total_pop_employment = population_change + job_change
per_capita_employee = road_expenditure.loc['Total', 'Inflation Adjusted 2022 Dollars']/total_pop_employment

per_capita_employee_category_values = {}
projected_per_capita_employee_tax = pd.DataFrame(columns=years)
result_for_one_cat_ce= pd.DataFrame(columns=years)
results_for_one_cat_all_regions_ce = pd.DataFrame(columns=years)

debt_service = pd.DataFrame(columns=years)
bond_interest_rate = 0.045

def road_expenditure_per_capita_employee():
    
    result_for_one_cat_ce= pd.DataFrame(columns=years)
    for r in regions:
        r_people = people_generated()[0][r].astype(float)
        r_employment = job_type()[1].loc[r].astype(float)
        r_people.loc['Employment'] = r_employment
        per_capita_employee_category_values[r] = r_people.mul(per_capita_employee.squeeze(),axis=0)
        result_for_one_cat_ce.loc[r] = per_capita_employee_category_values[r].loc['SFD':'Employment',years].sum()

        debt_service.loc[r] = result_for_one_cat_ce.loc[r].mul(bond_interest_rate, axis=0)

    return per_capita_employee_category_values, result_for_one_cat_ce, debt_service