# Generated by Django 4.0.4 on 2022-07-18 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=4, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=280)),
            ],
            options={
                'verbose_name': 'Board',
                'verbose_name_plural': 'Boards',
            },
        ),
    ]
