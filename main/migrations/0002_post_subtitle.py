# Generated by Django 2.2.4 on 2019-09-15 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default='', help_text='Nie jest wymagane', max_length=100),
        ),
    ]