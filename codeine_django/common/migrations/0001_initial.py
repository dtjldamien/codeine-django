# Generated by Django 3.1.7 on 2021-04-12 14:23

import common.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_suspended', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('first_name', models.CharField(max_length=150, null=True)),
                ('last_name', models.CharField(max_length=150, null=True)),
                ('profile_photo', models.ImageField(blank=True, default=None, null=True, upload_to=common.models.user_directory_path)),
                ('age', models.PositiveIntegerField(null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')], max_length=10, null=True)),
                ('location', models.CharField(max_length=150, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('stats', models.JSONField(default=common.models.get_default_member_stats)),
                ('unique_id', models.CharField(default=None, max_length=10, null=True, unique=True)),
                ('membership_tier', models.TextField(choices=[('FREE', 'Free'), ('PRO', 'Pro')], default='FREE')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('organization_name', models.CharField(max_length=255, unique=True)),
                ('organization_photo', models.ImageField(blank=True, default=None, null=True, upload_to=common.models.org_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentTransaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('payment_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('payment_status', models.TextField(choices=[('PENDING_COMPLETION', 'Pending Completion'), ('PENDING_REFUND', 'Pending Refund'), ('COMPLETED', 'Completed'), ('REFUNDED', 'Refunded'), ('FAILED', 'Failed')], default='PENDING_COMPLETION')),
                ('payment_type', models.TextField(choices=[('VISA', 'Visa'), ('MASTER', 'Mastercard'), ('AMEX', 'American Express')])),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('job_title', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('bio', models.TextField(blank=True, default='', null=True)),
                ('org_admin', models.BooleanField(default=False)),
                ('organization', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partners', to='common.organization')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipSubscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('month_duration', models.PositiveSmallIntegerField(default=1)),
                ('expiry_date', models.DateTimeField()),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='membership_subscriptions', to='common.member')),
                ('payment_transaction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='membership_subscription', to='common.paymenttransaction')),
            ],
            options={
                'ordering': ['expiry_date'],
            },
        ),
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=255)),
                ('organisation', models.CharField(max_length=100)),
                ('start_date', models.DateField(default=None, null=True)),
                ('end_date', models.DateField(default=None, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cvs', to='common.member')),
            ],
            options={
                'ordering': ['-end_date', '-start_date'],
            },
        ),
        migrations.CreateModel(
            name='BankDetail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('bank_account', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=255)),
                ('swift_code', models.CharField(max_length=20)),
                ('bank_country', models.CharField(max_length=255)),
                ('bank_address', models.CharField(max_length=255)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_details', to='common.partner')),
            ],
        ),
    ]
