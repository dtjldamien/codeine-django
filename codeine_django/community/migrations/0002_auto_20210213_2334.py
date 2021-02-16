# Generated by Django 3.1.5 on 2021-02-13 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_partner_org_admin'),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date_edited']},
        ),
        migrations.RemoveField(
            model_name='article',
            name='base_user',
        ),
        migrations.RemoveField(
            model_name='articlecomment',
            name='base_user',
        ),
        migrations.AddField(
            model_name='article',
            name='member',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='common.member'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='member',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='article_comments', to='common.member'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to='community.articlecomment'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_edited',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_activated',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='articlecomment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comments', to='community.article'),
        ),
    ]