from django.db import models

from django.contrib.auth.models import User


class Task(models.Model):

    name=models.CharField(max_length=200)
    
    status=models.BooleanField(default=False)

    assigned_date=models.DateTimeField(auto_now_add=True)

    user_object=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):

        return self.name