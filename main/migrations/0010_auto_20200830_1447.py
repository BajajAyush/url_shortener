# Generated by Django 3.0.8 on 2020-08-30 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200830_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_extension',
            name='extension',
            field=models.CharField(default='f', max_length=200, unique=True),
        ),
    ]
