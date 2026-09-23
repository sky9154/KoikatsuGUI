from PyQt6.QtWidgets import QWidget, QGridLayout, QFrame
from layouts import LoadModLayout, ModInfoLayout


class ModPage(QWidget):

  def __init__(self, config):
    super().__init__()

    self.grid_layout = QGridLayout()
    self.setLayout(self.grid_layout)

    load_mod = LoadModLayout(config)
    mod_info = ModInfoLayout(config)

    line = QFrame()
    line.setFrameShape(QFrame.Shape.VLine)
    line.setStyleSheet("color: gray;")

    self.grid_layout.addWidget(load_mod, 0, 0)
    self.grid_layout.addWidget(line, 0, 1)
    self.grid_layout.addWidget(mod_info, 0, 2)

    load_mod.mod_info.connect(load_mod.update_info)
    load_mod.mod_info.connect(mod_info.update_info)
