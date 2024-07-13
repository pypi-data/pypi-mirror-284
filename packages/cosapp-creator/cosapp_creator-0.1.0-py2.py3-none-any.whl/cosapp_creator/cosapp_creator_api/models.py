from django.db import models

class detectConnectionError(models.Model):
    systemList = models.JSONField('systemList')
    connectionList = models.JSONField('connectionList')
    packages = models.JSONField('packages')

    class Meta:
        ordering = ['systemList']