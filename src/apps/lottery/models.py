from django.db import models


class Lottery_Term(models.Model):
    lo_id = models.IntegerField(primary_key=True)
    red_0 = models.IntegerField()
    red_1 = models.IntegerField()
    red_2 = models.IntegerField()
    red_3 = models.IntegerField()
    red_4 = models.IntegerField()
    red_5 = models.IntegerField()
    blue = models.IntegerField()
    open_date = models.DateField()

    reserved_0 = models.IntegerField()
    reserved_1 = models.CharField(max_length=8)
    reserved_2 = models.CharField(max_length=128)
    reserved_3 = models.CharField(max_length=512)
    reserved_4 = models.CharField(max_length=1024)

    class Meta:
        db_table = "Lottery_Term"
