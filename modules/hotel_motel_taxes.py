import pandas as pd
from modules.projected_units import people_generated
from modules.employment_data import job_type

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]


emp_res_tax_reg = {}
hotel_motel_tax_per_region ={}
per_captia_employee_factor = 7.79

total_hotel_motel_tax_per_region = pd.DataFrame(columns=years)

def hotel_motel():
    # for i in range(len(regions)):
        
    #     r = regions[i]
    #     a = assessed_cat[i]
        r_people = people_generated()[1].astype(float)
        # .loc[['SFD','SFA','Condo_Apts','Rentals','ADUS']]
        
        r_employment = job_type()[1].astype(float)
        # r_employment.index = ['SFD','SFA','Condo_Apts','Rentals','ADUS']
        
        emp_res_count = r_people + r_employment
        emp_res_tax = emp_res_count*per_captia_employee_factor
    #     emp_res_tax.loc['Total'] = emp_res_tax[emp_res_tax.columns.to_list()].sum()
    #     emp_res_tax_reg[r] = emp_res_tax
    #     total_hotel_motel_tax_per_region.loc[r] = emp_res_tax.loc['Total']
    # total_hotel_motel_tax_per_region.loc['Total'] = total_hotel_motel_tax_per_region[total_hotel_motel_tax_per_region.columns.to_list()].sum()
    
        return emp_res_tax
# emp_res_tax_reg, total_hotel_motel_tax_per_region