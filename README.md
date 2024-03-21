# Stock Prediction Application

This repository contains a simple stock prediction application built with Python, utilizing machine learning algorithms to forecast stock prices. Below is an overview of the files contained in this repository:

## Files:

### main.py

This file contains the main code for the stock prediction application. It includes functionalities to retrieve stock data using the Yahoo Finance API, preprocess the data, train a Prophet model for forecasting, and visualize the results using Streamlit and Plotly.

### unit_test.py

This file contains unit tests to ensure the functionality of the `test_stock_prediction` function in `main.py`. These tests validate various scenarios such as selecting valid and invalid stocks, checking forecast durations, handling case sensitivity in ticker inputs, and testing empty inputs.

## Usage:

1. **main.py**: Run this file to launch the stock prediction application. It prompts users to input a stock ticker, start date, and number of years for forecasting. The application retrieves historical stock data, trains a predictive model, and displays forecasted prices and trends.

2. **unit_test.py**: Run this file to execute unit tests for the `test_stock_prediction` function. It validates the correctness of the stock prediction logic under different conditions.

## Instructions:

1. Ensure you have the necessary dependencies installed. You can install them using `pip install -r requirements.txt`.

2. Run `main.py` to start the stock prediction application. Follow the instructions provided by the application to input the stock ticker, start date, and forecast duration.

3. Optionally, you can run `unit_test.py` to execute unit tests and verify the correctness of the stock prediction function.

## Contributors:

- Kush Bhandari

For any questions or issues, please contact the author.

