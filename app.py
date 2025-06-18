from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox
)
import sys
from gui.main_gui import MorseRunnerGUI

def main():
    """Entry point for the PySide-based Morse Runner."""
    app = QApplication(sys.argv)
    config_file = "config/settings.ini"  # Config placeholder
    window = MorseRunnerGUI(config_file)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()