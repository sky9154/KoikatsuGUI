import os
import configparser
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QLineEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from widgets import CoverImage


class ModInfoLayout(QWidget):

  def __init__(self, main_config):
    super().__init__()

    widget_config_path = os.path.join(main_config['Paths']['config'],
                                      'widget_config.ini')

    widget_config = configparser.ConfigParser()
    widget_config.read(widget_config_path)

    cover_image = CoverImage(main_config, 'mod_info')
    cover_image = cover_image.initUI()

    mod_info_group = QGroupBox(widget_config['General']['mod_info_title'])
    mod_info_group.setFont(QFont(mod_info_group.font().family(), 12))

    mod_info_layout = QVBoxLayout()

    self.info_inputs = {}

    for name, value in widget_config['ModInfo'].items():
      label = QLabel(f'{value}：', self)
      label.setFixedHeight(50)
      label.setFont(QFont(label.font().family(), 10))

      info_input = QLineEdit(self)
      info_input.setObjectName(name)
      info_input.setFixedHeight(40)
      info_input.setFont(QFont(info_input.font().family(), 10))
      info_input.setCursor(Qt.CursorShape.CustomCursor)
      info_input.setFocusPolicy(Qt.FocusPolicy.NoFocus)
      info_input.setPlaceholderText(None)

      self.info_inputs[name] = info_input

      hbox_name = QHBoxLayout()
      hbox_name.addWidget(label, 3)
      hbox_name.addWidget(info_input, 7)

      mod_info_layout.addLayout(hbox_name)

    mod_info_group.setLayout(mod_info_layout)

    layout = QVBoxLayout(self)
    layout.addLayout(cover_image)
    layout.addSpacing(20)
    layout.addWidget(mod_info_group)
    layout.setSpacing(10)
    layout.addStretch()

    self.setLayout(layout)

  def update_info(self, new_info):
    for name, value in new_info.items():
      if name in self.info_inputs:
        self.info_inputs[name].setText(value)
