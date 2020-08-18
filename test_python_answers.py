# -*- coding: utf-8 -*-
from python_questions_and_answers import *
import unittest

class test_python_answers(unittest.TestCase):
  def test_read_data(self):
    df = read_data('https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey=NQW2B7EP84XGZ82L')
    self.assertIsInstance(df, pd.DataFrame)
    
  def test_transform_df(self):
    df = transform_df(df)
    self.assertTrue(len(df.columns)) == 2
    
  def test_calculate_weekly_price(self):
    df = calculate_weekly_price(df)
    self.assertTrue(len(df)) > 0
  
  def test_calculate_rolling_3(self):
    df = calculate_rolling_3(df)
    self.assertTrue(len(df)) > 0
    
  def test_calculate_rolling_7(self):
    df = calculate_rolling_7(df)
    self.assertTrue(len(df)) > 0
 
if __name__ == “__main__“:
  test_read_data()
  test_transform_df()
  test_calculate_weekly_price()
  test_calculate_rolling_3()
  test_calculate_rolling_7()
