from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGroupBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import pyqtSignal
from widgets import CoverImage, DragFile, LoadModButton, OpenButton
from functions import Config


class LoadModLayout(QWidget):

  mod_info = pyqtSignal(dict)

  def __init__(self, main_config):
    super().__init__()

    self.update_mod_info = {}

    config = Config(main_config['Paths']['config'])
    widget_config = config.load_config('widget_config')

    cover_image = CoverImage(main_config, 'load_mod')
    cover_image = cover_image.initUI()

    load_mod_group = QGroupBox(widget_config['General']['load_mod_title'])
    load_mod_group.setFont(QFont(load_mod_group.font().family(), 12))

    drag_file = DragFile(main_config)
    drag_file = drag_file.initUI()

    load_mod_button = LoadModButton(main_config,
                                    widget_config['LoadMod']['load_mod_info'],
                                    self.mod_info, drag_file)
    load_mod_button = load_mod_button.initUI()

    open_folder_button = OpenButton(
        main_config, widget_config['LoadMod']['open_mod_folder'], 'mod_folder',
        self.update_mod_info)
    open_folder_button = open_folder_button.initUI()

    load_mod_layout = QVBoxLayout()
    load_mod_layout.addWidget(drag_file)
    load_mod_layout.addWidget(load_mod_button)
    load_mod_layout.addWidget(open_folder_button)

    load_mod_group.setLayout(load_mod_layout)

    layout = QVBoxLayout(self)
    layout.addLayout(cover_image)
    layout.addSpacing(20)
    layout.addWidget(load_mod_group)
    layout.setSpacing(10)
    layout.addStretch()

    self.setLayout(layout)

  def update_info(self, new_info):
    for name, value in new_info.items():
      self.update_mod_info[name] = value
