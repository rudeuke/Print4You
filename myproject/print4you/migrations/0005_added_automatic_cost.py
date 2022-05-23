# Generated by Django 4.0.4 on 2022-05-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('print4you', '0004_added_automatic_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(choices=[('poczta', 'Przesyłka pocztowa (+6,70zł)'), ('kurier', 'Przesyłka kurierska (+10,90zł)'), ('paczkomat', 'Odbiór w paczkomacie (+8,99zł)')], default='poczta', max_length=30),
        ),
    ]