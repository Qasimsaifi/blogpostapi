# Generated by Django 4.2.2 on 2023-06-21 07:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author_email',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='author_name',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='author_picture',
            field=models.URLField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
