# Generated by Django 4.2.6 on 2023-10-26 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('assunto', models.CharField(max_length=120, verbose_name='Assunto')),
                ('mensagem', models.CharField(max_length=300, verbose_name='Mensagem')),
            ],
        ),
    ]