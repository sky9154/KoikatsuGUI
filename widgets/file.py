import os
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QMessageBox, QLineEdit, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon, QFont, QDragEnterEvent, QDropEvent
from functions import Config


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

        return

      event.acceptProposedAction()
