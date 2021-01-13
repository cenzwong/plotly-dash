def df_column_draw_pie_chart(columnName):
    labels = [arr for arr in df[columnName].unique()]
    values = [df[columnName].value_counts()[label] for _,label in enumerate(labels)]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    return fig
    
df_column_draw_pie_chart('Gender').show()
