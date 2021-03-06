# Generated by Django 2.2.8 on 2019-12-19 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0002_auto_20191219_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название поезда')),
                ('travel_time', models.IntegerField(verbose_name=' Время пути')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_city', to='cities.City', verbose_name='Откуда')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_city', to='cities.City', verbose_name='Куда')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Поезда',
                'verbose_name': 'Поезд',
            },
        ),
    ]
