import pandas as pd
import tabula as tb
import streamlit as st
import sqlite3 as db

conn = db.connect('hocobydesign.db')
c = conn.cursor()

# table1 = tb.read_pdf('hocobydesign.pdf',pages=6, multiple_tables=True)
# table1_1=table1[0]
# table1_1.iloc[11,0]='Total'
# table1_1 = pd.DataFrame(table1_1).to_sql('table1_1',conn)

# table1_2 = table1[1].columns.to_frame().T.append(table1[1], ignore_index=True)
# table1_2.columns=['Category', 'FY 2023','% Total', 'Methodology','Factor']
# table1_2 = pd.DataFrame(table1_2).to_sql('table1_2',conn)

# table2 = tb.read_pdf('hocobydesign.pdf',pages=7)
# table2[0].loc[19.5]= ['Single Family Attached', 0, 0, 0]
# table2[0].loc[19.6] = ['Condo Apartment', 0, 0, 0]
# table2[0]=table2[0].sort_index().reset_index(drop=True)
# table2_1=table2[0]
# table2_1.columns = ['Category','Market Value Per unit','Assessed Value Ratio','Assessed Value Per unit']
# table2_1 = pd.DataFrame(table2_1).to_sql('table2_1',conn)

# table3 = tb.read_pdf('hocobydesign.pdf',pages=14)
# table3_1 = table3[0].shift()
# table3_1.loc[0]=['Income Taxes','$540,869,664','41.90%','Taxable Income','3.20%']
# table3_1.columns = ['Category', 'FY 2023','% Total', 'Methodology','Factor']
# table3_1.loc[4]=['Admission and Amusement Tax','$2,200,000','0.17%','Per Capita','$6.49']
# table3_1 = pd.DataFrame(table3_1).to_sql('table3_1',conn)

# table4=[["Highway Users' Tax", '$3,874,000','0.30%', 'Per Capita','$11.42']]
# table4 = pd.DataFrame(table4)
# table4.columns = ['Category', 'FY 2023','% Total', 'Methodology','Factor']
# table4 = table4.to_sql('table4',conn)

# table5 = tb.read_pdf('hocobydesign.pdf',pages=16)
# table5_1 = table5[0].shift()
# table5_1.loc[0]=['Traders License','$350,000','0.03%','Per Employee','$1.55']
# table5_1.loc[15]=['Peddlers & Solicitors','$13,000','0.00%','Fixed','$0.00']
# table5_1.columns = ['Category', 'FY 2023','% Total', 'Methodology','Factor']
# table5_1 = table5_1.to_sql('table5_1',conn)

# table6 = tb.read_pdf('hocobydesign.pdf',pages=17)
# table6_1=table6[0].drop(0)
# table6_1 = table6_1.to_sql('table6_1',conn)

# table7 = tb.read_pdf('hocobydesign.pdf',pages=18)
# table7_1 = table7[0].shift()
# table7_1.loc[0]=['CATV Franchise Fee', '$5,200,000', '0.40%',' Per Capita','$15.33']
# table7_1.loc[19]=['Extension of Developer Agreements','$16,000','0.00%','Fixed','$0.00']
# table7_1.columns = ['Category', 'FY 2023','% Total', 'Methodology','Factor']
# table7_1 = table7_1.to_sql('table7_1',conn)

# table8 = tb.read_pdf('hocobydesign.pdf',pages=19)
# table8_1 = table8[0].shift()
# table8_1.columns = ['Category $FY2023','% Total', 'Methodology','Factor']
# table8_1.loc[0]=['Other $800,001','0.06%','Fixed','$0.00']
# table8_1.loc[20]=['Other Fines and Forfeitures $60,000', '0.00%', 'Per Capita', '$0.18']
# table8_2 = table8_1.iloc[0:5,:].drop(4)
# table8_2[['Category', 'FY 2023']] = table8_2['Category $FY2023'].str.split("$", expand = True)
# table8_3 = table8_1.iloc[15:,:].drop([15,16])
# table8_3[['Category', 'FY 2023']] = table8_3['Category $FY2023'].str.split("$", expand = True)
# table8_2=table8_2.drop(columns='Category $FY2023')
# table8_2 = table8_2[['Category', 'FY 2023', '% Total', 'Methodology', 'Factor']]
# table8_3=table8_3.drop(columns='Category $FY2023')
# table8_3 = table8_3[['Category', 'FY 2023', '% Total', 'Methodology', 'Factor']]
# table8_2 = table8_2.to_sql('table8_2',conn)
# table8_3 = table8_3.to_sql('table8_3',conn)

# table9 = tb.read_pdf('hocobydesign.pdf',pages=20)
# table9_1 = table9[0].shift()
# table9_1.columns = ['Category', '$FY2023','% Total', 'Methodology','Factor']
# table9_1.loc[0]=['Other - Operating Transfer In Budget',  '$5,889,000' ,' 0.46%',' Fixed','$0.00']
# table9_1.loc[24]=['Other - Employee Health Fund','$29,051','0.00%','Fixed', '$0.00']
# table9_1 = table9_1.to_sql('table9_1',conn)

# table10 = tb.read_pdf('results.pdf',pages=2)
# table10_1 = table10[0]
# table10_1=table10_1.to_sql('table10_1',conn)

# table11=tb.read_pdf('results.pdf',pages=3)
# table11_1 = table11[0].drop(columns='Job Type')
# table11_1=table11_1.rename(columns={'Unnamed: 0':'Job Type'})
# table11_1.iloc[4,0] = 'Total'
# table11_1=table11_1.set_index('Job Type')
# table11_1 = table11_1.replace(',',"", regex=True).astype(float)
# table11_1=table11_1.to_sql('table11_1',conn)