# Generated by Django 4.0.4 on 2022-07-18 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=8000)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_threads', to='board.board')),
            ],
            options={
                'verbose_name': 'Thread',
                'verbose_name_plural': 'Threads',
            },
        ),
    ]
