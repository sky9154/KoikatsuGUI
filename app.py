import sys
import os
import ctypes
import shutil
import traceback
import configparser
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar, QWidget, QStackedWidget, QHBoxLayout
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import QLockFile
from pages import HomePage, ModPage, CharacterPage
from widgets.message_box import show_message


class MainWindow(QMainWindow):

  def __init__(self, config):
    super().__init__()

    self.setWindowTitle(config["General"]["title"])
    self.setWindowIcon(QIcon(config["General"]["icon"]))
    self.setFixedSize(int(config["General"]["width"]),
                      int(config["General"]["height"]))

    menu_bar = QMenuBar(self)
    self.setMenuBar(menu_bar)

    page_names = config["Pages"]
    pages = [(page_names["home"], HomePage), (page_names["mod"], ModPage),
             (page_names["character"], CharacterPage)]

    self.stack = QStackedWidget()

    central_widget = QWidget()
    self.setCentralWidget(central_widget)

    for index, (name, PageClass) in enumerate(pages):
      action = QAction(name, self)
      action.triggered.connect(
          lambda checked, index=index: self.display_page(index))

      menu_bar.addAction(action)

      page = PageClass(config=config)
      self.stack.addWidget(page)

    hbox = QHBoxLayout()
    hbox.addWidget(self.stack)
    central_widget.setLayout(hbox)

  def display_page(self, index):
    self.stack.setCurrentIndex(index)


class LockFile:

  def __init__(self, config, lock_file_path):
    self.config = config
    self.lock_file_path = lock_file_path
    self.lock = None

  def create(self):
    if not self.prepare_legacy_lock():
      self.show_warning()
      return False

    self.lock = QLockFile(self.lock_file_path)
    self.lock.setStaleLockTime(0)

    if self.lock.tryLock(0):
      return True

    self.show_warning()
    return False

  def prepare_legacy_lock(self):
    try:
      with open(self.lock_file_path, "r", encoding="utf-8") as lock_file:
        lines = lock_file.read().splitlines()

      if len(lines) != 1:
        return True

      pid = int(lines[0].strip())
    except FileNotFoundError:
      return True
    except (OSError, UnicodeError, ValueError):
      return True

    if self.is_process_running(pid):
      return False

    try:
      os.remove(self.lock_file_path)
    except FileNotFoundError:
      pass
    except OSError:
      return False

    return True

  def show_warning(self):
    show_message(self.config["General"]["title"], "既に起動しています。")

  def remove(self):
    if self.lock and self.lock.isLocked():
      self.lock.unlock()

  @staticmethod
  def is_process_running(pid):
    if pid <= 0:
      return False

    synchronize = 0x00100000
    wait_timeout = 0x00000102
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel32.OpenProcess.argtypes = (ctypes.c_ulong, ctypes.c_int,
                                     ctypes.c_ulong)
    kernel32.OpenProcess.restype = ctypes.c_void_p
    kernel32.WaitForSingleObject.argtypes = (ctypes.c_void_p, ctypes.c_ulong)
    kernel32.WaitForSingleObject.restype = ctypes.c_ulong
    kernel32.CloseHandle.argtypes = (ctypes.c_void_p, )
    kernel32.CloseHandle.restype = ctypes.c_int

    handle = kernel32.OpenProcess(synchronize, False, pid)

    if not handle:
      return ctypes.get_last_error() == 5

    try:
      return kernel32.WaitForSingleObject(handle, 0) == wait_timeout
    finally:
      kernel32.CloseHandle(handle)


def resource_directory():
  return getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))


def application_directory():
  if getattr(sys, "frozen", False):
    return os.path.dirname(os.path.abspath(sys.executable))

  return os.path.dirname(os.path.abspath(__file__))


def load_main_config():
  resources = resource_directory()
  main_config_path = os.path.join(resources, "assets", "config",
                                  "main_config.ini")

  config = configparser.ConfigParser()

  if not config.read(main_config_path, encoding="utf-8"):
    raise FileNotFoundError("設定ファイルが見つかりません。")

  for name in ["assets", "config", "images"]:
    path = config["Paths"][name]

    if not os.path.isabs(path):
      path = os.path.join(resources, path)

    config["Paths"][name] = os.path.abspath(path)

  main_folder = os.path.expanduser(os.path.expandvars(config["Paths"]["main"]))
  config["Paths"]["main"] = main_folder
  config["General"]["icon"] = os.path.join(config["Paths"]["images"],
                                           config["General"]["icon"])

  return config


def install_exception_handler(app, config, lock_file):

  def handle_exception(exception_type, exception, exception_traceback):
    details = "".join(
        traceback.format_exception(exception_type, exception,
                                   exception_traceback))
    error_log_path = os.path.join(application_directory(), "app-error.log")

    try:
      with open(error_log_path, "w", encoding="utf-8") as error_log:
        error_log.write(details)
    except OSError:
      pass

    lock_file.remove()
    show_message(config["General"]["title"], "エラーが発生しました。")
    app.exit(1)

  sys.excepthook = handle_exception


def cleanup():
  temp_dir = getattr(sys, "_MEIPASS", None)

  if temp_dir:
    shutil.rmtree(temp_dir, ignore_errors=True)


def main():
  app = QApplication(sys.argv)
  config = None
  lock_file = None

  try:
    config = load_main_config()
    app.setApplicationName(config["General"]["title"])
    app.setWindowIcon(QIcon(config["General"]["icon"]))

    lock_file_path = os.path.join(application_directory(), "app.lock")
    lock_file = LockFile(config, lock_file_path)

    if not lock_file.create():
      return 1

    app.aboutToQuit.connect(lock_file.remove)
    install_exception_handler(app, config, lock_file)

    window = MainWindow(config)

    window.show()
    return app.exec()
  except Exception:
    title = "コイカツ！"

    if config is not None and config.has_option("General", "title"):
      title = config["General"]["title"]

    show_message(title, "起動に失敗しました。")
    return 1
  finally:
    if lock_file:
      lock_file.remove()

    cleanup()


if __name__ == "__main__":
  sys.exit(main())
