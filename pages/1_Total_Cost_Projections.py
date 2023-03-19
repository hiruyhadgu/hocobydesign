import streamlit as st
import pandas as pd
import sqlite3 as db
from modules.total_expenditure_projections import compiled_operating_expenditure_projections, compiled_capital_expenditure_projections
from PIL import Image
import plotly.express as px


st.header('HoCoByDesign Total Expenditure Projections')
st.markdown('---')

case = ['County Funding Only', 'County and State Funding']
select_case = st.selectbox('Pick a Method',case, key=1)
if select_case:
    display = compiled_operating_expenditure_projections()[case[case.index(select_case)]]

    st.dataframe(display.style.format('$ {:,.2f}'))

    fig = px.line(display.T, width=700, height=500,\
            labels=dict(index="Year", value="Annual Operating Expenditure ($)"))
    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ))

    st.plotly_chart(fig)


case1 = ['HoCoByDesign Approach 50% PAYGO and 50% Debt', '100% PAYGO using county\'s per-student costs',\
                                              '100% PAYGO using updated per-student costs']

select_case1 = st.selectbox('Pick a Method',case1, key=2)
if select_case1:
    display1 = compiled_capital_expenditure_projections()[case1[case1.index(select_case1)]]
    st.dataframe(display1.style.format('$ {:,.2f}'))

    fig1 = px.line(display1.T, width=700, height=500,\
               labels=dict(index="Year", value="Annual Capital Expenditure ($)"))
    fig1.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ))
    st.plotly_chart(fig1)



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