# Generated by Django 4.1.6 on 2023-03-17 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lat', models.CharField(max_length=50)),
                ('lng', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.CharField(choices=[('Petrol Bunk', 'Petrol Bunk'), ('Mechanic', 'Mechanic')], max_length=50)),
            ],
        ),
    ]