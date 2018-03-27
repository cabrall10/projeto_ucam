# Generated by Django 2.0.3 on 2018-03-27 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0005_auto_20180322_1045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='classe_produto',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='nome_produto',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='qtd_estoque',
            new_name='quantidade',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='und_medida',
            new_name='unidade_medida',
        ),
        migrations.AlterField(
            model_name='produto',
            name='observacao',
            field=models.TextField(),
        ),
    ]
