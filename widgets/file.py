import os
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QMessageBox, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon, QFont


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

      msg_box.layout().addWidget(layout_widget, 0, 0, 1,
                                 msg_box.layout().columnCount())
      msg_box.exec()

      raise SystemExit(1)
    else:
      with open(self.lock_file_path, 'w') as lock_file:
        lock_file.write(str(os.getpid()))

  @staticmethod
  def remove(lock_file_path):
    if os.path.exists(lock_file_path):
      os.remove(lock_file_path)
