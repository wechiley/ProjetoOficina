# Generated by Django 4.2.7 on 2023-11-30 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0007_ordemdeservico_imagemos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordemdeservico',
            name='ImagemOs',
        ),
    ]