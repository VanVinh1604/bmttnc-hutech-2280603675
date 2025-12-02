import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow

# Caesar cipher logic
def caesar_encrypt(text, key):
    try:
        shift = int(key) % 26
    except ValueError:
        return "Key must be an integer!"
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def caesar_decrypt(text, key):
    try:
        shift = int(key) % 26
    except ValueError:
        return "Key must be an integer!"
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char
    return result

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Map đúng tên widget trong UI
        self.ui.pushButton.clicked.connect(self.encrypt_text)
        self.ui.pushButton_2.clicked.connect(self.decrypt_text)

    def encrypt_text(self):
        plain_text = self.ui.textEdit.toPlainText()
        key = self.ui.textEdit_2.toPlainText()
        cipher_text = caesar_encrypt(plain_text, key)
        self.ui.textEdit_3.setText(cipher_text)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Encrypted Successfully")
        msg.exec_()

    def decrypt_text(self):
        cipher_text = self.ui.textEdit_3.toPlainText()
        key = self.ui.textEdit_2.toPlainText()
        plain_text = caesar_decrypt(cipher_text, key)
        self.ui.textEdit.setText(plain_text)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Decrypted Successfully")
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
