# Generated by Django 4.2.6 on 2023-11-12 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0012_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=600),
        ),
    ]