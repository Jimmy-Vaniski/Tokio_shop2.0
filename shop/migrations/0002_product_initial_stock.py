# Generated by Django 4.2.1 on 2023-06-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='initial_stock',
            field=models.PositiveIntegerField(default=10),
            preserve_default=False,
        ),
    ]