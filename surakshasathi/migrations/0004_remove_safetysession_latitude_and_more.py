# Generated by Django 5.0.7 on 2024-12-27 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surakshasathi', '0003_safetysession_latitude_safetysession_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='safetysession',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='safetysession',
            name='longitude',
        ),
    ]
