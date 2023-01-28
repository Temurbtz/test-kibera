from django.db import models
from django.contrib.auth.models import User

class New(models.Model):
    name=models.CharField(max_length=50, primary_key=True)
    text=models.TextField()
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    date_created=models.DateTimeField( null=False, blank=False, auto_now=True)

    def  __str__(self):
        return  self.name