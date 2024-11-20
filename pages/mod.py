from PyQt6.QtWidgets import QWidget, QGridLayout, QFrame
from widgets import ModImportWidget


class ModPage(QWidget):
  def __init__(self, parent=None, config=None):
    super().__init__(parent)

    self.layout = QGridLayout()
    self.setLayout(self.layout)

    self.system_widget = ModImportWidget(config)

    self.line = QFrame()
    self.line.setFrameShape(QFrame.Shape.VLine)
    self.line.setStyleSheet('color: gray;')

    self.layout.addWidget(self.system_widget, 0, 0)
    # self.layout.addWidget(self.line, 0, 1)