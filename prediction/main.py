# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 23:45:22 2024

@author: Kush Bhandari
"""

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

# Function to define main application logic

def stock_prediction ():
    
    st.title("Stock Prediction application")
    
    max_date = datetime.date(2024, 3, 20)
    START = st.date_input("Enter the Start date of the stock price ", datetime.date(2010, 1, 1), max_value=max_date )
    TODAY = date.today().strftime("%Y-%m-%d")
    #List of all stocks available for prediction 
    
    #A textbox to enter stock ticker
    ticker = st.text_input("Enter the ticker name: ")
    if not ticker.strip():
        st.write("Ticker is empty! Please enter a ticker")
        return
    
    #A slider to choose years of prediction from
    n_years = st.slider("Number of years of forecast data needed: ", 1, 5)
    period = n_years*365
        
    #Using yfinance library to retrieve stock data
    data = yf.download(ticker, START, TODAY)
    #Reset index for date to be included as a column
    data.reset_index(inplace=True)
    data = pd.DataFrame(data)
    
    if data.empty:
        st.write("Data is empty! Please check if right ticker is entered")
        return

    #Displaying front row of raw data retrieved from yfinance
    st.subheader("Raw data - head")
    st.write(data.head())
    
    #Displaying end row of raw data retrieved from yfinance
    st.subheader("Raw data - tail")
    st.write(data.tail())
    
    #Creating a figure object to display raw data
    fig = go.Figure(data = [go.Candlestick(x=data.index,
                            open = data['Open'],
                            high = data['High'],
                            low = data['Low'],
                            close = data['Close'])])
    st.subheader("Raw data - graph")
    st.plotly_chart(fig)
    
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
        return
    
    #Displaying head and tail of the forecast data
    st.header("Forecast data - head")
    st.write(forecast.head())
    st.header("Forecast data - tail")
    st.write(forecast.tail())
    
    #Displaying forecast data using graphs
    fig1 = model.plot(forecast)
    st.subheader("Forecast data - graph")
    st.plotly_chart(fig1)
    
    #Displaying forecast data's components
    st.subheader("Forecast components - graph")
    fig2 = model.plot_components(forecast)
    st.write(fig2)
    

def test_stock_prediction(ticker, START, period):
    
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
    
    
  
def main():

    stock_prediction()

if __name__ == '__main__':
    main()
