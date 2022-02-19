from django.db import models

# Create your models here.

class Projects(models.Model):
    project_name = models.CharField(max_length=60)
    project_id = models.CharField(max_length=10)
    project_desc = models.TextField()

    project_contributor_1 = models.CharField(max_length=20)
    project_contributor_2 = models.CharField(max_length=20)
    project_contributor_3 = models.CharField(max_length=20)
    project_contributor_4 = models.CharField(max_length=20)

    year = models.IntegerField()

    # project_image_1 = models.ImageField()
    # project_image_2 = models.ImageField()

    project_tech = models.TextField()


    def __str__(self):
        return self.project_name
