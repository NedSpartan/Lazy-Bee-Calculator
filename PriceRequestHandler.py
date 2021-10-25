import requests


class PriceRequestHandler:

    def __init__(self, typeid):

        self.type_id = typeid

        """List of acceptable items to price check"""
        self.AcceptableItemsList = {
            'Sleeper Drone AI Nexus': 30747,
            'Sleeper Data Library': 30745,
            'Neural Network Analyzer': 30744,
            'Ancient Coordinates Database': 30746,
        }

        """Builds the url to submit a get request"""
        self.URL = f'https://api.evemarketer.com/ec/marketstat/json?typeid={self.type_id}&usesystem=30002187'

    """Requests the max buy price from an item"""
    def getprice(self):
        response = requests.get(f'{self.URL}')
        jsonresponse = response.json()

        price = float(jsonresponse[0]['buy']['max'])

        return price

    def checkifbluebook(self, items):

        """Checks if items in clipboard are sleeper cache loot"""
        if items not in self.AcceptableItemsList.keys():
            print('No')
        elif items in self.AcceptableItemsList.keys():
            print('yes')


if __name__ == '__main__':
    new = PriceRequestHandler(21815)
    new.getprice()
