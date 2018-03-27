# Generated by Django 2.0.3 on 2018-03-27 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0007_auto_20180327_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='custo',
        ),
        migrations.AddField(
            model_name='produto',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9),
            preserve_default=False,
        ),
    ]
