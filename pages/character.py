from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout


class CharacterPage(QWidget):

  def __init__(self, config):
    super().__init__()

    self.layout = QVBoxLayout()
    self.setLayout(self.layout)

    self.label = QLabel('')
    self.layout.addWidget(self.label)
