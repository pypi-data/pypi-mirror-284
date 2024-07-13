import tempfile

from pathlib import Path

import pytest

from clapper.rc import UserDefaults

from bob.bio.base.database.utils import download_file

RESOURCE_URL = "https://www.idiap.ch/software/bob/databases/latest/base/atnt-f529acef.tar.gz"
RESOURCE_NAME = "atnt-f529acef.tar.gz"
RESOURCE_EXTRACTED_NAME = "atnt"
RESOURCE_CHECKSUM = "f529acef"
INVALID_URL_VALID_NAME = (
    "https://localhost/ysnctp/not/a/valid/path/atnt-f529acef.tar.gz"
)
INVALID_URL_INVALID_NAME = "https://localhost/ysnctp/not/a/valid/path"


def _create_custom_rc(rc_path: Path, **kwargs):
    """This creates a config file dynamically, with the content of kwargs."""
    rc_path.parent.mkdir(exist_ok=True)
    rc = UserDefaults(rc_path)
    for k, v in kwargs.items():
        rc[k] = v
    rc.write()


def test_download_file_defaults(monkeypatch: pytest.MonkeyPatch):
    "Downloads to bob_data_dir, with all default settings."
    with tempfile.TemporaryDirectory(prefix="test_download_") as tmp_dir:
        dir_path = Path(tmp_dir)
        data_path = dir_path / "bob_data"
        monkeypatch.setenv("HOME", dir_path.as_posix())
        expected_result = data_path / RESOURCE_NAME
        local_filename = download_file(urls=RESOURCE_URL)
        assert local_filename == expected_result
        assert local_filename.is_file()


def test_download_file_custom_data_dir_no_subdir(
    monkeypatch: pytest.MonkeyPatch,
):
    "Downloads to a custom bob_data_dir, with all default settings."
    with tempfile.TemporaryDirectory(prefix="test_download_") as tmp_dir:
        dir_path = Path(tmp_dir)
        data_path = dir_path / "custom_bob_data"
        rc_path = dir_path / ".config" / "bobrc.toml"
        _create_custom_rc(rc_path=rc_path, bob_data_dir=data_path.as_posix())
        monkeypatch.setenv("HOME", dir_path.as_posix())
        expected_result = data_path / RESOURCE_NAME
        local_filename = download_file(urls=RESOURCE_URL)
        assert local_filename == expected_result
        assert local_filename.is_file()


def test_download_file_custom_data_dir_and_subdir(
    monkeypatch: pytest.MonkeyPatch,
):
    "Downloads to a custom bob_data_dir, with all default settings."
    with tempfile.TemporaryDirectory(prefix="test_download_") as tmp_dir:
        dir_path = Path(tmp_dir)
        data_path = dir_path / "custom_bob_data"
        rc_path = dir_path / ".config" / "bobrc.toml"
        _create_custom_rc(rc_path=rc_path, bob_data_dir=data_path.as_posix())
        monkeypatch.setenv("HOME", dir_path.as_posix())
        subdir = Path("download") / "subdir"
        expected_result = data_path / subdir / RESOURCE_NAME
        local_filename = download_file(
            urls=RESOURCE_URL, destination_sub_directory=subdir
        )
        assert local_filename == expected_result
        assert local_filename.is_file()


def test_download_file_to_dir_no_subdir():
    with tempfile.TemporaryDirectory(prefix="test_download_") as tmp_dir:
        destination = Path(tmp_dir) / "download_dir"
        expected_result = destination / RESOURCE_NAME
        local_filename = download_file(
            urls=RESOURCE_URL,
            destination_directory=destination,
        )
        assert local_filename == expected_result
        assert local_filename.is_file()


def test_download_file_to_dir_and_subdir():
    with tempfile.TemporaryDirectory(prefix="test_download_") as tmp_dir:
        destination = Path(tmp_dir)
        subdir = Path("download") / "subdir"
        expected_result = destination / subdir / RESOURCE_NAME
        local_filename = download_file(
            urls=RESOURCE_URL,
            destination_directory=destination,
            destination_sub_directory=subdir,
        )
        assert local_filename == expected_result
        assert local_filename.is_file()


def test_download_file_rename():
    with tempfile.TemporaryDirectory(prefix="test_download_") as tmp_dir:
        destination = Path(tmp_dir)
        subdir = Path("download") / "subdir"
        new_name = "custom_name.tar.gz"
        expected_result = destination / subdir / new_name
        local_filename = download_file(
            urls=RESOURCE_URL,
            destination_directory=destination,
            destination_sub_directory=subdir,
            destination_filename=new_name,
        )
        assert local_filename == expected_result
        assert local_filename.is_file()


def test_download_file_with_checksum():
    with tempfile.TemporaryDirectory(prefix="test_download_") as tmp_dir:
        destination = Path(tmp_dir)
        expected_result = destination / RESOURCE_NAME
        local_filename = download_file(
            urls=RESOURCE_URL,
            destination_directory=destination,
            checksum=RESOURCE_CHECKSUM,
        )
        assert local_filename == expected_result
        assert local_filename.is_file()


def test_download_file_multi_url_valid_names():
    with tempfile.TemporaryDirectory(prefix="test_download_") as tmp_dir:
        destination = Path(tmp_dir)
        expected_result = destination / RESOURCE_NAME
        local_filename = download_file(
            urls=[INVALID_URL_VALID_NAME, RESOURCE_URL],
            destination_directory=destination,
            checksum=RESOURCE_CHECKSUM,
        )
        assert local_filename == expected_result
        assert local_filename.is_file()


def test_download_file_multi_url_invalid_names():
    with tempfile.TemporaryDirectory(prefix="test_download_") as tmp_dir:
        destination = Path(tmp_dir)
        with pytest.raises(ValueError):
            download_file(
                urls=[RESOURCE_URL, INVALID_URL_INVALID_NAME],
                destination_directory=destination,
                checksum=RESOURCE_CHECKSUM,
            )


def test_download_file_extract_no_subdir():
    with tempfile.TemporaryDirectory(prefix="test_download_") as tmp_dir:
        destination = Path(tmp_dir)
        expected_result = destination
        local_filename = download_file(
            urls=RESOURCE_URL,
            destination_directory=destination,
            checksum=RESOURCE_CHECKSUM,
            extract=True,
        )
        assert local_filename == expected_result
        assert (local_filename / RESOURCE_EXTRACTED_NAME).is_dir()


def test_download_file_extract_with_subdir():
    with tempfile.TemporaryDirectory(prefix="test_download_") as tmp_dir:
        destination = Path(tmp_dir)
        subdir = Path("download") / "subdir"
        expected_result = destination / subdir
        local_filename = download_file(
            urls=RESOURCE_URL,
            destination_directory=destination,
            destination_sub_directory=subdir,
            checksum=RESOURCE_CHECKSUM,
            extract=True,
        )
        assert local_filename == expected_result
        assert (local_filename / RESOURCE_EXTRACTED_NAME).is_dir()
