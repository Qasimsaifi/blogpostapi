# Generated by Django 4.2.2 on 2023-07-12 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0012_alter_fileupload_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='product_images', to='ecommerce.productimage'),
        ),
    ]