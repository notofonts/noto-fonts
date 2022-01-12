import collections
from fontTools import ttLib
from lxml import etree
from pathlib import Path
import pytest
from typing import Tuple


_KNOWN_PATHLESS = {
  "NotoSansSymbols-Regular-Subsetted.ttf",
  "NotoColorEmoji.ttf",
  "NotoColorEmojiFlags.ttf",
  "NotoSansSymbols-Regular-Subsetted2.ttf",
}



def _repo_root() -> Path:
  root = (Path(__file__).parent / "..").absolute()
  if not (root / "LICENSE").is_file():
    raise IOError(f"{root} does not contain LICENSE")
  return root


def _noto_4_android_file() -> Path:
  xml_file = _repo_root() / "android-connection" / "noto-fonts-4-android.xml"
  if not xml_file.is_file():
    raise IOError(f"No file {xml_file}")
  return xml_file


def _font_file(font_el) -> str:
  return ("".join(font_el.itertext())).strip()


def _font_path(font_el) -> Path:
  name = _font_file(font_el)
  path = font_el.attrib["path"]
  return _repo_root() / path / name


def _is_collection(font_el) -> bool:
  return _font_file(font_el).lower().endswith(".ttc")


def _open_font(font_el) -> ttLib.TTFont:
  path = _font_path(font_el)
  if not path.is_file():
    raise IOError(f"No such file: {path}")

  if _is_collection(font_el):
    return ttLib.TTFont(str(path), fontNumber=int(font_el.attrib["index"]))
  return ttLib.TTFont(str(path))


def _open_font_path(path, fontNumber) -> ttLib.TTFont:
  if not path.is_file():
    raise IOError(f"No such file: {path}")
  if str(path).lower().endswith(".ttc"):
    return ttLib.TTFont(str(path), fontNumber=int(fontNumber))
  return ttLib.TTFont(str(path))


def _axis(font, tag):
  if "fvar" not in font:
    return None
  axes = tuple(a for a in font["fvar"].axes if a.axisTag == tag)
  if not axes:
    return None
  assert len(axes) < 2, f"only 0 or 1 fvar entries supported; {tag} has more"
  return axes[0]


def _weight(font: ttLib.TTFont) -> Tuple[int, int, int]:
  maybe_wght = _axis(font, "wght")
  if maybe_wght:
    return (maybe_wght.minValue, maybe_wght.defaultValue, maybe_wght.maxValue)
  os2_weight = font["OS/2"].usWeightClass
  return (os2_weight, os2_weight, os2_weight)


def test_fonts_have_path():
  root = etree.parse(str(_noto_4_android_file()))
  bad = []
  for font in root.iter("font"):
    font_file = _font_file(font)
    if font_file in _KNOWN_PATHLESS:
      assert "path" not in font.attrib, f"{font_file} not expected to have path. Correct _KNOWN_PATHLESS if you just added path"
      continue

    if not font.attrib.get("path", ""):
      bad.append(font_file)
  assert not bad, "Missing path attribute: " + ", ".join(bad)


def test_ttcs_have_index():
  root = etree.parse(str(_noto_4_android_file()))
  bad = []
  for font in root.iter("font"):
    if not _is_collection(font):
      continue
    if "index" not in font.attrib:
      bad.append(_font_file(font))
  assert not bad, "Missing index attribute: " + ", ".join(bad)


def test_font_paths_are_valid():
  root = etree.parse(str(_noto_4_android_file()))
  bad = []
  for font in root.xpath("//font[@path]"):
    path = _font_path(font)
    if not path.is_file():
      bad.append(str(path))
  assert not bad, "No such file: " + ", ".join(bad)


def test_font_weights():
  root = etree.parse(str(_noto_4_android_file()))
  errors = []
  for font_el in root.xpath("//font[@path]"):
    xml_weight = int(font_el.attrib["weight"])
    path = _font_path(font_el)

    font = _open_font(font_el)
    min_wght, default_wght, max_weight = _weight(font)

    if xml_weight < min_wght or xml_weight > max_weight:
      errors.append(f"{_font_file(font_el)} weight {xml_weight} outside font capability {min_wght}..{max_weight}")

  assert not errors, ", ".join(errors)


def test_font_full_weight_coverage():
  root = etree.parse(str(_noto_4_android_file()))
  errors = []
  for family in root.iter("family"):
    font_to_xml_weights = collections.defaultdict(set)
    for font in family.xpath("//font[@path]"): 
      font_to_xml_weights[(_font_path(font), font.attrib.get("index", -1))].add(int(font.attrib["weight"]))

  # now you have a map of font path => set of weights in xml
  for (font_path, font_number), xml_weights in font_to_xml_weights.items():
  # open the font, compute the 100 weights between it's min/max weight
  # if xml_weights != computed weights add this to the error list
    font = _open_font_path(font_path, font_number)
    min_wght, default_wght, max_weight = _weight(font)
    if min(xml_weights) > min_wght or max(xml_weights) < max_weight:
      errors.append(f"{font_path} weight range {min(xml_weights)}..{max(xml_weights)} could be expanded to {min_wght}..{max_weight}")

  assert not errors, ", ".join(errors)


def test_font_psnames():
  pass
