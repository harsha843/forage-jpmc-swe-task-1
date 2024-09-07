################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(stock):
    bid_price = stock['bid']
    ask_price = stock['ask']
    # Compute the price using the formula
    price = (bid_price + ask_price) / 2
    # Return the data point (assuming other details are included as well)
    return {'price': price, 'bid': bid_price, 'ask': ask_price}


def getRatio(price_a, price_b):
    # Avoid division by zero
    if price_b == 0:
        return float('inf')  # or handle it as needed
    else:
        return price_a / price_b


def main():
    # Dictionary to store prices
    prices = {}
    
    # Example stock names
    stock_a = 'AAPL'
    stock_b = 'GOOG'
    
    # Get data points
    prices[stock_a] = getDataPoint(stock_a)
    prices[stock_b] = getDataPoint(stock_b)
    
    # Extract prices
    price_a = prices[stock_a]['price']
    price_b = prices[stock_b]['price']
    
    # Get and print the ratio
    ratio = getRatio(price_a, price_b)
    print(f"Ratio of {stock_a} to {stock_b}: {ratio}")
