# Generated by Django 2.0.5 on 2018-05-12 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20180512_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formmodel',
            old_name='uvulaleft',
            new_name='uvula',
        ),
        migrations.RemoveField(
            model_name='formmodel',
            name='uvularight',
        ),
    ]
