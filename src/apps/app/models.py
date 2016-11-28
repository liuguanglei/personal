from django.db import models


class Visitor(models.Model):
    id = models.IntegerField(primary_key=True)
    ip = models.CharField(max_length=32)
    visit_time = models.DateTimeField(auto_now=True)
    trace = models.CharField(max_length=1024)

    reserved_0 = models.IntegerField()
    reserved_1 = models.CharField(max_length=8)
    reserved_2 = models.CharField(max_length=128)
    reserved_3 = models.CharField(max_length=512)
    reserved_4 = models.CharField(max_length=1024)

    class Meta:
        db_table = "Visitor"
