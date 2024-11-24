from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QGroupBox
from functions import Config
from widgets import CoverImage, OpenButton


class StudioLayout(QWidget):

  def __init__(self, main_config):
    super().__init__()

    config = Config(main_config['Paths']['config'])
    widget_config = config.load_config('widget_config')

    cover_image = CoverImage(main_config, 'studio')
    cover_image = cover_image.initUI()

    studio_group = QGroupBox(widget_config['General']['studio_title'])
    studio_group.setFont(QFont(studio_group.font().family(), 12))

    studio_layout = QVBoxLayout()

    for name, value in widget_config['StudioButton'].items():
      button = OpenButton(main_config, value, 'Studio',
                          name.replace('_button', ''))
      button = button.initUI()

      studio_layout.addWidget(button)

    studio_group.setLayout(studio_layout)

    layout = QVBoxLayout()
    layout.addLayout(cover_image)
    layout.addSpacing(20)
    layout.addWidget(studio_group)
    layout.setSpacing(10)
    layout.addStretch()

    self.setLayout(layout)
