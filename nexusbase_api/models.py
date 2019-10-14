from django.db import models

class Collection(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    attributes = models.TextField()
    default_view = models.CharField(max_length=255, default="table")
    table_view = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Card(models.Model):
    attributes = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
