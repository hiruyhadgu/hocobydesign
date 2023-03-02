import pandas as pd
import sqlite3 as db
from modules.get_tables import school_enrollment, bea_employment_rate
import numpy as np

conn = db.connect('hocobydesign.db', check_same_thread=False)
c = conn.cursor()

def assumptions():
    assumptions = [['Assessed Value Ratio (Residential)', 'Assessed Value Ratio (Non Residential)', 'Affordability Ratio','Mortgage Interest Rate',\
                    'Down Payment','Income Tax Rate','HOA Fee','SFD/SFA Insurance','Condo Insurance','Rental Affordability Ratio','MIHU Tax Adjustment'\
                        ,'MIHU','Projected Years','Bond Interest Rate', 'Bond Debt Financing (years)'],\
                        [0.92, 1, 0.28, 0.05, 0.2, 0.032,50, 50, 33.33,0.32,0.6,0.15,18,0.045,20]]
    assumptions = pd.DataFrame(assumptions)
    assumptions = assumptions.T
    assumptions.columns = ['Category','Value']
    assumptions['Value'] = assumptions['Value'].astype(float)
    assumptions = assumptions.set_index('Category')

    return assumptions

def taxes_fees():
    taxes_fees = [['County Tax','State Tax','Fire Tax','Ad Valorem','Trash Fee'],[1.014,.112, .236, 0.08, 325]]
    taxes_fees = pd.DataFrame(taxes_fees).T
    taxes_fees.columns = ['Category','Value']
    taxes_fees = taxes_fees.set_index('Category')
    taxes_fees['Value']=taxes_fees['Value'].astype(float)
    
    return taxes_fees

def tax_exemptions():
    tax_exemptions = [['SFD', 'SFA','Condo_Apts','Rentals','ADUS','Non Rental Exemption','Rental Exemption'],[3.22, 2.68, 2.09, 2.09, 1.5, 3200,3400]]
    tax_exemptions = pd.DataFrame(tax_exemptions).T
    tax_exemptions.columns = ['Category','Value']
    tax_exemptions=tax_exemptions.set_index('Category')
    tax_exemptions['Value']=tax_exemptions['Value'].astype(float)

    return tax_exemptions

def tax_cat_factors():
    tax_category = [['Highway User Tax', 'Per Capita',11.42], ['Traders License','Per Employee', 1.55], ['Sign Permits', 'Per Employee', 0.18],\
                ['Beer and Wine License','Per Capita', 0.59], ['Concert and Special Events Permits', 'Per Capita',0.12], ['Marriage License Surcharge','Per Capita', 0.24],\
                ['Animal License - Dog', 'Per Capita', 0.17], ['Parking Fees', 'Per Capita',0.04], ['From State Government Inc. 911 Fee','Per Capita', 10.32],\
                ['State Aid Protection', 'Per Capita', 21.09], ['CATV Franchise Fee', 'Per Capita', 15.33], ['Tax Certification', 'Per Capita', 1.47],\
                ['Police Records Check', 'Per Capita', 0.13], ['Civil Marriages','Per Capita', 0.03], ['Redlight Camera Violations','Per Capita and Employee',3.21],\
                ['Parking Violations','Per Capita and Employee',0.23],['False Alarm Fees and Fines','Per Capita',0.88],['Other Fines and Forfeitures','Per Capita',0.18]]
    
    tax_category = pd.DataFrame(tax_category, columns=['Category','Methodology', 'Factor']).set_index('Category')

    return tax_category

def transfer_tax_allocation():
    
    tax_allocation =[['School Land Acquisition and Construction', 0.003125],\
        ['Park Construction and Development', 0.003125], \
            ['Agricultural Land Preservation', 0.0025], \
                ['Housing and Community Development', 0.001875], \
                    ['Fire and Rescue Captial Equipment', 0.001875]]
    tax_allocation = pd.DataFrame(tax_allocation, columns=['Tax Category','Allocation Percent']).set_index('Tax Category')

    tax_allocation.loc['Total']=tax_allocation['Allocation Percent'].sum()

    return tax_allocation

