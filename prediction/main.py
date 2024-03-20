def stock_prediction ():
    
    st.title("Stock Prediction application")
    
    START = "2000-01-01"
    TODAY = date.today().strftime("%Y-%m-%d")
    
    #A selectbox to choose stock from
    #ticker = st.selectbox("Select stock for prediction ", stocks)
    ticker = st.text_input("Enter the ticker name: ")
    
    #A slider to choose years of prediction from
    n_years = st.slider("Number of years of forecast data needed: ", 1, 5)
    period = n_years*365
        
    #Using yfinance library to retrieve stock data
    data = yf.download(ticker, START, TODAY)
    #Reset index for date to be included as a column
    data.reset_index(inplace=True)
    data = pd.DataFrame(data)
    
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
