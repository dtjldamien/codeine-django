# Generated by Django 3.1.7 on 2021-04-05 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('helpdesk', '0005_auto_20210401_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='assigned_admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_tickets', to=settings.AUTH_USER_MODEL),
        ),
    ]
