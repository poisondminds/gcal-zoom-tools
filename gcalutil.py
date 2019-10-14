from __future__ import print_function
import pickle
import os.path
import datetime
from dateutil import parser
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('calendar', 'v3', credentials=creds)

def upcoming_events(limit):
    now_utc_formatted = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = get().events().list(calendarId='primary', timeMin=now_utc_formatted,
                                        maxResults=limit, singleEvents=True,
                                        orderBy='startTime').execute()
    return events_result.get('items', [])

def current_events(limit):
    current = []

    events = upcoming_events(limit)

    for event in events:
        start_time = event['start'].get('dateTime')
        end_time = event['end'].get('dateTime')
        if start_time == None or end_time == None:
            continue
        start = parser.parse(start_time)
        end = parser.parse(end_time)
        now_local = datetime.datetime.now(start.tzinfo)

        if start <= now_local <= end:
            current.append(event)

    return current
