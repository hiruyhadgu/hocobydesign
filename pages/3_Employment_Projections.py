import streamlit as st
from modules.employment_data import job_type

st.header(':factory_worker: :farmer: :scientist: :office_worker: Projected Annual Employment')

st.write("""
The fiscal impact methdology and analysis assumes that 31,500 jobs will be created by 2040. The jobs
are spread out among the planning areas. The total number of jobs are are divided by 18 years to calculate 
jobs created per year.
""")
         
st.markdown('---')

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
year1=2023
years = [year1+x for x in range(18)]

expander = st.expander('Projected Jobs by Plan Area')

with expander:
    select_planning_area = st.selectbox('Select Planning Area',regions)

    if select_planning_area:
        st.markdown('#### Jobs Created by Plan Area')
        display_jobs_by_planning_area = job_type()[0][regions[regions.index(select_planning_area)]]
        display_jobs_by_planning_area.loc['Total'] = display_jobs_by_planning_area[years].sum()
        st.dataframe(display_jobs_by_planning_area.style.format(precision=2))

st.markdown('---')

expander1 = st.expander('Total Jobs')
with expander1:
    st.markdown('#### Total Number of Jobs')
    display_total_jobs = job_type()[1]
    display_total_jobs.loc['Total'] = display_total_jobs.loc['Columbia':'South East',years].sum()
    st.dataframe(display_total_jobs.style.format(precision=2))

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