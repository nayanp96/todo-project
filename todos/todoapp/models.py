from email.policy import default
from django.db import models
from datetime import datetime
# Create your models here.
class Mytodo(models.Model):
    task = models.CharField(max_length=50)
    date_time=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.task

      