# Generated by Django 5.1 on 2024-08-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calummara', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='venda',
            name='quantidade',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]