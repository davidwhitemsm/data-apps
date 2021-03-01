# import libraries needed
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# scrape 2020 race results from web and read into dataframe

df1 = pd.read_html('https://www.formula1.com/en/results.html/2020/drivers.html',header = 0)
df2 = df1[0]
df3 = df2.drop(columns=['Unnamed: 0','Unnamed: 6','Pos'])
df4 = df3.set_index('Driver')

# set wide page width

st.set_page_config(layout="wide")

# display title
st.title("2020 Formula 1 Drivers' Championship - Final Results")

# data source and additional information


st.write("""
Source: [formula1.com](https://www.formula1.com/en/results.html/2020/drivers.html)


""")


# plot bar chart
st.bar_chart(df4)
