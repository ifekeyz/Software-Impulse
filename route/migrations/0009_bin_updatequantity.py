# Generated by Django 3.2.9 on 2022-10-26 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0008_remove_bin_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bin',
            name='updateQuantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
