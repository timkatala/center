# Generated by Django 2.2.1 on 2020-01-22 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_auto_20200122_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='fathers_phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Otasing nomeri'),
        ),
        migrations.AlterField(
            model_name='student',
            name='mothers_phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Onasing nomeri'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='Tel. nomeri'),
        ),
    ]
