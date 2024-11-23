import os
import configparser
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont
from functions import OpenFile


class OpenButton(QPushButton):
  def __init__(self, main_config, name, event, value):
    super().__init__()

    self.main_config = main_config
    self.widget_config = self.load_widget_config()
    self.name = name
    self.event = event
    self.value = value

  def initUI(self):
    button = QPushButton(self.name, self)
    button.setFixedHeight(50)
    button.setFont(QFont(button.font().family(), 10))
    button.clicked.connect(lambda: self.open())

    return button

  def load_widget_config(self):
    widget_config_path = os.path.join(self.main_config['Paths']['config'], 'widget_config.ini')

    widget_config = configparser.ConfigParser()
    widget_config.read(widget_config_path)

    return widget_config

  def open(self):
    open_file = OpenFile(self.main_config)
    open_file.open(self.event, self.value)