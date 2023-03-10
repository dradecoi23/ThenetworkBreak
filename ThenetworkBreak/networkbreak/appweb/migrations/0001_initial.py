# Generated by Django 4.0.6 on 2022-09-20 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('fotos', models.ImageField(null=True, upload_to='Fotos')),
                ('instagram', models.CharField(blank=True, max_length=30, null=True)),
                ('onliFans', models.CharField(blank=True, max_length=30, null=True)),
                ('pagTransmision', models.CharField(max_length=30)),
                ('concursante', models.BooleanField()),
                ('valor', models.IntegerField()),
                ('genero', models.ImageField(choices=[(1, 'male'), (2, 'female')], default=1, upload_to='')),
            ],
            options={
                'ordering': ('-valor',),
            },
        ),
    ]
