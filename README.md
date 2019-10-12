# Google Calendar Zoom Tools

Hate clicking around just to find the link to join or share to the Zoom meeting your currently apart of? Maybe not, but I do, so I made this.

## Setup
* Python 3.x
* `pip`
* Google Calendar Python API Tools (Step 1 and 2 [here](https://developers.google.com/calendar/quickstart/python)). Make sure to save `credentials.json` file in the same directory as this tool.
* Install the following required Python libraries
```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install google-auth-oauthlib
pip install python-dateutil
```
* Run tool once to get logged in with Google

## Usage
Your meeting started, but you're too lazy to open your calendar or the Zoom app to join the correct one:
```bash
python zoomtool.py join
```

You're listening in on a meeting via a Zoom room or someone elses computer, and your boss asks you to share your screen. You don't want to join, show your face, and create a bunch of audio feedback in the room. YOU JUST WANT TO SHARE YOUR SCREEN.
```bash
python zoomtool.py share
```

This was fun.
