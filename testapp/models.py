from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Profile(models.Model):
    Asia = "Asia/Kolkata"
    America= "America/Los_Angeles"
    Timezone = [
        (Asia,"Asia/Kolkata"),(America,"America/Los_Angeles")
    ]
    user_id = models.CharField(max_length=15,null=True,blank=True)
    real_name = models.CharField(max_length=50,null=True,blank=True)
    timezone = models.CharField(choices=Timezone,max_length=32,default=timezone.now())

    def __str__(self):
        return self.real_name

class ProfileActivity(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name="activity_periods")
    activity_start_date = models.DateTimeField(default=datetime.datetime.now(),null=True,blank=True)
    activity_end_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.profile.real_name

    @property
    def start_date(self):
        return self.activity_start_date.strftime("%b %d %Y %H:%M:%p")

    @property
    def end_date(self):
        return self.activity_end_date.strftime("%b %d %Y %H:%M:%p")