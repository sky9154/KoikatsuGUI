import os
import configparser
from PyQt6.QtWidgets import QHBoxLayout, QLabel
from PyQt6.QtGui import QPixmap
from functions import Config


class CoverImage(QLabel):

  def __init__(self, main_config, name):
    super().__init__()

    self.main_config = main_config

    config = Config(self.main_config['Paths']['config'])

    self.widget_config = config.load_config('widget_config')
    self.name = name

  def initUI(self):
    images_path = self.main_config['Paths']['images']
    image_name = self.widget_config['CoverImage'][self.name]
    image_path = os.path.join(images_path, image_name)

    image = QPixmap(image_path)
    image = image.scaled(128, 128)

    self.setPixmap(image)

    cover_image = QHBoxLayout()
    cover_image.addStretch(1)
    cover_image.addWidget(self)
    cover_image.addStretch(1)

    return cover_image
