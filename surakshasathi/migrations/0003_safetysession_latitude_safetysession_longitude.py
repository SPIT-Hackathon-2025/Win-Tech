# Generated by Django 5.0.7 on 2024-12-27 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surakshasathi', '0002_safetysession'),
    ]

    operations = [
        migrations.AddField(
            model_name='safetysession',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='safetysession',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
    ]
