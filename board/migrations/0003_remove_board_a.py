# Generated by Django 4.0.2 on 2022-02-23 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_board_a'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='a',
        ),
    ]
