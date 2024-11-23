import sys
import os
import atexit
import configparser
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar, QWidget, QStackedWidget, QHBoxLayout
from PyQt6.QtGui import QIcon, QAction
from functions import LockFile
from pages import HomePage, ModPage, CharacterPage


class MainWindow(QMainWindow):
  def __init__(self, config):
    super().__init__()

    self.setWindowTitle(config['General']['title'])
    self.setWindowIcon(QIcon(config['General']['icon']))
    self.setFixedSize(int(config['General']['width']), int(config['General']['height']))

    menu_bar = QMenuBar(self)
    self.setMenuBar(menu_bar)

    page_names = config['Pages']
    pages = [
      (page_names['home'], HomePage),
      (page_names['mod'], ModPage),
      (page_names['character'], CharacterPage)
    ]

    self.stack = QStackedWidget()

    central_widget = QWidget()
    self.setCentralWidget(central_widget)

    for index, (name, PageClass) in enumerate(pages):
      action = QAction(name, self)
      action.triggered.connect(lambda checked, index=index: self.display_page(index))

      menu_bar.addAction(action)

      page = PageClass(config=config)
      self.stack.addWidget(page)

    hbox = QHBoxLayout()
    hbox.addWidget(self.stack)
    central_widget.setLayout(hbox)

  def display_page(self, index):
    self.stack.setCurrentIndex(index)

if __name__ == '__main__':
  app = QApplication(sys.argv)

  main_config_path = os.path.join(os.getcwd(), 'assets', 'config', 'main_config.ini')
  lock_file_path = os.path.join(os.getcwd(), 'app.lock')

  config = configparser.ConfigParser()
  config.read(main_config_path)

  config['General']['icon'] = os.path.join(config['Paths']['images'], config['General']['icon'])

  lock_file = LockFile(app, config, lock_file_path)
  lock_file.create()
  atexit.register(lock_file.remove, lock_file_path)

  window = MainWindow(config)

  window.show()
  sys.exit(app.exec())