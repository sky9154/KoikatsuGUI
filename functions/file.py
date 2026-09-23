import os
from functions import Config


class File:

  def __init__(self, main_config):
    self.main_config = main_config

    config = Config(self.main_config["Paths"]["config"])

    self.widget_config = config.load_config("widget_config")
    self.event_config = config.load_config("event_config")

  def open(self, event, value):
    main_folder = self.main_config["Paths"]["main"]

    if not os.path.isdir(main_folder):
      self.show_missing_path_warning()
      return

    if event == "mod_folder":
      mods_folder = self.event_config["System"]["mods"]

      mod_folder = os.path.join(main_folder, mods_folder)
      mod_author_folder = os.path.join(mod_folder, "MAIN MOD", value)

      target = (mod_author_folder
                if os.path.exists(mod_author_folder) else mod_folder)
    else:
      open_file = self.event_config[event][value]
      target = os.path.join(main_folder, open_file)

    if not os.path.exists(target):
      self.show_missing_path_warning()
      return

    try:
      os.startfile(target)
    except OSError:
      self.show_missing_path_warning()

  def show_missing_path_warning(self):
    from widgets.message_box import show_message

    show_message(self.main_config["General"]["title"],
                 "ファイルまたはフォルダが見つかりません。")
