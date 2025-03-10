# Generated by Django 5.1.2 on 2025-01-05 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surakshasathi', '0010_trustedcontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='SafetyIncident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('media', models.ImageField(upload_to='incidents/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
