# Generated by Django 3.1.7 on 2021-03-12 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0027_course_paid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='paid',
            new_name='pro',
        ),
    ]
