# Generated by Django 3.2.6 on 2021-09-25 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion', '0002_cart_orderplaced_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('TS', 'Tshirts'), ('W', 'Watches'), ('P', 'Perfumes'), ('S', 'Shoes')], max_length=2),
        ),
    ]
