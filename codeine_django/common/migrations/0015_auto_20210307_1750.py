# Generated by Django 3.1.5 on 2021-03-07 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0014_auto_20210307_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membershipsubscription',
            name='expiry_date',
            field=models.DateTimeField(),
        ),
    ]
