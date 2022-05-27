
import plotly.express as px
import pandas as pd

d = {[{'date': [1, 2], 'jaccard distance': [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]},{'date': [10, 20], 'jaccard distance': [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}]}
df = pd.DataFrame(data=d)

print(type(df))

fig = px.line(df, x="date", y=df.columns,
              hover_data={"date": "|%B %d, %Y"},
              title='Potency of topics based on ')
fig.update_xaxes(
    dtick="M1",
    tickformat="%b\n%Y",
    ticklabelmode="period")
fig.show()
