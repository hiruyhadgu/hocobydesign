import pandas as pd
from modules.assumptions_and_constants import taxes_fees, assumptions, tax_exemptions

def property_tax(market_value, av_ratio):
    property_tax = (market_value*av_ratio/100*taxes_fees().iloc[:4,:].sum()+taxes_fees().iloc[4,0])/12
    return  property_tax

def mortgage_calculation(p,i,n):
    i=i/12
    monthly_payment = p*(i*(1+i)**n)/((1+i)**n-1)
    return monthly_payment

def income_tax(region,assessed_val_cat):
    r = len(assessed_val_cat['Market Value Per unit'])
    list_avail = ['Category','SFD', 'SFA','Condo_Apts']
    region[:0]=['Gross Income']
    region =pd.DataFrame(region).T
    region.columns=list_avail
    region = region.set_index('Category')
    region.loc['Monthly Income']=region.iloc[0,:]/12
    region.loc['Affordability Amount']=region.iloc[1,:]*assumptions().iloc[2,0]
    region.loc['Market Value']=assessed_val_cat.iloc[:r,1].tolist()
    region.loc['Loan Amount']=region.loc['Market Value']*(1-assumptions().iloc[4,0])
    region.loc['Mortgage Payment']=[0]*r
    region.loc['Property Taxes']=[0]*r
    

    x=0
    for i in region.iloc[4,:].tolist():
        region.iloc[5,x]=mortgage_calculation(i,assumptions().iloc[3,0],360).squeeze()
        x=x+1
    x=0
    for i in region.iloc[3,:].tolist():
        region.iloc[6,x]=property_tax(i,assumptions().iloc[0,0]).squeeze()
        x=x+1

    region.loc['HOA']=assumptions().iloc[6,0]
    insurance_assignment = [assumptions().iloc[7,0],assumptions().iloc[7,0],assumptions().iloc[8,0]]
    region.loc['Insurance']=insurance_assignment[0:r]
    region.loc['Total Monthly Payment']=region.iloc[5:,:].sum()
    region.loc['First Month Interest']=region.loc['Loan Amount']*assumptions().iloc[3,0]/12
    region.loc['Gross Income to Market Value Ratio']=region.loc['Gross Income']/ region.loc['Market Value']
    region.loc['Monthly Mortgage Deduction']=[0]*r
    y=0
    for i in region.loc['Property Taxes'].tolist():
        i=i.squeeze()*12
        if i >10000: 
            i = 10000 
        interest_ded = i/12
        region.iloc[12,y]= interest_ded + region.iloc[10,y]
        y=y+1
    region.loc['Annual Mortgage Deduction']=region.loc['Monthly Mortgage Deduction']*12
    region.loc['Number of Exemptions']=tax_exemptions()['Value'].to_list()[:r]
    region.loc['Adjustment of AGI']=region.loc['Number of Exemptions']*tax_exemptions().loc['Non Rental Exemption'].squeeze()
    region.loc['Total Adjustments - Net Taxable Income']= region.loc['Gross Income']-(region.loc['Annual Mortgage Deduction']+region.loc['Adjustment of AGI'])
    region.loc['Net Taxable Income Ratio']=region.loc['Total Adjustments - Net Taxable Income']/region.loc['Gross Income']
    region.loc['Resulting Income Tax per Unit']=region.loc['Total Adjustments - Net Taxable Income']*assumptions().loc['Income Tax Rate'].squeeze()

    return region


def rental_income_tax(region,assessed_val_cat):
    region = pd.DataFrame(region).reset_index()
    region.columns = ['Category','Rental Apts']
    r = len(assessed_val_cat['Market Value Per unit'])
    region.iloc[0,0]='Gross Income'
    region = region.set_index('Category')
    region.loc['Monthly Income']=region.iloc[0,:]/12
    region.loc['Affordability Amount']=region.iloc[1,:]*assumptions().iloc[9,0]
    region.loc['Number of Exemptions']=tax_exemptions()['Value'].to_list()[2]
    region.loc['Adjustment of AGI']=region.loc['Number of Exemptions']*tax_exemptions().loc['Rental Exemption'].squeeze()
    region.loc['Standard State Deduction']=tax_exemptions().loc['Rental Exemption'].squeeze()
    region.loc['Total Adjustments - Net Taxable Income']= region.loc['Gross Income']-(region.loc['Standard State Deduction']+region.loc['Adjustment of AGI'])
    region.loc['Net Taxable Income Ratio']=region.loc['Total Adjustments - Net Taxable Income']/region.loc['Gross Income']
    region.loc['Resulting Income Tax per Unit']=region.loc['Total Adjustments - Net Taxable Income']*assumptions().loc['Income Tax Rate'].squeeze()
    region.loc['Income Tax for MIHU']=region.loc['Resulting Income Tax per Unit']*assumptions().loc['MIHU Tax Adjustment'].squeeze()
    region.loc['Weighted Average Income Tax'] = region.loc['Income Tax for MIHU']*assumptions().loc['MIHU'].squeeze()+\
            region.loc['Resulting Income Tax per Unit']*(1-assumptions().loc['MIHU'].squeeze())
    return region

