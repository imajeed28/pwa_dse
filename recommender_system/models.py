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

class CollegeComparisonModel(models.Model):
    college_code = models.IntegerField(primary_key=True)
    college_name = models.CharField(max_length=255)
    college_location = models.CharField(max_length=255)
    degree_type = models.CharField(max_length=255)
    established_year = models.IntegerField()
    college_status = models.CharField(max_length=255)
    minority_status = models.CharField(max_length=255)
    duration = models.IntegerField()
    mode = models.CharField(max_length=255)
    approval = models.CharField(max_length=255)
    course1 = models.CharField(max_length=255)
    course2 = models.CharField(max_length=255)
    course3 = models.CharField(max_length=255)
    course4 = models.CharField(max_length=255)
    course5 = models.CharField(max_length=255)
    course6 = models.CharField(max_length=255)
    course7 = models.CharField(max_length=255)
    course8 = models.CharField(max_length=255)
    infra1 = models.CharField(max_length=255)
    infra2 = models.CharField(max_length=255)
    infra3 = models.CharField(max_length=255)
    infra4 = models.CharField(max_length=255)
    infra5 = models.CharField(max_length=255)
    infra6 = models.CharField(max_length=255)
    infra7 = models.CharField(max_length=255)
    infra8 = models.CharField(max_length=255)
    infra9 = models.CharField(max_length=255)
    class Meta:
        db_table="college_details_v1"