# Generated by Django 5.0.4 on 2025-05-19 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
