import streamlit as st
from modules.projected_units import plan_area, people_generated

st.header('Projected Units and Population')

st.write("""
The fiscal impact methdology and analysis assumes that 25,000 units will be developed by 2040.
The total number of units are divided by 18 years to calculate the number of units per year. Also,
the number of people per unit (see Assumptions and Constants) are used to calculate the increase in
population per year.
""")
         
st.markdown('---')

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
year1=2023
years = [year1+x for x in range(18)]

expander = st.expander('Projected Units and Employment by Plan Area')

with expander:
    select_planning_area = st.selectbox('Select Planning Area',regions)
    if select_planning_area:
        st.markdown('#### Number of Units by Plan Area')
        display_units_by_plan_area = plan_area()[0][select_planning_area]
        display_units_by_plan_area.loc['Total'] = display_units_by_plan_area[years].sum()
        st.dataframe(display_units_by_plan_area.style.format(precision=2))

        st.markdown('---')

        st.markdown('#### People by Plan Area')
        display_units_by_people_area = people_generated()[0][select_planning_area]
        display_units_by_people_area.loc['Total'] = display_units_by_people_area[years].sum()
        st.dataframe(display_units_by_people_area.style.format(precision=2))

st.markdown('---')

expander1 = st.expander('Total Projected Units and Employment')
with expander1:
    st.markdown('#### Total Number of Units')
    display_plan_area = plan_area()[1]
    display_plan_area.loc['Total'] = display_plan_area.loc['Columbia':'South East',years].sum()
    st.dataframe(display_plan_area.style.format(precision=2))

    st.markdown('---')
    
    st.markdown('#### Total Number of People')
    display_people_generated = people_generated()[1]
    display_people_generated.loc['Total'] = display_people_generated.loc['Columbia':'South East',years].sum()
    st.dataframe(display_people_generated.style.format(precision=2))
    


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