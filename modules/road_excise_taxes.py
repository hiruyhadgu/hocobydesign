import pandas as pd
from modules.projected_units import plan_area
from modules.assessment_tables_and_income_tax_per_unit import assessment_tables, plan_area_assessment_tables
from modules.projected_ronresidential_build import non_res_builds


regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]


res_road_taxes_per_region = {}
road_taxes_per_region = {}

total_road_taxes_per_region = pd.DataFrame(columns=years)

rural_west = [['SFD', 7244],['SFA',2500],['Condo_Apts',1521],['Rentals',1521]]
rural_west = pd.DataFrame(rural_west, columns=['Unit Type', 'Size sq.ft']).set_index('Unit Type')
east = [['SFD', 4989],['SFA',2500],['Condo_Apts',1521],['Rentals',1521]]
east = pd.DataFrame(east, columns=['Unit Type', 'Size sq.ft']).set_index('Unit Type')

multiplier = {'rural_west': rural_west, 'east': east}

charge = {'warehouse':0.86, 'rest':1.67}

def res_road_excise_tax():
    for i in range(len(regions)):
        
        r = regions[i]
        
        if r == 'Rural West':
            sq_size_key = 'rural_west'
        else:
            sq_size_key = 'east'

        rplan = plan_area()[0][r].loc['SFD':'Rentals'].astype(float)

        sq_size = multiplier[sq_size_key]
        res_road_taxes = rplan.mul(sq_size['Size sq.ft']*charge['rest'], axis=0)
        res_road_taxes_per_region[r] = res_road_taxes

    return res_road_taxes_per_region

non_res_by_office_warehouse = {}
non_res_road_taxes_per_region = {}
non_res_assessments = pd.DataFrame(columns=years)
non_res_collapse = pd.DataFrame(columns=years)
road_excise_tax_res_non_res = pd.DataFrame(columns=years)

def non_res_road_excise_tax():
    for r in regions:

        non_res_collapse.loc['Office'] = non_res_builds()[0][r].loc['Retail':'B/C/Flex Office'].sum()
        non_res_collapse.loc['Warehouse'] = non_res_builds()[0][r].loc['Ind./Manuf./Warehouse']
       
        non_res_by_office_warehouse[r]=non_res_collapse

        non_res_assessments.loc['Office'] = non_res_collapse.loc['Office']*charge['rest']
        non_res_assessments.loc['Warehouse'] = non_res_collapse.loc['Warehouse']*charge['warehouse']
        non_res_road_taxes_per_region[r] = non_res_assessments
        

    return non_res_by_office_warehouse, non_res_road_taxes_per_region

def road_excise_tax():
        
    for r in regions:
        res = res_road_excise_tax()[r]
        non_res = non_res_road_excise_tax()[1][r]

        road_excise_tax_res_non_res.loc[r]=res.loc['SFD':'Rentals',years].sum()
    road_excise_tax_res_non_res.loc['Non Residential']=non_res.loc['Office':'Warehouse', years].sum()

    return road_excise_tax_res_non_res