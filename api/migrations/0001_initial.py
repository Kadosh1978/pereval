# Generated by Django 5.0.6 on 2024-06-25 17:11

import api.utils
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spring', models.CharField(choices=[('н/к', 'н/к'), ('1A', '1A'), ('1B', '1B'), ('2A', '2A'), ('2B', '2B'), ('3A', '3A'), ('3B', '3B')], default='н/к', max_length=3)),
                ('summer', models.CharField(choices=[('н/к', 'н/к'), ('1A', '1A'), ('1B', '1B'), ('2A', '2A'), ('2B', '2B'), ('3A', '3A'), ('3B', '3B')], default='н/к', max_length=3)),
                ('autumn', models.CharField(choices=[('н/к', 'н/к'), ('1A', '1A'), ('1B', '1B'), ('2A', '2A'), ('2B', '2B'), ('3A', '3A'), ('3B', '3B')], default='н/к', max_length=3)),
                ('winter', models.CharField(choices=[('н/к', 'н/к'), ('1A', '1A'), ('1B', '1B'), ('2A', '2A'), ('2B', '2B'), ('3A', '3A'), ('3B', '3B')], default='н/к', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=80)),
                ('fam', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('otc', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=21)),
            ],
        ),
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('other_titles', models.CharField(max_length=128)),
                ('connect', models.CharField(max_length=128)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'new'), ('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')], default='new', max_length=10)),
                ('coords', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.coords')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.users')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=api.utils.get_path_upload_image)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('pereval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.pereval')),
            ],
        ),
    ]
