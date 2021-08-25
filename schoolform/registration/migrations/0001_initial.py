# Generated by Django 3.2.5 on 2021-08-25 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('phone', models.IntegerField(max_length=11)),
                ('guardian', models.CharField(max_length=25)),
                ('guardians_phone', models.IntegerField(max_length=11)),
                ('address', models.CharField(max_length=60)),
                ('course', models.CharField(choices=[('BSBA', 'BSBA'), ('BSIT', 'BSIT'), ('BS-EDUC', 'BS-EDUC'), ('BS-CRIM', 'BS-CRIM')], max_length=30)),
            ],
        ),
    ]