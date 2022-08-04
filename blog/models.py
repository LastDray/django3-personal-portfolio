from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title