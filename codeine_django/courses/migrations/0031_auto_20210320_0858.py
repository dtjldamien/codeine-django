# Generated by Django 3.1.7 on 2021-03-20 08:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0030_auto_20210314_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='label',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='labels',
        ),
        migrations.CreateModel(
            name='QuestionGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('label', models.CharField(max_length=255)),
                ('count', models.PositiveSmallIntegerField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_groups', to='courses.quiz')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='courses.questiongroup'),
        ),
    ]