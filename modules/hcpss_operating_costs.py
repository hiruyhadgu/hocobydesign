import pandas as pd
import numpy as np
from modules.get_tables import approved_operating_budget
from modules.get_tables import school_enrollment
from modules.student_generation_rate import student_generation_rate
import streamlit as st


regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
year1=2023
years = [year1+x for x in range(18)]

@st.cache_data
def school_operating_budget ():
    operating_cost = approved_operating_budget().loc[('Howard County Funding','Howard County-Above MOE'),:]
    operating_cost.loc['Total Howard County Funding']=operating_cost.loc['Howard County Funding':'Howard County-Above MOE',:].sum()
    operating_cost.loc['Subtotal State Funds']= approved_operating_budget().loc['Subtotal State Funds', :]
    operating_cost.loc['Total Other Funds']= approved_operating_budget().loc['Total Other Funds',:]
    operating_cost.loc['Total Funding'] = operating_cost.loc[('Total Howard County Funding','Subtotal State Funds','Total Other Funds'),:].sum()
    operating_cost.loc['Total Enrollment'] = school_enrollment().loc['TOTAL',:]
    operating_cost.loc['Spending Per Student (HoCo Funding Only)'] = operating_cost.loc['Total Howard County Funding',:]/operating_cost.loc['Total Enrollment',:]
    operating_cost.loc['Spending Per Student (Total Funding)'] = operating_cost.loc['Total Funding',:]/operating_cost.loc['Total Enrollment',:]
    operating_cost['Average'] = operating_cost.mean(axis=1)
    operating_cost['Std Deviation'] = operating_cost.loc[:,'FY2015':'FY2023'].std(axis=1)
   

    return operating_cost

total_projected_operating_cost = pd.DataFrame(columns=years)

@st.cache_data
def school_projected_operating_budget(method):

    if method == 'hocobydesign':
        total_projected_operating_cost = student_generation_rate()[3] *school_operating_budget().loc['Spending Per Student (HoCo Funding Only)','FY2023']
        total_projected_operating_cost.loc['Total'] = total_projected_operating_cost.loc['Columbia':'South East',years].sum()
    elif method == 'totalfundingmethod':
        total_projected_operating_cost  = student_generation_rate()[3] *school_operating_budget().loc['Spending Per Student (Total Funding)','FY2023']
        total_projected_operating_cost.loc['Total'] = total_projected_operating_cost.loc['Columbia':'South East',years].sum()

    return total_projected_operating_cost


total_opeb = pd.DataFrame(columns=years)
opeb_trust_fund_ratio = 126.65
def hcpss_opeb_trust_fund():

    total_opeb = student_generation_rate()[3] * opeb_trust_fund_ratio
    total_opeb.loc['Total'] = total_opeb.loc['Columbia':'South East',years].sum()

    return total_opeb
