# Generated by Django 3.2.7 on 2021-10-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.CharField(choices=[('primary', 'primary'), ('secondary', 'secondary')], default='', max_length=9),
        ),
        migrations.AddField(
            model_name='user',
            name='level_number',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
