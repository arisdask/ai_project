import pandas as pd
import numpy as np
def summarize(data):
    new_data={
        'Min':min(data),
        'Max':max(data),
        'Mean':data[int(len(data)/2)],
        'Average':np.average(data),
        'Standard Deviation':np.std(data)
    }
    df=pd.Series(new_data)
    return df
