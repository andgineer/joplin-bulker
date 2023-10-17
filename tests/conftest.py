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
