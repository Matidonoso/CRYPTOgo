import numpy as np
from flask import Flask, render_template, request
import fetch_market_data
from utils import plot_close_price
from normalization import normalization
from model import prediction


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    #These are for the API request
    TIME_DELTA = 1
    hours = 80 * 24 #DAYS PER HOURS

    #Retrieve form selected data
    selected_crypto = list(request.form.values())

    #Fetch market data
    crypto_series = fetch_market_data.get_historical_hourly_price(selected_crypto[0] , 'USD', hours, TIME_DELTA)

    #Normalization data 
    series_norm = normalization(crypto_series)
    pred = prediction(series_norm)

    #Este retorna el gráfico del api
    #return render_template('index.html', prediction_text='You selected: {}'.format(plot_close_price(crypto_series,selected_crypto[0])))

    #Este debería retornar el pred 
    #INTEL MKL ERROR: El sistema operativo no puede ejecutar %1. mkl_intel_thread.dll.
    #Intel MKL FATAL ERROR: Cannot load mkl_intel_thread.dll.
    return render_template('index.html', prediction_text='You selected: {}'.format(pred))



if __name__ == "__main__":
    app.run(debug=True)