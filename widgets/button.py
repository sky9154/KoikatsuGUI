from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont
from functions import Config, File, Mod


class OpenButton(QPushButton):

  def __init__(self, main_config, name, event, value):
    super().__init__()

    self.main_config = main_config

    config = Config(self.main_config['Paths']['config'])

    self.widget_config = config.load_config('widget_config')
    self.event_config = config.load_config('event_config')
    self.name = name
    self.event = event
    self.value = value

  def initUI(self):
    self.setText(self.name)
    self.setFixedHeight(50)
    self.setFont(QFont(self.font().family(), 10))
    self.clicked.connect(lambda: self.open_mod_folder()
                         if self.event == 'mod_folder' else self.open())

    return self

  def open(self):
    file = File(self.main_config)
    file.open(self.event, self.value)

  def open_mod_folder(self):
    if self.value:
      file = File(self.main_config)
      file.open('mod_folder', self.value['author'])


class LoadModButton(QPushButton):

  def __init__(self, main_config, name, mod_info, drag_file):
    super().__init__()

    self.main_config = main_config

    config = Config(self.main_config['Paths']['config'])

    self.widget_config = config.load_config('widget_config')
    self.name = name
    self.mod_info = mod_info
    self.drag_file = drag_file

  def initUI(self):
    self.setText(self.name)
    self.setFixedHeight(50)
    self.setFont(QFont(self.font().family(), 10))
    self.clicked.connect(lambda: self.load_mod())

    return self

  def load_mod(self):
    mod_file_path = self.drag_file.text()

    if mod_file_path:
      mod = Mod()
      mod_info = mod.read(mod_file_path)

      self.mod_info.emit(mod_info)
