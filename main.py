import sys
import requests
from PyQt5.QtWidgets import *

sys.path.append(".")

MEMBER_TIERS = ['Trial Member', 'Full Member', 'Public Guest']


class ContractCalc(QDialog):

    def __init__(self, parent=None):

        super(ContractCalc, self).__init__(parent)

        """Sets title of the app"""
        self.setWindowTitle('Lazy Bee Calculator')

        """Total amount to then have the tax bracket level deducted from it"""
        self.amount = int

        """Membership tax level bracket selector for dropdown menu"""
        self.tierList = QComboBox()
        self.tierList.addItem(MEMBER_TIERS[0])
        self.tierList.addItem(MEMBER_TIERS[1])
        self.tierList.addItem(MEMBER_TIERS[2])
        self.tierList.activated.connect(self.set_tax)

        """Current Blue book prices"""
        self.current = ContractCalc.get_prices

        """Final contract amount that will be automatically copied to clipboard"""
        self.contractAmount = int

        """Variable to store the tax level from the current membership level, it is expected that this will always be a
        integer as it will be what will be used to calculate at what tax bracket the contract will be"""
        self.taxLevel = int

        """GUI Representation of the user input area"""
        self.itemsLabel = QLabel('Items: ')
        self.items = QPlainTextEdit()

        """List of items copied from user input"""
        self.listOfItems = list

        self.items.setPlaceholderText('  Put stuff to appraise here \n \n # Protip: Ctrl+a, Ctrl+c, Ctrl+v')
        self.contractTotalLabel = QLabel(f'Total contract amount: {self.amount}')

        """Push button to submit data for query"""
        self.submit = QPushButton('Submit')
        self.submit.clicked.connect(self.submit_data)

        """Layout of the app. Each widget is added separately into a vertical alignment box"""
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tierList)
        self.layout.addWidget(self.itemsLabel)
        self.layout.addWidget(self.items)
        self.layout.addWidget(self.submit)

        """Sets GUI layout"""
        self.setLayout(self.layout)

    """Grabs the user input from items QPlainTextEdit Object once the submit button is clicked"""

    def submit_data(self):

        data = self.items.toPlainText()
        items = data.split('\n')
        self.listOfItems = items

        """Remove this before production"""
        print(self.listOfItems)

    """Calculates the appropriate level of tax"""

    def set_tax(self):

        selection = self.tierList.currentText()

        if selection.lower() == 'Trial Member'.lower():

            self.taxLevel = 0.85

        elif selection.lower() == 'Public Guest'.lower():

            self.taxLevel = 0.75

        elif selection.lower() == 'Full Member'.lower():

            self.taxLevel = 0.85

        """Remove before production"""
        print(selection)
        print(self.taxLevel)

    @staticmethod
    def get_prices():

        blue_book_ids = [30747, 30745, 30744, 30746]

        blue_book_names = ['Sleeper Drone AI Nexus', 'Sleeper Data Library', 'Neural Network Analyzer',
                           'Ancient Coordinates Database']

        current_prices = []

        items = f"{blue_book_ids[0]},{blue_book_ids[1]},{blue_book_ids[2]},{blue_book_ids[3]}"

        url = f'https://api.evemarketer.com/ec/marketstat/json?typeid={items}&usesystem=30002187'

        response = requests.get(f'{url}')
        json_response = response.json()
        counter = 0

        price_book = {}

        for i in json_response:
            new_price = json_response[counter]['buy']['max']
            current_prices.append(new_price)
            price_book[f'{blue_book_names[counter]}'] = f'{current_prices[counter]}'
            counter += 1

        """Remove before production"""
        print(price_book)

        return price_book

    def set_contract_amount(self):

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lbc = ContractCalc()
    lbc.get_prices()
    lbc.show()
    sys.exit(app.exec())
