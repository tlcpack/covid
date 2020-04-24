import pycountry
import plotly.express as px
import pandas as pd

URL = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df1 = pd.read_csv(URL)
print(df1.head(3))
print(df1.tail(3))