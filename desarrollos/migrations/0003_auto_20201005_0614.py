# Generated by Django 3.1.2 on 2020-10-05 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desarrollos', '0002_auto_20201005_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desarrollo',
            name='nombre_desarrollo',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]