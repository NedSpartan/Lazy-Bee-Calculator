import requests


class PriceRequestHandler:

    def __init__(self):

        self.type_id = int

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

    """Gets the type id of the items"""
    def gettypeid(self, items):

        pass

    def checkifbluebook(self, items):

        """Checks if items in clipboard are sleeper cache loot"""
        if items not in self.AcceptableItemsList.keys():

            return False

        elif items in self.AcceptableItemsList.keys():

            return True


if __name__ == '__main__':
    new = PriceRequestHandler()
    new.getprice()
