from android_connection import apply_to_android
from pathlib import Path
import pytest


def _testdata_dir() -> Path:
  return Path(__file__).parent / "testdata"


def _fake_android_dir() -> Path:
  return _testdata_dir() / "fake_android"


def test_apply_to_bad_dir():
  with pytest.raises(ValueError, match="not found"):
    apply_to_android._validate_android_path(_testdata_dir())


def test_apply_to_good_dir():
  apply_to_android._validate_android_path(_fake_android_dir())
