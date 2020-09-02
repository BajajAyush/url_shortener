# Generated by Django 3.0.8 on 2020-08-29 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_delete_custom_extension'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='long_url',
            name='extension',
        ),
        migrations.CreateModel(
            name='custom_extension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extension', models.CharField(default='', max_length=200)),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Long_URL')),
            ],
        ),
    ]
