from django.db import models

# Create your models here.
class PredictionModel(models.Model):
    id = models.IntegerField(primary_key=True)
    college_name = models.CharField(max_length=255)
    shift = models.CharField(max_length=255)
    seat_type = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    C1_2018 = models.CharField(max_length=100)
    C2_2018 = models.CharField(max_length=100)
    C3_2018 = models.CharField(max_length=100)
    C1_2019 = models.CharField(max_length=100)
    C2_2019 = models.CharField(max_length=100)
    C3_2019 = models.CharField(max_length=100)
    C1_2020 = models.CharField(max_length=100)
    C2_2020 = models.CharField(max_length=100)
    C2021 = models.DecimalField(max_digits=5 , decimal_places=2)
    class Meta:
        db_table="cutoff_prediction"
