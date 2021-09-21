from binance.client import Client
import config
import json
import pandas
import datetime
import openpyxl


class Binance:
    def __init__(self, api_key, api_secret, limit):
        self.api_key = api_key
        self.secure_key = api_secret
        self.limit = int(limit)
        client = Client(self.api_key, self.secure_key)
        orders = client.futures_get_all_orders(
            symbol='ETHUSDT', LIMIT=self.limit)
        with open("vithu.json", "w") as file:
            json.dump(orders, file)
        pandas.read_json("vithu.json").to_excel("vithu.xlsx")

    def avg_sell_price(self):
        wb_obj = openpyxl.load_workbook('vithu.xlsx')
        sheet = wb_obj.active
        price = 0
        exec_quantity = 0
        for i in range(1, self.limit+1):
            if sheet['O'][i].value == 'SELL':
                price += sheet['G'][i].value
                exec_quantity += sheet['I'][i].value
        return f'avg buy price {price/exec_quantity}'

    def avg_buy_price(self):
        wb_obj = openpyxl.load_workbook('vithu.xlsx')
        sheet = wb_obj.active
        price = 0
        exec_quantity = 0
        for i in range(1, self.limit+1):
            if sheet['O'][i].value == 'BUY':
                price += sheet['G'][i].value
                exec_quantity += sheet['I'][i].value
        return f'avg buy price {price/exec_quantity}'


account = Binance(config.api_key, config.api_secret, 10)
print(account.avg_buy_price())
print(account.avg_sell_price())
