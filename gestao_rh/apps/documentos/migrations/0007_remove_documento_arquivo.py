# Generated by Django 3.1 on 2020-08-13 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0006_documento_arquivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documento',
            name='arquivo',
        ),
    ]