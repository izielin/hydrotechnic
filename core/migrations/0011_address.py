# Generated by Django 3.0.8 on 2020-07-23 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200720_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('cityName', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
