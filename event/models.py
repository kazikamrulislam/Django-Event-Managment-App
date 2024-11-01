from django.db import models
from django.utils import timezone
from datetime import datetime


class Event(models.Model):
    title = models.CharField(max_length=50)
    evennt_date = models.DateField(default=datetime.now, blank=True)
    catagory = models.TextField(max_length=50)
    event_detail = models.TextField(max_length=200)
    
    def __str__(self):
        return self.title
