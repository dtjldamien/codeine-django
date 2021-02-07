# Generated by Django 3.1.5 on 2021-02-07 17:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20210207_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 2, 7, 17, 17, 35, 893860, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursematerial',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 2, 7, 17, 17, 41, 389203, tzinfo=utc)),
            preserve_default=False,
        ),
    ]