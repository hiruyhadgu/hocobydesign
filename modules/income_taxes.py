import pandas as pd
from modules.projected_units import plan_area
from modules.assessment_tables_and_income_tax_per_unit import income_tax_per_unit

non_rental_adu_income_tax = income_tax_per_unit()[0]
rental_adu_income_tax = income_tax_per_unit()[1]

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
sub_assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']

def reg_dev_type_income_tax():
   reg_dev_type_income_tax = {}
   c=0
   row_needed = 'Resulting Income Tax per Unit'
   for r in regions:


      g1 = non_rental_adu_income_tax.loc[r]
      g2 = rental_adu_income_tax.loc['Rentals']
      g3 = rental_adu_income_tax.loc['ADUS']
      g = pd.concat([g1, g2, g3])
      c = c +1
      # g = g.rename(index = {'SFA':'SFA','SFD':'SFD', 'Condos_Apt':'Condos_Apt','Income Tax Per Unit':'ADUS','Income Tax Per Unit':'Rentals'})
      g = pd.DataFrame(g, columns=['Values']).reset_index()
      g.rename(columns={'index':'Category'}, inplace=True)
      g.iloc[3,0] = 'Rentals'
      g.iloc[4,0] = 'ADUS'
      g.set_index('Category', inplace=True)
      reg_dev_type_income_tax[r] = g

   return reg_dev_type_income_tax

year1=2023
years = [year1+x for x in range(18)]
total_income_tax_by_region = pd.DataFrame(columns=years)
income_tax_by_region = {}
used_rates = {}
used_plans = {}
def project_income_tax():
   for i in range(len(regions)):
      
      r = regions[i]

      r_plan = plan_area()[0][r].astype(float)
      r_income_taxes = reg_dev_type_income_tax()[r].astype(float)
      used_rates[r] = r_income_taxes
      used_plans[r] = r_plan
      
      r_income_taxes_by_region = r_plan.mul(r_income_taxes['Values'], axis=0)
      income_tax_by_region[r] = r_income_taxes_by_region
      total_income_tax_by_region.loc[r] = r_income_taxes_by_region[years].sum()
      
   
   return total_income_tax_by_region, income_tax_by_region, used_rates, used_plans
