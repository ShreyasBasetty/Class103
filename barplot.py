import pandas as pd
import plotly.express as px

dr=pd.read_csv("data.csv")
fig=px.bar(dr,x="Country", y="InternetUsers")
fig.show()