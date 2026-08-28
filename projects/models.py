from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.ImageField(upload_to="project_images/")
    url = models.URLField(blank=True, null=True)  # nouveau champ