# Generated by Django 5.0.4 on 2024-04-18 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
