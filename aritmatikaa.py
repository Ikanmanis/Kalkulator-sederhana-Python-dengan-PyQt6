from main_window import MainWindow #import class MainWindow dari file main_window.py

class Aritmatika(MainWindow):
    def __init__(self):
        super().__init__()

    def add_numbers(self):
        result = float(self.first_number.text()) + float(self.second_number.text())
        self.result_label.setText(str(result))

    def subtract_numbers(self):
        result = float(self.first_number.text()) - float(self.second_number.text())
        self.result_label.setText(str(result))

    def multiply_numbers(self):
        result = float(self.first_number.text()) * float(self.second_number.text())
        self.result_label.setText(str(result))

    def divide_numbers(self):
        result = float(self.first_number.text()) / float(self.second_number.text())
        self.result_label.setText(str(result))
    
    def fsisabagi(self):
        result = float(self.first_number.text()) % float(self.second_number.text())
        self.result_label.setText(str(result))
    
    def fpangkat(self):
        result = float(self.first_number.text()) ** float(self.second_number.text())
        self.result_label.setText(str(result))
