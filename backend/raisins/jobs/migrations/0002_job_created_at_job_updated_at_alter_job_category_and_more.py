# Generated by Django 4.1.1 on 2022-10-05 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.CharField(blank=True, choices=[('AT', 'Accounting'), ('AC', 'Administration and Clerical')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='cover_letter',
            field=models.CharField(blank=True, choices=[('R', 'Required'), ('O', 'Optional'), ('H', 'Hidden')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.department'),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='education',
            field=models.CharField(blank=True, choices=[('HC', 'High school coursework'), ('HS', 'High school or equivalent')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='employment_type',
            field=models.CharField(blank=True, choices=[('FT', 'Full-time'), ('PT', 'Part-time'), ('TM', 'Temporary'), ('CT', 'Contract'), ('IT', 'Internship'), ('SS', 'Seasonsal'), ('VT', 'Volunteer')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='experience',
            field=models.CharField(blank=True, choices=[('HS', 'Student (High school)'), ('CL', 'Studnet (College)')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='hiring_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hiring_manager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='job',
            name='max_hours',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='max_salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='min_hours',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='min_salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='phone',
            field=models.CharField(blank=True, choices=[('R', 'Required'), ('O', 'Optional'), ('H', 'Hidden')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='photo',
            field=models.CharField(blank=True, choices=[('R', 'Required'), ('O', 'Optional'), ('H', 'Hidden')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='pipeline',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='recruiter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recruiter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='job',
            name='remote',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='requirements',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='resume',
            field=models.CharField(blank=True, choices=[('R', 'Required'), ('O', 'Optional'), ('H', 'Hidden')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='zip_code',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
