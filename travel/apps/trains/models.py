from django.db import models
from cities.models import City
from django.core.exceptions import ValidationError


class Train(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название поезда')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Откуда', related_name='from_city')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Куда', related_name='to_city')
    travel_time = models.IntegerField(verbose_name=' Время пути')

    def __str__(self):
        return 'Поезд № {} из {} в {}'.format(self.name, self.from_city, self.to_city)

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['name']

    def clean(self, *args, **kwargs):
        if self.from_city == self.to_city:
            raise ValidationError('Измените город прибытия ')
        qs = Train.objects.filter(from_city=self.from_city,
                                  to_city=self.to_city,
                                  travel_time=self.travel_time).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('Измените время в пути')

        return super(Train, self).clean(*args, **kwargs)