def jobs_to_building_ratio():

    jobs_to_building = [['Retail',400],['A/B+ Office',302], ['B/C/Flex Office',317], ['Ind./Manuf./Warehouse',round((433+558+784)/3,2)]]
    jobs_to_building = pd.DataFrame(jobs_to_building, columns=['Category','Ratio (sq. ft per employee)']).set_index('Category')

    return jobs_to_building

def gross_income():
    non_rental_adu = pd.DataFrame([['Columbia',221695,154469, 90941],\
                                    ['Elkridge',155452,116959,99419],\
                                    ['Ellicott City',220373,166024,91445],\
                                    ['South East', 203266,119002,84077],\
                                    ['Rural West', 277369]])
    non_rental_adu.columns=['City','SFD', 'SFA','Condo_Apt']
    non_rental_adu.set_index('City', inplace=True)

    rental_adu = [['Rental Apts', 85313],['Accessory Dwelling Uint', 63305]]
    rental_adu = pd.DataFrame(rental_adu)
    rental_adu.columns = ['Category', 'Value']
    rental_adu.set_index('Category', inplace=True)

    return non_rental_adu, rental_adu


def housing_units():

    #estimate as of July 1, 2019
    
    annual_census_bureau_estimates = [['Year', 'Number of Units'],['2010', 109617], ['2011', 110602],\
                                      ['2012', 111615], ['2013', 113125], [ '2014', 115195], ['2015', 116446],\
                                      ['2016', 117826], ['2017',119773], ['2018',120793], ['2019', 122593]]
    return annual_census_bureau_estimates

def hoco_population():
    hoco_annual_population = [['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'],\
        [ 288627, 293583, 299184, 303527, 306909, 311297, 315416, 319251, 322621, 325690,328200, 334529, 339223]]
    hoco_annual_population = pd.DataFrame(hoco_annual_population).T.rename(columns={0:'Year',1:'Population'}).set_index('Year')
    hoco_annual_population['Population'] = hoco_annual_population['Population'].astype(float)

    return hoco_annual_population

def hcc_data():
    
    hcc = [['FY2018', 'FY2019', 'FY2020', 'FY2021','FY2022','FY2023'],[28985,29587,26143,21094,np.nan,np.nan],[np.nan,np.nan,3412000, 6437000, 16844000,15794000]]
    hcc = pd.DataFrame(hcc).T.rename(columns={0:'Year',1:'Unduplicated Head Count',2:'Capital Funds'}).set_index('Year').astype(float)
    hcc.loc['Average'] = hcc[['Unduplicated Head Count','Capital Funds']].mean()
    hcc.loc['Per Capita'] = hcc.loc['Average']/hoco_population().loc['2022'].squeeze()
    
    return hcc

def education_expenditure_factors():
    expenditure_type = [['HCPSS General Fund', 'Per New Student', 11341.32],['HCPSS OPEB Trust Fund', 'Per Capita', 126.65],\
        ['HCC General Fund', 'Per Capita', 118.98], ['HCC OPEB Trust Fund','Per Capita',0.72], ['Library General Fund','Per Captia',70.81],\
            ['Library OPEB Trust Fund','Per Capita',0.11]]
    expenditure_type = pd.DataFrame(expenditure_type, columns=['Category', 'Methodology', 'Factor']).set_index('Category')
    expenditure_type['Factor'] = expenditure_type['Factor'].astype(float)
    return expenditure_type

