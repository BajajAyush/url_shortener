# Generated by Django 3.0.8 on 2020-08-31 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200830_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom_extension',
            name='url',
        ),
        migrations.AddField(
            model_name='long_url',
            name='short',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.custom_extension'),
        ),
        migrations.AlterField(
            model_name='custom_extension',
            name='extension',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
