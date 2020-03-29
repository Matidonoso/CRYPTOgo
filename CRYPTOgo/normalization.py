from sklearn.preprocessing import MinMaxScaler
import numpy as np


#Here we normalize the values to -1 , 1 range

scaler = MinMaxScaler()

def normalization(dataframe):

  # The scaler expects the data to be shaped as (x, y), so we add a dummy dimension using reshape before applying it.
  close_price = dataframe.close.values.reshape(-1,1)

  scaled_close = scaler.fit_transform(close_price)

  # Let’s also remove NaNs since our model won’t be able to handle them well
  scaled_close = scaled_close[~np.isnan(scaled_close)]
  
  scaled_close = scaled_close.reshape(-1, 1)

  return scaled_close