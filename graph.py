import pandas as pd
import plotly.express as px

data = pd.read_csv("data.csv")
fig  = px.scatter(data , x = "date" , y = "cases" , color = "country", title = "Date Wise covid cases")
fig.show()