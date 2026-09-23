import os
import re
import zipfile
import xml.etree.ElementTree as ET


class Mod:

  def read(self, mod_path):
    mod_info = {}

    with zipfile.ZipFile(mod_path, "r") as zipmod:
      with zipmod.open("manifest.xml") as manifest:
        tree = ET.parse(manifest)
        root = tree.getroot()
        author = os.path.basename(mod_path)

        for child in root:
          mod_info[child.tag] = child.text.strip() if child.text else "None"

        if mod_info["author"] == "None" and (match := re.search(
            r"\[(.*?)\]", author)):
          mod_info["author"] = match.group(1)

    return mod_info
