#!/usr/bin/env python3
#
# usage: python3 update-status.py [ISSUE_ID] [STATUS]

import os
import sys

from redminelib import Redmine

status2id = {'ToDo': 1, 'Doing': 2, 'Done': 5}

SERVER_URL = 'https://rm.lsnl.jp/'
API_ACCESS_KEY = os.getenv('REDMINE_API_ACCESS_KEY')

redmine = Redmine(SERVER_URL, key=API_ACCESS_KEY)

resource_id = int(sys.argv[1])
status = sys.argv[2]

# get issue
issue = redmine.issue.get(resource_id)

# get original status
original_status = issue.status.name

# update issue status
redmine.issue.update(resource_id, status_id=status2id[status])

print(f'issue {resource_id} 「{issue}」: {original_status} → {status}')
