# Generated by Django 3.0.8 on 2020-07-25 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Other', '0002_auto_20200725_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='others',
            name='slug',
            field=models.SlugField(blank=True, max_length=1000, null=True),
        ),
    ]