def school_construction_cost():
    
    high_school = [['High School #13','New',1658, 129997000], ['Hammond High School','Renovation/Addition',200,106554000]]
    high_school = pd.DataFrame(high_school, columns=['Name','Project Type','Capacity','Cost']).set_index('Name')
    high_school.loc['Average',['Capacity','Cost']] = high_school[['Capacity','Cost']].mean()
    high_school.loc['Per Student Cost', 'Cost'] = high_school.loc['Average','Cost']/high_school.loc['Average','Capacity']
    high_school.loc['HoCoByDesign Values', 'Capacity'] = 1658
    high_school.loc['HoCoByDesign Values', 'Cost'] = 54394
    
    middle_school = [['Dunlogging Middle School','Renovation/Addition', 233, 53182000],\
        ['Oakland Mills Middle School','Renovation/Addition', 292, 55497000],['Wilde Lake Middle School','New/Replacement',760,45377000]]
    middle_school = pd.DataFrame(middle_school, columns=['Name','Project Type','Capacity','Cost']).set_index('Name')
    middle_school.loc['Average',['Capacity','Cost']] = middle_school[['Capacity','Cost']].mean()
    middle_school.loc['Per Student Cost', 'Cost'] = middle_school.loc['Average','Cost']/middle_school.loc['Average','Capacity']
    middle_school.loc['HoCoByDesign Values', 'Capacity'] = 798
    middle_school.loc['HoCoByDesign Values', 'Cost'] = 51352
    
    elementary_school = [['Talbott Springs Replacement','New/Replacement',540,43467000],['ES #43','New',788,68250000],['Hanover Hills','New',832,43873000]]
    elementary_school = pd.DataFrame(elementary_school, columns=['Name','Project Type','Capacity','Cost']).set_index('Name')
    elementary_school.loc['Average',['Capacity','Cost']] = elementary_school[['Capacity','Cost']].mean()
    elementary_school.loc['Per Student Cost', 'Cost'] = elementary_school.loc['Average','Cost']/elementary_school.loc['Average','Capacity']
    elementary_school.loc['HoCoByDesign Values', 'Capacity'] = 838
    elementary_school.loc['HoCoByDesign Values', 'Cost'] = 37945

    return elementary_school, middle_school, high_school

def cip_projection():

    cip = [['FY2018','FY2019','FY2020','FY2021','FY2022', 'FY2023'],[16055000,25455000,17118000,13498000,11067000,30630000]]
    cip = pd.DataFrame(cip).T.rename(columns={0:'Year',1:'Maintenance Cost'}).set_index('Year')
    cip['Per Student Cost']=cip['Maintenance Cost']/school_enrollment().loc['TOTAL']
    cip.loc['Average',['Maintenance Cost','Per Student Cost']] = cip[['Maintenance Cost','Per Student Cost']].mean()
    cip.loc['HoCoByDesign Values']=[33300000, 580.9]
    return cip

def land_acquisition_cost():
    elementary_school = school_construction_cost()[0]
    middle_school = school_construction_cost()[1]
    high_school = school_construction_cost()[2]
    land_acquisition = [['Acres Needed', 20,30,50],\
                        ['Cost Per Acre', 250000, 250000, 250000]]
    land_acquisition = pd.DataFrame(land_acquisition, columns = ['Category', 'Elementary School', 'Middle School', 'High School']).set_index('Category')
    land_acquisition.loc['Total Cost'] = land_acquisition.loc['Acres Needed']*land_acquisition.loc['Cost Per Acre']
    land_acquisition.loc['Average Capacity']=[elementary_school.loc['Average','Capacity'], middle_school.loc['Average','Capacity'],high_school.loc['Average','Capacity']]
    land_acquisition.loc['Per Student Cost'] = land_acquisition.loc['Total Cost']/land_acquisition.loc['Average Capacity']
    land_acquisition.loc['HoCoByDesign Values'] = [6010, 9398, 7359]
    return land_acquisition


