from modules.assessment_tables_and_income_tax_per_unit import assessment_tables
from modules.employment_data import job_type
from modules.assumptions_and_constants import jobs_to_building_ratio

## use a for loop to build projected property taxes by plan area
regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

non_r_assessment = assessment_tables()['table_non_res'].set_index('Category')

non_res_build_dict = {}
non_res_assessment_by_region = {}
## Jobs to building ratios:
def non_res_builds():
    
    jobs_to_build_ratio = jobs_to_building_ratio()

    for i in range(len(regions)):
        r = regions[i]
        r_employment = job_type()[0][r].astype(float)
        non_res_build_by_region = r_employment.mul(jobs_to_build_ratio['Ratio (sq. ft per employee)'], axis=0)
        assessment_calc = non_res_build_by_region.mul(non_r_assessment['Assessed Value Per unit'], axis=0)
        non_res_build_by_region.loc['Total'] = non_res_build_by_region[years].sum()
        assessment_calc.loc['Total'] = assessment_calc[years].sum()
        non_res_build_dict[r] = non_res_build_by_region
        non_res_assessment_by_region[r] = assessment_calc

    return non_res_build_dict, non_res_assessment_by_region