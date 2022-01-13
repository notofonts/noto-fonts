import collections
from fontTools import ttLib
from lxml import etree
from pathlib import Path
import pytest
from typing import Tuple
from android_connection.apply_to_android import (
  font_file,
  font_path,
  noto_4_android_path,
)


_KNOWN_PATHLESS = {
  "NotoSansSymbols-Regular-Subsetted.ttf",
  "NotoColorEmoji.ttf",
  "NotoColorEmojiFlags.ttf",
  "NotoSansSymbols-Regular-Subsetted2.ttf",
}


def _is_collection(font_el) -> bool:
  return font_file(font_el).lower().endswith(".ttc")


def _open_font(font_el) -> ttLib.TTFont:
  path = font_path(font_el)
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
  root = etree.parse(str(noto_4_android_path()))
  bad = []
  for font in root.iter("font"):
    name = font_file(font)
    if name in _KNOWN_PATHLESS:
      assert "path" not in font.attrib, f"{name} not expected to have path. Correct _KNOWN_PATHLESS if you just added path"
      continue

    if not font.attrib.get("path", ""):
      bad.append(name)
  assert not bad, "Missing path attribute: " + ", ".join(bad)


def test_ttcs_have_index():
  root = etree.parse(str(noto_4_android_path()))
  bad = []
  for font in root.iter("font"):
    if not _is_collection(font):
      continue
    if "index" not in font.attrib:
      bad.append(font_file(font))
  assert not bad, "Missing index attribute: " + ", ".join(bad)


def test_font_paths_are_valid():
  root = etree.parse(str(noto_4_android_path()))
  bad = []
  for font in root.xpath("//font[@path]"):
    path = font_path(font)
    if not path.is_file():
      bad.append(str(path))
  assert not bad, "No such file: " + ", ".join(bad)


def test_font_weights():
  # TODO: remove expected errors once https://github.com/googlefonts/noto-fonts/issues/2210 fixed
  expected_errors = {
    "NotoNastaliqUrdu-Bold.ttf weight 700 outside font capability 400..400", 
    "NotoSerifMyanmar-Bold.ttf weight 700 outside font capability 400..400"
  }
  root = etree.parse(str(noto_4_android_path()))
  errors = []
  for font_el in root.xpath("//font[@path]"):
    xml_weight = int(font_el.attrib["weight"])
    path = font_path(font_el)

    font = _open_font(font_el)
    min_wght, default_wght, max_weight = _weight(font)

    if xml_weight < min_wght or xml_weight > max_weight:
      error_str = f"{font_file(font_el)} weight {xml_weight} outside font capability {min_wght}..{max_weight}"
      if error_str not in expected_errors:
        errors.append(error_str)

  assert not errors, ", ".join(errors)


def test_font_full_weight_coverage():
  root = etree.parse(str(noto_4_android_path()))
  errors = []
  for family in root.iter("family"):
    font_to_xml_weights = collections.defaultdict(set)
    for font in family.xpath("//font[@path]"): 
      path = font_path(font)
      ttc_idx = font.attrib.get("index", -1)
      font_to_xml_weights[(path, ttc_idx)].add(int(font.attrib["weight"]))

  # now you have a map of font path => set of weights in xml
  for (path, ttc_idx), xml_weights in font_to_xml_weights.items():
  # open the font, compute the 100 weights between it's min/max weight
  # if xml_weights != computed weights add this to the error list
    font = _open_font_path(path, ttc_idx)
    min_wght, default_wght, max_weight = _weight(font)
    if min(xml_weights) > min_wght or max(xml_weights) < max_weight:
      errors.append(f"{path} weight range {min(xml_weights)}..{max(xml_weights)} could be expanded to {min_wght}..{max_weight}")

  assert not errors, ", ".join(errors)


def test_font_psnames():
  pass
