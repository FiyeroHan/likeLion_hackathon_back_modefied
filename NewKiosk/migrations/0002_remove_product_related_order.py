# Generated by Django 3.2 on 2023-08-09 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewKiosk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='related_order',
        ),
    ]
