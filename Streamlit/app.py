import streamlit as st
import pandas as pd
st.write("""
# My first app
Hello *world!*
""")
df = pd.read_csv("./HistoricalQuotes.csv", index_col=0)
df[df.columns[:]] = df[df.columns[:]].replace('[\$,]', '', regex=True).astype(float)
st.line_chart(df[" Open"][:250])


st.write("""
# Apps with widgets!
""")
x = st.slider("Select a number", 0, 100, 17)
st.write("You selected", x)

