# Generated by Django 5.0.6 on 2024-07-14 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarvello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
