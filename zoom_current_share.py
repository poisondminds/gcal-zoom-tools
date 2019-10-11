import gcal_service
import zoom_id
from webbrowser import open

def display(event):
    id = zoom_id.from_gcal_event(event)
    return event["summary"] + "; Zoom ID: " + id

def print_current_events(events):
    print("Your current events:")
    print()
    for idx, event in enumerate(events):
        print(str(idx) + ": " + display(event))
    print()

def start_share(event):
    print("Sharing to " + display(event))
    id = zoom_id.from_gcal_event(event)
    open('https://zoom.us/share/' + id)

events = gcal_service.current_events()
zoom_events = []
for event in events:
    id = zoom_id.from_gcal_event(event)
    if id != None:
        zoom_events.append(event)

if len(zoom_events) == 0:
    print("No current events")
elif len(zoom_events) == 1:
    event = events[0]
    start_share(event)
else:
    print_current_events(zoom_events)
    try:
        idx = int(input("Which meeting would you like to share to? "))
        start_share(zoom_events[idx])
    except:
        print("Invalid input. Try again")
