import os
import configparser
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QPushButton
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt, pyqtSignal
from functions import DragFile, ReadMod


class LoadModWidget(QWidget):
  mod_info = pyqtSignal(dict)

  def __init__(self, main_config):
    super().__init__()

    widget_config_path = os.path.join(main_config['Paths']['config'], 'widget_config.ini')

    widget_config = configparser.ConfigParser()
    widget_config.read(widget_config_path)

    layout = QVBoxLayout(self)

    cover_image_path = os.path.join(main_config['Paths']['images'], widget_config['CoverImage']['load_mod'])

    cover_image = QPixmap(cover_image_path)
    cover_image = cover_image.scaled(128, 128)

    label = QLabel(self)
    label.setPixmap(cover_image)

    hbox_image = QHBoxLayout()
    hbox_image.addStretch(1)
    hbox_image.addWidget(label)
    hbox_image.addStretch(1)

    layout.addLayout(hbox_image)
    layout.addSpacing(20)

    load_mod_group = QGroupBox(widget_config['General']['load_mod_title'])
    load_mod_layout = QVBoxLayout()

    drag_file = DragFile()
    drag_file.setFixedHeight(50)
    drag_file.setFont(QFont(drag_file.font().family(), 10))
    drag_file.setCursor(Qt.CursorShape.CustomCursor)
    drag_file.setFocusPolicy(Qt.FocusPolicy.NoFocus)
    drag_file.setPlaceholderText(widget_config['LoadMod']['drag_file'])

    file_path_button = QPushButton(widget_config['LoadMod']['print_file_path'], self)
    file_path_button.setFixedHeight(50)
    file_path_button.setFont(QFont(file_path_button.font().family(), 10))
    file_path_button.clicked.connect(lambda: self.get_mod_info(drag_file.text()))

    load_mod_layout.addWidget(drag_file)
    load_mod_layout.addWidget(file_path_button)

    load_mod_group.setLayout(load_mod_layout)
    load_mod_group.setFont(QFont(load_mod_group.font().family(), 12))

    layout.addWidget(load_mod_group)

    layout.setSpacing(10)
    layout.addStretch()

    self.setLayout(layout)

  def get_mod_info(self, file_path):
    if file_path:
      mod = ReadMod(file_path)
      mod.get_info()

      self.mod_info.emit(mod.mod_info)