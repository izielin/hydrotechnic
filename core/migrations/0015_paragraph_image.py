# Generated by Django 3.0.8 on 2020-07-24 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200724_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='paragraph',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='paragraph'),
        ),
    ]
