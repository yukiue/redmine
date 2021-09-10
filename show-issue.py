#!/usr/bin/env python3

import os
import sys

from redminelib import Redmine

SERVER_URL = 'https://rm.lsnl.jp/'
API_ACCESS_KEY = os.getenv('REDMINE_API_ACCESS_KEY')

redmine = Redmine(SERVER_URL, key=API_ACCESS_KEY)

resource_id = int(sys.argv[1])

# issue = redmine.issue.get(resource_id)

# print(f'project: {issue.project.name}')
# print(f'project: {issue.project.name}')
# print(f'project: {issue.project.name}')

issue = redmine.issue.get(resource_id)

print(f'id: {issue.id}')
print(f'project: {issue.project.name}')
print(f'subject: {issue.subject}')
print(f'tracker: {issue.tracker.name}')
print('description:')
print('--- --- --- --- --- --- --- --- --- --- --- --- ---\n')
print(issue.description)
print('\n--- --- --- --- --- --- --- --- --- --- --- --- ---')
print(f'status: {issue.status.name}')
