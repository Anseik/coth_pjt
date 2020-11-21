# Generated by Django 3.1.2 on 2020-11-21 15:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_talkarticle_hits'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewcomment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reviewcomment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='talkcomment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='talkcomment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
