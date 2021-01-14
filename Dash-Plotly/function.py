## ============== Plotly Express (Return Figure)==========================
df_column_draw_pie_chart(df_covid,'Gender', 'Gender of the infected').show()
def df_column_draw_pie_chart(df, columnName, figTitle):
    labels = [arr for arr in df[columnName].unique()]
    values = [df[columnName].value_counts()[label] for _,label in enumerate(labels)]
    fig = go.Figure(data=[go.Pie(labels=labels, 
                                    values=values, 
                                    title=figTitle,
                                )
                        ]
                    )
    return fig

df_column_count_line_chart(df_covid, 'Report date', 'Infected People Daily').show()
df_column_count_line_chart(df_covid, 'Report date', 'Infected People Daily', 'cumsum').show()
def df_column_count_line_chart(df, columnName, figTitle, mode="count"):
    df_countByDate = df_covid[columnName].value_counts().sort_index()
    if mode == "count":
        fig = px.line(df_countByDate, title=figTitle)
    elif mode == "cumsum":
        fig = px.line(df_countByDate.cumsum(), title=figTitle)
    return fig

df_column_histogram(df_covid, "Age", "Histogram of the infected age").show()
def df_column_histogram(df, columnName, figTitle):
    fig = px.histogram(df, x=columnName, title=figTitle)
    return fig

df_bubble_chart(df_cluster2, "Report date", "Case no.", "Number of cases", "Cluster", "Cluster of the infected cases").show()
def df_bubble_chart(df, dfx, dfy, dfsize, hoverName, titleName):
    fig = px.scatter(df, x=dfx,y=dfy,
	                    size=dfsize,  
                        hover_name=hoverName, size_max=60, title=titleName)
    return fig

## ============== Plotly GO (Return Go Obj) =======================
def go_df_plot(df,dfx,dfy,lineName):
    go_obj = go.Scatter(x=df[dfx].to_list(), y=df[dfy].to_list(),
                    mode='lines',
                    name=lineName)
    return go_obj

def go_df_count_plot(df,dfx,lineName,mode="count"):
    df_countByDate = df[dfx].value_counts().sort_index()
    if mode == 'cumsum':
        df_countByDate = df_countByDate.cumsum()
    go_obj = go.Scatter(x=df_countByDate.index.to_list(),y=df_countByDate.to_list(),
                    mode='lines',
                    name=lineName)
    return go_obj

def go_df_bubble_chart(df,dfx,dfy,dfsize,dfhover, lineName):
    go_obj = go.Scatter(
        x=df[dfx].to_list(), y=df[dfy].to_list(),
        mode='markers',
        marker=dict(
            size=df[dfsize].to_list(),
            sizemode='area',
            sizeref=0.2,
            sizemin=1,
        ),
        hovertext=df[dfhover].to_list(),
        name=lineName,
    )
    return go_obj

# from plotly.subplots import make_subplots
# # Create figure with secondary y-axis
# fig = make_subplots(specs=[[{"secondary_y": True}]])
# fig.add_trace(go_df_bubble_chart(df_cluster2,"Report date","Case no.","Number of cases","Cluster", lineName="Big Cluster"))
# fig.add_trace(go_df_count_plot(df_covid,"Report date", lineName="Total Infected Case",mode="cumsum"))
# fig.add_trace(go_df_count_plot(df_covid,"Report date", lineName="Daily Infected Case",mode="count"), secondary_y=True)
# # Add figure title
# fig.update_layout(
#     title_text="Summary of Hong Kong COVID19 Cases"
# )
# # Set x-axis title
# fig.update_xaxes(title_text="Date")
# # Set y-axes titles
# fig.update_yaxes(title_text="<b>Total</b> Cases", secondary_y=False)
# fig.update_yaxes(title_text="<b>Daily</b> Cases", secondary_y=True)
# fig.show()

