import zipfile
import xml.etree.ElementTree as ET


class Mod:

  def read(self, file_path):
    mod_info = {}

    with zipfile.ZipFile(file_path, 'r') as zipmod:
      with zipmod.open('manifest.xml') as manifest:
        tree = ET.parse(manifest)
        root = tree.getroot()

        for child in root:
          mod_info[child.tag] = child.text.strip() if child.text else 'None'

    return mod_info
