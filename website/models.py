from django.db import models
from django.contrib.auth.models import AbstractUser


class ServiceChoice(models.TextChoices):
    medowyi = 'Медовый'
    limfodrenaznyj = 'Лимфодренажный'
    classicheskij = 'Классический'
    waakumnyj = 'Вакуумный'
    guasha = 'ГуаШа'
    antiwozrastnoj = 'Антивозрастной'
    skulpturirujushchij = 'Скульптурирующий'
    laminirowanie = 'Ламинирование ресниц'
    laminirowanie_botoks = 'Ламинирование ресниц + ботокс'

#
# class Customer(models.Model):
#     name = models.CharField(max_length=30)
#     lastname = models.CharField(max_length=30)
#     gender = models.CharField(max_length=1)
#     # phone_number = models.PositiveSmallIntegerField()
#     email = models.EmailField()
#
#     def __str__(self):
#         return f'{self.name} {self.lastname}'


class User(AbstractUser):
    gender = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.username} - {self.first_name:} {self.last_name}'


class Service(models.Model):
    service = models.CharField(max_length=50, choices=ServiceChoice.choices)
    text = models.TextField()
    duration = models.PositiveSmallIntegerField(default=60)
    price = models.PositiveSmallIntegerField(default=25)
    # date_of_the_service = models.DateTimeField()
    # recording = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.service


class Recording(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_the_service = models.DateTimeField(unique=True)
    service_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.service} - {self.date_of_the_service} - {self.customer}'
