# Generated by Django 3.1.7 on 2021-03-12 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('industry_projects', '0001_initial'),
        ('analytics', '0001_initial'),
        ('courses', '0028_auto_20210312_0407'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='eventlog',
            name='industry_project',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='industry_projects.industryproject'),
        ),
        migrations.AddField(
            model_name='eventlog',
            name='quiz',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.quiz'),
        ),
        migrations.AddField(
            model_name='eventlog',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
