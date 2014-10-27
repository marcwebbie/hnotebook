from django.db import models

class Notebook(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    private = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.name)
