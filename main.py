import sys
from PyQt5.QtWidgets import *


class ContractCalc(QDialog):

    # noinspection PyArgumentList
    def __init__(self, parent=None):
        super(ContractCalc,self).__init__(parent)

        # Window title setter
        self.setWindowTitle('Lazy Bee Calculator')

        self.amount = ''

        # Set up to accept user input to be appraised
        self.itemsLabel = QLabel('Items: ')
        self.items = QPlainTextEdit()
        self.items.setPlaceholderText('  Put stuff to appraise here \n \n # Protip: Ctrl+a, Ctrl+c, Ctrl+v')
        self.contractTotalLabel = QLabel(f'Total contract amount: {self.amount}')

        # Push Button to submit the query
        self.submit = QPushButton('Submit')
        self.submit.clicked.connect(self.submitdata)

        # Main layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.itemsLabel)
        self.layout.addWidget(self.items)
        self.layout.addWidget(self.contractTotalLabel)
        self.layout.addWidget(self.submit)

        # Layout setter
        self.setLayout(self.layout)

    def submitdata(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lbc = ContractCalc()
    lbc.show()
    sys.exit(app.exec())
