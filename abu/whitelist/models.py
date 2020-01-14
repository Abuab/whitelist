from django.db import models
from django.utils import timezone

class Ip(models.Model):
    ip=models.CharField(max_length=15)
    hostname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    created=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ip
