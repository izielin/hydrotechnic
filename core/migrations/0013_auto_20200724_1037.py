# Generated by Django 3.0.8 on 2020-07-24 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_box'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='amount',
            field=models.SmallIntegerField(default=None),
        ),
    ]
