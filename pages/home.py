from PyQt6.QtWidgets import QWidget, QGridLayout, QFrame
from widgets import SystemWidget, CharacterDesignWidget, StudioWidget


class HomePage(QWidget):
  def __init__(self, config=None):
    super().__init__()

    self.layout = QGridLayout()
    self.setLayout(self.layout)

    system = SystemWidget(config)
    character_design = CharacterDesignWidget(config)
    studio = StudioWidget(config)

    line1 = QFrame()
    line1.setFrameShape(QFrame.Shape.VLine)
    line1.setStyleSheet('color: gray;')

    line2 = QFrame()
    line2.setFrameShape(QFrame.Shape.VLine)
    line2.setStyleSheet('color: gray;')

    self.layout.addWidget(system, 0, 0)
    self.layout.addWidget(line1, 0, 1)
    self.layout.addWidget(character_design, 0, 2)
    self.layout.addWidget(line2, 0, 3)
    self.layout.addWidget(studio, 0, 4)