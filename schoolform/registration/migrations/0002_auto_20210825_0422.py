# Generated by Django 3.2.5 on 2021-08-25 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='guardians_phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='phone',
            field=models.IntegerField(),
        ),
    ]