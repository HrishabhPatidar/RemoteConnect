


from django.db import models


# Create your models here.

class Status(models.Model):
    status = models.CharField(default="True", max_length=10, unique=True )

    def __str__(self):
        return self.status


