# Generated by Django 2.2 on 2020-02-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0002_auto_20200213_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
