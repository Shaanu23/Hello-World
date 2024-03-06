import streamlit as st
import pandas as pd
import numpy as np
import datetime

def main():
    st.title('Bye Everyone!')
    st.sidebar.title('Shaanu Sidebar.')
    st.sidebar.write('You can add widgets here:')
    st.write('')

    import streamlit as st
 
import streamlit as st


st.sidebar.markdown('<h1 style="color: pink;">Dashboard</h1>', unsafe_allow_html=True)
 
selection = st.sidebar.radio(
    label='Gehe zu:',
    options=['Todo','Rezepte','Rechnungen']
)

st.subheader('Welcome to the Website', divider='blue')
st.subheader('Data elements :heart:')
st.subheader(' ',divider='blue')


df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))

st.table(df)
st.subheader('Chart elements')
st.subheader(' ',divider='blue')

chart_data = pd.DataFrame(
       {
           "col1": np.random.randn(20),
           "col2": np.random.randn(20),
           "col3": np.random.choice(["Yes", "No", "Neither"], 20),
       }
    )

st.line_chart(chart_data, x="col1", y="col2", color="col3")

st.subheader('Input Widgets :birthday:')
st.subheader(' ',divider='blue')

d = st.date_input("When's your birthday", datetime.date(1999,12,23))
st.write('Your birthday is:', d)





