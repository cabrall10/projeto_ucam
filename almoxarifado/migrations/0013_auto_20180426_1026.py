# Generated by Django 2.0.4 on 2018-04-26 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0012_auto_20180403_1912'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fornecedor',
            options={'verbose_name_plural': 'Fornecedores'},
        ),
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name_plural': 'Materiais'},
        ),
        migrations.AlterModelOptions(
            name='unidademedida',
            options={'verbose_name_plural': 'Unidades de Medida'},
        ),
        migrations.AlterField(
            model_name='entrada',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='entradas_fornecedor', to='almoxarifado.Fornecedor'),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='nome_atendente',
            field=models.CharField(max_length=255, verbose_name='Nome do atendente'),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='razao_social',
            field=models.CharField(max_length=255, verbose_name='Razão Social'),
        ),
        migrations.AlterField(
            model_name='itementrada',
            name='entrada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='itemEntrada_material', to='almoxarifado.Entrada'),
        ),
        migrations.AlterField(
            model_name='itementrada',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='itemEntrada_material', to='almoxarifado.Material'),
        ),
        migrations.AlterField(
            model_name='unidademedida',
            name='abreviacao',
            field=models.CharField(max_length=3, unique=True, verbose_name='Abreviação'),
        ),
    ]
