import pandas as pd
from modules.projected_units import people_generated


regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]


per_cap_tax_reg = {}
admission_amusement_tax = {}


total_admission_amusement_tax = pd.DataFrame(columns=years)
per_captia_factor = 6.49
per_captia_employee_factor = 7.79

def admission_amusement():
    for i in range(len(regions)):
        
        r = regions[i]

        r_people = people_generated()[0][r].loc[['SFD','SFA','Condo_Apts','Rentals','ADUS']].astype(float)
        per_cap_tax = r_people*per_captia_employee_factor
        per_cap_tax.loc['Total'] = per_cap_tax[per_cap_tax.columns.to_list()].sum()
        per_cap_tax_reg[r] = per_cap_tax
        total_admission_amusement_tax.loc[r] = per_cap_tax.loc['Total']
    # total_admission_amusement_tax.loc['Total'] = total_admission_amusement_tax[total_admission_amusement_tax.columns.to_list()].sum()
    

    return per_cap_tax_reg, total_admission_amusement_tax
