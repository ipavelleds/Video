#coding: utf-8
from django.db import models


class Request(models.Model):
    name = models.CharField(max_length=250, verbose_name="Имя заказчика")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Почта")

    def __unicode__(self):
        return self.name