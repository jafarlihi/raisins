# Generated by Django 4.1.1 on 2022-10-09 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_remove_job_category_remove_job_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='employment_type',
        ),
    ]