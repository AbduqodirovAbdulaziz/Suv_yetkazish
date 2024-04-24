from django.db import models
from django.contrib.auth.models import User


class Suv(models.Model):
    brend = models.CharField(max_length=50)
    narx = models.FloatField()
    litr = models.FloatField()
    batafsil = models.TextField()

    def __str__(self):
        return f"{self.brend} {self.narx}"


class Mijoz(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)
    manzil = models.CharField(max_length=100)
    qarz = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism


class Adminlik(models.Model):
    ism = models.CharField(max_length=50)
    yosh = models.IntegerField()
    ish_vaqti = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism


class Haydovchi(models.Model):
    ism = models.CharField(max_length=500)
    tel = models.CharField(max_length=15)
    k_sana = models.DateField()

    def __str__(self):
        return self.ism


class Buyurtma(models.Model):
    suv = models.ForeignKey(Suv, on_delete=models.CASCADE)
    qachon = models.DateTimeField()
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    miqdori = models.PositiveIntegerField()
    umumiy_narxi = models.PositiveIntegerField()
    admin = models.ForeignKey(Adminlik, on_delete=models.CASCADE)
    yetkazib_berish_haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.suv.brend} {self.qachon}"
