# Generated by Django 3.2.23 on 2024-01-24 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionario',
            name='funcao',
            field=models.CharField(choices=[('', '')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionario',
            name='nome',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionario',
            name='telefone',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
    ]
