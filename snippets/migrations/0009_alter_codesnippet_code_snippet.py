# Generated by Django 4.2.2 on 2023-06-23 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0008_alter_codesnippet_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codesnippet',
            name='code_snippet',
            field=models.TextField(blank=True, null=True),
        ),
    ]