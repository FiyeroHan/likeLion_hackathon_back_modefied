# Generated by Django 3.2 on 2023-08-09 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewKiosk', '0003_auto_20230809_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipt',
            old_name='주문상품',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='receipt',
            old_name='주문정보',
            new_name='product',
        ),
    ]