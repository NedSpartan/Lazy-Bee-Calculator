
import sys
import requests
from PyQt5.QtWidgets import *

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
        self.current = float

        """Final contract amount pre-tax"""
        self.contract_amount_pre_tax = float

        """Final Contract amount after tax"""
        self.contract_amount_after_tax = float

        """Variable to store the tax level from the current membership level, it is expected that this will always be a
        integer as it will be what will be used to calculate at what tax bracket the contract will be"""
        self.taxLevel = 0.85

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
        final_count_list = []

        counter = 0
        
        for i in items:

            final_count_list.append(items[counter].split('\t'))
            counter += 1

        counter = 0
        item_quantities = {}
        current = ContractCalc.get_prices()

        for i in final_count_list:

            item_quantities[f'{final_count_list[counter][0]}'] = float(final_count_list[counter][1])
            counter += 1

        final_product = []
        counter = 0 

        for keys in current:

            price = current[keys] * item_quantities[keys]
            final_product.append(price)
            counter += 1

        self.contract_amount_pre_tax = sum(final_product)

        self.contract_amount_after_tax = self.contract_amount_pre_tax * float(self.taxLevel)

        self.listOfItems = item_quantities

        """Remove this before production"""
        print(self.contract_amount_pre_tax)
        print(self.contract_amount_after_tax)

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
            price_book[f'{blue_book_names[counter]}'] = float(f'{current_prices[counter]}')
            counter += 1

        """Remove before production"""
        print(price_book)

        return price_book


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lbc = ContractCalc()
    lbc.get_prices()
    lbc.show()
    sys.exit(app.exec())