# Generated by Django 3.2.8 on 2023-01-09 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20230107_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passanger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('second', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank='True', related_name='passangers', to='flights.Flight')),
            ],
        ),
    ]
