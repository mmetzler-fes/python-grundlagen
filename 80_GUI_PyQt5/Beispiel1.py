from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec()

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
button_top=QPushButton('Top')
layout.addWidget(button_top)
button_top.clicked.connect(on_button_clicked)
button_top.show()
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec()
