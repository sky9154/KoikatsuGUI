from PyQt6.QtWidgets import QGridLayout, QWidget, QLabel, QVBoxLayout
from widgets import SystemWidget, CharacterDesignWidget, StudioWidget


class CharacterPage(QWidget):
  def __init__(self, config=None):
    super().__init__()

    self.layout = QVBoxLayout()
    self.setLayout(self.layout)

    self.label = QLabel('')
    self.layout.addWidget(self.label)