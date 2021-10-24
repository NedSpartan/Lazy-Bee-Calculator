import requests
import csv


class PriceRequestHandler:
    BLUE_BOOKS = ['Sleeper Data Library', 'Neural Network Analyzer', 'Ancient Coordinates Database',
                  'Sleeper Drone AI Nexus']

    def __init__(self, typeid):
        self.type_id = typeid

        self.URL = f'https://api.evemarketer.com/ec/marketstat/json?typeid={self.type_id}&usesystem=30002187'

    def getprice(self):
        response = requests.get(f'{self.URL}')
        jsonresponse = response.json()

        price = float(jsonresponse[0]['buy']['max'])

        return price


if __name__ == '__main__':
    new = PriceRequestHandler(21815)
    new.getprice()