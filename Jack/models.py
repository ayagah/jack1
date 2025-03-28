from django.db import models

class CV(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    summary = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()

    def __str__(self):
        return self.name

