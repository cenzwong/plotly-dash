import streamlit as st
import pandas as pd
st.write("""
# Interactive Example Page
Hello *world!*
""")

if st.button('Say Hello'):
    st.write('Why hello there')
else:
    st.write('Goodbyte')

st.write("""
## This is Check box
""")

agree = st.checkbox('I agree')
if agree:
    st.write('Great!')

st.write("""
## This is Radio button
""")
genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")

st.write("""
## This is Select Box
""")
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)

st.write("""
## This is MultiSelect
""")
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])
st.write('You selected:', options)

st.write("""
## This is Slider
""")
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

from datetime import time
appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

from datetime import datetime
start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

st.write("""
## This is select_slider
""")
color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)


st.write("""
## This is text_input
""")

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

st.write("""
## This is number_input
""")
number = st.number_input('Insert a number')
st.write('The current number is ', number)

st.write("""
## This is text_area
""")
txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')
st.write('Text:', txt)

st.write("""
## This is date_input
""")
import datetime
d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

st.write("""
## This is time_input
""")
t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)

st.write("""
## This is file_uploader
""")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.read()
    st.write(bytes_data)
    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

st.write("""
## This is color_picker
""")
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)