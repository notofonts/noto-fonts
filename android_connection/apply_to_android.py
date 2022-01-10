from pathlib import Path
import sys


def _require_exists(a_file: Path) -> Path:
  if not a_file.is_file():
    raise ValueError(f"{a_file} not found")
  return a_file


def _fonts_xml(android_dir: Path) -> Path:
  return _require_exists(android_dir / "frameworks" / "base" / "data" / "fonts" / "fonts.xml")


def _fonts_mk(android_dir: Path) -> Path:
  return _require_exists(android_dir / "external" / "noto-fonts" / "fonts.mk")


def _validate_android_path(android_dir: Path):
  assert android_dir.is_dir(), f"{android_dir} should be a directory"
  _fonts_xml(android_dir)  # just to trigger it's checks
  _fonts_mk(android_dir)  # just to trigger it's checks


def main():
  if len(sys.argv) != 2:
    raise ValueError("Must have one arg, path to an Android checkout")
  android_dir = Path(sys.argv[1])
  _validate_android_path(android_dir)


if __name__ == "__main__":
  main()