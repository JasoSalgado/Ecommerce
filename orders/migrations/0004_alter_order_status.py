# Generated by Django 4.1 on 2022-09-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelado'), ('Complete', 'Completado'), ('New', 'Nuevo'), ('Accepted', 'Aceptado')], default='New', max_length=50),
        ),
    ]
