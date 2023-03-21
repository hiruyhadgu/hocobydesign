import streamlit as st
from modules.projected_ronresidential_build import non_res_builds

st.header(':office: :department_store: :factory: Projected Non Residential Expansion')

st.write("""
The fiscal impact methdology and analysis assumes that 31,500 jobs will be created by 2040. The jobs
are spread out among the planning areas. The total number of jobs are are divided by 18 years to calculate 
jobs created per year.
""")
         
st.markdown('---')

regions = ['Columbia','Elkridge','Ellicott City', 'Rural West','South East']
assessed_cat = ['table_columbia', 'table_elkridge','table_ellicott_city','table_rural_west','table_south_east']
year1=2023
years = [year1+x for x in range(18)]

expander = st.expander('Projected Non Residential Addition by Square Footage and Assessments')
with expander:

    select_region2 = st.selectbox('**Select Planning Area:**',regions)

    if select_region2:
        reg = regions[regions.index(select_region2)]
        st.markdown('#### Projected Non Residential Addition by Square Footage')
        st.dataframe(non_res_builds()[0][reg].style.format(precision=2))

        st.markdown('---')

        st.markdown('#### Assessment of Projected Non Residential Addition')
        st.dataframe(non_res_builds()[1][reg].style.format('$ {:,.2f}'))

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