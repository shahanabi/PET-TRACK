# Generated by Django 5.2 on 2025-04-06 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_doggroomingroutine'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatFoodRoutine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100)),
                ('sunday_morning1', models.CharField(max_length=255)),
                ('sunday_evening1', models.CharField(max_length=255)),
                ('monday_morning1', models.CharField(max_length=255)),
                ('monday_evening1', models.CharField(max_length=255)),
                ('tuesday_morning1', models.CharField(max_length=255)),
                ('tuesday_evening1', models.CharField(max_length=255)),
                ('wednesday_morning1', models.CharField(max_length=255)),
                ('wednesday_evening1', models.CharField(max_length=255)),
                ('thursday_morning1', models.CharField(max_length=255)),
                ('thursday_evening1', models.CharField(max_length=255)),
                ('friday_morning1', models.CharField(max_length=255)),
                ('friday_evening1', models.CharField(max_length=255)),
                ('saturday_morning1', models.CharField(max_length=255)),
                ('saturday_evening1', models.CharField(max_length=255)),
                ('cat', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.cat')),
            ],
        ),
    ]