def adu_income_tax(region,assessed_val_cat):
    region = pd.DataFrame(region).reset_index()
    region.columns = ['Category','Accessory Dwelling Units']
    r = len(assessed_val_cat['Market Value Per unit'])
    region.iloc[0,0]='Gross Income'
    region = region.set_index('Category')
    region.loc['Monthly Income']=region.iloc[0,:]/12
    region.loc['Affordability Amount']=region.iloc[1,:]*assumptions().iloc[2,0]
    region.loc['Market Value']=assessed_val_cat.iloc[:r,1].tolist()
    region.loc['Loan Amount']=region.loc['Market Value']*(1-assumptions().iloc[4,0])
    region.loc['Mortgage Payment']=[0]*r
    region.loc['Property Taxes']=[0]*r

    x=0
    for i in region.iloc[4,:].tolist():
        region.iloc[5,x]=mortgage_calculation(i,assumptions().iloc[3,0],360).squeeze()
        x=x+1
    x=0
    for i in region.iloc[3,:].tolist():
        region.iloc[6,x]=property_tax(i,assumptions().iloc[0,0]).squeeze()
        x=x+1
    region.loc['HOA']=assumptions().iloc[6,0]
    insurance_assignment = [assumptions().iloc[7,0],assumptions().iloc[7,0],assumptions().iloc[8,0]]
    region.loc['Insurance']=insurance_assignment[0:r]
    region.loc['Total Monthly Payment']=region.iloc[5:,:].sum()
    region.loc['First Month Interest']=region.loc['Loan Amount']*assumptions().iloc[3,0]/12
    region.loc['Gross Income to Market Value Ratio']=region.loc['Gross Income']/region.loc['Market Value']
    region.loc['Monthly Mortgage Deduction']=[0]*r
    y=0
    for i in region.loc['Property Taxes'].tolist():
        i=i*12
        if i >10000: 
            i = 10000 
        interest_ded = i/12
        region.iloc[12,y]= interest_ded + region.iloc[10,y]
        y=y+1

    region.loc['Annual Mortgage Deduction']=region.loc['Monthly Mortgage Deduction']*12
    region.loc['Number of Exemptions']=tax_exemptions()['Value'].to_list()[:r]
    region.loc['Adjustment of AGI']=region.loc['Number of Exemptions']*tax_exemptions().loc['Non Rental Exemption'].squeeze()
    region.loc['Total Adjustments - Net Taxable Income']= region.loc['Gross Income']-(region.loc['Annual Mortgage Deduction']+region.loc['Adjustment of AGI'])
    region.loc['Net Taxable Income Ratio']=region.loc['Total Adjustments - Net Taxable Income']/region.loc['Gross Income']
    region.loc['Resulting Income Tax per Unit']=region.loc['Total Adjustments - Net Taxable Income']*assumptions().loc['Income Tax Rate'].squeeze()

    return region

def rural_income_tax(region,assessed_val_cat):
    r = len(assessed_val_cat['Market Value Per unit'])
    list_avail = ['Category','SFD']
    region = region[0:r]
    region[:0]=['Gross Income']
    region =pd.DataFrame(region).T
    region.columns=list_avail
    region = region.set_index('Category')
    region.loc['Monthly Income']=region.iloc[0,:]/12
    region.loc['Affordability Amount']=region.iloc[1,:]*assumptions().iloc[2,0]
    region.loc['Market Value']=assessed_val_cat.iloc[:r,1].tolist()
    region.loc['Loan Amount']=region.loc['Market Value']*(1-assumptions().iloc[4,0])
    region.loc['Mortgage Payment']=[0]*r
    region.loc['Property Taxes']=[0]*r

    x=0
    for i in region.iloc[4,:].tolist():
        region.iloc[5,x]=mortgage_calculation(i,assumptions().iloc[3,0],360).squeeze()
        x=x+1
    x=0
    for i in region.iloc[3,:].tolist():
        region.iloc[6,x]=property_tax(i,assumptions().iloc[0,0]).squeeze()
        x=x+1

    region.loc['HOA']=assumptions().iloc[6,0]
    insurance_assignment = [assumptions().iloc[7,0],assumptions().iloc[7,0],assumptions().iloc[8,0]]
    region.loc['Insurance']=insurance_assignment[0:r]
    region.loc['Total Monthly Payment']=region.iloc[5:,:].sum()
    region.loc['First Month Interest']=region.loc['Loan Amount']*assumptions().iloc[3,0]/12
    region.loc['Gross Income to Market Value Ratio']=region.loc['Gross Income']/region.loc['Market Value']
    region.loc['Monthly Mortgage Deduction']=[0]*r
    y=0
    for i in region.loc['Property Taxes'].tolist():
        i=i.squeeze()*12
        if i >10000: 
            i = 10000 
        interest_ded = i/12
        region.iloc[12,y]= interest_ded + region.iloc[10,y]
        y=y+1
    region.loc['Annual Mortgage Deduction']=region.loc['Monthly Mortgage Deduction']*12
    region.loc['Number of Exemptions']=tax_exemptions()['Value'].to_list()[:r]
    region.loc['Adjustment of AGI']=region.loc['Number of Exemptions']*tax_exemptions().loc['Non Rental Exemption'].squeeze()
    region.loc['Total Adjustments - Net Taxable Income']= region.loc['Gross Income']-(region.loc['Annual Mortgage Deduction']+region.loc['Adjustment of AGI'])
    region.loc['Net Taxable Income Ratio']=region.loc['Total Adjustments - Net Taxable Income']/region.loc['Gross Income']
    region.loc['Resulting Income Tax per Unit']=region.loc['Total Adjustments - Net Taxable Income']*assumptions().loc['Income Tax Rate'].squeeze()

    return region