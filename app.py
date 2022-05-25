import pandas as pd # pip install pandas openpyxl
import plotly.express as px # pip install plotly-express
import streamlit as st # pip install streamlit

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dahsboard", page_icon=":barc_chart:", layout="wide")

df = pd.read_excel(
  io='supermarkt_sales.xlsx',
  engine='openpyxl',
  sheet_name='Sales',
  skiprows=3,
  usecols='B:R',
  nrows=1000
)

st.dataframe(df)