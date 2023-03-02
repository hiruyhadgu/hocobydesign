import pandas as pd
import sqlite3 as db
from modules.funcs import unpack_assessed_value
from modules.tax_calc import income_tax, rental_income_tax, adu_income_tax
from modules.get_tables import table2_1
from modules.assumptions_and_constants import gross_income


assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city',\
         'table_rural_west','table_south_east','table_non_res','rental_apts','adus']

all_regions = ['Columbia','Elkridge','Ellicott City',\
      'Rural West','South East','Non Residential','Rental Apts','Accessory Dwelling Unit']

def assessment_tables():
   assessed_value_category={}
   indexer = [(4,7),(9,12),(14,17),(19,22), (24,27),(30,34),(28,29),(7,8)]
   res_no_res = ['r','r','r','r','r','nr','r','r']
   j=0
   for i in assessed_cat:
      r1,r2 = indexer[j]
      assessed_value_category[i]= unpack_assessed_value(table2_1().iloc[r1:r2,1:3],res_no_res[j])
      j=j+1
   return assessed_value_category

r_assessment = {}

def plan_area_assessment_tables(table):
      
        assessment = pd.concat([assessment_tables()[table],\
                                    assessment_tables()['rental_apts'],\
                                    assessment_tables()['adus']]).set_index('Category')
        assessment.index=['SFD','SFA','Condo_Apts','Rentals','ADUS']
        
        if table == 'table_rural_west':
           assessment.loc['SFA'] = [693842, 0.92, 638334.64]
        
        return assessment
        
        

      #       assessment.loc['SFA'] = [693842, 0.92, 638334.64]


non_rental_adu = gross_income()[0]
rental_adu = gross_income()[1]
resulting_income_tax_per_unit = pd.DataFrame(columns=['SFD', 'SFA', 'Condo_Apts'])
rental_adu_income_tax = pd.DataFrame(columns=['Income Tax Per Unit'])
def income_tax_per_unit():

    for r in range(len(all_regions)-3):

        display = assessment_tables()[assessed_cat[r]]
        region = all_regions[r]
        gross_income_by_city = non_rental_adu.loc[region].tolist()
        gross_income_by_city = income_tax(gross_income_by_city,display)


        resulting_income_tax_per_unit.loc[all_regions[r]]=gross_income_by_city.loc['Resulting Income Tax per Unit']
    resulting_income_tax_per_unit.loc['Rural West','SFA']=3845.27

    rental_gross_income = rental_income_tax(rental_adu.loc['Rental Apts'],assessment_tables()['rental_apts'])
    adu_gross_income = adu_income_tax(rental_adu.loc['Accessory Dwelling Uint'],assessment_tables()['adus'])
    rental_adu_income_tax.loc['Rentals'] = rental_gross_income.loc['Weighted Average Income Tax'].squeeze()
    rental_adu_income_tax.loc['ADUS']= adu_gross_income.loc['Resulting Income Tax per Unit'].squeeze()
       
    return resulting_income_tax_per_unit, rental_adu_income_tax
        
        
