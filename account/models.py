from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    Name = models.TextField(max_length=10) #이름
    Personal_Num1 = models.CharField(max_length=13) #주민번호 앞자리
    Personal_Num2 = models.CharField(max_length=13) #뒷자리

    def __str__(self):
        return self.Name