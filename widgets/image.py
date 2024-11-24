import os
import configparser
from PyQt6.QtWidgets import QHBoxLayout, QLabel
from PyQt6.QtGui import QPixmap


class CoverImage(QLabel):

  def __init__(self, main_config, name):
    super().__init__()

    self.main_config = main_config
    self.widget_config = self.load_widget_config()
    self.name = name

  def initUI(self):
    image_path = os.path.join(self.main_config['Paths']['images'],
                              self.widget_config['CoverImage'][self.name])

    image = QPixmap(image_path)
    image = image.scaled(128, 128)

    self.setPixmap(image)

    cover_image = QHBoxLayout()
    cover_image.addStretch(1)
    cover_image.addWidget(self)
    cover_image.addStretch(1)

    return cover_image

  def load_widget_config(self):
    widget_config_path = os.path.join(self.main_config['Paths']['config'],
                                      'widget_config.ini')

    widget_config = configparser.ConfigParser()
    widget_config.read(widget_config_path)

    return widget_config
