from joplin_bulker.tag import parse_joplin
from io import StringIO


def test_parse_note(joplin_note):
    note_file = StringIO(joplin_note['note_str'])
    parsed_dict = parse_joplin(note_file, 'file_name')
    parsed_obj = parsed_dict[next(iter(parsed_dict))]
    assert parsed_obj['text'] == joplin_note['text']
