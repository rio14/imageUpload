# Generated by Django 3.0.6 on 2020-05-04 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfiles',
            name='up_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
