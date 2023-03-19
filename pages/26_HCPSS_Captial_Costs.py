import streamlit as st
from modules.hcpss_captial_costs import projected_school_construction_hocobydesign_method, cip_hocobydesign_method,\
      land_acquisition_hocobydesign_method, projected_school_construction_total_funding_method, cip_total_funding_method,\
      land_acquisition_total_funding_method, hcpss_captial_total_expenditure

st.header(':school: Projected HCPSS Capital Costs General Fund Expenditure')

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
school_type = ['Elementary School', 'Middle School', 'High School']
method = ['HoCoByDesign Approach 50% PAYGO and 50% Debt', '100% PAYGO using county\'s per-student costs',\
                                              '100% PAYGO using updated per-student costs']
year1=2023
years = [year1+x for x in range(18)]

st.markdown('---')

st.markdown("""
The County claims residential development pays for itself while using revenue from development to cover costs for
past captial expenditure. It uses bonds to pay for current capital expenditure and it pays debt service on that expenditure.
The calculation herein provides three methodologies to illustrate the impact of the county's assumptions.

The first method simply reproduces the county approach: 50% PAYGO and 50% Debt,\n
The second method modifies the county's approach as follows: 100% PAYGO using county's per-student costs,\n
The third method further modifies the county's approach as follows: 100% PAYGO using updated per-student costs

""")

expander = st.expander('Projection of School Capacity Costs by Different Methodologies')
with expander:
    select_method = st.selectbox('Pick a Method',method, key=3)
    if select_method == method[0]:
        display_projected_cost = projected_school_construction_hocobydesign_method()
        display_cip_cost = cip_hocobydesign_method()
        display_land_acquisition = land_acquisition_hocobydesign_method()
        display_total_expenditure = hcpss_captial_total_expenditure()[0]
        markdown_data = """
        The following table displays the total cost due to school construction, land-acquisition, and capital improvement plan
        calculated using the county's approach. In this case the county assumes half of the captial expenditure to build schools
        comes from PAYGO and the remaning is financed by debt.
        """
    elif select_method == method[1]:
        display_projected_cost = projected_school_construction_hocobydesign_method()
        display_cip_cost = cip_hocobydesign_method()
        display_land_acquisition = land_acquisition_hocobydesign_method()
        display_total_expenditure = hcpss_captial_total_expenditure()[1]
        markdown_data = """
        This table assumes that the entire cost of to build schools is funded by PAYGO. This is more accurate if the claim is that
        development pays for itself. It uses the county's per-student cost.
        """
    elif select_method == method[2]:
        display_projected_cost = projected_school_construction_total_funding_method()
        display_cip_cost = cip_total_funding_method()
        display_land_acquisition = land_acquisition_total_funding_method()
        display_total_expenditure = hcpss_captial_total_expenditure()[2]
        markdown_data = """
        This table also assumes that the entire cost of to build schools is funded by PAYGO. But the per-student cost is upated to
        reflect the actual historical costs inccurred by the county over the past few years.
        """
    display_total_expenditure.loc['Total']=display_total_expenditure.loc['Columbia':'South East', years].sum()
    st.markdown(markdown_data)
    st.dataframe(display_total_expenditure.style.format('$ {:,.2f}'))
   
st.markdown('---')

expander4 = st.expander('Projected Total Expenditure for School Construction, Land Acquisition, and Capital Improvement Plan')
with expander4:
    if select_method == method[0]:
        to_display = display_projected_cost[4]
        to_display2 = display_projected_cost[5]
        to_display.loc['Total'] = to_display.loc['Columbia':'South East', years].sum()
        to_display2.loc['Total'] = to_display2.loc['Columbia':'South East', years].sum()
        st.markdown('##### PAYGO HCPSS Capital Costs')
        st.dataframe(to_display.style.format('$ {:,.2f}'))
        st.markdown('---')
        st.markdown('##### Total Cumulative Debt Service')
        st.dataframe(to_display2.style.format('$ {:,.2f}'))
    else:
        to_display = display_projected_cost[3]
        to_display.loc['Total'] = to_display.loc['Columbia':'South East', years].sum()
        st.markdown('##### Total School Projected Construction Cost')
        st.dataframe(to_display.style.format('$ {:,.2f}'))
    st.markdown('---')
    st.markdown('##### Total School Land Acquisition Cost')
    to_display = display_land_acquisition[3]
    to_display.loc['Total'] = to_display.loc['Columbia':'South East', years].sum()
    st.dataframe(to_display.style.format('$ {:,.2f}'))
    st.markdown('---')
    st.markdown('##### Total Capital Improvement Plan')
    to_display = display_cip_cost
    to_display.loc['Total'] = to_display.loc['Columbia':'South East', years].sum()
    st.dataframe(to_display.style.format('$ {:,.2f}'))

st.markdown('---')

col1, col2 = st.columns(2)
with col1:
    select_region = st.selectbox('Select Planning Area',regions, key=1)
with col2:
    select_school_type = st.selectbox('Select School Type',school_type, key=2)

expander1 = st.expander('Projected School Construction and Land Acquisition Cost by Planning Area HoCoByDesign Method')
with expander1:
    if select_region and select_school_type:
        st.markdown(f'##### {select_school_type} Projected Construction Cost by Planning Area')
        st.dataframe(display_projected_cost[school_type.index(select_school_type)][regions[regions.index(select_region)]].style.format('$ {:,.2f}'))
        st.markdown('---')
        st.markdown(f'##### {select_school_type} Projected Land Acquisition Cost by Planning Area')
        st.dataframe(display_land_acquisition[school_type.index(select_school_type)][regions[regions.index(select_region)]].style.format('$ {:,.2f}'))