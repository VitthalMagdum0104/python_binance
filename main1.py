import time
from binance.client import Client
import config
import csv
import json
import pandas
import datetime
import openpyxl

client = Client(config.api_key, config.api_secret)
orders = client.futures_get_all_orders(
    symbol='ETHUSDT', LIMIT=10)
with open("main.json", "w") as file:
    json.dump(orders, file)
pandas.read_json("main.json").to_excel("main.xlsx")


def avg_sell_price():
    wb_obj = openpyxl.load_workbook('main.xlsx')
    sheet = wb_obj.active
    price = 0
    exec_quantity = 0
    for i in range(1, 11):
        if sheet['O'][i].value == 'SELL':
            price += sheet['G'][i].value
            exec_quantity += sheet['I'][i].value
    avg = price/exec_quantity
    return avg


def avg_buy_price():
    wb_obj = openpyxl.load_workbook('main.xlsx')
    sheet = wb_obj.active
    price = 0
    exec_quantity = 0
    for i in range(1, 11):
        if sheet['O'][i].value == 'BUY':
            price += sheet['G'][i].value
            exec_quantity += sheet['I'][i].value
    avg = price/exec_quantity
    return avg


print("avg price for buy", avg_buy_price())
print("avg price for sell", avg_sell_price())
