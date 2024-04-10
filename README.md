# Stock Prediction Application

This project is a Stock Prediction application built using Streamlit, which allows users to predict stock prices for various companies. Users can input the ticker symbol of a stock, select a start date, and specify the number of years for which they want to forecast the stock price. The application retrieves historical stock data using the Yahoo Finance API, processes it using the Prophet library, and generates forecast data along with interactive visualizations. The goal of the project is to provide users with insights into future stock price trends to aid in investment decision-making.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)

## Introduction

Provide a more detailed introduction to your project. Explain what it does, why it's useful, and any other relevant information.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   
2. Navigate to the project directory:
   ```bash
   cd <project_directory>
   
4. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

### Inside Terminal
1. Open your terminal and navigate to your project directory
   ```bash
   cd <project_directory>
2. Run your code by using the following code
   ```bash
   py -m streamlit run <filename.py>
3. You will be provided by a link to your application 

![image](https://github.com/KushBhandari15/Stock-Prediction/assets/98527317/80fd453d-a879-499e-9c0c-4947d9ae6620)

### Inside application

1. Enter a start date and a ticker name

![image](https://github.com/KushBhandari15/Stock-Prediction/assets/98527317/2029cac9-14b7-483c-b666-5b7414478a6a)

Note: If ticker name is not found it would print "Data is empty! Please check if right ticker is entered"

2. Choose number of years of forceast data you need using the slider

![image](https://github.com/KushBhandari15/Stock-Prediction/assets/98527317/b951f568-f9d2-48a7-8e82-df477c63707a)

3. Finally when all the data has been entered you can view the current data of the stock (displayed as raw data) and as well as its forecast which is displayed through both simple data table and graphs

![image](https://github.com/KushBhandari15/Stock-Prediction/assets/98527317/b67fced3-fc49-4537-ac32-62cc5b59b4b0)

![image](https://github.com/KushBhandari15/Stock-Prediction/assets/98527317/c1dcdf38-4a2f-465b-887e-94c3c026cbee)

![image](https://github.com/KushBhandari15/Stock-Prediction/assets/98527317/6869b614-4a08-4f89-bdc8-59110848595f)

![image](https://github.com/KushBhandari15/Stock-Prediction/assets/98527317/2dca6db0-930a-43e5-b368-dfa4f87f0e92)

![image](https://github.com/KushBhandari15/Stock-Prediction/assets/98527317/3360a0bd-e912-4743-afb7-a9de8822fb58)



## Testing

### Automated Testing

We have included some automated test cases to verify the functionality of the `test_stock_prediction` function in the `unit_test.py` file. These test cases cover various scenarios, including selecting invalid stocks, selecting valid stocks with different forecast durations, case-sensitive inputs, and empty inputs.

To run the automated tests, you can execute the `unit_test.py` file using the following command:

```bash
python unit_test.py
```

### Custom Testing
If needed, you can also create your own test cases by modifying the input parameters in the unit_test.py file and running the tests again. Ensure to provide valid input parameters for the stock ticker, start date, and forecast duration to test different scenarios.
The test results will indicate whether each test case passed or failed.

## Contributing

We welcome contributions from the community to improve this project. If you'd like to contribute, please follow these guidelines:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine:
   ```bash
   git clone https://github.com/your-username/your-repository.git

3. Create a new branch for your changes:
   ```bash
   git checkout -b feature-name
4. Replace feature-name with a descriptive name for your feature or fix.
5. Make your changes in the codebase.
6. Test your changes thoroughly to ensure they work as expected.
7. Commit your changes:
   ```bash
   git commit -am 'Add new feature' 
   ```
8. Push your changes to your forked repository:
   ```bash
   git push origin feature-name

9. Submit a pull request (PR) from your forked repository to the main branch of the original repository.
Provide a clear title and description for your PR, explaining the purpose of the changes.
Reference any related issues or pull requests, if applicable.
After submitting your pull request, it will be reviewed by the project maintainers. Please be patient, as it may take some time for your PR to be reviewed. We appreciate your contribution to the project!

Note: Please ensure that your changes adhere to the project's coding style and conventions. Also, avoid making unrelated changes in your pull requests. If you're unsure about anything, feel free to ask for clarification in the PR discussion.






