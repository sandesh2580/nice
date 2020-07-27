# Generated by Django 3.0.8 on 2020-07-20 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trending', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='trending_top',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trending.Trending')),
            ],
        ),
        migrations.CreateModel(
            name='body_block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15, null=True)),
                ('post_title', models.CharField(max_length=55, null=True)),
                ('paragraph1', models.TextField(null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='bodyblock_pics')),
                ('paragraph2', models.TextField(null=True)),
                ('slug', models.SlugField(blank=True, max_length=10, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]