from android_connection.apply_to_android import _validate_android_path
from lxml import etree
from pathlib import Path
import pytest


def _testdata_dir() -> Path:
  return Path(__file__).parent / "testdata"


def _fake_android_dir() -> Path:
  return _testdata_dir() / "fake_android"


def test_validate_bad_dir():
  with pytest.raises(ValueError, match="missing"):
    _validate_android_path(_testdata_dir())


def test_validate_good_dir():
  _validate_android_path(_fake_android_dir())

