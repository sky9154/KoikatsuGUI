import os
import configparser
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import QGroupBox
from functools import partial
from functions import OpenFile


class CharacterDesignWidget(QWidget):
  def __init__(self, main_config):
    super().__init__()

    widget_config_path = os.path.join(main_config['Paths']['config'], 'widget_config.ini')

    widget_config = configparser.ConfigParser()
    widget_config.read(widget_config_path)

    layout = QVBoxLayout()

    cover_image_path = os.path.join(main_config['Paths']['images'], widget_config['CoverImage']['character_design'])

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

    character_design_group = QGroupBox(widget_config['General']['character_design_title'])
    character_design_group.setFont(QFont(character_design_group.font().family(), 12))

    character_layout = QVBoxLayout()

    for name, value in widget_config['CharacterDesignButton'].items():
      button = QPushButton(value, self)
      button.setFixedHeight(50)
      button.setFont(QFont(button.font().family(), 10))

      character_layout.addWidget(button)

      open_file = OpenFile(main_config)

      button.clicked.connect(partial(open_file.open, 'CharacterDesign', name))

    character_design_group.setLayout(character_layout)
    layout.addWidget(character_design_group)

    layout.setSpacing(10)
    layout.addStretch()

    self.setLayout(layout)