# Generated by Django 3.1.5 on 2021-02-22 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_paymenttransaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenttransaction',
            name='payment_status',
            field=models.TextField(choices=[('PENDING_COMPLETION', 'Pending Completion'), ('PENDING_REFUND', 'Pending Refund'), ('COMPLETED', 'Completed'), ('REFUNDED', 'Refunded'), ('FAILED', 'Failed')], default='PENDING_COMPLETION'),
        ),
    ]