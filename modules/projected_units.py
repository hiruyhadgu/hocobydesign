import pandas as pd
from modules.get_tables import total_units
from modules.assumptions_and_constants import assumptions, tax_exemptions

unit_types = ['SFD','SFA','Condo_Apts','Rentals','ADUS']
total_units = total_units().loc[unit_types]

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
year1=2023
years = [year1+x for x in range(18)]
verify_total_units = pd.DataFrame(columns=years)

def plan_area():
    plan_areas = {}
    a=0
    no_years = assumptions().iloc[12,0]
    for a in range(len(regions)):

        one_area = pd.DataFrame(columns=years, index=unit_types)
        for i in unit_types:
            one_area.loc[i]=total_units.loc[i,regions[a]]/no_years
        one_area['Total']=one_area[one_area.columns.tolist()].sum(axis=1)
        plan_areas[regions[a]]=one_area
        verify_total_units.loc[regions[a]] = one_area[years].sum()
    return plan_areas, verify_total_units


total_people_by_region = pd.DataFrame(columns=years)
persons_per_unit = tax_exemptions().loc['SFD':'ADUS'].reset_index()
persons_per_unit = persons_per_unit.rename(columns={'Category':'Unit Type', 'Value':'Persons per Unit'}).set_index('Unit Type')
people_per_plan_area = {}

def people_generated():
    people_in_plan_area = pd.DataFrame(columns=years)
    for r in regions:
        one_plan_area=plan_area()[0][r]
        one_plan_area.index = ['SFD','SFA','Condo_Apts','Rentals','ADUS']
        people_in_plan_area=one_plan_area.mul(persons_per_unit['Persons per Unit'].astype(float), axis=0)
        people_per_plan_area[r] = people_in_plan_area
        total_people_by_region.loc[r] = people_in_plan_area.loc['SFD':'ADUS',years].sum()

    return people_per_plan_area, total_people_by_region


