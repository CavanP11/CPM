from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QFrame, QListWidget, QComboBox, QMessageBox
)
from PyQt5.QtCore import Qt
import sys
import random
import string


class PasswordManagerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Proton Pass - Inspired Password Manager")
        self.setGeometry(100, 100, 900, 600)

        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Sidebar
        self.create_sidebar()

        # Main Area
        self.main_frame = QFrame()
        self.main_frame.setStyleSheet("background-color: #2c2c2c;")
        self.main_layout.addWidget(self.main_frame, stretch=3)
        self.main_area_layout = QVBoxLayout()
        self.main_frame.setLayout(self.main_area_layout)

        # Initial screen
        self.show_login_screen()

    def create_sidebar(self):
        sidebar = QFrame()
        sidebar.setFixedWidth(250)
        sidebar.setStyleSheet("background-color: #1c1c1c; color: #ffffff;")
        self.main_layout.addWidget(sidebar)

        sidebar_layout = QVBoxLayout()
        sidebar.setLayout(sidebar_layout)

        # Branding Header
        header = QLabel("Proton Pass")
        header.setStyleSheet("font-size: 20px; font-weight: bold; text-align: center;")
        header.setAlignment(Qt.AlignCenter)
        sidebar_layout.addWidget(header)

        # Buttons
        buttons = [
            ("Dashboard 🏠", self.show_dashboard),
            ("Add Password ➕", self.show_add_password_screen),
            ("Settings ⚙️", self.show_settings),
            ("Logout 🚪", self.show_login_screen),
        ]
        for label, callback in buttons:
            btn = QPushButton(label)
            btn.setStyleSheet(
                "background-color: #444; color: #fff; border: none; padding: 10px; margin: 5px;"
            )
            btn.clicked.connect(callback)
            sidebar_layout.addWidget(btn)

        sidebar_layout.addStretch()  # Push everything up

        # Help button
        help_button = QPushButton("Help ❓")
        help_button.setStyleSheet("background-color: #007bff; color: #fff; border: none; padding: 10px; margin: 5px;")
        help_button.clicked.connect(self.show_help)
        sidebar_layout.addWidget(help_button)

    def clear_main_area(self):
        for i in reversed(range(self.main_area_layout.count())):
            widget = self.main_area_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

    def show_login_screen(self):
        self.clear_main_area()

        layout = QVBoxLayout()
        self.main_area_layout.addLayout(layout)

        label = QLabel("Welcome to Proton Pass")
        label.setStyleSheet("font-size: 18px; color: #fff; font-weight: bold;")
        layout.addWidget(label, alignment=Qt.AlignCenter)

        password_label = QLabel("Enter Master Password:")
        password_label.setStyleSheet("color: #fff;")
        layout.addWidget(password_label)

        password_entry = QLineEdit()
        password_entry.setEchoMode(QLineEdit.Password)
        password_entry.setStyleSheet("background-color: #444; color: #fff; padding: 5px; border: none;")
        layout.addWidget(password_entry)

        login_button = QPushButton("Login")
        login_button.setStyleSheet("background-color: #28a745; color: #fff; padding: 10px; border: none;")
        layout.addWidget(login_button, alignment=Qt.AlignCenter)
        login_button.clicked.connect(lambda: self.validate_master_password(password_entry.text()))

    def validate_master_password(self, password):
        # Placeholder validation logic
        if password == "password":
            self.show_dashboard()
        else:
            QMessageBox.warning(self, "Error", "Invalid Master Password")

    def show_dashboard(self):
        self.clear_main_area()

        label = QLabel("Dashboard")
        label.setStyleSheet("font-size: 16px; color: #fff; font-weight: bold;")
        self.main_area_layout.addWidget(label)

        # List widget for password entries
        password_list = QListWidget()
        password_list.setStyleSheet("background-color: #333; color: #fff; padding: 5px;")
        self.main_area_layout.addWidget(password_list)

        # Placeholder for passwords
        for i in range(10):
            password_list.addItem(f"Service {i+1} - Username {i+1}")

    def show_add_password_screen(self):
        self.clear_main_area()

        layout = QVBoxLayout()
        self.main_area_layout.addLayout(layout)

        label = QLabel("Add New Password")
        label.setStyleSheet("font-size: 16px; color: #fff; font-weight: bold;")
        layout.addWidget(label)

        form_layout = QVBoxLayout()
        layout.addLayout(form_layout)

        for field in ["Service", "Username", "Password"]:
            field_label = QLabel(field)
            field_label.setStyleSheet("color: #fff;")
            form_layout.addWidget(field_label)

            field_input = QLineEdit()
            field_input.setStyleSheet("background-color: #444; color: #fff; padding: 5px; border: none;")
            form_layout.addWidget(field_input)

        save_button = QPushButton("Save Password")
        save_button.setStyleSheet("background-color: #28a745; color: #fff; padding: 10px; border: none;")
        layout.addWidget(save_button, alignment=Qt.AlignCenter)

    def show_settings(self):
        self.clear_main_area()

        layout = QVBoxLayout()
        self.main_area_layout.addLayout(layout)

        label = QLabel("Settings")
        label.setStyleSheet("font-size: 16px; color: #fff; font-weight: bold;")
        layout.addWidget(label)

        theme_label = QLabel("Theme:")
        theme_label.setStyleSheet("color: #fff;")
        layout.addWidget(theme_label)

        theme_selector = QComboBox()
        theme_selector.addItems(["Dark", "Light"])
        theme_selector.setStyleSheet("background-color: #444; color: #fff; padding: 5px;")
        layout.addWidget(theme_selector)

    def show_help(self):
        QMessageBox.information(self, "Help", "Proton Pass Help:\n\n1. Use 'Dashboard' to view saved passwords.\n2. 'Add Password' to store new passwords.\n3. 'Settings' to configure the app.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordManagerGUI()
    window.show()
    sys.exit(app.exec_())
