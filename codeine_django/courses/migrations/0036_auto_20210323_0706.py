# Generated by Django 3.1.7 on 2021-03-23 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0035_auto_20210323_0514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
        migrations.AddField(
            model_name='questiongroup',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
