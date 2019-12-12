from django.db import models

# Create your models here.
class Doctor(models.Model):
    Name = models.TextField(max_length=10) #이름
    Phone_Num = models.CharField(max_length=13) #전화번호
    Location = models.CharField(max_length=30) #위치
    Type = models.CharField(max_length=15)


    def __str__(self):
        return self.Name
