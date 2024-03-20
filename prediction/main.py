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
    
