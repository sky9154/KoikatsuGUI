from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QGroupBox
from functions import Config
from widgets import OpenButton, CoverImage


class CharacterDesignLayout(QWidget):

  def __init__(self, main_config):
    super().__init__()

    config = Config(main_config['Paths']['config'])
    widget_config = config.load_config('widget_config')

    cover_image = CoverImage(main_config, 'character_design')
    cover_image = cover_image.initUI()

    character_design_group = QGroupBox(
        widget_config['General']['character_design_title'])
    character_design_group.setFont(
        QFont(character_design_group.font().family(), 12))

    character_layout = QVBoxLayout()

    for name, value in widget_config['CharacterDesignButton'].items():
      button = OpenButton(main_config, value, 'CharacterDesign',
                          name.replace('_button', ''))
      button = button.initUI()

      character_layout.addWidget(button)

    character_design_group.setLayout(character_layout)

    layout = QVBoxLayout()
    layout.addLayout(cover_image)
    layout.addSpacing(20)
    layout.addWidget(character_design_group)
    layout.setSpacing(10)
    layout.addStretch()

    self.setLayout(layout)
