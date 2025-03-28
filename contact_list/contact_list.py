"""The module defines the ContactList class."""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import  QMainWindow, QLineEdit, QPushButton, QTableWidget, QLabel, QVBoxLayout, QWidget, QTableWidgetItem
from PySide6.QtCore import Slot 
from PySide6.QtWidgets import QMessageBox 

class ContactList(QMainWindow):
    """Represents a window that provides the UI to manage contacts."""

    def __init__(self):
        """Initializes a new instance of the ContactList class."""

        super().__init__()
        self.__initialize_widgets()  
        self.add_button.clicked.connect(self.on_add_contact)    

    def __initialize_widgets(self):
        """Initializes the widgets on this Window.
        
        DO NOT EDIT.
        """
        self.setWindowTitle("Contact List")

        self.contact_name_input = QLineEdit(self)
        self.contact_name_input.setPlaceholderText("Contact Name")

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Phone Number")

        self.add_button = QPushButton("Add Contact", self)
        self.remove_button = QPushButton("Remove Contact", self)
        
        self.contact_table = QTableWidget(self)
        self.contact_table.setColumnCount(2)
        self.contact_table.setHorizontalHeaderLabels(["Name", "Phone"])

        self.status_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.contact_name_input)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.contact_table)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    @Slot()
    def on_add_contact(self):
        """
        This method will handle the addition of new contact
        and if the contact name or number is not valid it will send a message.
        """
        contact_name = self.contact_name_input.text()
        phone_number = self.phone_input.text()
        
        row_position = self.contact_table.rowCount()
        self.contact_table.insertRow(row_position)

        name_item = QTableWidgetItem(contact_name)
        phone_item = QTableWidgetItem(phone_number)

        self.contact_table.setItem(row_position, 0, name_item)
        self.contact_table.setItem(row_position, 1, phone_item)

        if not contact_name or phone_number:
            self.status_label.setText(f"Please enter a contact name and phone number")
        else:
            self.status_label.setText(f"Added contact: {contact_name}")

        