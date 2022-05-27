import pandas as pd
import logging
from logging.handlers import TimedRotatingFileHandler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib import ticker
from statsmodels.tsa.stattools import adfuller, acf, pacf

class DeepLearning:
    def __init__(self) -> None:
        logging.basicConfig(filename="../logs/deep_learning.log", level=logging.INFO, format="time: %(asctime)s, function: %(funcName)s, module: %(name)s, message: %(message)s \n")

    # create a differenced series
    def difference(self, dataset, interval=1):
        diff = list()
        for i in range(interval, len(dataset)):
            value = dataset[i] - dataset[i - interval]
            diff.append(value)
        logging.info("differnced time series data!")
        return pd.Series(diff)

    #correlation
    def corrPlots(self, array: np.array, prefix: str):
        plt.figure(figsize=(30, 5))
        plt.title(f"{prefix}  Autocorrelations of Store Sales Min Max Scaled")
        plt.bar(range(len(array)), array)
        plt.grid(True)
        logging.info("plotted autocorrelation!")
        plt.show()
       
    #partial autocorrelation
    def partial(self, df):
        pacfSalesScaled = pacf(df.Scaled_Sales.values, nlags=40)
        pacfSalesScaledNp = np.array(pacfSalesScaled)
        logging.info(" auto correlation plotted!")
        return pacfSalesScaledNp

    def windowed_dataset(self, series, window_size, batch_size): 
        series = tf.expand_dims(series, axis=-1)
        dataset = tf.data.Dataset.from_tensor_slices(series)
        dataset = dataset.window(window_size + 1, shift=1, drop_remainder=True) 
        dataset = dataset.flat_map(lambda window: window.batch(window_size + 1))
        dataset = dataset.map(lambda window: (window[:-1], window[-1:]))
        dataset = dataset.batch(batch_size).prefetch(1)
        return dataset