def annual_employment():
    hoco_employment_data = [['FY2017','FY2018','FY2019','FY2020','FY2021'],[171075, 171153, 174388, 174390, 163675]]
    hoco_employment_data = pd.DataFrame(hoco_employment_data).T
    hoco_employment_data = hoco_employment_data.rename(columns={0:'Year',1:'Total Employment'}).set_index('Year')

    bea_employment_data = bea_employment_rate()[0]
 
    bea_employment_data['Description'] = bea_employment_data['Description'].str.strip()
    bea_employment_data = bea_employment_data.reset_index().drop(columns='index').set_index('Description')
    bea_employment_data.loc[:,'2001':'2021']=bea_employment_data.loc[:,'2001':'2021'].replace('(D)',np.nan)
    bea_employment_data.loc[:,'2001':'2021']=bea_employment_data.loc[:,'2001':'2021'].astype(float)
    collapsed_tables = pd.DataFrame(columns=bea_employment_data.columns.to_list())
    collapsed_tables.loc['Retail/Shopping Center'] = bea_employment_data.loc['Retail trade']+bea_employment_data.loc['Accommodation and food services']
    collapsed_tables.loc['Office - Gov'] = bea_employment_data.loc['Government and government enterprises']
    collapsed_tables.loc['Office - Non Gov'] = bea_employment_data.loc['Private nonfarm employment'] - \
        bea_employment_data.loc['Wholesale trade'] - bea_employment_data.loc['Construction'] - \
        bea_employment_data.loc['Manufacturing'] - bea_employment_data.loc['Retail trade'] - \
        bea_employment_data.loc['Accommodation and food services']
    collapsed_tables.loc['Warehousing'] = bea_employment_data.loc['Farm employment'] + bea_employment_data.loc['Wholesale trade']
    collapsed_tables.loc['Manufacturing'] = bea_employment_data.loc['Construction'] + bea_employment_data.loc['Manufacturing']
    collapsed_tables['Average']=collapsed_tables[collapsed_tables.columns.to_list()].mean(axis=1)
    return hoco_employment_data, bea_employment_data, collapsed_tables

def non_residential_trip_constants():
   vehicle_trip_constants = [['Retail/Shopping Center', 42.94, 400, 0.32,0],
    ['Office - Gov', 11.01, 302, 0.50,0.206],
    ['Office - Non Gov', 11.01, 302, 0.50, 0.16],
    ['Warehousing', 4.96, 784, 0.50, 0],
    ['Manufacturing', 3.82, 558, 0.5, 0]]
   vehicle_trip_constants = pd.DataFrame(vehicle_trip_constants,\
        columns=['Category', 'Wkday Trip Ends per 1000 Sq. Ft', 'Sq Ft Per Employee', 'Trip Factors', 'Telecommuting Factors']).set_index('Category')
   
   return vehicle_trip_constants


def non_residential_vehicle_trips(method):

    constants = non_residential_trip_constants()

    if method == 'hocobydesign':
        employment_summary = annual_employment()[2].loc[:,'2020']
        employment_summary = (employment_summary*constants['Wkday Trip Ends per 1000 Sq. Ft']*\
            constants['Sq Ft Per Employee']*constants['Trip Factors']*(1-constants['Telecommuting Factors']))*0.001
        employment_summary = pd.DataFrame(employment_summary).rename(columns={0:'Value'})
        employment_summary.loc['Total']=employment_summary['Value'].sum()
    elif method =='average':
        employment_summary = annual_employment()[2].loc[:,'Average']
        employment_summary = (employment_summary*constants['Wkday Trip Ends per 1000 Sq. Ft']*\
            constants['Sq Ft Per Employee']*constants['Trip Factors']*(1-constants['Telecommuting Factors']))*0.001
        employment_summary = pd.DataFrame(employment_summary).rename(columns={0:'Value'})
        employment_summary.loc['Total']=employment_summary['Value'].sum()

    return employment_summary

def hcpss_debt_service():
    debt_service = [[2018, 55944513], [2019,55198943], [2020, 55270060], [2021, 52328909], [2022, 52123590],[2023, 48747588]]
    debt_service = pd.DataFrame(debt_service, columns=['Year','HCPSS Debt Service'])
    debt_service['Year'] = debt_service['Year'].astype(str)
    debt_service = debt_service.set_index('Year')
    debt_service.loc['Average'] = debt_service['HCPSS Debt Service'].mean()
    return debt_service