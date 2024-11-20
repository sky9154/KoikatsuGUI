import sys
import os
import configparser
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QMessageBox, QLineEdit, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon, QFont, QDragEnterEvent, QDropEvent


class LockFile:
  def __init__(self, app, config, lock_file_path):
    self.app = app
    self.config = config
    self.lock_file_path = lock_file_path

  def create(self):
    self.app.setApplicationName(self.config['General']['title'])

    if os.path.exists(self.lock_file_path):
      msg_box = QMessageBox()

      msg_box.setWindowTitle(self.config['General']['title'])
      msg_box.setWindowIcon(QIcon(self.config['General']['icon']))
      msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)

      label = QLabel('アプリケーションは既に実行中です。')
      font = QFont()
      font.setPointSize(10)
      label.setFont(font)
      label.setAlignment(Qt.AlignmentFlag.AlignCenter)

      layout = QVBoxLayout()
      layout.addWidget(label)
      layout_widget = QWidget()
      layout_widget.setLayout(layout)

      msg_box.layout().addWidget(layout_widget, 0, 0, 1, msg_box.layout().columnCount())
      msg_box.exec()

      sys.exit(1)
    else:
      with open(self.lock_file_path, 'w') as lock_file:
        lock_file.write(str(os.getpid()))

  @staticmethod
  def remove(lock_file_path):
    if os.path.exists(lock_file_path):
      os.remove(lock_file_path)


class DragFile(QLineEdit):
  def __init__(self, parent=None):
    super().__init__(parent)

    self.setAcceptDrops(True)
    self.file_path = None

  def dragEnterEvent(self, event: QDragEnterEvent):
    if event.mimeData().hasUrls():
      event.acceptProposedAction()

  def dropEvent(self, event: QDropEvent):
    if event.mimeData().hasUrls():
      self.file_path = event.mimeData().urls()[0].toLocalFile()
      self.setText(self.file_path)

      event.acceptProposedAction()


class OpenFile:
  def __init__(self, main_config):
    self.main_config = main_config
    self.event_config = self.load_event_config()

  def load_event_config(self):
    event_config_path = os.path.join(self.main_config['Paths']['config'], 'event_config.ini')
    event_config = configparser.ConfigParser()
    event_config.read(event_config_path)

    return event_config

  def open(self, event, button_id):
    button_event = button_id.replace('_button', '')
    self.event_config[event][button_event] = os.path.join(self.main_config['Paths']['main'], self.event_config[event][button_event])
    os.startfile(self.event_config[event][button_event])