from django.db import models

class Workspace(models.Model):
    name = models.TextField()

class Collection(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    fields = models.TextField()
    default_view = models.CharField(max_length=255, default="table")
    table_view = models.CharField(max_length=255)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Card(models.Model):
    fields = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
