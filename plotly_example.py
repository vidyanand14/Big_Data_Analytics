import plotly.express as px 

# using the iris dataset
df = px.data.iris() 

# plotting the bar chart
fig = px.bar(df, x="sepal_width", y="sepal_length") 

# showing the plot
fig.show()


