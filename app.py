import sys
import os
import atexit
import configparser
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QFrame
from PyQt5.QtGui import QIcon
from functions import LockFile
from layouts import MainLayout


class MainWindow(QMainWindow):
  def __init__(self, config):
    super().__init__()

    self.setWindowTitle(config['General']['title'])
    self.setWindowIcon(QIcon(config['General']['icon']))
    self.setFixedSize(int(config['General']['width']), int(config['General']['height']))

    central_widget = QWidget()
    self.setCentralWidget(central_widget)

    MainLayout(central_widget, config)

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