from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # judul 
        self.setWindowTitle('Kalkulator Sederhana')

        # membuat dua QLineEdit widgets untuk user memasukkan angka
        self.first_number = QLineEdit()
        self.second_number = QLineEdit()

        # membuat label untuk mengarahkan ke input dan untuk menampilkan hasil perhitungan 
        self.label_input1 = QLabel("Masukkan Angka 1")
        self.label_input2 = QLabel("Masukkan Angka 2")
        self.hasil_label = QLabel("Hasil Perhitungan ")
        self.result_label = QLabel()

        # membuat 4 QPushButton widgets sebagai pilihan bagi user untuk operasi aritmatika
        self.add_button = QPushButton('Tambah')
        self.subtract_button = QPushButton('Kurang')
        self.multiply_button = QPushButton('Kali')
        self.divide_button = QPushButton('Bagi')
        self.sisabagi_button = QPushButton('sisa bagi')
        self.pangkat_button = QPushButton('hasil pangkat')

        # menghubungkan button yang diklik dengan fungsi/method yang ada pada file aritmatika.py
        self.add_button.clicked.connect(self.add_numbers)
        self.subtract_button.clicked.connect(self.subtract_numbers)
        self.multiply_button.clicked.connect(self.multiply_numbers)
        self.divide_button.clicked.connect(self.divide_numbers)
        self.sisabagi_button.clicked.connect(self.fsisabagi)
        self.pangkat_button.clicked.connect(self.fpangkat)

        # membuat sebuah QVBoxLayout dan menambahkan widget
        layout = QVBoxLayout()
        layout.addWidget(self.label_input1)
        layout.addWidget(self.first_number)
        layout.addWidget(self.label_input2)
        layout.addWidget(self.second_number)
        layout.addWidget(self.add_button)
        layout.addWidget(self.subtract_button)
        layout.addWidget(self.multiply_button)
        layout.addWidget(self.divide_button)
        layout.addWidget(self.sisabagi_button)
        layout.addWidget(self.pangkat_button)
        layout.addWidget(self.hasil_label)
        layout.addWidget(self.result_label)


        # mengatur layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)




