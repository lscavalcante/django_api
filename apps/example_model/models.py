from django.db import models


class ExampleModel(models.Model):
    description = models.CharField(max_length=10)
