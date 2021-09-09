#!/usr/bin/env python3

import datetime
import os
import re

from redminelib import Redmine

SERVER_URL = 'https://rm.lsnl.jp/'
API_ACCESS_KEY = os.getenv('REDMINE_API_ACCESS_KEY')

redmine = Redmine(SERVER_URL, key=API_ACCESS_KEY)

# get current time
now = datetime.datetime.now()

# get issues on event notification
issues = redmine.issue.filter(tracker_id=5, status_id='open')

end_event = ''

for issue in issues:
    subject = issue.subject
    project = issue.project
    status = issue.status
    _id = issue.id

    # extract end time of event from subject
    regex = re.compile(
        r'(\d{4})-(\d{2})-(\d{2})\s(\d{2}):(\d{2})-(\d{2}):(\d{2})')
    mo = regex.search(subject)
    if mo is not None:
        year = int(mo.group(1))
        month = int(mo.group(2))
        day = int(mo.group(3))
        end_hour = int(mo.group(6))
        end_minute = int(mo.group(7))
        time = datetime.datetime(year, month, day, end_hour, end_minute)

        # show events whose end time has passed
        if now > time:
            print(project, subject, status, _id)
            end_event += f'{_id} '

print(end_event)
