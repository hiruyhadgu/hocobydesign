import pandas as pd
from modules.get_tables import fire_rescue_expenses
from modules.projected_units import people_generated
from modules.employment_data import job_type
from modules.assumptions_and_constants import non_residential_trip_constants, non_residential_vehicle_trips, hoco_population
from modules.projected_ronresidential_build import non_res_builds

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

fire_rescue = fire_rescue_expenses()
fire_rescue['FY23'] = fire_rescue['FY23'].astype(float)
total= fire_rescue['FY23'].sum()

def fire_rescue_factors():

    factor_calculation = pd.DataFrame(columns=['Residential','Non Residential'])
    factor_calculation.loc['Percent Allocation']=[0.589, 0.411]
    factor_calculation.loc['Expenditure'] = factor_calculation.loc['Percent Allocation']*total
    factor_calculation.loc['Demand Units'] = [hoco_population().loc['2022'].squeeze(), non_residential_vehicle_trips('hocobydesign').loc['Total'].squeeze()]
    factor_calculation.loc['Factors Used'] = factor_calculation.loc['Expenditure']/factor_calculation.loc['Demand Units']

    return factor_calculation

projected_non_residential_trips_by_region= {}
projected_non_residential_trips = pd.DataFrame(columns=years)
result_for_one_region= pd.DataFrame(columns=years)
non_residential_vehicle_trip_factors = non_residential_trip_constants().loc[['Retail/Shopping Center', 'Office - Non Gov', 'Warehousing']]
non_residential_vehicle_trip_factors=non_residential_vehicle_trip_factors.rename(index={'Office - Non Gov':'Office'})

def per_capita_trip_fire_rescue():
    r_jobs = pd.DataFrame(columns=years)
    for m in range(len(regions)):
        r = regions[m]
        r_jobs.loc['Retail/Shopping Center']= job_type()[0][r].loc['Retail'].astype(float)
        r_jobs.loc['Office']= job_type()[0][r].loc[['A/B+ Office','B/C/Flex Office']].astype(float).sum()
        r_jobs.loc['Warehousing']= job_type()[0][r].loc['Ind./Manuf./Warehouse'].astype(float)
        r_total_square_foot = r_jobs.mul(non_residential_vehicle_trip_factors['Sq Ft Per Employee'],axis=0)/1000
        result_for_one_region = r_total_square_foot.mul(non_residential_vehicle_trip_factors['Wkday Trip Ends per 1000 Sq. Ft']*\
            non_residential_vehicle_trip_factors['Trip Factors']* (1-non_residential_vehicle_trip_factors['Telecommuting Factors']),axis=0)
        projected_non_residential_trips_by_region[r] = result_for_one_region
        projected_non_residential_trips.loc[r] = result_for_one_region.loc['Retail/Shopping Center':'Warehousing',years].sum()
    
    return projected_non_residential_trips_by_region, projected_non_residential_trips

population = people_generated()[1]
non_res_trips = per_capita_trip_fire_rescue()[1]
project_expenditure_by_methodology={}
by_demand_unit_type = {}
expenditure_for_each_methodology = pd.DataFrame(columns=years)
fire_rescue_expense = pd.DataFrame(columns=years)

def project_fire_rescue():
 
    expenditure_for_each_methodology = people_generated()[1].mul(fire_rescue_factors().loc['Factors Used','Residential'].squeeze(),axis=0)
    by_demand_unit_type['Population']=expenditure_for_each_methodology
    expenditure_for_each_methodology = per_capita_trip_fire_rescue()[1].mul(fire_rescue_factors().loc['Factors Used','Non Residential'].squeeze(),axis=0)
    by_demand_unit_type['Non Residential Trips']=expenditure_for_each_methodology
    total_per_captia_trips = by_demand_unit_type['Population'] + by_demand_unit_type['Non Residential Trips']
    fire_rescue_expense.loc['Total Fire and Rescue'] = total_per_captia_trips.loc['Columbia':'South East', years].sum()
    
    

    return by_demand_unit_type, fire_rescue_expense