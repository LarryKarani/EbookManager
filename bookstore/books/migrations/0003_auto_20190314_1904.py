# Generated by Django 2.1.7 on 2019-03-14 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20190312_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_modified',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]