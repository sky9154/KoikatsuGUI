import os
import configparser
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, pyqtSignal
from widgets import CoverImage
from functions import OpenFile, DragFile, ReadMod


class LoadModLayout(QWidget):

  def __init__(self, main_config):
    super().__init__()

    self.main_config = main_config
    self.mod_info = pyqtSignal(dict)
    self.load_mod_info = {}

    widget_config_path = os.path.join(self.main_config['Paths']['config'],
                                      'widget_config.ini')

    widget_config = configparser.ConfigParser()
    widget_config.read(widget_config_path)

    cover_image = CoverImage(main_config, 'load_mod')
    cover_image = cover_image.initUI()

    load_mod_group = QGroupBox(widget_config['General']['load_mod_title'])
    load_mod_layout = QVBoxLayout()

    drag_file = DragFile()
    drag_file.setFixedHeight(50)
    drag_file.setFont(QFont(drag_file.font().family(), 10))
    drag_file.setCursor(Qt.CursorShape.CustomCursor)
    drag_file.setFocusPolicy(Qt.FocusPolicy.NoFocus)
    drag_file.setPlaceholderText(widget_config['LoadMod']['drag_mod'])

    file_path_button = QPushButton(widget_config['LoadMod']['get_mod_info'],
                                   self)
    file_path_button.setFixedHeight(50)
    file_path_button.setFont(QFont(file_path_button.font().family(), 10))
    file_path_button.clicked.connect(
        lambda: self.get_mod_info(drag_file.text()))

    open_folder_button = QPushButton(
        widget_config['LoadMod']['open_mod_folder'], self)
    open_folder_button.setFixedHeight(50)
    open_folder_button.setFont(QFont(open_folder_button.font().family(), 10))
    open_folder_button.clicked.connect(lambda: self.open_mod_folder())

    load_mod_layout.addWidget(drag_file)
    load_mod_layout.addWidget(file_path_button)
    load_mod_layout.addWidget(open_folder_button)

    load_mod_group.setLayout(load_mod_layout)
    load_mod_group.setFont(QFont(load_mod_group.font().family(), 12))

    layout = QVBoxLayout(self)
    layout.addLayout(cover_image)
    layout.addSpacing(20)
    layout.addWidget(load_mod_group)
    layout.setSpacing(10)
    layout.addStretch()

    self.setLayout(layout)

  def get_mod_info(self, file_path):
    if file_path:
      mod = ReadMod(file_path)

      self.load_mod_info = mod.get_info()
      self.mod_info.emit(mod.mod_info)

  def open_mod_folder(self):
    if self.load_mod_info == {}:
      print(None)
    else:
      open_file = OpenFile(self.main_config)
      open_file.open('mod_folder', self.load_mod_info['author'])
