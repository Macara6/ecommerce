# Generated by Django 4.2.5 on 2023-11-06 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_produit_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.CharField(max_length=5000),
        ),
    ]
