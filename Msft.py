import csv
import pandas as pd
from plotting import Ploty
import streamlit as st
from func_data import summarize

class mcft():
    def __init__(self):
        self.r=0
    def prlt(self):

        df =pd.read_csv('msft.csv')

        close_price=df['Close']
        open_price=df['Open']
        low_price=df['Low']
        high_price=df['High']

        close = Ploty(close_price)
        close.ploty('close price')

        close_data=summarize(close_price)
        st.write(close_data)


        open1 = Ploty(open_price)
        open1.ploty('open price')

        open1_data=summarize(open_price)
        st.write(open1_data)

        low = Ploty(low_price)
        low.ploty('low price')

        low_data=summarize(low_price)
        st.write(low_data)

        high = Ploty(high_price)
        high.ploty('high price')

        high_data=summarize(high_price)
        st.write(high_data)