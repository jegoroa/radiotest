from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])
win = QWidget()
win.setStyleSheet('''font-size:32px; background-color:green''')
win.setWindowTitle('вопрос про питон')
win.resize(500, 300)

line = QVBoxLayout()

text = QLabel('какая последняя версия питона сейчас?')
line.addWidget(text, alignment=Qt.AlignCenter)

btn1 = QRadioButton('3.0')
btn2 = QRadioButton('3.10')
btn3 = QRadioButton('3.12')
line.addWidget(btn1)
line.addWidget(btn2)
line.addWidget(btn3)

def lose():
    result = QMessageBox()
    result.setWindowTitle('финал')
    result.setText('неправильно!')
    result.exec()

def check_answer():
    if btn3.isChecked():
        result = QMessageBox()
        result.setWindowTitle('финал')
        result.setText('правильно!')
        result.exec()

        text.setText('какая версия майнкрафта самая новая?')
        btn1.setText('1.19')
        btn2.setText('1.8')
        btn3.setText('0.32')
        btn3.clicked.disconnect(check_answer)
        btn3.clicked.connect(lose)
        btn1.clicked.connect(check_minecraft_answer)

def check_minecraft_answer():
    #тут проверка след. вопроса
    pass

check = QPushButton('проверить')
check.clicked.connect(check_answer)
line.addWidget(check)
#или так или так....
btn1.clicked.connect(lose)
btn2.clicked.connect(lose)
btn3.clicked.connect(check_answer)

win.setLayout(line) #устанавливаем линию в окно
win.show()
app.exec()
