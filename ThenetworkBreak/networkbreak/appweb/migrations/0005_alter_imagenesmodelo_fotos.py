# Generated by Django 4.0.6 on 2022-09-27 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0004_imagenesmodelo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenesmodelo',
            name='fotos',
            field=models.ImageField(upload_to='Fotos'),
        ),
    ]
