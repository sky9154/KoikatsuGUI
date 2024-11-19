import os
import configparser


def load_event_config(main_config):
  event_config_path = os.path.join(main_config['Paths']['config'], 'event_config.ini')

  event_config = configparser.ConfigParser()
  event_config.read(event_config_path)

  return event_config

def open(event, main_config, button_id):
  event_config = load_event_config(main_config)
  button_event = button_id.replace('_button', '')

  event_config[event][button_event] = os.path.join(main_config['Paths']['main'], event_config[event][button_event])

  os.startfile(event_config[event][button_event])