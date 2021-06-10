from django.db import models
from datetime import date
import datetime

# Create your models here.


class TodoList(models.Model):
    name = models.CharField(max_length=40, verbose_name="제목")
    description = models.TextField(max_length=200, verbose_name="할일 내용")
    date_created = models.DateField(auto_now_add=True, verbose_name="생성 날짜")
    date_deadline = models.DateField(verbose_name="마감 날짜")
    
    def remaining_days(self):
        delta = self.date_deadline - date.today()
        days = delta.days 
        return days


    def __str__(self):
        return f' 제목 : {self.name} |내용 : {self.description} |생성일 : {self.date_created} | 마감일 : {self.date_deadline}'


