import pandas as pd
import numpy as np
from modules.student_generation_rate import student_generation_rate
from modules.assumptions_and_constants import school_construction_cost
from modules.assumptions_and_constants import cip_projection
from modules.assumptions_and_constants import land_acquisition_cost
import streamlit as st

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

@st.cache_data
def projected_school_construction_hocobydesign_method():
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
    
    return elementary_school_construction_cost_by_planning_area, middle_school_construction_cost_by_planning_area,\
    high_school_construction_cost_by_planning_area, total_school_construction_cost, hocobydesign_approach, debt_service

@st.cache_data
def projected_school_construction_total_funding_method():
    for i in range(len(regions)):
        r = regions[i]
        elementary_school_construction_cost_by_planning_area[r]=student_generation_rate()[0][r].mul(elementary_school.loc['Per Student Cost','Cost'], axis=0)
        middle_school_construction_cost_by_planning_area[r]=student_generation_rate()[1][r].mul(middle_school.loc['Per Student Cost','Cost'], axis=0)
        high_school_construction_cost_by_planning_area[r]=student_generation_rate()[2][r].mul(high_school.loc['Per Student Cost','Cost'], axis=0)
        total_school_construction_cost.loc[r] = elementary_school_construction_cost_by_planning_area[r].loc['SFD':'APT'].sum()+\
        middle_school_construction_cost_by_planning_area[r].loc['SFD':'APT'].sum()+\
            high_school_construction_cost_by_planning_area[r].loc['SFD':'APT'].sum()

    return elementary_school_construction_cost_by_planning_area, middle_school_construction_cost_by_planning_area,\
    high_school_construction_cost_by_planning_area, total_school_construction_cost

total_cip = cip_projection()
total_cip_projection = pd.DataFrame(columns=years)
@st.cache_data
def cip_hocobydesign_method():
    for i in range(len(regions)):
        r = regions[i]
        total_cip_projection.loc[r]=student_generation_rate()[3].loc[r].mul(total_cip.loc['HoCoByDesign Values','Per Student Cost'], axis=0)
        
    return total_cip_projection

@st.cache_data
def cip_total_funding_method():
    for i in range(len(regions)):
        r = regions[i]
        total_cip_projection.loc[r]=student_generation_rate()[3].loc[r].mul(total_cip.loc['Average','Per Student Cost'], axis=0)

    return total_cip_projection

elementary_school_land_acquisition_by_planning_area = {}
middle_school_land_acquisition_by_planning_area = {}
high_school_land_acquisition_by_planning_area = {}
total_land_acquisition_by_planning_area = pd.DataFrame(columns=years)
land_cost = land_acquisition_cost()

@st.cache_data
def land_acquisition_hocobydesign_method():
    for i in range(len(regions)):
        r = regions[i]
        elementary_school_land_acquisition_by_planning_area[r]=student_generation_rate()[0][r].mul(land_cost.loc['HoCoByDesign Values','Elementary School'], axis=0)
        middle_school_land_acquisition_by_planning_area[r]=student_generation_rate()[1][r].mul(land_cost.loc['HoCoByDesign Values','Middle School'], axis=0)
        high_school_land_acquisition_by_planning_area[r]=student_generation_rate()[2][r].mul(land_cost.loc['HoCoByDesign Values','High School'], axis=0)
        total_land_acquisition_by_planning_area.loc[r] = elementary_school_land_acquisition_by_planning_area[r].loc['SFD':'APT'].sum()+\
        middle_school_land_acquisition_by_planning_area[r].loc['SFD':'APT'].sum()+\
            high_school_land_acquisition_by_planning_area[r].loc['SFD':'APT'].sum()

    return elementary_school_land_acquisition_by_planning_area, middle_school_land_acquisition_by_planning_area,\
        high_school_land_acquisition_by_planning_area, total_land_acquisition_by_planning_area

@st.cache_data
def land_acquisition_total_funding_method():
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

@st.cache_data
def hcpss_capital_total_expenditure():
    total_school_capital_costs_hocobydesign_method = projected_school_construction_hocobydesign_method()[4]+projected_school_construction_hocobydesign_method()[5]+cip_hocobydesign_method()+land_acquisition_hocobydesign_method()[3]
    total_school_capital_costs_full_funds_and_debt = projected_school_construction_hocobydesign_method()[3]+projected_school_construction_hocobydesign_method()[5]+cip_hocobydesign_method()+land_acquisition_hocobydesign_method()[3]
    total_school_capital_costs_total_funding = projected_school_construction_total_funding_method()[3]+cip_total_funding_method()+land_acquisition_total_funding_method()[3]

    return total_school_capital_costs_hocobydesign_method, total_school_capital_costs_full_funds_and_debt, total_school_capital_costs_total_funding