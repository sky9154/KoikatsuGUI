from PyQt6.QtWidgets import QGridLayout, QWidget, QLabel, QVBoxLayout
from widgets import SystemWidget, CharacterDesignWidget, StudioWidget


class CharacterPage(QWidget):
  def __init__(self, parent=None, config=None):
    super().__init__(parent)

    self.layout = QVBoxLayout()
    self.setLayout(self.layout)

    self.label = QLabel('Character Page')
    self.layout.addWidget(self.label)