import json
import pathlib
from pathlib import Path
from typing import List, Optional

import pytest


JOPLIN_NOTES = [
    {
        'text': 'Text\n\n\n',
        'note_str': """Text

id: ed32a42ecfc543138de7e5364c3d96df
parent_id: c46ed30189d64b1aac07f7bb14237998
created_time: 2012-04-02T08:11:31.000Z
updated_time: 2012-04-02T08:11:31.000Z
is_conflict: 0
latitude: 0.00000000
longitude: 0.00000000
altitude: 0.0000
author: 
source_url: 
is_todo: 0
todo_due: 0
todo_completed: 0
source: joplin-desktop
source_application: net.cozic.joplin-desktop
application_data: 
order: 0
user_created_time: 2012-04-02T08:11:31.000Z
user_updated_time: 2012-04-02T08:11:31.000Z
encryption_cipher_text: 
encryption_applied: 0
markup_language: 1
type_: 1""",
    }
]


@pytest.fixture(scope='function', params=JOPLIN_NOTES)
def joplin_note(request):
    return request.param


def _get_repo_root_dir() -> str:
    """
    :return: path to the project folder.
    `tests/` should be in the same folder and this file should be in the root of `tests/`.
    """
    return str(Path(__file__).parent.parent)


ROOT_DIR = _get_repo_root_dir()
RESOURCES = pathlib.Path(f"{ROOT_DIR}/tests/resources")


def paths_content_is_same(path1: Path, path2: Path) -> bool:
    if path1.is_file():
        assert (
            path1.open("r", encoding="utf8").read()
            == path2.open("r", encoding="utf8").read()  # with assert we leverage pytest diff
        ), f"{path1.parent.name}/{path1.name}"
        return True

    subpath_rel_1 = [f"{folder.name}" for folder in path1.glob("*")]
    subpath_rel_2 = [f"{folder.name}" for folder in path2.glob("*")]
    assert subpath_rel_1 == subpath_rel_2, set(subpath_rel_1).difference(set(subpath_rel_2))

    for subpath in path1.glob("*"):
        paths_content_is_same(subpath, (path2 / subpath.name))  # do not need result
    return True


class JoplinRawTestCase:
    diff: Optional[List[str]] = None

    def __init__(self, folder: str):
        self.expected_folder = RESOURCES / folder / "expected"
        self.source_folder = RESOURCES / folder / "source"

    def check(self, folder: str, expected_folder: str = None) -> bool:
        if expected_folder is None:
            expected_folder = self.expected_folder
        return paths_content_is_same(Path(expected_folder), Path(folder))

    def copy_existed(self, folder: Path, source: Optional[Path] = None) -> None:
        if source is None:
            source = self.source_folder
        for subpath in source.glob("*"):
            if subpath.is_file():
                (folder / subpath.name).write_bytes(subpath.read_bytes())
            else:
                (folder / subpath.name).mkdir()
                self.copy_existed(folder / subpath.name, subpath)


@pytest.fixture(scope="function", params=["tag_school"])
def test_case(request) -> JoplinRawTestCase:
    return JoplinRawTestCase(request.param)
