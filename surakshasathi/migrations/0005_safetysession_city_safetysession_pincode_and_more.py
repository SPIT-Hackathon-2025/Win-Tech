# Generated by Django 5.0.7 on 2024-12-27 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surakshasathi', '0004_remove_safetysession_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='safetysession',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='safetysession',
            name='pincode',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='safetysession',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='safetysession',
            name='street_address',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
