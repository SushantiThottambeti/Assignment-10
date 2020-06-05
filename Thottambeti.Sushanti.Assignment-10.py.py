"""
File: Python Programming
Author: Sushanti Thottambeti
DU ID: 873406925
Date: 06/05/2020
Title: Adding Functions to the Stock Problem
Description: This program creates a line graph with Matplotlib for stock data imported 
from a JSON file. The graph shows variation in closing price for each stock over time.Also uploading in GitHub 

"""


# -*- coding: utf-8 -*-

# Import Packages
import json
from datetime import datetime as dt
import matplotlib.pyplot as plt

# File path for the json data source file
filepath = r"C:\Users\Desktop\Sushanti\Week 8\AllStocks (1).json"

# Read data in the json file and assign a variable
# Using json.load() since the source data is from a file rather than a variable
with open(filepath) as jsonData:
    stock_data = json.load(jsonData)

# Initialize dictionaries to save all the extracted data from the json file
AIG = {}
F = {}
FB = {}
GOOG = {}
M = {}
MSFT = {}
RDSA = {}

# Data extraction from assigned variable and transferring to
# the dictionaries that have been initialized
for item in stock_data:
    
    while item['Symbol'] == 'AIG':
        closing_price = item.get('Close')
        AIG.setdefault('closing_value', list()).append(closing_price)
        date_field = item.get('Date')
        parse_date = dt.strptime(date_field, "%d-%b-%y").date()
        AIG.setdefault('date_value', list()).append(parse_date)
        break

    while item['Symbol'] == 'F':
        closing_price = item.get('Close')
        F.setdefault('closing_value', list()).append(closing_price)
        date_field = item.get('Date')
        parse_date = dt.strptime(date_field, "%d-%b-%y").date()
        F.setdefault('date_value', list()).append(parse_date)
        break

    while item['Symbol'] == 'FB':
        closing_price = item.get('Close')
        FB.setdefault('closing_value', list()).append(closing_price)
        date_field = item.get('Date')
        parse_date = dt.strptime(date_field, "%d-%b-%y").date()
        FB.setdefault('date_value', list()).append(parse_date)
        break
    
    while item['Symbol'] == 'GOOG':
        closing_price = item.get('Close')
        GOOG.setdefault('closing_value', list()).append(closing_price)
        date_field = item.get('Date')
        parse_date = dt.strptime(date_field, "%d-%b-%y").date()
        GOOG.setdefault('date_value', list()).append(parse_date)
        break
        
    while item['Symbol'] == 'M':
        closing_price = item.get('Close')
        M.setdefault('closing_value', list()).append(closing_price)
        date_field = item.get('Date')
        parse_date = dt.strptime(date_field, "%d-%b-%y").date()
        M.setdefault('date_value', list()).append(parse_date)
        break
    
    while item['Symbol'] == 'MSFT':
        closing_price = item.get('Close')
        MSFT.setdefault('closing_value', list()).append(closing_price)
        date_field = item.get('Date')
        parse_date = dt.strptime(date_field, "%d-%b-%y").date()
        MSFT.setdefault('date_value', list()).append(parse_date)
        break
    
    while item['Symbol'] == 'RDS-A':
        closing_price = item.get('Close')
        RDSA.setdefault('closing_value', list()).append(closing_price)
        date_field = item.get('Date')
        parse_date = dt.strptime(date_field, "%d-%b-%y").date()
        RDSA.setdefault('date_value', list()).append(parse_date)
        break

# Generate plots utilizing dictionaries
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(AIG['date_value'],AIG['closing_value'])
plt.plot(F['date_value'],F['closing_value'])
plt.plot(FB['date_value'],FB['closing_value'])
plt.plot(GOOG['date_value'],GOOG['closing_value'])
plt.plot(M['date_value'],M['closing_value'])
plt.plot(MSFT['date_value'],MSFT['closing_value'])
plt.plot(RDSA['date_value'],RDSA['closing_value'])
plt.title('Assignment 8', fontsize=16)
plt.xlabel('Dates', fontsize=14)
plt.ylabel("Closing values", fontsize=12)
fig.autofmt_xdate()
plt.tick_params(axis='both',which='major',labelsize='16')
plt.savefig('outputGraph.png')
plt.show()
