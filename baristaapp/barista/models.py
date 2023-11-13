from django.db import models
from django.contrib.postgres.fields import ArrayField



class Source(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    source_name = models.CharField(max_length=100, unique=True)
    metadata = models.CharField(max_length=100, unique=True)

class Beans(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    source_id = models.ForeignKey(Source, on_delete=models.CASCADE)
    bean_name = models.CharField(max_length=100, unique=True)
    ideal_prep = models.JSONField()
