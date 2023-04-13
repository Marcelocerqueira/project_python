# Generated by Django 4.2 on 2023-04-13 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField()),
                ('carga_horaria', models.IntegerField()),
                ('logo', models.FileField(upload_to='logos')),
                ('cor_principal', models.CharField(max_length=7)),
                ('cor_secundaria', models.CharField(max_length=7)),
                ('cor_fundo', models.CharField(max_length=7)),
            ],
        ),
    ]
