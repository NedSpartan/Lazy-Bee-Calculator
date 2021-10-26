import sys
from PyQt5.QtWidgets import *

sys.path.append(".")

MEMBER_TIERS = ['Trial Member', 'Full Member', 'Public Guest']


class ContractCalc(QDialog):

    # noinspection PyArgumentList
    def __init__(self, parent=None):

        super(ContractCalc, self).__init__(parent)

        # Window title setter
        self.setWindowTitle('Lazy Bee Calculator')

        """Total amount to then have the tax bracket level deducted from it"""
        self.amount = int

        # Set up for member tier list & Level
        self.tierList = QComboBox()
        self.tierList.addItem(MEMBER_TIERS[0])
        self.tierList.addItem(MEMBER_TIERS[1])
        self.tierList.addItem(MEMBER_TIERS[2])

        """Final contract amount that will be automatically copied to clipboard"""
        self.contractAmount = int

        """Variable to store the current Membership level for tax purposes, it is expected that the variable will 
        always be a string """
        self.membershipLevel = str

        """Variable to store the tax level from the current membership level, it is expected that this will always be a
        integer as it will be what will be used to calculate at what tax bracket the contract will be"""
        self.taxLevel = int

        # Set up to accept user input to be appraised
        self.itemsLabel = QLabel('Items: ')
        self.items = QPlainTextEdit()

        # list of items separated from the items QPlainTextEdit object
        self.listOfItems = []

        self.items.setPlaceholderText('  Put stuff to appraise here \n \n # Protip: Ctrl+a, Ctrl+c, Ctrl+v')
        self.contractTotalLabel = QLabel(f'Total contract amount: {self.amount}')

        # Push Button to submit the query
        self.submit = QPushButton('Submit')
        self.submit.clicked.connect(self.submitdata)

        """Layout of the app. Each widget is added separately into a vertical alignment box"""
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tierList)
        self.layout.addWidget(self.itemsLabel)
        self.layout.addWidget(self.items)
        self.layout.addWidget(self.submit)

        # Layout setter
        self.setLayout(self.layout)

    """Grabs the user input from items QPlainTextEdit Object"""
    def submitdata(self):

        data = self.items.toPlainText()
        items = data.split('\n')
        self.listOfItems = items
        print(self.listOfItems)

    def calculatetax(self):

        if self.membershipLevel == 'Trial Member' or 'Full Member':

            self.taxLevel = 0.85

        elif self.membershipLevel == 'Public Guest':

            self.taxLevel = 0.75


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lbc = ContractCalc()
    lbc.show()
    sys.exit(app.exec())
