# Generated by Django 2.0.5 on 2018-05-15 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0018_estoque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='material',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='almoxarifado.Material'),
        ),
    ]