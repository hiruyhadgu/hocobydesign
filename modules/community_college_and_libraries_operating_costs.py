import pandas as pd
from modules.projected_units import people_generated
from modules.assumptions_and_constants import hoco_population, education_expenditure_factors

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
year1=2023
years = [year1+x for x in range(18)]

hoco_population = hoco_population()
fy2022_credit_noncredit = 12943 + 10156
student_per_capita = fy2022_credit_noncredit/hoco_population.loc['2022'].squeeze()
hcc_budget_history = [['Year', 'FY2021', 'FY2022', 'FY2023'],[ 'Approved Budget', 36559860, 37510616, 40361000]]
hcc_budget_history = pd.DataFrame(hcc_budget_history).T.rename(columns={0:'Year', 1:'Approved Budget'}).set_index('Year')
per_student_cost = hcc_budget_history.loc['FY2023'].squeeze()/fy2022_credit_noncredit
student_per_captia_cost = student_per_capita*per_student_cost
hocobydesign_per_capita = education_expenditure_factors().loc['HCC General Fund','Factor'].squeeze()

def hcc_expenditure(method):
    total_hcc = pd.DataFrame(columns=years)

    if method == 'hocobydesign':
        total_hcc = people_generated()[1].mul(hocobydesign_per_capita)
        total_hcc.loc['Total'] = total_hcc.loc['Columbia':'South East',years].sum()
    elif method == 'student_per_capita_method':
        total_hcc = people_generated()[1].mul(student_per_captia_cost)
        total_hcc.loc['Total'] = total_hcc.loc['Columbia':'South East',years].sum()

    return total_hcc

total_hcc_opeb = pd.DataFrame(columns=years)
opeb_trust_fund_ratio = education_expenditure_factors().loc['HCC OPEB Trust Fund','Factor'].squeeze()

def hcc_opeb_trust_fund():

    people_generated_by_region = people_generated()[1]
    total_hcc_opeb = people_generated_by_region*opeb_trust_fund_ratio
    total_hcc_opeb.loc['Total'] = total_hcc_opeb.loc['Columbia':'South East',years].sum()

    return total_hcc_opeb


### Library
fy2023_projected_total_borrowing = 7700000
per_capita_borrowing = fy2023_projected_total_borrowing/hoco_population.loc['2022'].squeeze()
hcl_budget_history = [['Year', 'FY2021', 'FY2022', 'FY2023'],[ 'Approved Budget', 21880020, 22448901, 24020324]]
hcl_budget_history = pd.DataFrame(hcl_budget_history).T.rename(columns={0:'Year', 1:'Approved Budget'}).set_index('Year')
per_capita_cost = hcl_budget_history.loc['FY2023'].squeeze()/fy2023_projected_total_borrowing
per_captia_borrowing_cost = per_capita_borrowing*per_capita_cost

hocobydesign_per_capita = education_expenditure_factors().loc['Library General Fund','Factor'].squeeze()

def hcl_expenditure(method):
    total_hcl = pd.DataFrame(columns=years)

    if method == 'hocobydesign':
        total_hcl = people_generated()[1].mul(hocobydesign_per_capita)
        total_hcl.loc['Total'] = total_hcl.loc['Columbia':'South East',years].sum()
    elif method == 'per_captia_borrowing_cost':
        total_hcl = people_generated()[1].mul(per_captia_borrowing_cost)
        total_hcl.loc['Total'] = total_hcl.loc['Columbia':'South East',years].sum()

    return total_hcl

total_hcl_opeb = pd.DataFrame(columns=years)
opeb_trust_fund_ratio = education_expenditure_factors().loc['Library OPEB Trust Fund','Factor'].squeeze()

def hcl_opeb_trust_fund():

    people_generated_by_region = people_generated()[1]
    total_hcl_opeb = people_generated_by_region*opeb_trust_fund_ratio
    total_hcl_opeb.loc['Total'] = total_hcl_opeb.loc['Columbia':'South East',years].sum()

    return total_hcl_opeb
