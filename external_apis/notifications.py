

# Standard library
import json

# 3rd party
import requests

def check_for_notifications(repo):
    if repo.site_url is None:
        repo.notifications = 0

    else:
        url = "{0}/api/notifications".format(repo.site_url)
        response = requests.get(url)

        if response.ok:
            result = json.loads(response.text or response.content)
            repo.notifications = result['value']

        else:
            repo.notifications = 0
