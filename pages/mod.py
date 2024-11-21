from PyQt6.QtWidgets import QWidget, QGridLayout, QFrame
from widgets import LoadModWidget, ModInfoWidget


class ModPage(QWidget):
  def __init__(self, config=None):
    super().__init__()

    self.layout = QGridLayout()
    self.setLayout(self.layout)

    load_mod = LoadModWidget(config)
    mod_info = ModInfoWidget(config)

    line = QFrame()
    line.setFrameShape(QFrame.Shape.VLine)
    line.setStyleSheet('color: gray;')

    self.layout.addWidget(load_mod, 0, 0)
    self.layout.addWidget(line, 0, 1)
    self.layout.addWidget(mod_info, 0, 2)

    load_mod.mod_info.connect(mod_info.update_info)