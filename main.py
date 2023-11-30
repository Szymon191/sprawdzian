import random
import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.order.clicked.connect(self.orderrr)

        self.show()

    def orderrr(self):
        price = 0
        if self.ui.hawai.isChecked():
            price = 30
            pizza = "hawajską"
        elif self.ui.margherita.isChecked():
            price = 28
            pizza = "margheritę"
        elif self.ui.capricciosa.isChecked():
            price = 32
            pizza = "capricciosę"
        elif self.ui.quattro.isChecked():
            price = 34
            pizza = "quattro fromaggi"
        if self.ui.checkCheese.isChecked():
            price += 5

        email = self.ui.emailValue.text()

        time = random.randint(10,100)

        if "@" in email :
            self.ui.ordered.setText(f'Użytkownik {email} zamówił pizzę {pizza}. Cena: {price}zł. Przewidywany czas dostawy: {time}min ')
        else:
            self.ui.ordered.setText(f'Niepoprawny email')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())
