# Generated by Django 3.0.8 on 2020-07-26 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_auto_20200724_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='writer_of_week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('topics', models.CharField(choices=[('Politics', 'Politics'), ('Science and Technology', 'Science and Technology'), ('Sports', 'Sports'), ('Health', 'Health')], max_length=30, null=True)),
                ('image', models.ImageField(null=True, upload_to='writer_of_week')),
                ('soeciality', models.CharField(max_length=20, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]