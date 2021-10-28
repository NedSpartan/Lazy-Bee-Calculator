import sys
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

        # Test to see if it works, this has to be removed.
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
            # Test to see if it works, this has to be removed.
        print(selection)
        print(self.taxLevel)

    def fetch_price(self):

        pass

    def set_contract_amount(self):

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lbc = ContractCalc()
    lbc.show()
    sys.exit(app.exec())
