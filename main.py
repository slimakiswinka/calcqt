from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QGridLayout, QLineEdit, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CalcQT")
        self.setGeometry(100, 100, 350, 500)

        self.createAppLayout()

    def createAppLayout(self):
        widget = QWidget()
        layout = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setReadOnly(False)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        self.display.setFont(QFont("Arial", 24))
        self.display.setStyleSheet("""
            background-color: #333; 
            color: #fff; 
            padding: 10px; 
            border: none; 
            border-radius: 10px;
            margin-bottom: 20px;
        """)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(2, 2)
        shadow.setColor(QColor(0, 0, 0, 160))
        self.display.setGraphicsEffect(shadow)

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
            btn = QPushButton(button)
            btn.setFont(QFont("Arial", 18))
            btn.setStyleSheet(self.buttonStyle(button))
            btn.clicked.connect(self.buttonClicked)

            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(10)
            shadow.setOffset(2, 2)
            shadow.setColor(QColor(0, 0, 0, 160))
            btn.setGraphicsEffect(shadow)

            gridLayout.addWidget(btn, *position)

        layout.addLayout(gridLayout)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def buttonStyle(self, button):
        base_style = """
            QPushButton {
                background-color: #444; 
                color: white; 
                border: 1px solid #555;
                border-radius: 20px;
                padding: 15px;
                margin: 5px;
                min-width: 60px;
                min-height: 60px;
            }
            QPushButton:hover {
                background-color: #555;
            }
            QPushButton:pressed {
                background-color: #666;
            }
        """
        special_buttons = {
            '=': "background-color: #ff5722;",
            'C': "background-color: #e91e63;",
            '<-': "background-color: #9c27b0;"
        }
        return base_style + special_buttons.get(button, "")

    def buttonClicked(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            self.calculateResult()
        elif text == "C":
            self.clear()
        elif text == "<-":
            self.backspace()
        else:
            self.buildExpression(text)

    def buildExpression(self, text):
        current_text = self.display.text()
        new_text = current_text + text
        self.display.setText(new_text)

    def calculateResult(self):
        try:
            result = eval(self.display.text())
            self.display.setText(str(result))
        except:
            self.display.setText("ERROR")

    def backspace(self):
        current_text = self.display.text()
        new_text = current_text[:-1]
        self.display.setText(new_text)

    def clear(self):
        self.display.clear()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    calc = Calculator()
    calc.show()

    sys.exit(app.exec_())
