import pandas as pd
from modules.get_tables import projected_employment
from modules.assumptions_and_constants import assumptions

year1=2023
years = [year1+x for x in range(18)]
unit_types = ['SFD','SFA','Condo_Apts','Rentals','ADUS']
job_categories = ['Retail', 'A/B+ Office','B/C/Flex Office','Ind./Manuf./Warehouse']
regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
total_jobs = pd.DataFrame(columns=years)
# job_type_by_plan_area.index.rename('Job Type', inplace=True)

def job_type():
    job_type = {}
    # a=0
    no_years = assumptions().iloc[12,0]
    for a in regions:
        job_type_by_plan_area = pd.DataFrame(columns=years)
        for i in job_categories:
            job_type_by_plan_area.loc[i]=projected_employment().loc[i,a]/no_years
        job_type[a]=job_type_by_plan_area
        total_jobs.loc[a] = job_type_by_plan_area[years].sum()

    return job_type, total_jobs