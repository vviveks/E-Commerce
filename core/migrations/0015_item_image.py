# Generated by Django 4.0.4 on 2022-05-18 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_payment_order_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
