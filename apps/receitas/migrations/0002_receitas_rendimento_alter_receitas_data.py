# Generated by Django 4.1.7 on 2023-03-11 18:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receitas',
            name='rendimento',
            field=models.CharField(default='2 unidades', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='receitas',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 11, 15, 1, 56, 865729)),
        ),
    ]
