import os
import configparser
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import QGroupBox
from functools import partial
from functions import OpenFile


class SystemWidget(QWidget):
  def __init__(self, main_config):
    super().__init__()

    widget_config_path = os.path.join(main_config['Paths']['config'], 'widget_config.ini')

    widget_config = configparser.ConfigParser()
    widget_config.read(widget_config_path)

    layout = QVBoxLayout()

    cover_image_path = os.path.join(main_config['Paths']['images'], widget_config['CoverImage']['system'])

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

    system_group = QGroupBox(widget_config['General']['system_title'])
    system_group.setFont(QFont(system_group.font().family(), 12))

    system_layout = QVBoxLayout()

    for name, value in widget_config['SystemButton'].items():
      button = QPushButton(value, self)
      button.setFixedHeight(50)
      button.setFont(QFont(button.font().family(), 10))

      system_layout.addWidget(button)

      open_file = OpenFile(main_config)

      button.clicked.connect(partial(open_file.open, 'System', name))

    system_group.setLayout(system_layout)
    layout.addWidget(system_group)

    layout.setSpacing(10)
    layout.addStretch()

    self.setLayout(layout)