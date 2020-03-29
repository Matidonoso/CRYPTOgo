import matplotlib.pyplot as plt


def plot_close_price(dataframe, crypto):

  plt.plot(dataframe['close'], label="Close Price", color='red')
  plt.title('{} Historical Series'.format(crypto))
  plt.xlabel('Time')
  plt.ylabel('Price (USD)')
  plt.legend(loc='best')
  plt.show()
  