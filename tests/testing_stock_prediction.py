import streamlit as st
from datetime import date
import pandas as pd
import yfinance as yf
from prophet.plot import plot_plotly
from prophet import Prophet
from plotly.offline import plot
from plotly import graph_objs as go
import matplotlib.pyplot as plt
import datetime

def test_stock_prediction(ticker, START, period):
  
    """
    Test function for stock prediction using Facebook Prophet.

    This function tests the stock prediction functionality for a given ticker symbol,
    start date, and prediction period. It checks if the provided ticker is empty,
    fetches historical stock data using the Yahoo Finance API (yfinance), preprocesses
    the data for Prophet's input requirements, trains a Prophet model, and attempts
    to forecast future stock prices.

    Args:
        ticker (str): The ticker symbol of the stock to predict.
        START (datetime.date): The start date for retrieving historical stock prices.
        period (int): The number of days for forecasting future stock prices.

    Returns:
        bool: True if the prediction was successful and forecast data was generated, False otherwise.

    Raises:
        None
    """
  
    if not ticker.strip():
        st.write("Ticker is empty! Please enter a ticker")
        return False

    TODAY = date.today().strftime("%Y-%m-%d")
    #Using yfinance library to retrieve stock data
    data = yf.download(ticker, START, TODAY)
    #Reset index for date to be included as a column
    data.reset_index(inplace=True)
    data = pd.DataFrame(data)
    
    if data.empty:
        st.write("Data is empty! Please check if right ticker is entered")
        return False
            
    
    #Pre-processing the data before predicting
    #Prophet function needs the column to named as ds(Date) and y(Close)
    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})
    
    #Training our model
    model = Prophet()
    model.fit(df_train)
    
    #Forecasting stocks prices
    future = model.make_future_dataframe(periods = period)
    forecast = model.predict(future)
    
    if forecast.empty:
        st.write("Error: Unable to generate forecast for the selected stock and time period.")
        return False
     
    return True
