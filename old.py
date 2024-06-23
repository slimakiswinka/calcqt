from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QGridLayout, QLineEdit
from PyQt5.QtCore import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 230)

        self.createAppLayout()

    def createAppLayout(self):
        widget = QWidget()
        layout = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setReadOnly(False)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        layout.addWidget(self.display)

        gridLayout = QGridLayout()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', '=', '+',
            '<-', 'C'
        ]

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, button in zip(positions, buttons):
            if button == '=':
                btn = QPushButton(button)
                btn.clicked.connect(self.calculateResult)
                gridLayout.addWidget(btn, *position)
                continue

            if button == '<-':
                btn = QPushButton(button)
                btn.clicked.connect(self.backspace)
                gridLayout.addWidget(btn, *position)
                continue

            if button == 'C':
                btn = QPushButton(button)
                btn.clicked.connect(self.clear)
                gridLayout.addWidget(btn, *position)
                continue

            btn = QPushButton(button)
            btn.clicked.connect(self.buildExpression)
            gridLayout.addWidget(btn, *position)

        layout.addLayout(gridLayout)
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def buildExpression(self):
        button = self.sender()
        newExpression = self.display.text() + button.text()
        self.display.setText(newExpression)

    def calculateResult(self):
        try:
            result = eval(self.display.text())
            self.display.setText(str(result))
        except:
            self.display.setText("ERROR")

    def backspace(self):
        text = self.display.text()[:-1]
        self.display.setText(text)

    def clear(self):
        self.display.clear()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    calc = Calculator()
    calc.show()

    sys.exit(app.exec_())
