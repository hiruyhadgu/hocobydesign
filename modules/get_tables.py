import pandas as pd
import sqlite3 as db
import numpy as np

conn = db.connect('hocobydesign.db', check_same_thread=False)
c = conn.cursor()


def projected_employment():
    projected_employment = pd.read_sql_query('select * from table11_1',conn)
    projected_employment.rename(columns={'Southeast':'South East'}, inplace=True)
    projected_employment.loc[0:4, projected_employment.columns.to_list()[1:]] = projected_employment.loc[0:4, projected_employment.columns.to_list()[1:]].replace(',',"", regex=True).astype(float)
    projected_employment = projected_employment.set_index('Job Type')
    return projected_employment

def table2_1():
    table2_1 = pd.read_sql_query('select * from table2_1',conn)

    return table2_1

def total_units():
    total_units = pd.read_sql_query('select * from table10_1',conn)
    total_units = total_units.drop(columns='index')
    total_units.rename(columns={'Southeast':'South East'}, inplace=True)
    total_units.loc[0:5, total_units.columns.to_list()[1:]] = total_units.loc[0:5, total_units.columns.to_list()[1:]].replace(',',"", regex=True).astype(float)
    total_units.set_index('Unit Type',inplace=True)

    return total_units

def property_taxes():
    ## read FY2023 property taxes from methods and assumptions
    property_taxes = pd.read_sql_query('select * from table1_2',conn)
    property_taxes = property_taxes.drop(columns='index').set_index('Category')

    return property_taxes

def approved_operating_budget():
    ## read FY2023 property taxes from methods and assumptions
    hcpss_operating_budget = pd.read_sql_query('select * from approved_operating_budget',conn)
    hcpss_operating_budget.iloc[3,0] = 'Total Howard County Funding'
    hcpss_operating_budget = hcpss_operating_budget.set_index('Category')
    hcpss_operating_budget = hcpss_operating_budget.replace('',np.nan)
    hcpss_operating_budget = hcpss_operating_budget.replace('-',np.nan)
    hcpss_operating_budget = hcpss_operating_budget.astype(float)

    return hcpss_operating_budget

def school_enrollment():
    ## read FY2023 property taxes from methods and assumptions
    hcpss_enrollment = pd.read_sql_query('select * from enrollment',conn)
    hcpss_enrollment = hcpss_enrollment.set_index('Category')

    return hcpss_enrollment

def student_yields():

    elementary_schools = pd.read_sql_query('select * from elementary_school_yield',conn)
    elementary_schools=elementary_schools.drop(columns='index')
    elementary_schools = elementary_schools.set_index('Planning Area')
    elementary_schools= elementary_schools.astype(float)
    middle_schools = pd.read_sql_query('select * from middle_school_yield',conn)
    middle_schools=middle_schools.drop(columns='index')
    middle_schools = middle_schools.set_index('Planning Area')
    middle_schools= middle_schools.astype(float)
    high_schools = pd.read_sql_query('select * from high_school_yield',conn)
    high_schools=high_schools.drop(columns='index')
    high_schools = high_schools.set_index('Planning Area')
    high_schools = high_schools.astype(float)
    all_schools = pd.read_sql_query('select * from all_level_yield',conn)
    all_schools=all_schools.drop(columns='index')
    all_schools = all_schools.set_index('Planning Area')
    all_schools = all_schools.astype(float)

    return elementary_schools, middle_schools, high_schools, all_schools

def public_safety_method():
    public_safety_method = pd.read_sql_query('select * from public_safety',conn)

    return public_safety_method

def fire_rescue_expenses():
    fire_rescue = pd.read_sql_query('select * from fire_rescue', conn)
    
    return fire_rescue


def public_facilities_expense():
    public_facilities_expense = pd.read_sql_query('select * from public_facilities', conn)
    public_facilities_expense=public_facilities_expense.drop(columns='index')
    public_facilities_expense['FY23 Budget']=[x[1:] for x in public_facilities_expense['FY23 Budget']]
    public_facilities_expense['FY23 Budget']= public_facilities_expense['FY23 Budget'].replace(',','', regex=True).astype(float)
    public_facilities_expense.columns = ['Category', 'FY23 Budget', '%of Total General Fund', 'Methodology','Factor']
    public_facilities_expense['Factor']=[x[1:] for x in public_facilities_expense['Factor']]
    public_facilities_expense['Factor']= public_facilities_expense['Factor'].replace(',','', regex=True).astype(float)
    public_facilities_expense = public_facilities_expense.set_index('Category')
    return public_facilities_expense

def community_services_expense():
    community_services_expense = pd.read_sql_query('select * from community_services', conn)
    community_services_expense=community_services_expense.drop(columns='index')
    community_services_expense['FY23 Budget']=[x[1:] for x in community_services_expense['FY23 Budget']]
    community_services_expense['FY23 Budget']= community_services_expense['FY23 Budget'].replace(',','', regex=True).astype(float)
    community_services_expense['Factor']=[x[1:] for x in community_services_expense['Factor']]
    community_services_expense['Factor']= community_services_expense['Factor'].replace(',','', regex=True).astype(float)
    community_services_expense = community_services_expense.set_index('Category')
    return community_services_expense

def other_govt_expenses():
    general_govt_expenses = pd.read_sql_query('select * from other_general_government', conn)
    general_govt_expenses = general_govt_expenses.drop(columns='index')
    general_govt_expenses['FY23 Budget']=[x[1:] for x in general_govt_expenses['FY23 Budget']]
    general_govt_expenses['FY23 Budget']= general_govt_expenses['FY23 Budget'].replace(',','', regex=True).astype(float)
    general_govt_expenses['Factor']=[x[1:] for x in general_govt_expenses['Factor']]
    general_govt_expenses['Factor']= general_govt_expenses['Factor'].replace(',','', regex=True).astype(float)
    general_govt_expenses = general_govt_expenses.set_index('Category')

    return general_govt_expenses

def general_county_bonds():
    general_county_bonds_table = pd.read_sql_query('select * from general_county_bonds', conn)
    general_county_bonds_table = general_county_bonds_table.set_index('Category')

    return general_county_bonds_table

def road_expenditure():
    road = pd.read_sql_query('select * from road_expenditure', conn)
    road = road.drop(columns='index')
    road = road.set_index('Fiscal Year')

    return road

def bea_employment_rate():
    raw_bea_employment_data = pd.read_sql_query('select * from employment_rate', conn)
    raw_bea_employment_data = pd.DataFrame(raw_bea_employment_data)
    bea_employment_data = raw_bea_employment_data.iloc[2:,4:]

    return bea_employment_data, raw_bea_employment_data