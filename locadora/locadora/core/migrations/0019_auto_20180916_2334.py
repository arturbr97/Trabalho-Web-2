# Generated by Django 2.1.1 on 2018-09-17 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20180916_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='status',
            field=models.CharField(choices=[('DISPONÍVEL', 'Disponível'), ('INDISPONÍVEL', 'Indisponível')], max_length=20),
        ),
    ]