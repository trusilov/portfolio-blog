from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    gitLink = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


