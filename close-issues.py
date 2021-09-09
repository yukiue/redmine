#!/usr/bin/env python3

import os
import sys

from redminelib import Redmine

SERVER_URL = 'https://rm.lsnl.jp/'
API_ACCESS_KEY = os.getenv('REDMINE_API_ACCESS_KEY')

redmine = Redmine(SERVER_URL, key=API_ACCESS_KEY)

resource_ids = sys.argv[1:]

for resource_id in resource_ids:
    # get issue
    issue = redmine.issue.get(resource_id)
    # update issue status
    redmine.issue.update(resource_id, status_id=5)
    print(f'issue {resource_id} 「{issue}」DONE')
