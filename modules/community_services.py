import pandas as pd
from modules.get_tables import community_services_expense
from modules.projected_units import people_generated

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

community_services = community_services_expense()

per_capita_table = community_services.loc[community_services['Methodology']=='Per Capita']
per_captia_category_values = {}
projected_per_capita_tax = pd.DataFrame(columns=years)
results_for_one_cat_all_regions = pd.DataFrame(columns=years)

def community_services_per_capita():
    r_people= people_generated()[1].loc['Columbia':'South East'].astype(float)

    for i in per_capita_table.index.to_list():
        result_for_one_cat = r_people.mul(per_capita_table.loc[i,'Factor'], axis=0)
        per_captia_category_values[i] = result_for_one_cat
        projected_per_capita_tax.loc[i]=result_for_one_cat.loc['Columbia':'South East', years].sum()
   
    return per_captia_category_values, projected_per_capita_tax