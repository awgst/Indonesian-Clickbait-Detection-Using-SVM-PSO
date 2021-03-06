from django.db import models

# Create your models here.
class dataUji(models.Model):
    id_pengujian = models.AutoField(primary_key=True)
    tanggal = models.DateField()
    total_dataset = models.IntegerField()
    data_train = models.IntegerField()
    data_test = models.IntegerField()
    presisi = models.FloatField()
    recall = models.FloatField()
    akurasi = models.FloatField()
    model = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'pengujian'