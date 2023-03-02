import pandas as pd
import numpy as np
from modules.get_tables import student_yields
from modules.projected_units import plan_area


regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
year1=2023
years = [year1+x for x in range(18)]


elementary_school_generation_by_planning_area = {}
middle_school_generation_by_planning_area = {}
high_school_generation_by_planning_area = {}
total_school_generation = pd.DataFrame(columns=years)

def student_generation_rate():
    for i in range(len(regions)):
        r = regions[i]

        r_plan = plan_area()[0][r].astype(float)
        r_plan.index = ['SFD','SFA','Condo_Apts','Rentals','ADUS']
        r_plan_yeild = r_plan.loc['SFD':'SFA'].copy()
        r_plan_yeild.loc['APT'] = r_plan.loc['Condo_Apts':'ADUS'].sum()
        elementary_school_yield = student_yields()[0]
        middle_school_yield = student_yields()[1]
        high_school_yield = student_yields()[2]
        elementary_school_generation_by_planning_area[r] = r_plan_yeild.mul(elementary_school_yield.iloc[i,:], axis=0)
        middle_school_generation_by_planning_area[r] = r_plan_yeild.mul(middle_school_yield.iloc[i,:], axis=0)
        high_school_generation_by_planning_area[r] = r_plan_yeild.mul(high_school_yield.iloc[i,:], axis=0)
        total_school_generation.loc[r] = elementary_school_generation_by_planning_area[r].loc['SFD':'APT'].sum()+\
            middle_school_generation_by_planning_area[r].loc['SFD':'APT'].sum()+\
                high_school_generation_by_planning_area[r].loc['SFD':'APT'].sum()


    return elementary_school_generation_by_planning_area, middle_school_generation_by_planning_area,\
             high_school_generation_by_planning_area, total_school_generation
