# Generated by Django 4.1 on 2022-09-13 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_orderproduct_color_remove_orderproduct_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelado'), ('Accepted', 'Aceptado'), ('Complete', 'Completado'), ('New', 'Nuevo')], default='New', max_length=50),
        ),
    ]
