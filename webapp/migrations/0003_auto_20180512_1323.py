# Generated by Django 2.0.5 on 2018-05-12 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_formmodel_section4name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formmodel',
            old_name='jawjerkleft',
            new_name='jawjerk',
        ),
        migrations.RemoveField(
            model_name='formmodel',
            name='jawjerkright',
        ),
    ]