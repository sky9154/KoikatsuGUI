from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGroupBox
from PyQt6.QtGui import QFont
from widgets import CoverImage, InfoLabel, InfoLineEdit
from functions import Config


class ModInfoLayout(QWidget):

  def __init__(self, main_config):
    super().__init__()

    config = Config(main_config['Paths']['config'])
    widget_config = config.load_config('widget_config')

    cover_image = CoverImage(main_config, 'mod_info')
    cover_image = cover_image.initUI()

    mod_info_group = QGroupBox(widget_config['General']['mod_info_title'])
    mod_info_group.setFont(QFont(mod_info_group.font().family(), 12))

    mod_info_layout = QVBoxLayout()

    self.info_line_edits = {}

    for name, value in widget_config['ModInfo'].items():
      info_label = InfoLabel(value)
      info_label = info_label.initUI()

      info_line_edit = InfoLineEdit(name)
      info_line_edit = info_line_edit.initUI()

      self.info_line_edits[name] = info_line_edit

      info = QHBoxLayout()
      info.addWidget(info_label, 3)
      info.addWidget(info_line_edit, 7)

      mod_info_layout.addLayout(info)

    mod_info_group.setLayout(mod_info_layout)

    layout = QVBoxLayout(self)
    layout.addLayout(cover_image)
    layout.addSpacing(20)
    layout.addWidget(mod_info_group)
    layout.setSpacing(10)
    layout.addStretch()

    self.setLayout(layout)

  def update_info(self, new_info):
    for name, value in new_info.items():
      if name in self.info_line_edits:
        self.info_line_edits[name].setText(value)
