# Generated by Django 3.0.8 on 2020-07-23 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('amount', models.SmallIntegerField()),
                ('experience', models.BooleanField(default=False)),
            ],
        ),
    ]