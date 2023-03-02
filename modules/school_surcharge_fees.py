import pandas as pd
from modules.projected_units import plan_area

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

rural_west = [['SFD', 7244],['SFA',2500],['Condo_Apts',1521],['Rentals',1521]]
rural_west = pd.DataFrame(rural_west, columns=['Unit Type', 'Size sq.ft']).set_index('Unit Type')
east = [['SFD', 4989],['SFA',2500],['Condo_Apts',1521],['Rentals',1521]]
east = pd.DataFrame(east, columns=['Unit Type', 'Size sq.ft']).set_index('Unit Type')

surcharge = [['SFD', 7.5], ['SFA', 6.75], ['Condo_Apts', 6.75], ['Rentals',6.75]]
surcharge = pd.DataFrame(surcharge, columns=['Unit Type','Rate']).set_index('Unit Type')


school_surcharge_per_region = {}
total_school_surcharge_per_region = pd.DataFrame(columns=years)
multiplier = {'rural_west': rural_west, 'east': east}
def school_surcharge():
    for i in range(len(regions)):
        
        r = regions[i]
        
        if r == 'Rural West':
            sq_size_key = 'rural_west'
        else:
            sq_size_key = 'east'

        r_plan = plan_area()[0][r].astype(float)
        r_plan.index = ['SFD','SFA','Condo_Apts','Rentals','ADUS']
        units_used_in_calculation = r_plan.loc[['SFD','SFA','Condo_Apts','Rentals'],:]
        sq_size = multiplier[sq_size_key]
        total_square_ft = units_used_in_calculation.mul(sq_size['Size sq.ft'], axis=0)
        school_surcharge_one_region = total_square_ft.mul(surcharge['Rate'], axis=0)
        school_surcharge_one_region.loc['Total'] = school_surcharge_one_region[years].sum()
        school_surcharge_per_region[r]=school_surcharge_one_region



        total_school_surcharge_per_region.loc[r] = school_surcharge_one_region.loc['Total']
    
    

    return school_surcharge_per_region, total_school_surcharge_per_region