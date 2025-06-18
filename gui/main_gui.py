from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox
)
from simulation.contest import ContestManager
import sys


class MorseRunnerGUI(QMainWindow):
    def __init__(self, config_file):
        super().__init__()
        self.config_file = config_file
        self.contest_manager = ContestManager()

        # Set up the main window
        self.setWindowTitle("Morse Runner - Python Edition")
        self.setGeometry(100, 100, 400, 200)
        self._setup_ui()

    def _setup_ui(self):
        """Set up the GUI layout."""
        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create the layout
        layout = QVBoxLayout()

        # Add a label
        title_label = QLabel("Morse Runner")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; text-align: center;")
        layout.addWidget(title_label)

        # Add a "Start Contest" button
        start_button = QPushButton("Start Contest")
        start_button.clicked.connect(self.start_contest)
        layout.addWidget(start_button)

        # Add layout to central widget
        central_widget.setLayout(layout)

    def start_contest(self):
        """Callback for starting a contest."""
        duration = 60  # Example duration
        # Simulate starting the contest logic
        self.contest_manager.start_contest()
        # Show a message box when the contest is completed
        QMessageBox.information(self, "Contest Completed", "The contest session has ended!")
