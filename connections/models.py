from django.db import models


class ConnectedDev(models.Model):
    twitter_id = models.CharField(max_length=100, null=False, default="")
    twitter_username = models.CharField(max_length=100, null=False, default="")
    github_id = models.CharField(max_length=100, null=False, default="")
    github_username = models.CharField(max_length=100, null=False, default="")


class RequestRecord(models.Model):
    registered_at = models.DateTimeField()
    dev_1 = models.ForeignKey(to=ConnectedDev, on_delete=models.CASCADE, null=False, related_name="dev_1")
    dev_2 = models.ForeignKey(to=ConnectedDev, on_delete=models.CASCADE, null=False, related_name="dev_2")
    connected = models.BooleanField()
    common_organizations = models.TextField(max_length=100, default="[]", null=False)
