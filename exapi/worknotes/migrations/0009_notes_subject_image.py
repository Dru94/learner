# Generated by Django 3.2.7 on 2022-02-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worknotes', '0008_alter_notes_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='subject_image',
            field=models.ImageField(null=True, upload_to='notes_image/%Y/%m/%d/'),
        ),
    ]
