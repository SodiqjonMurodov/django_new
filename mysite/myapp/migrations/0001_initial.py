# Generated by Django 4.0.5 on 2022-07-03 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('telephone', models.IntegerField(default=998)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vegetables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('kg', models.IntegerField()),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_name_veg', to='myapp.farmers')),
            ],
        ),
        migrations.CreateModel(
            name='Fruits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('kg', models.IntegerField()),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_name_fruit', to='myapp.farmers')),
            ],
        ),
    ]
