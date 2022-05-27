from turtle import title
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100,blank=False)
    body = models.TextField(blank=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title