# Generated by Django 4.2.2 on 2023-07-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
