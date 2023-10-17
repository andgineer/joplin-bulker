import argparse
import yaml
import os.path
import os
from typing import TextIO


CONFIG_FILE_NAME = 'config.yaml'


class Types:
    TAG_RELATION = '6'
    NOTE = '1'
    TAG = '5'


notes = {}
tags = {}


def parse_args():
    parser = argparse.ArgumentParser(description='Joplin tags operations')
    parser.add_argument('--rm',
                        help='delete the tag')

    return parser.parse_args()


def load_config() -> dict:
    return yaml.full_load(open(CONFIG_FILE_NAME, 'rb'))


def joplin_file_name(joplin_dir: str) -> str:
    """
    Generator that iterates all joplin files
    """
    for (_, _, files) in os.walk(joplin_dir):
        for filename in files:
            file_full_name = os.path.join(joplin_dir, filename)
            if os.path.isfile(file_full_name):
                yield file_full_name


def parse_joplin(joplin_file: TextIO, file_name: str) -> dict:
    """
    Extracts all headers from a Joplin file

    Returns dict (<id> - the file ID)
        {
            <id>: {
                'id': <id>,
                'tags': <array of tag IDs>,
                'note_id': <note_id>,
                'type': <type>, # see class Types
                'title': <title>,
                'text': <text>,
                'file_name': <file_name>,
            }
        }
    """
    headers = {
        'tag_id:': {
            'target_name': 'tags',
            'isArray': True
        },
        'id:': {
            'target_name': 'id',
        },
        'note_id:': {
            'target_name': 'note_id',
        },
        'type_:': {
            'target_name': 'type',
        },
    }

    file_headers = {value['target_name']: [] for name, value in headers.items() if 'isArray' in value}
    text = []
    title = None

    text_stop = False
    for line in joplin_file:
        for header_name, header in headers.items():
            if line.startswith(header_name):
                text_stop = True  # headers section. the file text was above so we stop collecting it.
                header_value = line[len(header_name):].strip()

                if 'isArray' in header:
                    if header['target_name'] not in file_headers:
                        file_headers[header['target_name']] = []
                    file_headers[header['target_name']].append(header_value)
                else:
                    file_headers[header['target_name']] = header_value
                break
        else:
            if not text_stop:
                if not title:
                    title = line
                text.append(line)

    file_headers.update({
        'file_name': file_name,
        'title': title,
        'text': '\n'.join(text),
    })
    if 'id' not in file_headers:
        print(f'Unknown file id for {file_name}')
        file_headers['id'] = None
    if 'type' not in file_headers:
        print(f'Unknown file type for {file_name}')
        file_headers['type'] = None
    if file_headers['id'] == 'cbc8be10ea884d69adcdd587857224d6':
        print(file_headers['type'] == Types.NOTE)
    return {file_headers['id']: file_headers}


def remove_tag(remove_tag_name: str):
    if remove_tag_name not in tags:
        print(f'Tag {remove_tag_name} was not found')
        return 0

    remove_tag_id = tags[remove_tag_name]
    relations_removed = 0

    for note in notes.values():
        if note['type'] == Types.TAG_RELATION:
            for tag_id in note['tags']:
                if tag_id == remove_tag_id:
                    print(f'Removing tag relation file {note["id"]}')
                    os.remove(note['file_name'])
                    relations_removed += 1
                    break
    print(f'Removed the tag {remove_tag_name} from {relations_removed} occurrences')

    print(f'Removing tag file: {notes[remove_tag_id]["file_name"]} ...')
    os.remove(notes[remove_tag_id]['file_name'])

    return relations_removed


def main():
    args = parse_args()
    config = load_config()

    for file_name in joplin_file_name(os.path.abspath(config['folder'])):
        with open(file_name, 'r', encoding='utf8', errors='ignore') as joplin_file:
            joplin_obj = parse_joplin(joplin_file, file_name)
            notes.update(joplin_obj)

    # fill note dict for fast tag ID search by tag name
    # add tags ids to notes 'tags' header
    for note in notes.values():
        if note['type'] == Types.TAG_RELATION:
            note_id = note['note_id']
            if 'tags' in note:
                for tag_id in note['tags']:
                    if tag_id in notes:
                        tags.update({notes[tag_id]['text'].strip(): notes[tag_id]['id']})
                        if note_id in notes:
                            notes[note_id]['tags'].append(tag_id)
                        else:
                            print('!' * 50, f'no tag file for relation {note["id"]}')
                    else:
                        print('!'*50, f'no tag file for relation {note["id"]}')
            else:
                print(f'No tag_id in relation {note["id"]}')

    if hasattr(args, 'rm') and args.rm:
        remove_tag(args.rm)
    else:
        # list tags
        for tag in tags:
            print(tag, tags[tag])


if __name__ == '__main__':
    main()