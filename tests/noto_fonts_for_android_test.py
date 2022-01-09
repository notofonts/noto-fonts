from lxml import etree
from pathlib import Path
import pytest


_KNOWN_PATHLESS = {
  "NotoSansSyriacEastern-Regular.ttf",
  "NotoSansSyriacWestern-Regular.ttf",
  "NotoSansSymbols-Regular-Subsetted.ttf",
  "NotoColorEmoji.ttf",
  "NotoColorEmojiFlags.ttf",
  "NotoSansSymbols-Regular-Subsetted2.ttf",
  "NotoSansSoyombo-VF.ttf",
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


def test_font_paths_are_valid():
  root = etree.parse(str(_noto_4_android_file()))
  bad = []
  for font in root.xpath("//font[@path]"):
    path = font.attrib["path"]
    file = _font_file(font)
    if not (_repo_root() / path / file).is_file():
      bad.append((path, file))
  assert not bad, "No such file: " + ", ".join(bad)
