import datetime
import json

from django.http import JsonResponse
from django.conf import settings

from github import Github, GithubException
from tweepy import TweepError, AppAuthHandler, API

from connections.models import ConnectedDev, RequestRecord


def realtime(request, dev_1_id, dev_2_id):
    errors = []
    # Create GitHub instance using GitHub token.
    try:
        g = Github(settings.GITHUB_TOKEN)
    except GithubException:
        errors.append("GitHub token is not valid.")

    # Create Twitter instance using key and secret.
    try:
        auth = AppAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
        api = API(auth)
    except TweepError:
        errors.append("Twitter consumer key and consumer secret are not valid.")

    if errors:
        return JsonResponse({"errors": errors})

    try:
        dev_1 = ConnectedDev.objects.get(pk=dev_1_id)
    except ConnectedDev.DoesNotExist:
        errors.append("ID {} is not correct".format(dev_1_id))
    try:
        dev_2 = ConnectedDev.objects.get(pk=dev_2_id)
    except ConnectedDev.DoesNotExist:
        errors.append("ID {} is not correct".format(dev_2_id))

    if errors:
        return JsonResponse({"errors": errors})

    result = dict()
    connected = False

    github_dev_1 = g.get_user_by_id(dev_1.github_id)
    github_dev_2 = g.get_user_by_id(dev_2.github_id)

    github_dev_1_orgs = set([org.name for org in github_dev_1.get_orgs()])
    github_dev_2_orgs = set([org.name for org in github_dev_2.get_orgs()])
    common_orgs = list(github_dev_1_orgs.intersection(github_dev_2_orgs))
    if common_orgs:
        twitter_dev_1 = api.get_user(dev_1.twitter_id)
        twitter_dev_2 = api.get_user(dev_2.twitter_id)
        if (dev_2.twitter_id in set([str(friend_id) for friend_id in twitter_dev_1.friends()])
                and dev_1.twitter_id in set([str(friend_id) for friend_id in twitter_dev_2.friends()])):
            connected = True
            result = {"connected": True, "organizations": common_orgs}
        else:
            result = {"connected": False}
    else:
        result = {"connected": False}

    RequestRecord.objects.create(
        registered_at=datetime.datetime.now(),
        dev_1=dev_1,
        dev_2=dev_2,
        connected=connected,
        common_orgs=json.dumps(common_orgs)
    )
    return JsonResponse(result)


def register(request, dev_1_id, dev_2_id):
    pass
