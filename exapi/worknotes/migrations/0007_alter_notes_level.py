# Generated by Django 3.2.7 on 2022-01-13 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worknotes', '0006_alter_notes_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='level',
            field=models.CharField(choices=[('Primary', 'Primary'), ('Secondary', 'Secondary')], default='', max_length=9),
        ),
    ]
