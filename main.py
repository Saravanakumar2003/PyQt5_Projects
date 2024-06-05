from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.uic import loadUi
import sys
from email_sender import send_email

# Create a class for the email sender
class EmailSender(QMainWindow):
    def __init__(self):
        super(EmailSender, self).__init__()
        loadUi("main.ui", self)
        
        self.emailButton.clicked.connect(self.send_email)
        
    def send_email(self): 
        if self.lineEdit.text(): # Check if the recipient is not empty
            send_email(recipient=self.lineEdit.text(), subject=self.lineEdit_2.text(), email=self.textEdit.toPlainText()) # Send the email
            self.lineEdit.clear() # Clear
            self.textEdit.clear() 
            self.lineEdit_2.clear()
            message = QMessageBox() # Create a message box to show the status of the email 
            message.setIcon(QMessageBox.Information)  # Set the icon of the message box
            message.setText("Email sent successfully!")
            message.setWindowTitle("Success!")
            message.exec_()
        else:
            message = QMessageBox() 
            message.setIcon(QMessageBox.Critical)
            message.setText("Invalid recipient") 
            message.setWindowTitle("Error!")
            message.exec_()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmailSender()
    window.show()
    app.exec_()