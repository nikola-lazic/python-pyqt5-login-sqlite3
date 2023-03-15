# **Python PyQT5 Login Window**

![Python logo](/img/main_animation.GIF)

</br>LoginWindow.ui is done by using QtDesinger, and then file is converted into .py by using the command:
```
python -m PyQt5.uic.pyuic -x LoginWindow.ui -o LoginWindow.py
```
Main logic is written into login.py.
</br>Credentials for login are stored into users.db.

Libraries used:
- sqlite3, for storing credentials
- pyqt5, for GUI
- black, for code formatting

</br>Please, use: 
```
pip install -r requirements.txt
```