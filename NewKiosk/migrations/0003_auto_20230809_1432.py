# Generated by Django 3.2 on 2023-08-09 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewKiosk', '0002_remove_product_related_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipt',
            old_name='order',
            new_name='주문상품',
        ),
        migrations.RenameField(
            model_name='receipt',
            old_name='product',
            new_name='주문정보',
        ),
    ]