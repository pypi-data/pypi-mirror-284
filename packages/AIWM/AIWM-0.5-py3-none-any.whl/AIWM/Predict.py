import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
import warnings
warnings.filterwarnings('ignore')
from statsmodels.tsa.stattools import adfuller
import pmdarima as pm
from pmdarima.arima import auto_arima
import statsmodels.api as sm
from datetime import datetime
import requests
import json

#Appd Configuration and parsing the data
def appD(appUrl,auth):
    try:
        url=appUrl+ "525600&output=json&rollup=false"
        headers = {'Authorization': 'Basic '+auth}
        r = requests.get(url,headers=headers,verify=false)
        y = json.dumps(json.loads(r.text)[0])
        str = json.loads(y)
        json_array  = str["metricValues"]
        df=pd.DataFrame(json_array)
        df['Date']=pd.to_datetime(df['startTimeInMillis'],unit='ms').dt.date
        return predict_forecast(df)
    except:
            return pd.DataFrame()
#forecasting by applying the model

def forecast(ARIMA_model, df, periods=30):
# Forecast
    try:
        
        n_periods = periods
        fitted, confint = ARIMA_model.predict(n_periods=n_periods, return_conf_int=True)
       
        index_of_fc = pd.date_range(df.index[-1], periods = n_periods, freq='D')
        fitted_series = pd.Series(fitted, index=index_of_fc)
        lower_series = pd.Series(confint[:, 0], index=index_of_fc)
        upper_series = pd.Series(confint[:, 1], index=index_of_fc)
        
        # Plot
        plt.figure(figsize=(15,7))
        plt.plot(df['Observed'], color='#1f76b4')
        # plt.plot(dfTest['Observed'], color='Orange')
        plt.plot(fitted_series, color='darkgreen')
        plt.fill_between(lower_series.index, 
                        lower_series, 
                        upper_series, 
                        color='k', alpha=.15)
    
        plt.title("Forecast of calls/min")
        plt.show()
        return {'Predicted Peak' : int(upper_series.max()), 'Predicted Steady' : int(fitted.max())}
    except:
        return{'Something went wrong'}


#Load Data

def predict_forecast(data_file):
#  Picking the max hit from the day
    try:
        df = pd.read_csv(data_file)
        df['Date'] = pd.to_datetime(df['Date'],errors='coerce')
        #df = df.groupby('Date')['Observed'].max()
        df = df.groupby('Date')['Observed'].max()
        
    # Making the data readablw to the model by saving 
        df.to_csv("formatted.csv")
        df = pd.read_csv("formatted.csv")
        df['Date'] = pd.to_datetime(df['Date'],errors='coerce')
    
    #  Get the dates sorted 
        startDate = datetime.today()
        startDate = startDate.replace(year=startDate.year - 1).replace(day=startDate.day+1).replace(month=startDate.month + 1).strftime('%Y-%m-%d')
        endDate = datetime.today()
        endDate = endDate.replace(year=endDate.year - 1).replace(month=endDate.month + 2) .strftime('%Y-%m-%d')
        appDate = df['Date'].min()
        appDate = appDate.replace(month=appDate.month + 1).strftime('%Y-%m-%d' )
    
    # Indexing with time series
        df.index
        dfTrain = df.set_index(['Date'])
    
    # Aplpy Sarima auto model to identify the parameters
        
        SARIMA_model = pm.auto_arima(dfTrain['Observed'], start_p=1, start_q=1,
                                 test='adf',
                                 max_p=3, max_q=3, 
                                 m=12, #12 is the frequncy of the cycle
                                 start_P=0, 
                                 seasonal=True, #set to seasonal
                                 d=None, 
                                 D=1, #order of the seasonal differencing
                                 trace=False,
                                 error_action='ignore',  
                                 suppress_warnings=True, 
                                 stepwise=True)
        
        # SARIMA_model.plot_diagnostics(figsize=(15,12))
        # plt.show()
        
        return forecast(SARIMA_model,dfTrain)
    except:
        return{'something went wrong'}

