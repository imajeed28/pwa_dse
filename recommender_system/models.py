from django.db import models

class RecommendationSystemModel(models.Model):
    id = models.IntegerField(primary_key=True)
    college_code = models.IntegerField()
    college_name = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    college_location = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    seat_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    minority = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=5 , decimal_places=2)
    class Meta:
        db_table="recommendation_system_21"