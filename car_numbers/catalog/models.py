from os import name
from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.core.validators import MaxValueValidator

# Create your models here.
class Region(models.Model):
    number = models.IntegerField(validators=[MaxValueValidator(999)], verbose_name='Номер региона')
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Название')

    class Meta:
        ordering = ['number']

    def __str__(self):
        if self.name:
            return f'{self.number} ({self.name})'
        else:
            return str(self.number)

class Plate(models.Model):
    number = models.CharField(max_length=6, verbose_name='Номер (А111АА)')
    region = models.ForeignKey(Region, on_delete=DO_NOTHING, verbose_name='Регион')
    owner = models.CharField(max_length=60, null=True, blank=True, verbose_name='Владелец')
    car = models.CharField(max_length=60, null=True, blank=True, verbose_name='Автомобить')
    notes = models.CharField(max_length=100, null=True, blank=True, verbose_name='Примечания')

    class Meta:
        ordering = ['number']
        permissions = (
            ('can_edit', 'Manage car numbers'),
        )

    def __str__(self):
        return str(self.number)

    def save(self, *args, **kwargs):
        self.number = self.number.lower()
        return super().save(*args, **kwargs)
