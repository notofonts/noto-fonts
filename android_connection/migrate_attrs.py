"""Quick & dirty script to tweak original sources format"""

from lxml import etree
from pathlib import Path

fs_root = Path(__file__).parent.parent

print(fs_root)

xml_file = Path(__file__).parent / 'noto-fonts-4-android.xml'
root = etree.parse(str(xml_file))

drop_me = []

for fsp in root.iter("fontsourcepath"):
  drop_me.append(fsp)

  rel_path_to_font = fsp.attrib["path"]
  if rel_path_to_font == "TBD":
    continue

  assert (fs_root / rel_path_to_font).is_file(), f"Missing {rel_path_to_font}"

  font = fsp.getnext()
  while font is not None and font.tag == "font":
    font_file =  (''.join(font.itertext())).strip()
    assert Path(rel_path_to_font).name == font_file, f"{rel_path_to_font} mismatched with {font_file}"

    rel_path_to_dir = str(Path(rel_path_to_font).parent)
    assert (fs_root / rel_path_to_dir).is_dir(), rel_path_to_dir

    font_path = font.attrib.get("noto_repo_path", rel_path_to_dir)
    assert font_path == rel_path_to_dir, f"<font> path {font_path} to_dir {rel_path_to_dir}"
    font.attrib["path"] = rel_path_to_dir

    font = font.getnext()


for el in reversed(drop_me):
  el.getparent().remove(el)

root.write(str(xml_file), encoding="utf-8", xml_declaration=True)

