import streamlit as st
from modules.hcpss_captial_costs import projected_school_construction, cip, land_acquisition

st.header('Projected HCPSS Capital Costs General Fund Expenditure')

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
year1=2023
years = [year1+x for x in range(18)]

hcpss_selected = st.checkbox('Use Total Funding Method')
if hcpss_selected==False:
    method = 'hocobydesign'
else:
    method = 'totalfundingmethod'

st.markdown('---')

expander1 = st.expander('Projected Elementary School Construction Cost by Planning Area')
with expander1:
    select_region = st.selectbox('Select Planning Area',regions, key=1)
    if select_region:
        st.markdown('##### Elementary School Projected Construction Cost by Planning Area')
        st.dataframe(projected_school_construction(method)[0][regions[regions.index(select_region)]].style.format('$ {:,.2f}'))
        st.markdown('---')
        st.markdown('##### Elementary School Projected Land Acquisition Cost by Planning Area')
        st.dataframe(land_acquisition(method)[0][regions[regions.index(select_region)]].style.format('$ {:,.2f}'))

st.markdown('---')

expander2 = st.expander('Projected Middle School Construction Cost by Planning Area')
with expander2:
    select_region1 = st.selectbox('Select Planning Area',regions, key=2)
    if select_region:
        st.markdown('##### Middle School Projected Construction Cost by Planning Area')
        st.dataframe(projected_school_construction(method)[1][regions[regions.index(select_region1)]].style.format('$ {:,.2f}'))
        st.markdown('---')
        st.markdown('##### Middle School Projected Land Acquisition Cost by Planning Area')
        st.dataframe(land_acquisition(method)[1][regions[regions.index(select_region1)]].style.format('$ {:,.2f}'))

st.markdown('---')

expander3 = st.expander('Projected High School Construction Cost by Planning Area')
with expander3:
    select_region2 = st.selectbox('Select Planning Area',regions, key=3)
    if select_region:
        st.markdown('##### High School Projected Construction Cost by Planning Area')
        st.dataframe(projected_school_construction(method)[2][regions[regions.index(select_region2)]].style.format('$ {:,.2f}'))
        st.markdown('---')
        st.markdown('##### High School Projected Land Acquisition Cost by Planning Area')
        st.dataframe(land_acquisition(method)[2][regions[regions.index(select_region2)]].style.format('$ {:,.2f}'))
   
st.markdown('---')

expander4 = st.expander('Projected Total Expenditure for School Construction, Land Acquisition, and Capital Improvement Plan')
with expander4:
    st.markdown('##### Total School Projected Construction Cost')
    to_display = projected_school_construction(method)[3]
    to_display.loc['Total'] = to_display.loc['Columbia':'South East', years].sum()
    st.dataframe(to_display.style.format('$ {:,.2f}'))
    st.markdown('---')
    st.markdown('##### Total School Land Aqcuisition Cost')
    to_display = land_acquisition(method)[3]
    to_display.loc['Total'] = to_display.loc['Columbia':'South East', years].sum()
    st.dataframe(to_display.style.format('$ {:,.2f}'))
    st.markdown('---')
    st.markdown('##### Total Capital Improvement Plan')
    to_display = cip(method)
    to_display.loc['Total'] = to_display.loc['Columbia':'South East', years].sum()
    st.dataframe(to_display.style.format('$ {:,.2f}'))

st.markdown('---')

expander4 = st.expander('Projected Total Expenditure for School Construction, Land Acquisition, and Capital Improvement Plan\                        Assuming 50% PAYGO and 50% Debt Service')
with expander4:
    st.markdown('##### PAYGO HCPSS Capital Costs')
    projected_school_construction(method)[4].loc['Total'] = projected_school_construction(method)[4].loc['Columbia':'South East', years].sum()
    st.dataframe(projected_school_construction(method)[4])
    st.markdown('---')
    st.markdown('##### Total Cumulative Debt Service')
    projected_school_construction(method)[5].loc['Total'] = projected_school_construction(method)[5].loc['Columbia':'South East', years].sum()
    st.dataframe(projected_school_construction(method)[5].cumsum(axis=1))