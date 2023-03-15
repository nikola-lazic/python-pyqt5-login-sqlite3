from PyQt5.QtWidgets import QMainWindow, QLineEdit
from ui.LoginWindow import Ui_MainWindow

import sys
import sqlite3


class LoginWindow(QMainWindow, QLineEdit, Ui_MainWindow):
    """Class for the Login window"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        """Signal-slots connections"""
        self.button_login.clicked.connect(self.log_in_button)
        self.lineEdit_username.textEdited.connect(self.status_bar_reset)
        self.lineEdit_password.textEdited.connect(self.status_bar_reset)
        self.checkBox_show_password.stateChanged.connect(self.show_hide_password)

    def status_bar_reset(self):
        """This function resets color and status of statusbar"""
        self.statusBar.clearMessage()  # Clear Message
        self.statusBar.setStyleSheet(
            "background-color : #f0f0f0"
        )  # This is default gray color:

    def show_hide_password(self):
        """This function is showing and hidding text in password field"""
        if self.checkBox_show_password.isChecked():
            self.lineEdit_password.setEchoMode(QLineEdit.Normal)  # Text is visible
        else:
            self.lineEdit_password.setEchoMode(QLineEdit.Password)  # Text is masked

    def log_in_button(self):
        """This function open database (users.db) and check
        if entered username/password combination exists in database"""

        # First, we check if Username is entered:
        if self.lineEdit_username.text() == "":
            self.statusBar.showMessage("Please, enter a username.")
            self.statusBar.setStyleSheet("background-color : pink")

        # We check if Password is entered:
        elif self.lineEdit_password.text() == "":
            self.statusBar.showMessage("Please, enter a password.")
            self.statusBar.setStyleSheet("background-color : pink")

        # In this block username and password are entered:
        else:
            username = self.lineEdit_username.text()
            password = self.lineEdit_password.text()

            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            statement = f"SELECT username FROM credentials WHERE username='{username}' AND password = '{password}';"
            cursor.execute(statement)

            # Finaly, we check if entered usename/password exists in database:
            if not cursor.fetchone():  # Wrong data is entered
                self.statusBar.showMessage("Username or Password is incorrect.")
                self.statusBar.setStyleSheet("background-color : pink")
            else:  # Username and Password exist in database
                self.statusBar.showMessage("Access granted!")
                self.statusBar.setStyleSheet("background-color : lightgreen")


if __name__ == "__main__":
    from PyQt5 import QtWidgets

    # Create PyQt5 app
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    # Create the instance of our Window
    win = LoginWindow()
    win.show()
    # start the app
    sys.exit(app.exec())
