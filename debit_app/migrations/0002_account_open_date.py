# Generated by Django 4.1.2 on 2023-08-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debit_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='open_date',
            field=models.DateField(default='2000-01-01'),
            preserve_default=False,
        ),
    ]
