# Generated by Django 2.0.5 on 2018-05-09 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0013_auto_20180426_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSaida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='almoxarifado.Material')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Saida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now=True)),
                ('observacao', models.TextField()),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='almoxarifado.PessoaFisica')),
            ],
        ),
        migrations.AddField(
            model_name='itemsaida',
            name='saida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item_saida', to='almoxarifado.Saida'),
        ),
    ]
