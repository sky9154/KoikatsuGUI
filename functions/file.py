import os
from functions import Config


class File:

  def __init__(self, main_config):
    self.main_config = main_config

    config = Config(self.main_config['Paths']['config'])

    self.widget_config = config.load_config('widget_config')
    self.event_config = config.load_config('event_config')

  def open(self, event, value):
    main_folder = self.main_config['Paths']['main']

    if event == 'mod_folder':
      mods_folder = self.event_config['System']['mods']

      mod_folder = os.path.join(main_folder, mods_folder)
      mod_author_folder = os.path.join(mod_folder, 'MyMods', value)

      os.startfile(mod_author_folder if os.path.exists(mod_author_folder
                                                       ) else mod_folder)
    else:
      open_file = self.event_config[event][value]
      open_file = os.path.join(main_folder, open_file)

      os.startfile(open_file)
