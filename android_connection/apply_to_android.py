from absl import app
from absl import flags
import filecmp
from lxml import etree
from pathlib import Path
import shutil


FLAGS = flags.FLAGS


flags.DEFINE_string("android_root", None, "Root of android repo")
flags.DEFINE_bool("dry_run", True, "If False actually update files")


def _require_exists(a_file: Path) -> Path:
  if not a_file.is_file():
    raise ValueError(f"{a_file} missing or not a file")
  return a_file


def _require_dir_exists(a_dir: Path) -> Path:
  if not a_dir.is_dir():
    raise ValueError(f"{a_dir} missing or not a dir")
  return a_dir


def _fonts_xml(android_dir: Path) -> Path:
  return _require_exists(android_dir / "frameworks" / "base" / "data" / "fonts" / "fonts.xml")


def _fonts_mk(android_dir: Path) -> Path:
  return _require_exists(android_dir / "external" / "noto-fonts" / "fonts.mk")


def _font_dir(android_dir: Path) -> Path:
  return _require_dir_exists(android_dir / "external" / "noto-fonts" / "other")


def _repo_root() -> Path:
  root = (Path(__file__).parent.parent).absolute()
  if not (root / "LICENSE").is_file():
    raise IOError(f"{root} does not contain LICENSE")
  return root


def noto_4_android_path() -> Path:
  xml_file = _repo_root() / "android_connection" / "noto-fonts-4-android.xml"
  if not xml_file.is_file():
    raise IOError(f"No file {xml_file}")
  return xml_file


def font_file(font_el) -> str:
  return ("".join(font_el.itertext())).strip()


def font_path(font_el) -> Path:
  name = font_file(font_el)
  path = font_el.attrib["path"]
  return _require_exists(_repo_root() / path / name)


def _validate_android_path(android_dir: Path):
  assert android_dir.is_dir(), f"{android_dir} should be a directory"
    # just to trigger existance validation
  _fonts_xml(android_dir)
  _fonts_mk(android_dir)
  _font_dir(android_dir)


def main(_):
  if not FLAGS.android_root:
    raise ValueError("Must provide --android_root")
  android_dir = Path(FLAGS.android_root)
  _validate_android_path(android_dir)

  # gather fonts that should be copied to Android
  noto_for_android = etree.parse(str(noto_4_android_path()))
  new_paths = {}
  for font_el in noto_for_android.xpath("//font[@path]"):
    path = font_path(font_el)
    if new_paths.get(path.name, path) != path:
      raise IOError(f"Multiple paths for {path.name}")
    new_paths[path.name] = path
  old_paths = {p.name: p for p in _font_dir(android_dir).glob("Noto*.[ot]t[fc]")}

  new_names = set(new_paths.keys())
  old_names = set(old_paths.keys())

  delta_sz = 0

  deleted_files = old_names - new_names
  print(f"{len(deleted_files)} DELETED")
  for delete_me in sorted(deleted_files):
    print(f"  {delete_me}")
    if not FLAGS.dry_run:
      old_paths[delete_me].unlink()
  del delete_me
  del deleted_files
  print()

  added_files = new_names - old_names
  print(f"{len(added_files)} ADDED")
  for add_me in sorted(added_files):
    dest = _font_dir(android_dir) / add_me
    print(f"  {add_me}")
    if not FLAGS.dry_run:
      shutil.copy(new_paths[add_me], dest)
  del add_me
  del added_files
  print()

  updated_files = new_names & old_names
  untouched = 0
  print(f"{len(updated_files)} UPDATED")
  for update_me in sorted(updated_files):
    if filecmp.cmp(new_paths[update_me], old_paths[update_me], shallow=False):
      untouched += 1
      continue

    dest = _font_dir(android_dir) / update_me
    print(f"  {update_me}")
    if not FLAGS.dry_run:
      shutil.copy(new_paths[update_me], dest)
  del update_me
  del updated_files
  print()

  print(f"{untouched} did not change")
  print()

  print(f"Done updating files, you should manually update {_fonts_xml(android_dir)}"
        f" from {noto_4_android_path()}")


if __name__ == "__main__":
    app.run(main)