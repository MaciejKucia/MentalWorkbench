# Triggering Bitbucket Server Pull Request builds

The following code can be used within Jenkins job triggered every few minutes. 

It will get a list of currently open pull requests. Then get build data for every last commit in pull request. If the commit is not build then trigger Jenkins job.

```
# -*- coding: utf-8 -*-
import requests, re, os, json, datetime, time
from requests.auth import HTTPBasicAuth
JENKINS_URL   = os.environ['JENKINS_URL']
STASH_URL     = os.environ['STASH_URL']
JOB_NAME      = 'JOB_NAME'
JENKINS_TRIG  = JENKINS_URL+"/job/"+JOB_NAME+"/buildWithParameters"
CREDENTIALS   = os.environ['CREDENTIALS'].split(':') # ex user:password
STASH_PRLIST  = STASH_URL + "/rest/api/1.0/projects/PROJECT/repos/REPO/pull-requests"
STASH_PRLIST += r"?limit=20&withAttributes=false&withProperties=false"
STASH_BUILDS  = STASH_URL + "/rest/build-status/1.0/commits/"
JOB_TOKEN     = r"POOLINGISBAD"
userAuth      = HTTPBasicAuth(CREDENTIALS[0], CREDENTIALS[1])
pull_requests = []
trigger       = []

print('Fetching list of open Pull Requests', 
      STASH_PRLIST, 
      datetime.datetime.utcnow().isoformat(),
      'UTC')

def getPullRequestsList():
    isLastPage    = False
    nextPageStart = 0
    while not isLastPage:
        spage = '' if nextPageStart is 0 else '&start='+str(nextPageStart)
        r     = requests.get(STASH_PRLIST + spage, auth=userAuth, timeout=10)
        if r.status_code is not requests.codes.ok:
            raise Exception('Failed to fetch list of open PRs', 
                            [r.status_code, r.text])
        data          = json.loads(r.text)
        isLastPage    = data['isLastPage']
        nextPageStart = data.get('nextPageStart', 0)
	pull_requests.extend(data['values'])
    return pull_requests

def checkAndTriggerIfRequired():
    for PR in getPullRequestsList():
        PR_commit = PR['fromRef']['latestCommit']
        PR_title  = PR['title']
        PR_id     = PR['id']
        r         = requests.get(STASH_BUILDS + PR_commit, auth=userAuth, timeout=10)
        PR_data   = json.loads(r.text)
        PR_val    = PR_data['values']
        PR_lastState = 'NULL' if len(PR_val) is 0 else PR_val[0]['state']
        PR_doTrigger = 'trigger' if PR_lastState is 'NULL' else 'skip'

        print('\u2022 {:<4} {:} {:<10} {:<7} {:}'.format(PR_id,
                                                         PR_commit,
                                                         PR_lastState,
                                                         PR_doTrigger,
                                                         PR_title))
        if PR_doTrigger is 'trigger': trigger.append([PR_id, PR_title])

    if len(trigger) is 0:
        print('Nothing to trigger.')
        return 0

	print()
    for trig in trigger:
        URL = JENKINS_TRIG+'?token='+JOB_TOKEN+'&ID='+str(trig[0])
        print('\u2022 Triggering:', trig[1], URL)
        r = requests.put(URL, auth=userAuth)
        if r.status_code is not requests.codes.ok:
            raise Exception('Failed to trigger Jenkins job', [r.status_code, r.text])
    return 0

exitcode = checkAndTriggerIfRequired()
print('Let Jenkins process, start the build and notify Stash')
print('Doing nothing for mandatory period of 10 seconds')
time.sleep(10)
exit(exitcode)

```