# Generated by Django 3.2.7 on 2022-10-04 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
