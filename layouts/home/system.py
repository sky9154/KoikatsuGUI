from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QGroupBox
from functions import Config
from widgets import CoverImage, OpenButton


class SystemLayout(QWidget):

  def __init__(self, main_config):
    super().__init__()

    config = Config(main_config['Paths']['config'])
    widget_config = config.load_config('widget_config')

    cover_image = CoverImage(main_config, 'system')
    cover_image = cover_image.initUI()

    system_group = QGroupBox(widget_config['General']['system_title'])
    system_group.setFont(QFont(system_group.font().family(), 12))

    system_layout = QVBoxLayout()

    for name, value in widget_config['SystemButton'].items():
      button = OpenButton(main_config, value, 'System',
                          name.replace('_button', ''))
      button = button.initUI()

      system_layout.addWidget(button)

    system_group.setLayout(system_layout)

    layout = QVBoxLayout()
    layout.addLayout(cover_image)
    layout.addSpacing(20)
    layout.addWidget(system_group)
    layout.setSpacing(10)
    layout.addStretch()

    self.setLayout(layout)
