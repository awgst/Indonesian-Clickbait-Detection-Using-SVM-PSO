from django.db import models

# Create your models here.
class dataCek(models.Model):
    id_cek = models.AutoField(primary_key=True)
    tanggal = models.DateField()
    konten = models.TextField(blank=True, null=True)
    preprocessing = models.TextField(blank=True, null=True)
    tfidf = models.TextField(blank=True, null=True)
    klasifikasi = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'cek_clickbait'