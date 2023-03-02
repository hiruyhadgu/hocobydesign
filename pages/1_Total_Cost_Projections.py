import streamlit as st
import pandas as pd
import sqlite3 as db
from modules.total_expenditure_projections import compiled_operating_expenditure_projections, compiled_capital_expenditure_projections
from PIL import Image

method = 'hocobydesign'

st.header('HoCoByDesign Total Expenditure Projections')
st.markdown('---')

st.dataframe(compiled_operating_expenditure_projections(method).style.format('$ {:,.2f}'))

st.dataframe(compiled_capital_expenditure_projections(method).style.format('$ {:,.2f}'))



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