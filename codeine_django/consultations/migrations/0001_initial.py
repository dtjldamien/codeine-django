# Generated by Django 3.1.7 on 2021-04-12 14:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultationApplication',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('is_cancelled', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ConsultationSlot',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('meeting_link', models.TextField(default='')),
                ('is_cancelled', models.BooleanField(default=False)),
                ('price_per_pax', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('max_members', models.IntegerField()),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consultation_slots', to='common.partner')),
            ],
            options={
                'ordering': ['start_time', 'end_time'],
            },
        ),
        migrations.CreateModel(
            name='ConsultationPayment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('consultation_application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consultation_payments', to='consultations.consultationapplication')),
                ('payment_transaction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='consultation_payment', to='common.paymenttransaction')),
            ],
        ),
        migrations.AddField(
            model_name='consultationapplication',
            name='consultation_slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consultation_applications', to='consultations.consultationslot'),
        ),
        migrations.AddField(
            model_name='consultationapplication',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consultation_applications', to='common.member'),
        ),
    ]
