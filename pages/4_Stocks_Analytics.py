import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from test import Tesla
from Sp500 import SP
from Msft import mcft
st.title("Stock Market Calculations")


with st.form("myform"):
    import streamlit as st

    col1, col2 = st.columns(2)
    with col1:
        # Create a menu of choices
        option = st.selectbox(
            'Select an option:',
            ('Tesla', 'sp500', 'Microsoft')
        )
    with col2:
        submitted = st.form_submit_button("Submit")

    # Execute code based on the selected choice
    str='Stocks Analytics'
    if option == 'Tesla':
        st.write(option+' '+str)
        Plots = Tesla()
        Plots.prlt()
    elif option == 'sp500':
        st.write(option+' '+str)
        # Add code to execute for Option 2
        Plts=SP()
        Plts.prlt()
    elif option == 'Microsoft':
        st.write(option+' '+str)
        Plts1=mcft()
        Plts1.prlt()
        # Add code to execute for Option 3

