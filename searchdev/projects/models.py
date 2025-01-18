from django.db import models
import uuid

from django.db.models.deletion import CASCADE



class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000,null=True, blank=True)
    source_link = models.CharField(max_length=2000,null=True, blank=True)
    created = models.DateTimeField(default="2025-01-01T00:00:00")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.title


    
