from PyQt6.QtWidgets import QWidget, QGridLayout, QFrame
from widgets import SystemWidget, CharacterDesignWidget, StudioWidget


class HomePage(QWidget):
  def __init__(self, parent=None, config=None):
    super().__init__(parent)

    self.layout = QGridLayout()
    self.setLayout(self.layout)

    self.system_widget = SystemWidget(config)
    self.character_design_widget = CharacterDesignWidget(config)
    self.studio_widget = StudioWidget(config)

    self.line1 = QFrame()
    self.line1.setFrameShape(QFrame.Shape.VLine)
    self.line1.setStyleSheet('color: gray;')

    self.line2 = QFrame()
    self.line2.setFrameShape(QFrame.Shape.VLine)
    self.line2.setStyleSheet('color: gray;')

    self.layout.addWidget(self.system_widget, 0, 0)
    self.layout.addWidget(self.line1, 0, 1)
    self.layout.addWidget(self.character_design_widget, 0, 2)
    self.layout.addWidget(self.line2, 0, 3)
    self.layout.addWidget(self.studio_widget, 0, 4)