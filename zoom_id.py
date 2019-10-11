import re

def from_gcal_event(event):
    if 'description' not in event:
        return None

    zoom_match = re.search("Meeting ID: (([0-9]{3}\s?){3})", event['description'])
    if zoom_match:
        return zoom_match.group(1).replace(' ', '').strip()

    return None
