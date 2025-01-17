from django.db import models
import uuid

from django.db.models.deletion import CASCADE
from users.models import Profile



class Project(models.Model):
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    feature_image = models.ImageField(
        null=True, blank=True, default="default.jpg"
    )
# Create your models here.
