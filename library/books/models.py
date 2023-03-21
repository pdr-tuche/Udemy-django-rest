from django.db import models
from uuid import uuid4
# Create your models here.

class Books (models.Model):
    idBook = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title =  models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    releaseYear = models.IntegerField()
    state = models.CharField(max_length=50),
    pages = models.IntegerField(),
    publishingCompany = models.CharField(max_length=255)
    createAt = models.DateField(auto_now_add=True)
    