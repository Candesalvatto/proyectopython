# Generated by Django 4.2.6 on 2023-11-14 21:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0013_alter_producto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
