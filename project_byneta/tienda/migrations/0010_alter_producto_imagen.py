# Generated by Django 4.2.6 on 2023-11-12 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0009_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='default.jpg', upload_to='media/productos'),
        ),
    ]
