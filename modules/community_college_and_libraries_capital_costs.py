import pandas as pd
from modules.projected_units import people_generated
from modules.assumptions_and_constants import hoco_population, hcc_data
from modules.projected_units import people_generated

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
year1=2023
years = [year1+x for x in range(18)]



total_hcc_capital_costs = pd.DataFrame(columns=years)
hcc_capital_cost_per_capita = hcc_data().loc['Average','Capital Funds']/hoco_population().loc['2022']
def hcc_capital_costs():
    
    total_hcc_capital_costs = people_generated()[1].mul(hcc_capital_cost_per_capita.squeeze())
    total_hcc_capital_costs.loc['Total'] = total_hcc_capital_costs.loc['Columbia':'South East',years].sum()

    return total_hcc_capital_costs

### Library

total_hcl_capital_costs = pd.DataFrame(columns=years)
hcl_capital_cost_per_capita = 10.5
def hcl_capital_costs():
    
    total_hcl_capital_costs = people_generated()[1].mul(hcl_capital_cost_per_capita)
    total_hcl_capital_costs.loc['Total'] = total_hcl_capital_costs.loc['Columbia':'South East',years].sum()

    return total_hcl_capital_costs