# Generated by Django 3.2.9 on 2022-10-26 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0006_bin_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bin',
            old_name='balance',
            new_name='initalQty',
        ),
        migrations.AddField(
            model_name='stock',
            name='pickStatus',
            field=models.CharField(choices=[('Collected', 'Collected'), ('Not Collected', 'Not Collected')], default='Not Collected', max_length=50),
        ),
    ]
