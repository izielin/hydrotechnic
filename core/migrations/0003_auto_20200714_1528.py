# Generated by Django 3.0.8 on 2020-07-14 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200714_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='content',
            field=models.TextField(),
        ),
    ]
