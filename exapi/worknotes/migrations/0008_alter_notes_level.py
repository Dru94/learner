# Generated by Django 3.2.7 on 2022-01-13 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worknotes', '0007_alter_notes_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='level',
            field=models.CharField(choices=[('Primary', 'Primary'), ('Senior', 'Senior')], default='', max_length=9),
        ),
    ]
