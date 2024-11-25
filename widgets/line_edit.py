import os
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtGui import QFont, QDragEnterEvent, QDropEvent
from functions import Config


class DragFile(QLineEdit):

  def __init__(self, main_config):
    super().__init__()

    config = Config(main_config['Paths']['config'])

    self.widget_config = config.load_config('widget_config')

    self.setAcceptDrops(True)
    self.file_path = None

  def initUI(self):
    self.setFixedHeight(50)
    self.setFont(QFont(self.font().family(), 10))
    self.setCursor(Qt.CursorShape.CustomCursor)
    self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
    self.setPlaceholderText(self.widget_config['LoadMod']['drag_mod'])

    return self

  def is_mod_file(self, file_path):
    file_extension = os.path.splitext(file_path)[1]
    mod_extensions = ['.zip', 'rar', '7z', '.zipmod']

    return file_extension in mod_extensions

  def dragEnterEvent(self, event: QDragEnterEvent):
    if event.mimeData().hasUrls():
      event.acceptProposedAction()

  def dropEvent(self, event: QDropEvent):
    if event.mimeData().hasUrls():
      self.file_path = event.mimeData().urls()[0].toLocalFile()

      if self.is_mod_file(self.file_path):
        self.setText(self.file_path)
      else:
        event.ignore()

      event.acceptProposedAction()


class InfoLineEdit(QLineEdit):

  def __init__(self, value):
    super().__init__()

    self.value = value

  def initUI(self):
    self.setFixedHeight(40)
    self.setFont(QFont(self.font().family(), 10))
    self.setCursor(Qt.CursorShape.CustomCursor)
    self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
    self.setPlaceholderText(None)

    return self
