from PyQt6.QtCore import Qt
from PyQt6.QtGui import QShowEvent
from PyQt6.QtWidgets import QGridLayout, QLabel, QMessageBox


class MessageBox(QMessageBox):

  def showEvent(self, a0: QShowEvent | None):
    super().showEvent(a0)
    self.setFixedSize(320, 150)


def show_message(title, text):
  message_box = MessageBox()
  message_box.setWindowTitle(title)
  message_box.setText(text)
  message_box.setIcon(QMessageBox.Icon.NoIcon)
  message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
  message_label = message_box.findChild(QLabel, "qt_msgbox_label")

  if message_label is not None:
    message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    message_layout = message_box.layout()

    if isinstance(message_layout, QGridLayout):
      message_layout.removeWidget(message_label)
      message_layout.addWidget(message_label, 0, 0, 1, 2,
                               Qt.AlignmentFlag.AlignCenter)

  message_box.exec()
