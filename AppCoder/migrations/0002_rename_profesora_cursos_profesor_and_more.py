# Generated by Django 4.2.4 on 2023-09-04 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cursos',
            old_name='profesora',
            new_name='profesor',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nroCliente',
        ),
    ]
