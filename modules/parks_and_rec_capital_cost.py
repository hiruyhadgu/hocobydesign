import pandas as pd
from modules.projected_units import people_generated

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

per_capital_cost = 21.52

per_captia_category_values = {}
projected_per_capita_expenditure = pd.DataFrame(columns=years)
results_for_one_cat_all_regions = pd.DataFrame(columns=years)

def parks_recs_per_capita():
    r_people= people_generated()[1].loc['Columbia':'South East'].astype(float)

    projected_per_capita_expenditure = r_people.mul(per_capital_cost, axis=0)
    projected_per_capita_expenditure.loc['Total']=projected_per_capita_expenditure.loc['Columbia':'South East', years].sum()
   
    return projected_per_capita_expenditure