# Generated by Django 4.1.7 on 2023-04-16 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_remove_orderproduct_variation_orderproduct_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='variation',
            new_name='variations',
        ),
    ]
