import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import seaborn as sns
class Ploty():
    def __init__(self,data):
        self.data=data
        self.x=np.arange(0,len(self.data),1)
    def ploty(self,str):
        fig, axs = plt.subplots(1, 2, figsize=(12, 6))

        # Plot on the first subplot
        axs[0].plot(self.x, self.data)
        axs[0].set_title('Plot')

        # Create a box plot on the second subplot
        sns.boxplot(self.data, ax=axs[1])
        axs[1].set_title('Box Plot')

        # Adjust layout
        plt.tight_layout()

        plt.ylabel(str)
        plt.xlabel('Last 100 days '+str)
        plt.grid(True)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()


