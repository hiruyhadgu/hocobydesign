import pandas as pd
import numpy as np
from modules.student_generation_rate import student_generation_rate
from modules.assumptions_and_constants import school_construction_cost
from modules.assumptions_and_constants import cip_projection
from modules.assumptions_and_constants import land_acquisition_cost


regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
year1=2023
years = [year1+x for x in range(18)]

elementary_school = school_construction_cost()[0]
middle_school = school_construction_cost()[1]
high_school = school_construction_cost()[2]

elementary_school_construction_cost_by_planning_area = {}
middle_school_construction_cost_by_planning_area = {}
high_school_construction_cost_by_planning_area = {}
total_school_construction_cost = pd.DataFrame(columns=years)
debt_service = pd.DataFrame(columns=years)
bond_interest_rate = 0.045
hocobydesign_approach = pd.DataFrame(columns=years)

def projected_school_construction(method):
    if method == 'hocobydesign':
        for i in range(len(regions)):
            r = regions[i]
            elementary_school_construction_cost_by_planning_area[r]=student_generation_rate()[0][r].mul(elementary_school.loc['HoCoByDesign Values','Cost'], axis=0)
            middle_school_construction_cost_by_planning_area[r]=student_generation_rate()[1][r].mul(middle_school.loc['HoCoByDesign Values','Cost'], axis=0)
            high_school_construction_cost_by_planning_area[r]=student_generation_rate()[2][r].mul(high_school.loc['HoCoByDesign Values','Cost'], axis=0)
            total_school_construction_cost.loc[r] = elementary_school_construction_cost_by_planning_area[r].loc['SFD':'APT'].sum()+\
            middle_school_construction_cost_by_planning_area[r].loc['SFD':'APT'].sum()+\
                high_school_construction_cost_by_planning_area[r].loc['SFD':'APT'].sum()
            debt_service.loc[r] = total_school_construction_cost.loc[r].cumsum().mul(0.5*bond_interest_rate, axis=0)
            hocobydesign_approach.loc[r] = total_school_construction_cost.loc[r].mul(0.5)
    elif method == 'totalfundingmethod':
        for i in range(len(regions)):
            r = regions[i]
            elementary_school_construction_cost_by_planning_area[r]=student_generation_rate()[0][r].mul(elementary_school.loc['Per Student Cost','Cost'], axis=0)
            middle_school_construction_cost_by_planning_area[r]=student_generation_rate()[1][r].mul(middle_school.loc['Per Student Cost','Cost'], axis=0)
            high_school_construction_cost_by_planning_area[r]=student_generation_rate()[2][r].mul(high_school.loc['Per Student Cost','Cost'], axis=0)
            total_school_construction_cost.loc[r] = elementary_school_construction_cost_by_planning_area[r].loc['SFD':'APT'].sum()+\
            middle_school_construction_cost_by_planning_area[r].loc['SFD':'APT'].sum()+\
                high_school_construction_cost_by_planning_area[r].loc['SFD':'APT'].sum()

    return elementary_school_construction_cost_by_planning_area, middle_school_construction_cost_by_planning_area,\
        high_school_construction_cost_by_planning_area, total_school_construction_cost, hocobydesign_approach, debt_service


total_cip = cip_projection()
total_cip_projection = pd.DataFrame(columns=years)
def cip(method):
    if method == 'hocobydesign':
        for i in range(len(regions)):
            r = regions[i]
            total_cip_projection.loc[r]=student_generation_rate()[3].loc[r].mul(total_cip.loc['HoCoByDesign Values','Per Student Cost'], axis=0)
            
    elif method == 'totalfundingmethod':
        for i in range(len(regions)):
            r = regions[i]
            total_cip_projection.loc[r]=student_generation_rate()[3].loc[r].mul(total_cip.loc['Average','Per Student Cost'], axis=0)

    return total_cip_projection

elementary_school_land_acquisition_by_planning_area = {}
middle_school_land_acquisition_by_planning_area = {}
high_school_land_acquisition_by_planning_area = {}
total_land_acquisition_by_planning_area = pd.DataFrame(columns=years)
land_cost = land_acquisition_cost()

def land_acquisition(method):
    if method == 'hocobydesign':
        for i in range(len(regions)):
            r = regions[i]
            elementary_school_land_acquisition_by_planning_area[r]=student_generation_rate()[0][r].mul(land_cost.loc['HoCoByDesign Values','Elementary School'], axis=0)
            middle_school_land_acquisition_by_planning_area[r]=student_generation_rate()[1][r].mul(land_cost.loc['HoCoByDesign Values','Middle School'], axis=0)
            high_school_land_acquisition_by_planning_area[r]=student_generation_rate()[2][r].mul(land_cost.loc['HoCoByDesign Values','High School'], axis=0)
            total_land_acquisition_by_planning_area.loc[r] = elementary_school_land_acquisition_by_planning_area[r].loc['SFD':'APT'].sum()+\
            middle_school_land_acquisition_by_planning_area[r].loc['SFD':'APT'].sum()+\
                high_school_land_acquisition_by_planning_area[r].loc['SFD':'APT'].sum()
    elif method == 'totalfundingmethod':
        for i in range(len(regions)):
            r = regions[i]
            elementary_school_land_acquisition_by_planning_area[r]=student_generation_rate()[0][r].mul(land_cost.loc['Per Student Cost','Elementary School'], axis=0)
            middle_school_land_acquisition_by_planning_area[r]=student_generation_rate()[1][r].mul(land_cost.loc['Per Student Cost','Middle School'], axis=0)
            high_school_land_acquisition_by_planning_area[r]=student_generation_rate()[2][r].mul(land_cost.loc['Per Student Cost','High School'], axis=0)
            total_land_acquisition_by_planning_area.loc[r] = elementary_school_land_acquisition_by_planning_area[r].loc['SFD':'APT'].sum()+\
            middle_school_land_acquisition_by_planning_area[r].loc['SFD':'APT'].sum()+\
                high_school_land_acquisition_by_planning_area[r].loc['SFD':'APT'].sum()

    return elementary_school_land_acquisition_by_planning_area, middle_school_land_acquisition_by_planning_area,\
        high_school_land_acquisition_by_planning_area, total_land_acquisition_by_planning_area


def hcpss_captial_total_expenditure():
    total_school_captial_costs = projected_school_construction('hocobydesign')[4]+cip('hocobydesign')+land_acquisition('hocobydesign')[3]
    # total_school_captial_costs.loc['Total']=total_school_captial_costs.loc['Columbia':'South East', years].sum()

    return total_school_captial_costs