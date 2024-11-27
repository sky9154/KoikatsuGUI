import os
from PyQt6.QtWidgets import QPushButton, QFileDialog
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt, QSize
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
    self.setCursor(Qt.CursorShape.PointingHandCursor)
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

  def __init__(self, main_config, name, mod_info, mod_path):
    super().__init__()

    self.main_config = main_config

    config = Config(self.main_config['Paths']['config'])

    self.widget_config = config.load_config('widget_config')
    self.name = name
    self.mod_info = mod_info
    self.mod_path = mod_path

  def initUI(self):
    self.setText(self.name)
    self.setFixedHeight(50)
    self.setFont(QFont(self.font().family(), 10))
    self.setCursor(Qt.CursorShape.PointingHandCursor)
    self.clicked.connect(lambda: self.load_mod())

    return self

  def load_mod(self):
    mod_path = self.mod_path.text()

    if mod_path:
      mod = Mod()
      mod_info = mod.read(mod_path)

      self.mod_info.emit(mod_info)


class DialogModButton(QPushButton):

  def __init__(self, main_config, drag_mod):
    super().__init__()

    self.main_config = main_config

    config = Config(self.main_config['Paths']['config'])

    self.widget_config = config.load_config('widget_config')
    self.drag_mod = drag_mod

  def initUI(self):
    images_path = self.main_config['Paths']['images']
    icon_name = self.widget_config['CoverImage']['dialog_mod']
    icon_path = os.path.join(images_path, icon_name)
    icon = QIcon(icon_path)

    self.setFixedHeight(50)
    self.setIconSize(QSize(26, 30))
    self.setIcon(icon)
    self.setStyleSheet('''
      border : 0;
      background: transparent;
    ''')
    self.setCursor(Qt.CursorShape.PointingHandCursor)
    self.clicked.connect(lambda: self.show_mod_dialog())

    return self

  def show_mod_dialog(self):
    mod_dialog = QFileDialog()
    mod_dialog.setWindowTitle(self.widget_config['General']['dialog_mod_title'])
    mod_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)

    mod_dialog.setNameFilter('Mod Files (*.zip *.rar *.7z *.zipmod)')
    mod_dialog.fileSelected.connect(self.print_mod_path)
    mod_dialog.setDirectory(os.path.dirname(self.drag_mod.text()))
    mod_dialog.exec()

  def print_mod_path(self, mod_path):
    self.drag_mod.setText(mod_path)
