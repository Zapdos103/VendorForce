# Generated by Django 3.2.23 on 2024-02-07 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0003_funcionario_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='empresa',
            name='cargo',
            field=models.CharField(choices=[('S', 'Sócio/Proprietário'), ('CEO', 'CEO'), ('GC', 'Gestor Comercial'), ('GR', 'Gestor RH'), ('BP', 'Bussiness Partner RH'), ('V', 'Vendedor')], max_length=10),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='qtd_vendedores',
            field=models.CharField(choices=[('1-5', 'De 01 a 05'), ('6-10', 'De 06 a 10'), ('11-15', 'De 11 a 15'), ('16-30', 'De 16 a 30'), ('30+', 'Acima de 30')], max_length=10),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='segmento',
            field=models.CharField(choices=[('A', 'Alimentação'), ('T', 'Transporte'), ('Cons', 'Consultoria'), ('V', 'Vestuário'), ('PE', 'Peças e Equipamentos'), ('M', 'Manutenção'), ('Q', 'Química'), ('F', 'Farmaceutica'), ('Cosm', 'Cosmético'), ('E', 'Educação'), ('O', 'Outro')], max_length=10),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='setor',
            field=models.CharField(choices=[('V', 'Varejo'), ('A', 'Atacado'), ('S', 'Serviço'), ('T', 'Tecnologia'), ('I', 'Industria'), ('Outro', 'Outro')], max_length=10),
        ),
    ]
