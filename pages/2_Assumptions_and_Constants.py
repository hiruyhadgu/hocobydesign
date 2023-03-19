import streamlit as st
from modules.assumptions_and_constants import assumptions, tax_exemptions, taxes_fees, tax_cat_factors,\
     jobs_to_building_ratio, transfer_tax_allocation, gross_income, hoco_population, education_expenditure_factors,\
        school_construction_cost, hcc_data, non_residential_trip_constants, cip_projection, land_acquisition_cost,\
            non_residential_vehicle_trips, hcpss_debt_service, general_obligation_bonds_trend
from modules.get_tables import student_yields, school_enrollment, road_expenditure
st.header('Assumptions, Constants, and Factors Used in Projections')

st.markdown('---')

col1, col2 = st.columns(2)

with col1:
    expander1 = st.expander('Assumptions used to Calculate Income Tax Rates')
    with expander1:
        st.dataframe(assumptions().reset_index())

with col2:
    expander2 = st.expander('Other Revenues Factors')
    with expander2: 
        st.dataframe(tax_cat_factors().reset_index())

st.markdown('---')


col3, col4 = st.columns(2)

with col3:
    expander3 = st.expander('Tax Exemptions and Persons Per Unit')
    with expander3:
        st.dataframe(tax_exemptions().reset_index())

with col4:
    expander4 = st.expander('Taxes and Fees')
    with expander4:
        st.dataframe(taxes_fees().reset_index())

st.markdown('---')

col5, col6 = st.columns(2)

with col5:

    expander5 = st.expander('Transfer Tax and Allocations')
    with expander5:
        st.dataframe(transfer_tax_allocation().reset_index())

with col6:
    expander6 = st.expander('Jobs to Building Ratio')
    with expander6:
        st.dataframe(jobs_to_building_ratio().reset_index())

st.markdown('---')

col7, col8 = st.columns(2)

with col7:
    expander7 = st.expander('Gross Income (SFD, SFA, Condos)')
    with expander7:
        st.dataframe(gross_income()[0].reset_index())

with col8:
    expander8 = st.expander('Gross Income (Rentals, ADUs)')
    with expander8:
        st.dataframe(gross_income()[1].reset_index())
   
st.markdown('---')


# col9, col10 = st.columns(2)

# with col9:
expander7 = st.expander('Annual School Enrollment)')
with expander7:
    st.dataframe(school_enrollment())

st.markdown('---')

expander8 = st.expander('Student Yield (Elementary and Middle)')
with expander8:
    col9, col10 = st.columns(2)
    with col9:
        st.dataframe(student_yields()[0])
    with col10:
        st.dataframe(student_yields()[1])

st.markdown('---')

expander9 = st.expander('Student Yield (High School and Total')
with expander9:
    col11, col12 = st.columns(2)
    with col11:
        st.dataframe(student_yields()[2])
    with col12:
        st.dataframe(student_yields()[3])

st.markdown('---')

expander10 = st.expander('HoCo Population and Education Expenditure Factors')
with expander10:
    col13, col14 = st.columns(2)
    with col13:
        st.dataframe(hoco_population())
    with col14:
        st.dataframe(education_expenditure_factors())

st.markdown('---')

expander11 = st.expander('HoCo School Construction')
with expander11:
    st.dataframe(school_construction_cost()[0])
    st.markdown('---')
# with col16:
    st.dataframe(school_construction_cost()[1])
    st.markdown('---')
# col17, col18 = st.columns(2)
# with col17:
    st.dataframe(school_construction_cost()[2])
    st.markdown('---')
# with col18:
    st.dataframe(cip_projection())
    st.markdown('---')
    st.dataframe(land_acquisition_cost())

st.markdown('---')

expander12 = st.expander('Howard Community College Historical Captial Funding')
with expander12:
    st.dataframe(hcc_data())

st.markdown('---')

expander13 = st.expander('Non Residential Trip Calculation Constants')
with expander13:
    st.dataframe(non_residential_trip_constants())

st.markdown('---')

expander14 = st.expander('Total Vehicle Trip Calculation and Historical HCPSS Debt Service')
with expander14:
    col15, col16 = st.columns(2)
    with col15:
        st.dataframe(non_residential_vehicle_trips('hocobydesign'))
    with col16:
        st.dataframe(hcpss_debt_service())

st.markdown('---')

expander15 = st.expander('Historical Road Construction Spending')
with expander15:
    st.dataframe(road_expenditure())

expander16 = st.expander('Historical General Obligation Bonds')
with expander16:
    st.dataframe(general_obligation_bonds_trend())

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)