from django.db import models

# Create your models here.
class Dataset(models.Model):
    id_dataset  = models.AutoField(primary_key=True)
    konten = models.TextField(blank=True, null=True)
    label = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'dataset'
