# Generated by Django 4.2.6 on 2023-11-12 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0005_carrito_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='imagen',
            field=models.ImageField(default='default.jpg', upload_to='productos'),
        ),
    ]
