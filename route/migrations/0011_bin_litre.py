# Generated by Django 3.2.9 on 2022-11-02 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0010_bin_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bin',
            name='litre',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
