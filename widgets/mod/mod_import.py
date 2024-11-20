import os
import configparser
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from functions import DragFile


class ModImportWidget(QWidget):
  def __init__(self, main_config):
    super().__init__()

    widget_config_path = os.path.join(main_config['Paths']['config'], 'widget_config.ini')

    widget_config = configparser.ConfigParser()
    widget_config.read(widget_config_path)

    layout = QVBoxLayout(self)

    cover_image_path = os.path.join(main_config['Paths']['images'], widget_config['CoverImage']['mod_import'])

    cover_image = QPixmap(cover_image_path)
    cover_image = cover_image.scaled(128, 128)

    label = QLabel(self)
    label.setPixmap(cover_image)

    hbox_image = QHBoxLayout()
    hbox_image.addStretch(1)
    hbox_image.addWidget(label)
    hbox_image.addStretch(1)

    layout.addLayout(hbox_image)
    layout.addSpacing(20)

    button_group = QGroupBox(widget_config['General']['mod_import_title'])
    button_layout = QVBoxLayout()

    drag_file = DragFile()

    drag_file.setFixedHeight(50)
    drag_file.setPlaceholderText(widget_config['ModImport']['drag_file'])
    drag_file.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    file_path_button = QPushButton(widget_config['ModImport']['print_file_path'], self)
    file_path_button.setFixedHeight(50)
    file_path_button.clicked.connect(lambda: print(drag_file.text()))

    button_layout.addWidget(drag_file)
    button_layout.addWidget(file_path_button)

    button_group.setLayout(button_layout)
    layout.addWidget(button_group)

    layout.setSpacing(10)
    layout.addStretch()

    self.setLayout(layout)