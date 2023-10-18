from os import mkdir
from pathlib import Path
from unittest.mock import patch

from click.testing import CliRunner

from joplin_bulker.tag import main


def test_main(test_case):
    runner = CliRunner()
    with runner.isolated_filesystem():
        mkdir("joplin")
        folder = Path("joplin")
        test_case.copy_existed(folder)
        
        mocked_config = {
            'folder': str(folder)  # Point the folder in the config to the test folder
        }

        with patch('joplin_bulker.tag.load_config', return_value=mocked_config):
            main(remove_tag_name='school')
            assert test_case.check(str(folder))



