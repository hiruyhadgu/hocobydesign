import streamlit as st
import pandas as pd
import sqlite3 as db
from modules.total_revenues_projection import cumulative_projections
from PIL import Image
import plotly.express as px

image = Image.open('combined.jpeg')
# st.sidebar.image("combined.jpeg", use_column_width=True)
st.set_page_config(page_title='HoCo By Design r', page_icon=image)

conn5 = db.connect('hocobydesign.db')
c = conn5.cursor()

year1=2023
years = [year1+x for x in range(18)]

st.header('HoCoByDesign Total Revenue Projections')

st.markdown('---')

projected_revenues = cumulative_projections()
projected_revenues.loc['Total Revenues']=projected_revenues.loc['Total Operating Revenues'] + projected_revenues.loc['Total Capital Revenues']
st.dataframe(projected_revenues.style.format('$ {:,.2f}'))

fig = px.line(projected_revenues.T, width=700, height=500,\
               labels=dict(index="Year", value="Annual Revenue ($)"))
fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01
))

st.plotly_chart(fig)

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