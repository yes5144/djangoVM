from django.db import models

# Create your models here.


class Version(models.Model):
    project = models.CharField(max_length=32)
    zone = models.CharField(max_length=32)
    version = models.CharField(max_length=64)
    create_time = models.DateTimeField('create time')
    update_time = models.DateTimeField('update time')

    def __str__(self):
        return self.project + '-' + self.zone
