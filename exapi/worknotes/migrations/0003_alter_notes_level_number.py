# Generated by Django 3.2.7 on 2021-10-28 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worknotes', '0002_auto_20211028_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='level_number',
            field=models.PositiveIntegerField(default=1, verbose_name='class'),
        ),
    ]
