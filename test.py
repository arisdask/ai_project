import csv
import pandas as pd
from plotting import Ploty
import streamlit as st
from func_data import summarize

class Tesla():
    def __init__(self):
        self.r=0
    def prlt(self):
        data = [
            ["Date", "Close Price", "Open Price", "Low Price", "High Price"],
            ["2024-04-01", 960.25, 965.50, 955.75, 970.00],
            ["2024-04-02", 965.75, 960.00, 955.25, 970.50],
            ["2024-04-03", 970.50, 975.00, 965.25, 978.00],
            ["2024-04-04", 972.25, 970.25, 965.75, 975.50],
            ["2024-04-05", 974.00, 975.50, 970.25, 978.25],
            ["2024-04-06", 975.75, 977.00, 973.50, 980.00],
            ["2024-04-07", 973.50, 975.75, 970.00, 977.25],
            ["2024-04-08", 972.75, 975.00, 970.25, 976.00],
            ["2024-04-09", 975.25, 973.00, 968.75, 977.00],
            ["2024-04-10", 978.50, 977.25, 973.00, 981.00],
            ["2024-04-11", 982.25, 980.50, 976.75, 985.00],
            ["2024-04-12", 986.00, 982.75, 978.50, 988.25],
            ["2024-04-13", 989.75, 987.25, 983.00, 992.00],
            ["2024-04-14", 993.25, 991.00, 988.25, 996.50],
            ["2024-04-15", 996.50, 994.00, 991.75, 998.75],
            ["2024-04-16", 999.00, 997.00, 994.25, 1002.50],
            ["2024-04-17", 1002.75, 1001.00, 998.25, 1005.00],
            ["2024-04-18", 1005.25, 1003.00, 1000.25, 1008.50],
            ["2024-04-19", 1007.75, 1006.50, 1003.75, 1010.25],
            ["2024-04-20", 1010.00, 1008.00, 1005.25, 1012.75],
            ["2024-04-21", 1013.25, 1011.25, 1008.50, 1015.50],
            ["2024-04-22", 1016.50, 1014.00, 1010.25, 1018.75],
            ["2024-04-23", 1019.00, 1017.25, 1014.50, 1022.00],
            ["2024-04-24", 1021.25, 1020.00, 1017.50, 1023.75],
            ["2024-04-25", 1023.75, 1022.25, 1020.00, 1026.50],
            ["2024-04-26", 1025.50, 1024.00, 1021.75, 1028.75],
            ["2024-04-27", 1027.75, 1026.00, 1023.25, 1030.25],
            ["2024-04-28", 1030.25, 1028.50, 1026.00, 1032.50],
            ["2024-04-29", 1033.00, 1031.00, 1028.25, 1035.25],
            ["2024-04-30", 1035.50, 1034.00, 1031.25, 1037.75]
        ]

# Save data to a CSV file
        with open('tesla_stock_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        print("Data has been saved to tesla_stock_data.csv")
        import pandas as pd
        df =pd.read_csv('tesla_stock_data.csv')

        close_price=df['Close Price']
        open_price=df['Open Price']
        low_price=df['Low Price']
        high_price=df['High Price']

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