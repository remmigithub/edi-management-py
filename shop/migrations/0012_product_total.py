# Generated by Django 2.1.5 on 2019-02-24 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20190224_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
