from PyQt6.QtWidgets import QWidget, QGridLayout, QFrame
from layouts import SystemLayout, CharacterDesignLayout, StudioLayout


class HomePage(QWidget):

  def __init__(self, config):
    super().__init__()

    self.grid_layout = QGridLayout()
    self.setLayout(self.grid_layout)

    system = SystemLayout(config)
    character_design = CharacterDesignLayout(config)
    studio = StudioLayout(config)

    line1 = QFrame()
    line1.setFrameShape(QFrame.Shape.VLine)
    line1.setStyleSheet("color: gray;")

    line2 = QFrame()
    line2.setFrameShape(QFrame.Shape.VLine)
    line2.setStyleSheet("color: gray;")

    self.grid_layout.addWidget(system, 0, 0)
    self.grid_layout.addWidget(line1, 0, 1)
    self.grid_layout.addWidget(character_design, 0, 2)
    self.grid_layout.addWidget(line2, 0, 3)
    self.grid_layout.addWidget(studio, 0, 4)
