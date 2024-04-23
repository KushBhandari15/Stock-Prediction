import unittest
from testing_stock_prediction import test_stock_prediction

class TestStockPredictionApp(unittest.TestCase):
    """
    A test case class for the stock prediction application.
    """
    
    def test_select_invalid_stock(self):
        """
        Test case for selecting an invalid stock.
        """
        result = test_stock_prediction('XYZ', "2010-01-01", 2 * 365)
        expected_output = False
        self.assertEqual(result, expected_output)
            
    def test_select_stock_and_forecast_duration(self):
        """
        Test case for selecting a valid stock and forecast duration.
        """
        result = test_stock_prediction('AAPL', "2010-01-01", 2 * 365)
        expected_output = True
        self.assertEqual(result, expected_output)    
        
    def test_case_sensitive_input(self):
        """
        Test case for case-sensitive input.
        """
        result = test_stock_prediction('aapl', "2015-01-01", 365)
        expected_output = True
        self.assertEqual(result, expected_output)
        
    def test_select_stock_and_forecast_duration2(self):
        """
        Test case for selecting a stock and a different forecast duration.
        """
        result = test_stock_prediction('MSFT', "2015-01-01", 1 * 365)
        expected_output = True
        self.assertEqual(result, expected_output)
        
    def test_empty_input(self):
        """
        Test case for empty input.
        """
        result = test_stock_prediction('', "2015-01-01", 365)
        expected_output = False
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()

