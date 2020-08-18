# -*- coding: utf-8 -*-
from python_questions_and_answers import *

def test_read_data():
  df = read_data('https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey=NQW2B7EP84XGZ82L')
  self.assertIsInstance(df, pd.DataFrame)
  return df

def test_transform_df(df):
  df = transform_df(df)
  self.assertTrue(len(df.columns)) == 2

def test_calculate_weekly_price(df):
  df = calculate_weekly_price(df)
  self.assertTrue(len(df)) > 0

def test_calculate_rolling_3(df):
  df = calculate_rolling_3(df)
  self.assertTrue(len(df)) > 0

def test_calculate_rolling_7(df):
  df = calculate_rolling_7(df)
  self.assertTrue(len(df)) > 0
 
if __name__ == “__main__“:
  test_read_data()
  test_transform_df(df)
  test_calculate_weekly_price(df)
  test_calculate_rolling_3(df)
  test_calculate_rolling_7(df)
