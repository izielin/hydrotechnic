# Generated by Django 3.0.8 on 2020-07-15 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200715_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='link',
            field=models.CharField(choices=[("{% url 'core:about'%}", 'O Firmie'), ("{% url 'core:offer'%}", 'Oferta'), ("{% url 'core:gallery'%}", 'Galeria'), ("{% url 'core:contact'%}", 'Kontakt')], max_length=50),
        ),
    ]
