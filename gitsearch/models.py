from django.db import models
from django.utils import timezone

# Create your models here.

class SavedGit(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    star=models.DecimalField(max_digits=1, decimal_places=0)
    avtar=models.ImageField(upload_to='templates', height_field=None, width_field=None, max_length=None)
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
