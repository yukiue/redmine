#!/usr/bin/env python3

import datetime
import os
import re

from redminelib import Redmine

COLOR_RED = '\033[31m'
COLOR_END = '\033[0m'
FLAG = COLOR_RED + '***' + COLOR_END

SERVER_URL = 'https://rm.lsnl.jp/'
API_ACCESS_KEY = os.getenv('REDMINE_API_ACCESS_KEY')

redmine = Redmine(SERVER_URL, key=API_ACCESS_KEY)

# get current time
now = datetime.datetime.now()

# get issues on event notification
issues = redmine.issue.filter(tracker_id=5, status_id='open')

events = []

for issue in issues:
    subject = issue.subject
    project = issue.project
    # status = issue.status
    _id = issue.id

    # event notification format
    regex = re.compile(
        r'(\d{4})-(\d{2})-(\d{2})\s(\d{2}):(\d{2})-(\d{2}):(\d{2})')
    mo = regex.search(subject)
    if mo is not None:
        events.append(f'{subject} {project} {_id}')

for event in sorted(events):
    if now.strftime('%Y-%m-%d') in event:
        print(FLAG, event)
    else:
        print(event)
