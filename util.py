import re
import gcalutil
from webbrowser import open

def zoom_id_from_gcal_event(event):
    if 'description' not in event:
        return None

    zoom_match = re.search("Meeting ID: (([0-9]{3}\s?){3})", event['description'])
    if zoom_match:
        return zoom_match.group(1).replace(' ', '').strip()

    return None

def display(event):
    id = zoom_id_from_gcal_event(event)
    return event["summary"] + "; Zoom ID: " + id

def print_events(events):
    for idx, event in enumerate(events):
        print(str(idx) + ": " + display(event))

def filter_zoom_events(events):
    zoom_events = []
    for event in events:
        id = zoom_id_from_gcal_event(event)
        if id != None:
            zoom_events.append(event)
    return zoom_events

def start_share(event):
    print("Sharing to " + display(event))
    id = zoom_id_from_gcal_event(event)
    open('https://zoom.us/share/' + id)

def join(event):
    print("Joining " + display(event))
    id = zoom_id_from_gcal_event(event)
    open('https://zoom.us/j/' + id)

def prompt_events(events, verb):
    suffix = ""
    if verb == "join":
        suffix = "join"
    elif verb == "share":
        suffix = "share to"
    else:
        print("Invalid verb " + verb)
        return

    print_events(events)
    print()
    try:
        idx = int(input("Which meeting would you like to " + suffix + "? "))
        do(verb, events[idx])
    except:
        print("Invalid input. Try again")

def do(verb, event):
    if verb == "join":
        join(event)
    elif verb == "share":
        start_share(event)
    else:
        print("Invalid verb " + verb)

def main(verb):
    events = gcalutil.current_events(5)
    zoom_events = filter_zoom_events(events)

    if len(zoom_events) == 0:
        events = gcalutil.upcoming_events(10)
        zoom_events = filter_zoom_events(events)

        if len(zoom_events) == 0:
            # Still?
            print("No current or upcoming events")
            return

        print("No current events. Here are some upcoming events:\n")
        prompt_events(zoom_events, verb)
    elif len(zoom_events) == 1:
        event = events[0]
        do(verb, event)
    else:
        print("Your current events:\n")
        prompt_events(zoom_events, verb)
