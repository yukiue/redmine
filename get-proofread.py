#!/usr/bin/env python3

import os
import subprocess
import sys

from redminelib import Redmine

SERVER_URL = 'https://rm.lsnl.jp/'
API_ACCESS_KEY = os.getenv('REDMINE_API_ACCESS_KEY')

redmine = Redmine(SERVER_URL, key=API_ACCESS_KEY)

resource_id = int(sys.argv[1])

issue = redmine.issue.get(resource_id)

# download attachments
att_list = []
for att in issue.attachments:
    att_list.append(att.filename)
    att_url = att.content_url.replace('http', 'https')
    redmine.download(att_url, savepath='./')
    # display message
    print(f'Download "{att.filename}" with attachment id "{att.id}"')

# add annotations
for ant in [i for i in att_list if '.ant' in i]:
    pdf = ant.replace('.ant', '.pdf')
    if pdf in att_list:
        # run pdf-annot
        # see https://github.com/yukiue/pdf-annot for details
        subprocess.call(["annot", pdf])
        print(f'Add annotations to "{pdf}"')
