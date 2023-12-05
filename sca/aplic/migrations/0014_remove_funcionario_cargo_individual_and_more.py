# Generated by Django 4.2.7 on 2023-11-30 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0013_remove_funcionario_cargos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='cargo_individual',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='cargos_multiplos',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='cargo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='funcionario', to='aplic.cargo'),
        ),
    ]